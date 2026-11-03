from fastapi import APIRouter

from app.api.v1.endpoints.categories import router as categories_router
from app.api.v1.endpoints.products import router as products_router
from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.demo_auth.view_auth import router as demo_auth_router

router = APIRouter()
router.include_router(products_router)
router.include_router(categories_router)
router.include_router(auth_router)
router.include_router(demo_auth_router)
