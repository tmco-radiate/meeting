from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 仮のDB（メモリ）
users_db = []
rooms_db = []
bookings_db = []

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


# ===== Users =====
@app.get("/users")
def read_user():
    return users_db

@app.post("/users")
def create_user(user: User):
    data = user.dict()
    data["key"] = str(len(users_db) + 1)  # 簡易ID
    users_db.append(data)
    return data


# ===== Rooms =====
@app.get("/rooms")
def read_room():
    return rooms_db

@app.post("/rooms")
def create_room(room: Room):
    data = room.dict()
    data["key"] = str(len(rooms_db) + 1)
    rooms_db.append(data)
    return data


# ===== Bookings =====
@app.get("/bookings")
def read_booking():
    return bookings_db

@app.post("/bookings")
def create_booking(booking: Booking):
    data = booking.dict()
    data["key"] = str(len(bookings_db) + 1)
    bookings_db.append(data)
    return data