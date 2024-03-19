from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Modelo de la tabla "data"
class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))

    def to_dict(self):
        return {"id": self.id, "name": self.name, "description": self.description}
