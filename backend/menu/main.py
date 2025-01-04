from fastapi import FastAPI
from shared.supabase import supabase
from .crud import create_menu
from .routers import menu_router

app = FastAPI()

@app.post("/menu/")
def create_menu_endpoint(id: int, restaurant_id: int, name: str, price: float, waste_saved: str):
    return create_menu(id, restaurant_id, name, price, waste_saved)

@app.get("/menu/")
async def get_restaurants():
    response = supabase.table('menu').select('*').execute()
    return response.data

app.include_router(menu_router, prefix="/menu", tags=["menu"])