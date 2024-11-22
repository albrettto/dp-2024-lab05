from interfaces.iorder_hadler import IOrderHandler


class BaseOrderHandler(IOrderHandler):
    """
    Базовый обработчик для цепочки обязанностей.

    Этот класс предоставляет базовую функциональность для создания цепочки обработчиков. Он реализует методы
    для установки следующего обработчика и для передачи обработки заказа следующему элементу в цепочке.
    """

    def __init__(self):
        """
        Инициализирует базовый обработчик с отсутствующим следующим обработчиком.
        """
        self._next_handler = None

    def set_next(self, handler: "IOrderHandler") -> "IOrderHandler":
        """
        Устанавливает следующий обработчик в цепочке обязанностей.

        Аргументы:
            handler (IOrderHandler): Следующий обработчик в цепочке.

        Возвращает:
            IOrderHandler: Текущий обработчик (для создания цепочки вызовов).
        """
        self._next_handler = handler
        return handler

    def handle(self, order: dict):
        """
        Передает обработку заказа следующему обработчику в цепочке.

        Если следующий обработчик не установлен, то обработка не происходит.

        Аргументы:
            order (dict): Заказ, который должен быть обработан.
        """
        if self._next_handler:
            self._next_handler.handle(order)
