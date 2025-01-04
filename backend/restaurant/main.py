from fastapi import FastAPI
from shared.supabase import supabase
from .crud import create_restaurant
from .routers import restaurant_router

app = FastAPI()

@app.post("/restaurants/")
def create_restaurant_endpoint(id: int, name: str, address: str, contact_number: str):
    return create_restaurant(id, name, address, contact_number)

@app.get("/restaurants/")
async def get_restaurants():
    response = supabase.table('restaurants').select('*').execute()
    return response.data

app.include_router(restaurant_router, prefix="/restaurants", tags=["restaurants"])
