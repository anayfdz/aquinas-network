from fastapi import WebSocket
import json
import requests

async def get_dogs_websocket(websocket: WebSocket):
    await websocket.accept()
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    data = response.json()
    await websocket.send_json(data)
    await websocket.close()
