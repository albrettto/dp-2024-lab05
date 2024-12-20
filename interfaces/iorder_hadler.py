from abc import ABC, abstractmethod


class IOrderHandler(ABC):
    """
    Интерфейс обработчика заказа.

    Этот интерфейс определяет методы для установки следующего обработчика в цепочке обязанностей
    и обработки заказа. Классы, реализующие этот интерфейс, будут участвовать в цепочке обработчиков,
    обрабатывая заказ по этапам (проверка товара, обработка платежа, доставка и т.д.).
    """

    @abstractmethod
    def set_next(self, handler: "IOrderHandler") -> "IOrderHandler":
        """
        Устанавливает следующий обработчик в цепочке.

        Аргументы:
            handler (IOrderHandler): Следующий обработчик в цепочке обязанностей.

        Возвращает:
            IOrderHandler: Возвращает текущий обработчик для возможности цепочки вызовов.
        """
        raise NotImplementedError("Метод 'set_next' должен быть реализован в подклассе")

    @abstractmethod
    def handle(self, order: dict):
        """
        Обрабатывает заказ.

        Этот метод выполняет действия с заказом, например, проверку товара, обработку платежа или
        планирование доставки, и передает заказ следующему обработчику в цепочке.

        Аргументы:
            order (dict): Заказ, который передается для обработки.
        """
        raise NotImplementedError("Метод 'handle' должен быть реализован в подклассе")
