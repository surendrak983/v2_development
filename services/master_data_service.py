"""
services.master_data_service

Provides a single interface for all stock master data.
"""

from repository.stock_repository import StockRepository
from repository.company_repository import CompanyRepository


class MasterDataService:

    @staticmethod
    def get(company_name):

        stock = StockRepository.get(company_name)

        if stock is None:
            return None

        scrip_code = stock.get("InstrmId")

        company = CompanyRepository.get_company_info(scrip_code)

        return {

            "company_name": stock.get("name"),

            "symbol": stock.get("symbol"),

            "security_code": stock.get("InstrmId"),

            "isin": stock.get("ISIN"),

            "price": stock.get("ClsPric"),

            "volume": stock.get("TtlTradgVol"),

            "sector": company.get("sector"),

            "industry": company.get("industry"),

            "market_cap": company.get("market_cap")

        }

    # ---------------------------------------------------------

    @staticmethod
    def exists(company_name):

        return StockRepository.exists(company_name)

    # ---------------------------------------------------------

    @staticmethod
    def get_price(company_name):

        stock = StockRepository.get(company_name)

        if stock is None:
            return None

        return stock.get("ClsPric")

    # ---------------------------------------------------------

    @staticmethod
    def get_volume(company_name):

        stock = StockRepository.get(company_name)

        if stock is None:
            return None

        return stock.get("TtlTradgVol")