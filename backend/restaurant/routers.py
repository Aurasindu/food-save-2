from fastapi import APIRouter
from restaurant.crud import create_restaurant

restaurant_router = APIRouter()

@restaurant_router.post("/")
def create_restaurant_endpoint(id: int, name: str, address: str, contact_number: str):
    return create_restaurant(id, name, address, contact_number)
