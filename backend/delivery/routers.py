from fastapi import APIRouter
from delivery.crud import create_delivery, update_delivery_status

delivery_router = APIRouter()

@delivery_router.post("/")
def create_delivery_endpoint(order_id: int, user_id: int, restaurant_id: int, status: str, order_time: str):
    return create_delivery(order_id, user_id, restaurant_id, status, order_time)

@delivery_router.put("/{order_id}")
def update_delivery_status_endpoint(order_id: int, status: str):
    return update_delivery_status(order_id, status)


