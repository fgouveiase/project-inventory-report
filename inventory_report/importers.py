import csv
from typing import Dict, Type, List
import json
from abc import ABC, abstractmethod

from inventory_report.product import Product


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path) as file:
            products = json.load(file)
            product_list = [Product(**product) for product in products]
        return product_list


class CsvImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.path, encoding="utf-8") as file:
            products = csv.DictReader(file)
            product_list = [Product(**product) for product in products]
        return product_list


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
