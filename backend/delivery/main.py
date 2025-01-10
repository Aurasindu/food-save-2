from fastapi import FastAPI
from fastapi import HTTPException, Depends, Header
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv
from shared.supabase import supabase
from crud import create_delivery
from crud import update_delivery_status
from crud import get_deliveries
from routers import delivery_router
import sys
import os
from pathlib import Path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

dotenv_path = Path(__file__).parent.parent / "shared" / ".env"
load_dotenv(dotenv_path)


API_KEY = os.getenv("API_KEY")
api_key_header = APIKeyHeader(name="X-API-Key")

app = FastAPI()

def validate_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    
@app.get("/")
def read_root():
    return {"message": "Welcome to Food Save API! Check /docs for more information."}

@app.post("/delivery/", dependencies=[Depends(validate_api_key)])
def create_delivery_endpoint(order_id: int, user_id: int, restaurant_id: int, status: str, order_time: str):
    return create_delivery(order_id, user_id, restaurant_id, status, order_time)

@app.put("/delivery/{order_id}", dependencies=[Depends(validate_api_key)])
def update_delivery_status_endpoint(order_id: int, status: str):
    return update_delivery_status(order_id, status)

@app.get("/delivery/", dependencies=[Depends(validate_api_key)])
async def get_all_deliveries():
    return get_deliveries()

app.include_router(delivery_router, prefix="/delivery", tags=["delivery"])

