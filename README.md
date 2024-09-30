# Ozon API v0.1.0.1
`dev`

### [Асинхронная Python библиотека для работы с Ozon API](https://pypi.org/project/ozon-api/)

## Установка

```bash
pip install ozon-api
```

## Использование
`.env`
```bash
# Данные полученные в ЛК Ozon API
CLIENT_ID = client_id
API_KEY = api_key
```
`main.py`
```python
import os
from dotenv import load_dotenv
from ozon_api import OzonAPI

load_dotenv()

api = OzonAPI(
    client_id=os.getenv("CLIENT_ID"),
    api_key=os.getenv("API_KEY")
)
```

_**Устанавливаем язык на котором будем получать ответ от API**_

```python
api.language = "RU"
```

_Наименование методов класса OzonAPI полностью соответствует фактическим_

## Атрибуты и характеристики Ozon

### _**[api.get_description_category_tree](https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_GetTree)**_

_**Получаем список всех категорий Ozon**_
___

```python
categories = asyncio.run(
    api.get_description_category_tree()
)
```

_**Пример части ответа (данные которые будут использоваться в дальнейшем)**_

```json
{
    "description_category_id": 17027949,
    "category_name": "Шины",
    "disabled": false,
    "children": [
        {
            "type_name": "Шины для легковых автомобилей",
            "type_id": 94765,
            "disabled": false,
            "children": []
        },
    ]
}
```

___

### _**[api.get_description_category_attribute](https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_GetAttributes)**_

_**Устанавливаем категорию и подкатегорию полученные с помощью метода get_description_category_tree**_
_**Получаем список атрибутов для указанной категории**_
___

```python
api.description_category_id = 17027949 # id категории
api.type_id = 94765 # id подкатегории

# Атрибуты для товара категории
attributes = ayncio.run(api.get_description_category_attribute())

```

_**Часть полученных данных:**_

```json
{
    "id": 85,
    "attribute_complex_id": 0,
    "name": "Бренд",
    "description": "Укажите наименование бренда, под которым произведен товар. Если товар не имеет бренда, используйте значение \"Нет бренда\".",
    "type": "String",
    "is_collection": false,
    "is_required": true,
    "is_aspect": false,
    "max_value_count": 0,
    "group_name": "Общие",
    "group_id": 1,
    "dictionary_id": 28732849,
    "category_dependent": true
}
```

___

### _**[api.get_description_category_attribute_values](https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_GetAttributeValues)**_

_**Получаем список значений атрибута**_
___

```python
# Возможные значения для указанного атрибута
attribute_values = ayncio.run(
    api.get_description_category_attribute_values(
        name="Бренд", # name нужного атрибута
        attribute_id=85, # id нужного атрибута
        last_value_id=0, # Идентификатор справочника, с которого нужно начать ответ
        limit=5000 # Количество значений в ответе. Максимум - 5000, минимум - 1
    )
)
```

_**Часть запрошенных данных:**_

```json
... {
    "id": 971010234,
    "value": "WINDFORCE",
    "info": "Автотовары",
    "picture": "https://cdn1.ozone.ru/s3/multimedia-p/6065115817.jpg"
}, ...
```

___

### _**[api.get_description_category_attribute_values_search](https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_SearchAttributeValues)**_

_**Поиск значения характеристики по заданному значению value в запросе.**_
___

```python
attribute_values = ayncio.run(
    api.get_description_category_attribute_values(
        attribute_id=85, # id атрибута
        value="WINDFORCE", # Искомое значение
        limit=100 # Количество значений в ответе. Максимум - 100, минимум - 1
    )
)
```

_**Пример ответа:**_

```json
{
    "id": 971010234,
    "value": "WINDFORCE",
    "info": "Автотовары",
    "picture": "https://cdn1.ozone.ru/s3/multimedia-p/6065115817.jpg"
}
```

___

### _**[api.get_full_category_info](#)**_

_**Дополнительный метод, реализованный на базе методов get_description_category_attribute и get_description_category_attribute_values.**_

`Метод позволяет получить полный список значений всех атрибутов категории`
___

```python
# Возвращает массив с полной информации о категории
full_category_info = asyncio.run(api.get_full_category_info())
```

_**Пример ответа:**_

```json
{
    "id": 85,
    "name": "Бренд",
    "description": "...",
    "values": [...],
    "is_required": true
},
{
    "id": 4080,
    "name": "3D-изображение",
    "description": "...",
    "values": [],
    "is_required": false
},
{
    "id": 4180,
    "name": "Название",
    "description": "...",
    "values": [],
    "is_required": false
}, ...
```

`Поле values содержит массив возможных значений`
___

## Загрузка и обновление товаров

### Модели данных

_Для валидации данных используйте модели из модуля ozon_api.models_

_**Пример:**_

```python
from ozon_api.models import (
    product_import,
    product_import_info,
    product_attributes_update,
    import_by_sku    
)

... работа с данными, формирование списка товаров ...
product_import_model = product_import.ProductImport
items = product_import_model.model_validate(<подготовленные данные>)
validated_items = items.model_dump(mode="json")
```

___

### _**[api.product_import](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ImportProductsV3)**_

_**Метод для создания товаров и обновления информации о них.**_

**В сутки можно создать или обновить определённое количество товаров. Чтобы узнать лимит, используйте `api.product_info_limit()`**

_В одном запросе можно передать до 100 товаров. Каждый товар — это отдельный элемент в массиве `items`._

```python
imported_products = asyncio.run(
    api.product_import(validated_items)
)
```

___

### _**[api.product_info_limit](https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetUploadQuota)**_

_**Метод для получения информации о лимитах.**_

```python
limits = api.product_info_limit()
```

___

### _**[api.product_import_info](https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoV2)**_

_**Узнать статус добавления товара.**_

```python
import_info = asyncio.run(
    api.product_import_info(
        product_import_info.ProductImportInfo(
            task_id=1234567  # task id полученный при выполнении метода product_import
        )
    )
)
```
___
### _**[api.product_import_by_sku](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ImportProductsBySKU)**_

_**Создать товар по Ozon ID.**_

```python
product_import_by_sku_info = api.product_import_by_sku(
    product_import_by_sku.ImportBySku(
        ...
    )
)
```
___
### _**[api.product_attributes_update](https://docs.ozon.ru/api/seller/#operation/ProductAPI_ImportProductsBySKU)**_

_**Создать товар по Ozon ID.**_

```python
product_attributes_update_item = api.product_attributes_update(
    product_attributes_update.ProductAttributesUpdate(
        ...
    )
)
```
___

- product_pictures_import
`complete`
- product_pictures_info
`complete`
- product_list
`complete`
