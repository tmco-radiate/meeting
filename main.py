from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client, Client
import os

app = FastAPI()

# ===== Supabase接続 =====
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


# ===== Models =====
class User(BaseModel):
    name: str
    age: int
    hometown: str


class Room(BaseModel):
    room_name: str
    capacity: int


class Booking(BaseModel):
    user_id: str
    room_id: str
    reserved_num: int
    start_date_time: str
    end_date_time: str
        
# ===== Users =====
@app.get("/users")
def read_user():
    res = supabase.table("users").select("*").execute()
    return res.data


@app.post("/users")
def create_user(user: User):
    res = supabase.table("users").insert(user.dict()).execute()
    return res.data


# ===== Rooms =====
@app.get("/rooms")
def read_room():
    res = supabase.table("rooms").select("*").execute()
    return res.data


@app.post("/rooms")
def create_room(room: Room):
    res = supabase.table("rooms").insert(room.dict()).execute()
    return res.data


# ===== Bookings =====
@app.get("/bookings")
def read_booking():
    res = supabase.table("bookings").select("*").execute()
    return res.data

# ===== Health Check =====
@app.get("/health")
def health_check():
    try:
        res = supabase.table("users").select("id").limit(1).execute()

        return {
            "status": "ok",
            "supabase": "connected"
        }

    except Exception as e:
        return {
            "status": "error",
            "supabase": "disconnected",
            "message": str(e)
        }

@app.post("/bookings")
def create_booking(booking: Booking):
    res = supabase.table("bookings").insert(booking.dict()).execute()
    return res.data
