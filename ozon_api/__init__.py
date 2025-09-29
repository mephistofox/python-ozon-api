"""
Ozon API Client Library
======================

Библиотека для работы с API Ozon Marketplace.

История версий:
- 1.2.0: Добавлена автоматическая публикация в PyPI
- 1.1.0: Добавлена валидация товаров
- 1.0.0: Первый стабильный релиз
- 0.1.0: Начальная версия с базовой функциональностью
"""

__version__ = "1.6.1"

from .base import OzonAPIBase
from .methods.category import OzonCategoryAPI
from .methods.product_archive import OzonProductArchiveAPI
from .methods.product_barcode_add import OzonProductBarcodeAddAPI
from .methods.product_barcode_generate import OzonProductBarcodeGenerateAPI
from .methods.product_import import OzonProductImportAPI
from .methods.product_info_list import OzonProductInfoListAPI
from .methods.product_list import OzonProductListAPI
from .methods.product_pictures import OzonProductPicturesAPI
from .methods.product_pictures_info import OzonProductPicturesInfoAPI
from .methods.product_rating import OzonProductRatingAPI
from .methods.product_related_sku import OzonProductRelatedSkuAPI
from .methods.product_subscription import OzonProductSubscriptionAPI
from .methods.product_update_offer_id import OzonProductUpdateOfferIdAPI


class OzonAPI(
    OzonCategoryAPI,
    OzonProductImportAPI,
    OzonProductInfoListAPI,
    OzonProductPicturesAPI,
    OzonProductListAPI,
    OzonProductRatingAPI,
    OzonProductUpdateOfferIdAPI,
    OzonProductArchiveAPI,
    OzonProductSubscriptionAPI,
    OzonProductRelatedSkuAPI,
    OzonProductPicturesInfoAPI,
    OzonProductBarcodeAddAPI,
    OzonProductBarcodeGenerateAPI,
):
    """
    Основной класс для работы с API Ozon.
    Объединяет все доступные методы API в единый интерфейс.
    """

    pass


__all__ = ["OzonAPI", "OzonAPIBase"]

# Импортируйте здесь бизнес-методы и собирайте публичный API
