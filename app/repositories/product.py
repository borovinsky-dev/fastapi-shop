from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.attributes import flag_modified

from app.schemas.product import ProductCreate, ProductUpdate, ProductUpdatePartial
from app.models.product import Product


class ProductRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, product_in: ProductCreate) -> Product:
        product = Product(**product_in.model_dump())
        self.session.add(product)
        await self.session.commit()
        await self.session.refresh(product)
        return product

    # получение
    async def get_by_id(self, product_id: int) -> Product | None:
        product: Product | None = await self.session.get(Product, product_id)
        return product

    async def get_all(self) -> list[Product]:
        statement = select(Product).order_by(Product.id)
        result_from_db = await self.session.execute(statement)
        products = list(result_from_db.scalars().all())
        return products

    # обновление, можно через setattr, но решил старым способом
    async def update(self, product: Product, product_in: ProductUpdate) -> Product:
        dict_product = product_in.model_dump()
        for k, v in dict_product.items():
            if k in product.__dict__:
                product.__dict__[k] = v
                flag_modified(product, k)
        await self.session.commit()
        await self.session.refresh(product)
        return product

    async def update_partial(
        self,
        product: Product,
        product_in: ProductUpdatePartial,
    ) -> Product:
        dict_product = product_in.model_dump(exclude_unset=True)

        for k, v in dict_product.items():
            if k in product.__dict__:
                product.__dict__[k] = v
                flag_modified(product, k)

        await self.session.commit()
        await self.session.refresh(product)
        return product

    async def delete_product(
        self,
        product: Product,
    ) -> None:
        await self.session.delete(product)
        await self.session.commit()
