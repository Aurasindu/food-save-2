from fastapi import FastAPI
from shared.supabase import supabase
from menu.crud import create_menu
from menu.routers import menu_router
import sys

print("PYTHONPATH:", sys.path)

app = FastAPI()

@app.post("/menu/")
def create_menu_endpoint(id: int, restaurant_id: int, name: str, price: float, waste_saved: str):
    return create_menu(id, restaurant_id, name, price, waste_saved)

@app.get("/menu/")
async def get_restaurants():
    response = supabase.table('menu').select('*').execute()
    return response.data

app.include_router(menu_router, prefix="/menu", tags=["menu"])