from fastapi import FastAPI
from finan.api.v1 import router as finan_router

app = FastAPI(title="Nia LeSane CEO")

app.include_router(finan_router, prefix="/api/finan", tags=["financial"])
