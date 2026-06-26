from repository.stock_repository import StockRepository
from repository.company_repository import CompanyRepository
from services.master_data_service import MasterDataService


def main():

    print("\nLoading repositories...\n")

    StockRepository.load()
    CompanyRepository.load()

    print()

    print("Stock Count :", StockRepository.count())
    print("Company Count :", CompanyRepository.count())

    print()

    company = input("Enter company name : ")

    result = MasterDataService.get(company)

    print("\nResult\n")

    print(result)


if __name__ == "__main__":
    main()