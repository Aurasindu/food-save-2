from fastapi import APIRouter
from .crud import create_menu

menu_router = APIRouter()

@menu_router.post("/")
def create_menu_endpoint(id: int, restaurant_id: int, name: str, price: float, waste_saved: str):
    return create_menu(id, restaurant_id, name, price, waste_saved)