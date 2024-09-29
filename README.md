# Pyozon v0.1.0 _by FxCode_ `в разработке`
### Асинхронная Python библиотека для работы с Ozon API

## Установка
```bash
pip install ozon-api
```
## Использование

```bash
# Данные полученные в ЛК Ozon API
CLIENT_ID = client_id
API_KEY = api_key
```

```python
import os
from dotenv import load_dotenv
from ozon_api import OzonAPI
api = OzonAPI(os.getenv("CLIENT_ID"), os.getenv("API_KEY"))
```
***Устанавливаем язык на котором будем получать ответ от API***

```python
api.language = "RU"
```

_Наименование методов класса OzonAPI полностью соответствует фактическим_

## Атрибуты и характеристики Ozon

### ***[api.get_description_category_tree](https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_GetTree)***
***Получаем список всех категорий Ozon***
___
```python
categories = asyncio.run(api.get_description_category_tree())
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
### ***[api.get_description_category_attribute](https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_GetAttributes)***
***Устанавливаем категорию и подкатегорию полученные с помощью метода get_description_category_tree***
***Получаем список атрибутов для указанной категории***
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
### ***[api.get_description_category_attribute_values](https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_GetAttributeValues)***
***Получаем список значений атрибута***
___
```python
# Возможные значения для указанного атрибута
attribute_values = ayncio.run(api.get_description_category_attribute_values(
    name="Бренд", # name нужного атрибута
    attribute_id=85, # id нужного атрибута
    last_value_id=0, # Идентификатор справочника, с которого нужно начать ответ
    limit=5000 # Количество значений в ответе. Максимум - 5000, минимум - 1
))
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
### ***[api.get_description_category_attribute_values_search](https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_SearchAttributeValues)***
***Поиск значения характеристики по заданному значению value в запросе.***
___
```python
attribute_values = ayncio.run(api.get_description_category_attribute_values(
    attribute_id=85, # id атрибута
    value="WINDFORCE", # Искомое значение
    limit=100 # Количество значений в ответе. Максимум - 100, минимум - 1
)) 
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
### ***[api.get_full_category_info](#)***
***Дополнительный метод, реализованный на базе методов get_description_category_attribute и get_description_category_attribute_values.***

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

### Реализованные методы:
- product_import
- product_import_info
- product_import_by_sku
- product_attributes_update
- product_pictures_import
- product_pictures_info
- product_list
- product_info_limit