from typing import Literal, Union
from pydantic import BaseModel, Field


class ProductImport_Item_Attribute(BaseModel):
    complex_id: int
    id: int = Field(description="Идентификатор характеристики.", title="Идентификатор характеристики")
    values: list = Field(description="Массив вложенных значений характеристики.", title="Массив вложенных значений характеристики.")


class ProductImport_Item(BaseModel):
    attributes: list[ProductImport_Item_Attribute] = Field(
        description="Характеристики товара.", title="Характеристики товара."
    )
    barcode: str = Field(description="Штрих-код.", title="Штрих-код")
    description_category_id: int = Field(
        description="Идентификатор категории.", title="Идентификатор категории"
    )
    new_description_category_id: int = Field(
        description="Новый идентификатор категории.",
        title="Новый идентификатор категории",
    )
    color_image: str = Field(
        description="Маркетинговый цвет.", title="Маркетинговый цвет"
    )
    complex_attributes: list[ProductImport_Item_Attribute] = Field(
        description="Вложенные характеристики. Например фото, видео.",
        title="Вложенные характеристики",
    )
    currency_code: Literal["RUB", "USD", "EUR", "KZT", "BYN", "CNY"] = Field(
        description="Валюта ваших цен.", title="Валюта ваших цен", default="RUB"
    )
    depth: Union[int, str] = Field(description="Длина.", title="Длина")
    dimension_unit: str = Field(
        description="Единица измерения длины.", title="Единица измерения длины"
    )
    height: Union[int, str] = Field(description="Высота.", title="Высота")
    images: list = Field(
        description="Ссылки на изображения. До 10 шт.", title="Изображения"
    )
    images360: list = Field(
        description="Ссылки на 360° изображения. До 70 шт.", title="360° изображения"
    )
    name: str = Field(description="Название.", title="Название")
    offer_id: str = Field(description="Артикул.", title="Артикул")
    old_price: Union[int, str] = Field(description="Старая цена.", title="Старая цена")
    pdf_list: list = Field(
        description="Ссылки на PDF-файлы.", title="Ссылки на PDF-файлы"
    )
    price: Union[int, str] = Field(description="Цена.", title="Цена")
    primary_image: str = Field(
        description="Основное изображение.", title="Основное изображение"
    )
    vat: Literal["0", "0.1", "0.2"] = Field(
        description="НДС. Допустимые значения: 0 (без НДС), 0.1 (НДС 10%), 0.2 (НДС 20%).",
        title="НДС",
    )
    weight: Union[int, str] = Field(description="Вес.", title="Вес")
    weight_unit: str = Field(
        description="Единица измерения веса.", title="Единица измерения веса"
    )
    width: Union[int, str] = Field(description="Ширина.", title="Ширина")


class ProductImport(BaseModel):
    items: list[ProductImport_Item] = Field(description="Товары", title="Товары")