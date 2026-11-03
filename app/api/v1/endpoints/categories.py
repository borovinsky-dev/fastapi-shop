from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import db_session
from app.repositories.category import CategoryRepo
from app.schemas.category import (
    CategoryCreate,
    CategoryRead,
    CategoryUpdate,
    CategoryUpdatePartial,
)

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post(
    "/",
    response_model=CategoryRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_category(
    category_create: CategoryCreate,
    session: AsyncSession = Depends(db_session.get_session),
) -> CategoryRead:
    category_repo = CategoryRepo(session=session)
    return await category_repo.create(category_create)


@router.get("/", response_model=list[CategoryRead])
async def get_all_categories(
    session: AsyncSession = Depends(db_session.get_session),
) -> list[CategoryRead]:
    category_repo = CategoryRepo(session=session)
    return await category_repo.get_all()


@router.get("/{category_id}/", response_model=CategoryRead)
async def get_category_by_id(
    category_id: int,
    session: AsyncSession = Depends(db_session.get_session),
) -> CategoryRead:
    category_repo = CategoryRepo(session=session)
    category = await category_repo.get_by_id(category_id)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )
    return category


@router.put("/{category_id}/", response_model=CategoryRead)
async def update_category(
    category_id: int,
    category_update: CategoryUpdate,
    session: AsyncSession = Depends(db_session.get_session),
) -> CategoryRead:
    category_repo = CategoryRepo(session=session)
    category = await category_repo.get_by_id(category_id)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )
    return await category_repo.update(category, category_update)


@router.patch("/{category_id}/", response_model=CategoryRead)
async def update_category_partial(
    category_id: int,
    category_update: CategoryUpdatePartial,
    session: AsyncSession = Depends(db_session.get_session),
) -> CategoryRead:
    category_repo = CategoryRepo(session=session)
    category = await category_repo.get_by_id(category_id)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )
    return await category_repo.update_partial(category, category_update)


@router.delete("/{category_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(
    category_id: int,
    session: AsyncSession = Depends(db_session.get_session),
) -> None:
    category_repo = CategoryRepo(session=session)
    category = await category_repo.get_by_id(category_id)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )
    await category_repo.delete_category(category)
