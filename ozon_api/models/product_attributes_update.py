from typing import Literal
from pydantic import BaseModel, Field


class ProductAttributesUpdate_Item_Attribute_Value(BaseModel):
    dictionary_value_id: int = Field(
        description="Идентификатор характеристики в словаре.", title="Идентификатор характеристики в словаре."
    )
    value: str = Field(description="Значение характеристики товара.", title="Значение характеристики.")

class ProductAttributesUpdate_Item_Attribute(BaseModel):
    complex_id: int = Field(
        description="Идентификатор характеристики, которая поддерживает вложенные свойства. У каждой из вложенных характеристик может быть несколько вариантов значений.", title="Идентификатор характеристики, которая поддерживает вложенные свойства"
    )
    id: int = Field(
        description="Идентификатор характеристики.", title="Идентификатор характеристики"
    )
    values: list[ProductAttributesUpdate_Item_Attribute_Value] = Field(
        description="Массив вложенных значений характеристики.", title="Массив вложенных значений характеристики."
    )


class ProductAttributesUpdate_Item(BaseModel):
    attributes: list[ProductAttributesUpdate_Item_Attribute] = Field(
        description="Характеристики товара.", title="Характеристики товара."
    )
    offer_id: str = Field(description="Артикул товара.", title="Артикул товара.")


class ProductAttributesUpdate(BaseModel):
    items: list[ProductAttributesUpdate_Item]
