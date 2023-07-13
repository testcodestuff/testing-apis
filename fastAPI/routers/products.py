from fastapi import APIRouter
from variables import list_of_products

router = APIRouter(
    prefix="/products",
    tags=["Products"],
    responses={404: {"error": "Not found"}}
)


@router.get("/")
async def get_products():
    return list_of_products


@router.get("/{id}")
async def get_product(id: int):
    return list_of_products[id]
