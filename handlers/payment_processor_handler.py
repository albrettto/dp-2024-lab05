from handlers.base_order_handler import BaseOrderHandler
from exceptions.payment_processing_error import PaymentProcessingError
from db.database import prices


class PaymentProcessorHandler(BaseOrderHandler):
    """
    Обработчик этапа обработки платежа.

    Этот класс реализует обработку этапа платежа в цепочке обязанностей. Он проверяет, достаточно ли средств для
    покупки товара. Если средств недостаточно, выбрасывается исключение `PaymentProcessingError`.
    """

    def handle(self, order: dict):
        """
        Обрабатывает этап платежа.

        Этот метод проверяет, достаточно ли средств для покупки товара. Если средства не покрывают цену товара,
        выбрасывается исключение `PaymentProcessingError`. В случае успешного платежа передается управление
        следующему обработчику.

        Аргументы:
            order (dict): Заказ, содержащий информацию о сумме платежа и товаре.

        Исключения:
            PaymentProcessingError: Если сумма платежа меньше стоимости товара.
        """
        payment = order.get("payment", 0)
        item_price = prices.get(order.get("item"), 0)
        if payment < item_price:
            raise PaymentProcessingError(
                f"Недостаточно средств для покупки: '{order.get('item')}'."
            )
        print(
            f"Бухгалтерия: Платеж для товара '{order.get('item')}' успешно обработан."
        )
        super().handle(order)
