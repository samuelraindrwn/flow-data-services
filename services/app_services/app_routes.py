from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_backend():
    return {"message": "App Service OK"}
