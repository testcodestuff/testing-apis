from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["Products"],
    responses={404: {"error": "Not found"}}
)

list_of_products = ["Product 1",
                    "Product 2",
                    "Product 3",
                    "Product 4",
                    "Product 5"]


@router.get("/")
async def get_products():
    return list_of_products


@router.get("/{id}")
async def get_product(id: int):
    return list_of_products[id]
