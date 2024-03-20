from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
from dotenv import load_dotenv
import os

load_dotenv()
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Dog(Base):
    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True, index=True)
    breed = Column(String, index=True)
    subbreeds = Column(JSON)

app = FastAPI()

@app.get("/api/data/{id}")
def get_dog(id: int):
    db = SessionLocal()
    dog = db.query(Dog).filter(Dog.id == id).first()
    db.close()
    if not dog:
        raise HTTPException(status_code=404, detail="Dog not found")
    return dog


@app.get("/api/data")
def get_data():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    data = response.json()
    return data


@app.post("/api/data")
def store_data():
    try:
        response = requests.get("https://dog.ceo/api/breeds/list/all")
        data = response.json()
        dogs = []
        for breed, subbreeds in data['message'].items():
            dog = Dog(id=None, breed=breed, subbreeds=subbreeds)
            dogs.append(dog)
        
        db = SessionLocal()
        db.add_all(dogs)
        db.commit()
        db.close()
        return {"message": "Data stored successfully"}
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": f"Database Error: {e}"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
