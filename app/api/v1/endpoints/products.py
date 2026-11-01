from fastapi import APIRouter, HTTPException, status, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.product import (
    ProductRead,
    ProductCreate,
    ProductUpdate,
    ProductUpdatePartial,
)
from app.core.database import db_session
from app.repositories.product import ProductRepo

router = APIRouter(prefix="/products", tags=["products"])


@router.post(
    "/",
    response_model=ProductRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(
    product_create: ProductCreate,
    session: AsyncSession = Depends(db_session.get_session),
):
    product_repo = ProductRepo(session=session)
    new_product = await product_repo.create(product_create)
    return new_product


@router.put("/{id_product}/", response_model=ProductRead)
async def put_product(
    id_product: int,
    product_update: ProductUpdate,
    session: AsyncSession = Depends(db_session.get_session),
) -> ProductRead:
    product_repo = ProductRepo(session=session)
    product_by_id = await product_repo.get_by_id(id_product)
    if product_by_id is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    product = await product_repo.update(product_by_id, product_update)
    return product


@router.patch("/{id_product}/", response_model=ProductRead)
async def patch_product(
    id_product: int,
    product_update_partial: ProductUpdatePartial,
    session: AsyncSession = Depends(db_session.get_session),
) -> ProductRead:
    product_repo = ProductRepo(session=session)
    product_by_id = await product_repo.get_by_id(id_product)
    if product_by_id is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    product = await product_repo.update_partial(product_by_id, product_update_partial)
    return product


@router.get("/", response_model=list[ProductRead])
async def get_all(session: AsyncSession = Depends(db_session.get_session)):
    product_repo = ProductRepo(session=session)
    return await product_repo.get_all()


@router.get("/{id_product}/", response_model=ProductRead)
async def get_product_by_id(
    id_product: int, session: AsyncSession = Depends(db_session.get_session)
) -> ProductRead:
    product_repo = ProductRepo(session=session)
    product_by_id = await product_repo.get_by_id(id_product)
    if product_by_id is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    return product_by_id


@router.delete("/{id_product}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    id_product: int, session: AsyncSession = Depends(db_session.get_session)
):
    product_repo = ProductRepo(session=session)
    product_by_id = await product_repo.get_by_id(id_product)
    if product_by_id is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )
    await product_repo.delete_product(product_by_id)
