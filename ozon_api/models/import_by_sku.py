from typing import Literal
from pydantic import BaseModel, Field

class ImportBySku_Item(BaseModel):
    name: str = Field(description="Название товара. До 500 символов.", title="Название")
    offer_id: str = Field(description="Идентификатор товара в системе продавца — артикул. Максимальная длина строки — 50 символов.", title="Идентификатор товара")
    old_price: str = Field(description="Цена до скидок (будет зачеркнута на карточке товара). Указывается в рублях. Разделитель дробной части — точка, до двух знаков после точки.", title="Старая цена")
    price: str = Field(description="Цена товара с учётом скидок, отображается на карточке товара. Если на товар нет скидок, укажите значение old_price в этом параметре.", title="Цена")
    sku: int = Field(description="Идентификатор товара в системе Ozon — SKU.", title="SKU")
    vat: Literal["0", "0.1", "0.2"] = Field(description="НДС. Допустимые значения: 0 (без НДС), 0.1 (НДС 10%), 0.2 (НДС 20%).", title="НДС")
    currency_code: Literal["RUB", "USD", "EUR", "KZT", "BYN", "CNY"] = Field(description="Переданное значение должно совпадать с валютой, которая установлена в настройках личного кабинета. По умолчанию передаётся RUB — российский рубль.", title="Валюта ваших цен")
    
class ImportBySku(BaseModel):
    items: list[ImportBySku_Item]