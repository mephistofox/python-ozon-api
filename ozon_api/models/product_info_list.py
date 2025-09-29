from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class ErrorLevel(str, Enum):
    UNSPECIFIED = "ERROR_LEVEL_UNSPECIFIED"
    ERROR = "ERROR_LEVEL_ERROR"
    WARNING = "ERROR_LEVEL_WARNING"
    INTERNAL = "ERROR_LEVEL_INTERNAL"


class ColorIndex(str, Enum):
    """Перечисление вариантов строковых представлений цветовых индексов"""
    UNSPECIFIED = "COLOR_INDEX_UNSPECIFIED"
    WITHOUT_INDEX = "COLOR_INDEX_WITHOUT_INDEX"
    GREEN = "COLOR_INDEX_GREEN"
    YELLOW = "COLOR_INDEX_YELLOW"
    RED = "COLOR_INDEX_RED"
    SUPER = "COLOR_INDEX_SUPER"


class ShipmentType(str, Enum):
    """Типы упаковки:
    UNSPECIFIED - не указано
    GENERAL - обычный товар
    BOX - коробка
    PALLET - палета
    """
    UNSPECIFIED = "SHIPMENT_TYPE_UNSPECIFIED"
    GENERAL = "SHIPMENT_TYPE_GENERAL"
    BOX = "SHIPMENT_TYPE_BOX"
    PALLET = "SHIPMENT_TYPE_PALLET"


class ProductInfoListRequest(BaseModel):
    """Формирует модель, описывающую тело запроса"""
    offer_id: Optional[List[str]] = Field(
        None, description="Идентификаторы товаров в системе продавца — артикулы."
    )
    product_id: Optional[List[int]] = Field(
        None, description="Идентификаторы товаров в системе Ozon — product_id."
    )
    sku: Optional[List[int]] = Field(
        None, description="Идентификаторы товаров в системе Ozon — SKU."
    )


class ProductInfoListError(BaseModel):
    attribute_id: Optional[int] = None
    code: Optional[str] = None
    field: Optional[str] = None
    level: Optional[ErrorLevel] = None
    state: Optional[str] = None
    texts: Optional[Dict[str, Any]] = None


class ProductInfoListCommission(BaseModel):
    """Информация о комиссиях"""
    delivery_amount: Optional[float] = Field(
        None, description="Стоимость доставки."
    )
    percent: float = Field(
        ..., description="Процент комиссии."
    )
    return_amount: Optional[float] = Field(
        None, description="Стоимость возврата."
    )
    sale_schema: str = Field(
        ..., description="Схема продажи."
    )
    value: float = Field(
        ..., description="Сумма комиссии."
    )
    currency_code: Optional[str] = Field(
        None, description="Код валюты."
    )


class ProductInfoListPriceIndexData(BaseModel):
    """Базовая схема ценовых индексов товара"""
    minimal_price: str | None = Field(
        ..., description="Минимальная цена."
    )
    minimal_price_currency: str | None = Field(
        ..., description="Валюта цены."
    )
    price_index_value: float = Field(
        ..., description="Значение индекса цены."
    )


class ProductInfoListPriceIndexes(BaseModel):
    """Ценовые индексы товара"""
    color_index: ColorIndex = Field(
        ..., description="Вид индекса цен."
    )

    external_index_data: ProductInfoListPriceIndexData | None = Field(
        ..., description="Цена товара у конкурентов на других площадках."
    )
    ozon_index_data: ProductInfoListPriceIndexData | None = Field(
        ..., description="Цена товара у конкурентов на Ozon."
    )
    self_marketplaces_index_data: ProductInfoListPriceIndexData | None = Field(
        ..., description="Цена товара на других площадках."
    )


class ProductInfoListModelInfo(BaseModel):
    """Информация о модели товара"""
    model_config = {"protected_namespaces": ()}

    count: int
    model_id: int


class ProductInfoListSource(BaseModel):
    """Информация о созданном товара"""
    sku: int = Field(
        ..., description="Идентификатор товара на Ozon."
    )
    source: str = Field(
        ..., description="Схема продажи."
    )
    created_at: str = Field(
        ..., description="Дата создания товара."
    )
    quant_code: str = Field(
        ..., description="Список квантов с товарами."
    )
    shipment_type: ShipmentType = Field(
        ..., description="Тип упаковки."
    )


class ProductInfoListStockStatus(BaseModel):
    """Остатки товара по схеме продаж"""
    present: int = Field(
        ..., description="Сейчас на складе."
    )
    reserved: int = Field(
        ..., description="Зарезервировано."
    )
    sku: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU."
    )
    source: str = Field(
        ..., description="Схема продаж."
    )


class ProductInfoListStatuses(BaseModel):
    """Описание состояний товара на Ozon"""
    status: str = Field(
        ..., description="Статус товара."
    )
    status_failed: str = Field(
        ..., description="Статус товара, в котором возникла ошибка."
    )
    moderate_status: str = Field(
        ..., description="Статус модерации."
    )
    validation_status: str = Field(
        ..., description="Статус валидации."
    )
    status_name: str = Field(
        ..., description="Название статуса товара."
    )
    status_description: str = Field(
        ..., description="Описание статуса товара."
    )
    is_created: bool = Field(
        ..., description="Товар создан корректно."
    )
    status_tooltip: str = Field(
        ..., description="Описание статуса."
    )
    status_updated_at: str = Field(
        ..., description="Время последнего изменения статуса."
    )


class ProductInfoListStocks(BaseModel):
    """Информация об остатках товара"""
    has_stock: bool = Field(
        ..., description="Наличие остатка на складах."
    )
    stocks: Optional[List[ProductInfoListStockStatus]] = Field(
        default_factory=list, description="Информация об остатках по схемам продаж."
    )


class ProductInfoListVisibilityDetails(BaseModel):
    """Видимость товара"""
    has_price: bool = Field(
        ..., description="На товар установлена цена."
    )
    has_stock: bool = Field(
        ..., description="Есть остаток на складах."
    )


class ProductInfoListItem(BaseModel):
    """Описание товара и товарной карточки"""
    model_config = {"protected_namespaces": ()}

    barcodes: Optional[List[str]] = Field(
        None, description="Все штрихкоды товара."
    )
    color_image: Optional[List[str]] = Field(
        None, description="URL маркетингового цвета."
    )
    commissions: Optional[List[ProductInfoListCommission]] = Field(
        None, description="Применяемые комиссии."
    )
    created_at: str = Field(
        ..., description="Дата и время создания товара."
    )
    currency_code: Optional[str] = Field(
        None, description="Код валюты."
    )
    description_category_id: Optional[int] = Field(
        None, description="Идентификатор категории."
    )
    discounted_fbo_stocks: Optional[int] = Field(
        None, description="Остатки уценённого товара на складе Ozon."
    )
    errors: Optional[List[ProductInfoListError]] = Field(
        None, description="Информация об ошибках."
    )
    has_discounted_fbo_item: Optional[bool] = Field(
        None, description="Есть уцененные товары на складе Ozon."
    )
    id: int = Field(
        ..., description="Идентификатор Ozon."
    )
    images: Optional[List[str]] = Field(
        None, description="Изображения товара."
    )
    images360: Optional[List[str]] = Field(
        None, description="Изображения товара для 360."
    )
    is_archived: bool = Field(
        ..., description="Товарная карточка в архиве."
    )
    is_autoarchived: bool = Field(
        ..., description="Товарная карточка архивируется автоматически."
    )
    is_discounted: bool = Field(
        ..., description="Товар является уцененным."
    )
    is_kgt:  bool = Field(
        ..., description="Товар является крупногабаритным."
    )
    is_prepayment_allowed: bool = Field(
        ..., description="Возможна предоплата."
    )
    is_super: bool = Field(
        ..., description="Является супер-товаром."
    )
    marketing_price: Optional[str] = Field(
        None, description="Цена на товар с учетом акций (значение указано на витрине)."
    )
    min_price: Optional[str] = Field(
        None, description="Минимальная цена товара при бустинге."
    )
    model_info: ProductInfoListModelInfo = Field(
        ..., description="Информация о модели товара."
    )
    name: str = Field(
        ..., description="Наименование товара."
    )
    offer_id: str = Field(
        ..., description="Идентификатор товара в системе продавца."
    )
    old_price: Optional[str] = Field(
        None, description="Цена до учёта скидок (на карточке товара отображается зачёркнутой)."
    )
    price: Optional[str] = Field(
        None, description="Текущая цена товара."
    )
    price_indexes: ProductInfoListPriceIndexes = Field(
        ..., description="Ценовые индексы товара."
    )
    primary_image: Optional[List[str]] = Field(
        None, description="Главное изображение (если не указано, то по индексам)."
    )
    sources: List[ProductInfoListSource] = Field(
        default_factory=list, description="Информация об источниках схожих предложений."
    )
    statuses: ProductInfoListStatuses = Field(
        ..., description="Описание состояний товара на Ozon."
    )
    stocks: ProductInfoListStocks = Field(
        ..., description="Информация об остатках товара."
    )
    type_id: Optional[int] = Field(
        None, description="Идентификатор типа товара."
    )
    updated_at: str = Field(
        ..., description="Дата и время обновления информации."
    )
    vat: Optional[str] = Field(
        None, description="Ставка НДС."
    )
    visibility_details: ProductInfoListVisibilityDetails
    volume_weight: Optional[float] = Field(
        None, description="Объемный вес товара."
    )


class ProductInfoListResponse(BaseModel):
    items: List[ProductInfoListItem] = Field(
        default_factory=list, description="Массив данных о товарах."
    )
