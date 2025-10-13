from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
from deta import Deta
import json

# 環境変数からプロジェクトキーを取得
deta = Deta(os.getenv("DETA_PROJECT_KEY"))  # ← ここを修正
users = deta.Base("fastapi-users")
rooms = deta.Base("fastapi-rooms")
bookings = deta.Base("fastapi-bookings")


app = FastAPI()

class User(BaseModel):
  name: str
  age: int
  hometown: str

class Room(BaseModel):
  room_name: str
  capacity: int

class Booking(BaseModel):
  user_key: str
  room_key: str
  reserved_num: int
  start_date_time: str
  end_date_time: str

@app.get("/users")
def read_user():
  return next(users.fetch())

@app.post("/users",status_code=200)
def create_user(user: User):
  user= users.put(user.dict())
  return json.dumps(user)

@app.get("/rooms")
def read_room():
  return next(rooms.fetch())

@app.post("/rooms",status_code=200)
def create_room(room: Room):
  room= rooms.put(room.dict())
  return json.dumps(room)

@app.get("/bookings")
def read_booking():
  return next(bookings.fetch())

@app.post("/bookings",status_code=200)
def create_booking(booking: Booking):
  booking= bookings.put(booking.dict())
  return json.dumps(booking)