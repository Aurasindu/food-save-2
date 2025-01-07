from fastapi import FastAPI
from shared.supabase import supabase
from crud import create_restaurant
from routers import restaurant_router
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Food Save API! Check /docs for more information."}

@app.post("/restaurants/")
def create_restaurant_endpoint(id: int, name: str, address: str, contact_number: str):
    return create_restaurant(id, name, address, contact_number)

@app.get("/restaurants/")
async def get_restaurants():
    response = supabase.table('restaurants').select('*').execute()
    return response.data

app.include_router(restaurant_router, prefix="/restaurants", tags=["restaurants"])
