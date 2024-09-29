from typing import Any, Dict, List, Literal, Optional, Type, Union
from aiohttp import ClientSession
from loguru import logger

import sys
logger.remove()
logger.add(sys.stderr, level="INFO")

class OzonAPI:
    """
    A class for interacting with the Ozon API.

    __client_id is the Client-Id provided by the Ozon API.
    __api_key is the Api-Key provided by the Ozon API.

    __api_url is the base URL of the Ozon API.
    __description_category_id is the description category ID to be used in the requests.
    __language is the language to be used in the requests.
    __type_id is the type ID to be used in the requests.

    """

    __client_id: str
    __api_key: str

    __api_url: Union[str, None] = "https://api-seller.ozon.ru"
    __description_category_id: Union[int, None] = None
    __language: Literal["DEFAULT", "RU", "EN", "TR", "ZH_HANS"] = "DEFAULT"
    __type_id: Union[int, None] = None
    

    @property
    def api_url(self) -> str:
        """
        The base URL of the Ozon API.

        Returns:
            str: The base URL of the Ozon API.
        """
        return self.__api_url

    @api_url.setter
    def api_url(self: Type["OzonAPI"], value: str) -> None:
        """
        Sets the base URL of the Ozon API.

        Args:
            value (str): The new base URL of the Ozon API.
        """
        self.__api_url = value

    @property
    def description_category_id(self) -> int:
        """
        The description category ID to be used in the requests.

        Returns:
            int: The description category ID.
        """
        return self.__description_category_id

    @description_category_id.setter
    def description_category_id(self: Type["OzonAPI"], value: int) -> None:
        """
        Sets the description category ID to be used in the requests.

        Args:
            value (int): The new description category ID.
        """
        self.__description_category_id = value

    @property
    def language(self) -> Literal["DEFAULT", "RU", "EN", "TR", "ZH_HANS"]:
        """The language to be used in the requests.

        Returns:
            Literal["DEFAULT", "RU", "EN", "TR", "ZH_HANS"]: The language to be used in the requests.
        """
        return self.__language

    @language.setter
    def language(self: Type["OzonAPI"], value: Literal["DEFAULT", "RU", "EN", "TR", "ZH_HANS"]) -> None:
        """
        Sets the language to be used in the requests.

        Args:
            value (Literal["DEFAULT", "RU", "EN", "TR", "ZH_HANS"]): The new language to be used in the requests.
        """
        self.__language = value

    @property
    def type_id(self) -> int:
        """The type ID to be used in the requests.

        Returns:
            int: The type ID.
        """
        return self.__type_id

    @type_id.setter
    def type_id(self: Type["OzonAPI"], value: int) -> None:
        """Sets the type ID to be used in the requests.

        Args:
            value (int): The new type ID.
        """
        self.__type_id = value

    @property
    def client_id(self) -> str:
        """The client ID to be used in the requests.

        Returns:
            str: The client ID.
        """
        return self.__client_id

    @client_id.setter
    def client_id(self: Type["OzonAPI"], value: str) -> None:
        """Sets the client ID to be used in the requests.

        Args:
            value (str): The new client ID.
        """
        self.__client_id = value

    @property
    def api_key(self) -> str:
        """The API key to be used in the requests.

        Returns:
            str: The API key.
        """
        return self.__api_key

    @api_key.setter
    def api_key(self: Type["OzonAPI"], value: str) -> None:
        """Sets the API key to be used in the requests.

        Args:
            value (str): The new API key.
        """
        self.__api_key = value

    def __init__(self: Type["OzonAPI"], client_id: str, api_key: str) -> None:
        """
        Initializes an instance of the OzonAPI class.

        Args:
            client_id (str): The client ID to be used in the requests.
            api_key (str): The API key to be used in the requests.
        """
        self.client_id = client_id
        self.api_key = api_key
        
        logger.info("Ozon API initialized successfully.")

    async def _request(
        self: Type["OzonAPI"],
        method: Literal["post", "get", "put", "delete"] = "post",
        api_version: str = "v1",
        endpoint: str = "",
        json: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """
        Helper method for making API requests.

        Args:
        method (str): The HTTP method to be used for the request. Defaults to "post".
            It can be one of the following: "post", "get", "put", or "delete".
        api_version (str): The API version to be used. Defaults to "v1".
        endpoint (str): The API endpoint to be called. Defaults to an empty string.
        json (Optional[dict[str, Any]]): Optional JSON payload to be sent with the request. Defaults to None.

        Returns:
        Dict[str, Any]: The JSON response from the API.
        """
        url = f"{self.__api_url}/{api_version}/{endpoint}"
        async with ClientSession(
            headers={
                "Client-Id": self.__client_id,
                "Api-Key": self.__api_key,
            }
        ) as session:
            async with getattr(session, method.lower())(url, json=json) as response:
                return await response.json()

    #############################
    # Атрибуты и характеристики #
    # Attributes and properties #
    #############################

    async def get_description_category_tree(self: Type["OzonAPI"]) -> dict[str, Any]:
        """
        Method: https://api-seller.ozon.ru/v1/description-category/tree
        Documentation: https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_GetTree

        Retrieves the description category tree from the Ozon API.

        This method makes a POST request to the Ozon API endpoint for retrieving the description category tree.
        The request is authenticated using the Client-Id and Api-Key provided in the class headers.

        Returns:
            dict[str, Any]: The JSON response from the API. The response contains the description category tree.
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="description-category/tree",
        )
        return response

    async def get_description_category_attribute(
        self: Type["OzonAPI"],
    ) -> dict[str, Any]:
        """
        Method: https://api-seller.ozon.ru/v1/description-category/attribute
        Documentation: https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_GetAttributes

        Retrieves the description category attributes from the Ozon API.

        Args:
        type_id (int, optional): The type ID to be used in the request. Defaults to 94765.

        Returns:
        dict[str, Any]: The JSON response from the API. The response contains the description category attributes.
        """
        return await self._request(
            method="post",
            api_version="v1",
            endpoint="description-category/attribute",
            json={
                "description_category_id": self.__description_category_id,
                "type_id": self.__type_id,
                "language": self.__language,
            },
        )

    async def get_description_category_attribute_values(
        self: Type["OzonAPI"],
        name: str,
        attribute_id: int = 0,
        last_value_id: int = 0,
        limit: int = 5000,
    ) -> List[Dict[str, Any]]:
        """

        Method: https://api-seller.ozon.ru/v1/description-category/attribute/values
        Documentation: https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_GetAttributeValues

        Retrieves the description category attribute values from the Ozon API.

        Parameters:
        self (class): The class instance calling this method. In this case, it should be `OzonAPI`.
        type_id (int): The type ID to be used in the request. Defaults to 94765.
        attribute_id (int): The attribute ID to be used in the request. Defaults to 0.
        last_value_id (int): The last value ID to be used in the request. Defaults to 0.
        limit (int): The limit of the number of records to be retrieved. Defaults to 5000.

        Returns:
        List[Dict[str, Any]]: The JSON response from the API. The response contains the description category attribute values.
        """

        result: List[Dict[str, Any]] = []
        while True:

            data = await self._request(
                method="post",
                api_version="v1",
                endpoint="description-category/attribute/values",
                json={
                    "attribute_id": attribute_id,
                    "description_category_id": self.__description_category_id,
                    "language": self.__language,
                    "last_value_id": last_value_id,
                    "limit": limit,
                    "type_id": self.__type_id,
                },
            )

            try:
                result.extend(data.get("result", []))
                last_value_id = data["result"][-1]["id"]
            except Exception as e:
                logger.debug(
                    f"Error getting attribute values for {name}: dictionary not found"
                )

            if not data.get("has_next"):
                break

        return result

    async def get_description_category_attribute_values_search(
        self: Type["OzonAPI"],
        attribute_id: int,
        value: str,
        limit: int = 100,
    ):
        """

        Method: https://api-seller.ozon.ru/v1/description-category/attribute/values/search
        Documentation: https://docs.ozon.ru/api/seller/#operation/DescriptionCategoryAPI_SearchAttributeValues

        Retrieves the description category attribute values by search query from the Ozon API.

        Args:
        attribute_id (int): The attribute ID to be used in the request.
        type_id (int): The type ID to be used in the request.
        value (str): The search query.
        limit (int, optional): The limit of the number of records to be retrieved. Defaults to 100.

        Returns:
        List[Dict[str, Any]]: The JSON response from the API. The response contains the description category attribute values.
        """
        return await self._request(
            method="post",
            api_version="v1",
            endpoint="description-category/attribute/values/search",
            json={
                "attribute_id": attribute_id,
                "description_category_id": self.__description_category_id,
                "language": self.__language,
                "limit": limit,
                "type_id": self.type_id,
                "value": value,
            },
        )

    async def get_full_category_info(self: Type["OzonAPI"]) -> List[Dict[str, Any]]:
        """

        Custom method, based on:
            https://api-seller.ozon.ru/v1/description-category/tree
            https://api-seller.ozon.ru/v1/description-category/attribute
            https://api-seller.ozon.ru/v1/description-category/attribute/values

        Get the full category info, including the description category attribute values.

        Returns:
            List[Dict[str, Any]]: The JSON response from the API. The response contains the description category attribute values.
        """
        fields_response = await self.get_description_category_attribute()
        fields = fields_response.get("result", [])

        category_info = []

        for field in fields:
            field_values = await self.get_description_category_attribute_values(
                attribute_id=field["id"], name=field["name"]
            )

            category_field = {
                "id": field["id"],
                "name": field["name"],
                "description": field["description"],
                "values": field_values,
                "is_required": field["is_required"],
            }
            category_info.append(category_field)

        return category_info

    #################################
    # Загрузка и обновление товаров #
    # Load and update products      #
    #################################

    async def product_import(self: Type["OzonAPI"], items: List[dict]):
        """
        Documentation: https://docs.ozon.ru/api/seller/#operation/ProductAPI_ImportProductsV3

        Imports products into the Ozon marketplace.

        Args:
        products (List[dict]): A list of product dictionaries, each containing the product details.
        Max length is 100 items
        """
        data = await self._request(
            method="post",
            api_version="v3",
            endpoint="product/import",
            json=items,
        )

        return data

    async def product_import_info(self: Type["OzonAPI"], task: int) -> dict[str, Any]:
        """
        Documentation: https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetImportProductsInfo

        Retrieves the status of a product import task.

        Args:
        task_id (int): The ID of the product import task.

        Returns:
        dict[str, Any]: The JSON response from the API. The response contains the import task status.
        """
        data = await self._request(
            method="post",
            api_version="v1",
            endpoint=f"product/import/info",
            json={"task_id": task},
        )

        return data

    async def product_import_by_sku(self: Type["OzonAPI"], items: dict) -> dict[str, Any]:
        """
        Documentation: https://docs.ozon.ru/api/seller/#operation/ProductAPI_ImportProductsBySKU

        Imports products by SKU into the Ozon marketplace.

        Returns:
        dict[str, Any]: The JSON response from the API. The response contains the import task status.
        """
        
        data = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/import-by-sku",
            json=items,
        )

        return data

    async def product_attributes_update(self: Type["OzonAPI"], items:dict) -> dict[str, int]:
        """
        Documentation: https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductUpdateAttributes

        Updates product attributes.

        Returns:
        dict[str, int]: The JSON response from the API. The response contains the updated product IDs.
        """
        data = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/attributes/update",
            json=items,
        )

        return data
    
    async def product_pictures_import(self: Type["OzonAPI"], images_data:dict) -> dict[str, Any]:
        """
        Documentation: https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductImportPictures

        Imports product pictures.

        Returns:
        dict[str, Any]: The JSON response from the API. The response contains the import task status.
        """
        data = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/pictures/import",
            json=images_data,
        )

        return data
  
    async def product_pictures_info(self: Type["OzonAPI"], product_id: list[str]) -> dict[str, Any]:
        """
        Documentation: https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductInfoPictures

        Retrieves the status of a product picture import task.

        Returns:
        dict[str, Any]: The JSON response from the API. The response contains the import task status.
        """
        data = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/pictures/info",
            json={"product_id": product_id},
        )

        return data
    
    async def product_list(self: Type["OzonAPI"], body: dict[str, Any]) -> dict[str, Any]:
        """
        Documentation: https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductList
        
        Retrieves a list of products.

        Returns:
        dict[str, Any]: The JSON response from the API. The response contains the product list.
        """
        
        data = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/list",
            json=body,
        )

        return data
    
    async def product_info_limit(self: Type["OzonAPI"]):
        """
        Documentation: https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetUploadQuota

        Retrieves the current product indo limit.

        Returns:
        dict[str, Any]: The JSON response from the API. The response contains the product indo limit.
        """
        
        data = await self._request(
            method="post",
            api_version="v4",
            endpoint="product/info/limit",
        )
        
        return data