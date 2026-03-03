from fastapi import APIRouter, Depends
from app.auth.guards import founder_required
from app.services.bird_dog.search_grants import search_grants
import os

router = APIRouter()

@router.get("/run")
async def run_bird_dog(query: str, user = Depends(founder_required)):
    api_key = os.getenv("SERPAPI_KEY", "")
    results = search_grants(query, api_key)
    return {"query": query, "results": results}
