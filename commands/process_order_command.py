from interfaces.icommand import ICommand
from interfaces.iorder_hadler import IOrderHandler


class ProcessOrderCommand(ICommand):
    """
    Класс команды для обработки заказа.

    Этот класс реализует паттерн "Команда" и инкапсулирует операцию обработки заказа. Он делегирует выполнение действия
    обработчику заказа.
    """

    def __init__(self, handler: IOrderHandler, order: dict):
        """
        Инициализирует команду с обработчиком и данными заказа.

        Аргументы:
            handler (IOrderHandler): Обработчик для выполнения логики обработки заказа.
            order (dict): Данные заказа, включая товар, оплату и адрес.
        """
        self.handler = handler
        self.order = order

    def execute(self):
        """
        Выполняет команду, делегируя обработку заказа соответствующему обработчику.

        Вызовет метод handle у обработчика заказа для выполнения логики обработки.
        """
        self.handler.handle(self.order)
