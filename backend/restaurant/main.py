from fastapi import FastAPI
from fastapi import HTTPException, Depends, Header
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv
from shared.supabase import supabase
from crud import create_restaurant
from routers import restaurant_router
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

@app.post("/restaurants/", dependencies=[Depends(validate_api_key)])
def create_restaurant_endpoint(id: int, name: str, address: str, contact_number: str):
    return create_restaurant(id, name, address, contact_number)

@app.get("/restaurants/", dependencies=[Depends(validate_api_key)])
async def get_restaurants(x_api_key: str = Header(None)):
    print(f"Received header X-API-Key: {x_api_key}")
    response = supabase.table('restaurants').select('*').execute()
    return response.data

app.include_router(restaurant_router, prefix="/restaurants", tags=["restaurants"])
