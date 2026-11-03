from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.attributes import flag_modified

from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
    CategoryUpdatePartial,
)
from app.models.category import Category


class CategoryRepo:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, category_in: CategoryCreate) -> Category:
        # превращает схему в словарь {}
        category = Category(**category_in.model_dump())
        self.session.add(category)
        await self.session.commit()
        await self.session.refresh(category)
        return category

    async def get_by_id(self, category_id: int) -> Category | None:
        category: Category | None = await self.session.get(Category, category_id)
        return category

    async def get_all(self) -> list[Category]:
        statement = select(Category).order_by(Category.id)
        result_from_db = await self.session.execute(statement)
        categories = list(result_from_db.scalars().all())
        return categories

    async def update(
        self,
        category: Category,
        category_in: CategoryUpdate,
    ) -> Category:
        dict_category = category_in.model_dump()
        for key, value in dict_category.items():
            if key in category.__dict__:
                category.__dict__[key] = value
                flag_modified(category, key)
        await self.session.commit()
        await self.session.refresh(category)
        return category

    async def update_partial(
        self,
        category: Category,
        category_in: CategoryUpdatePartial,
    ) -> Category:
        dict_category = category_in.model_dump(exclude_unset=True)
        for key, value in dict_category.items():
            if key in category.__dict__:
                category.__dict__[key] = value
                flag_modified(category, key)
        await self.session.commit()
        await self.session.refresh(category)
        return category

    async def delete_category(self, category: Category) -> None:
        await self.session.delete(category)
        await self.session.commit()
