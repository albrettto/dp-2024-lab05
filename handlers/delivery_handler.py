from handlers.base_order_handler import BaseOrderHandler
from exceptions.delivery_error import DeliveryError
from db.database import pick_up_point


class DeliveryHandler(BaseOrderHandler):
    """
    Обработчик этапа доставки заказа.

    Этот класс реализует обработку этапа доставки в цепочке обязанностей. Он проверяет, существует ли указанный
    адрес в базе данных пунктов выдачи, и если адрес валиден, планирует доставку.
    """

    def handle(self, order: dict):
        """
        Обрабатывает этап доставки заказа.

        Проверяет, существует ли указанный адрес в базе данных пунктов выдачи. Если адрес корректен, планируется доставка.
        Если адрес не найден, выбрасывается исключение `DeliveryError`.

        Аргументы:
            order (dict): Заказ, содержащий информацию о пункте выдачи.

        Исключения:
            DeliveryError: Если адрес пункта выдачи не существует в базе данных.
        """
        address = order.get("address")
        if not address in pick_up_point:
            raise DeliveryError(f"Несуществующий адрес пункта выдачи: {address}.")

        print(f"Курьер: Запланирована доставка до пункта выдачи: {address}.")
        super().handle(order)
