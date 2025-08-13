from fastapi import FastAPI
from services.data_services.data_routes import router as data_router
from services.app_services.app_routes import router as app_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

# Daftarkan router
app.include_router(data_router, prefix="/data", tags=["Data Services"])
app.include_router(app_router, prefix="/app", tags=["App Services"])
