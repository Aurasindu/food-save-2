from fastapi import FastAPI
from shared.supabase import supabase
from crud import create_delivery, update_delivery_status, get_deliveries
from routers import delivery_router

app = FastAPI()

@app.post("/delivery/")
def create_delivery_endpoint(order_id: int, user_id: int, restaurant_id: int, status: str, order_time: str):
    return create_delivery(order_id, user_id, restaurant_id, status, order_time)

@app.put("/delivery/{order_id}")
def update_delivery_status_endpoint(order_id: int, status: str):
    return update_delivery_status(order_id, status)

@app.get("/delivery/")
async def get_all_deliveries():
    return get_deliveries()

app.include_router(delivery_router, prefix="/delivery", tags=["delivery"])

