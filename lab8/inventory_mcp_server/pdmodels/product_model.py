from pydantic import BaseModel, Field


class ProductModel(BaseModel):
    name: str = Field(description="Product name")
    quantity: int = Field(description="Product Quantity or inventor level of a product")
