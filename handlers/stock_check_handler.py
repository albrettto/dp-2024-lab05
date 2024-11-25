from handlers.base_order_handler import BaseOrderHandler
from exceptions.out_of_stock_error import OutOfStockError
from db.database import products


class StockCheckHandler(BaseOrderHandler):
    """
    Обработчик этапа проверки наличия товара на складе.

    Этот класс реализует проверку наличия товара на складе в цепочке обязанностей. Если товар отсутствует,
    выбрасывается исключение `OutOfStockError`.
    """

    def handle(self, order: dict):
        """
        Проверяет наличие товара на складе.

        Этот метод проверяет, есть ли запрашиваемый товар на складе. Если товара нет в наличии, выбрасывается исключение
        `OutOfStockError`. Если товар есть в наличии, обработка заказа передается следующему обработчику.

        Аргументы:
            order (dict): Заказ, содержащий информацию о товаре.

        Исключения:
            OutOfStockError: Если товар отсутствует на складе.
        """
        item = order.get("item")
        if products[item]['quantity'] == 0:
            raise OutOfStockError(f"Нет в наличии товара '{item}'.")
        print(f"Склад: Доступен товар '{item}'.")
        super().handle(order)
