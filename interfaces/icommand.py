from abc import ABC, abstractmethod


class ICommand(ABC):
    """
    Интерфейс команды.

    Этот интерфейс определяет метод `execute`, который должен быть реализован в классах команд.
    """

    @abstractmethod
    def execute(self):
        """
        Выполняет команду.

        Этот метод должен быть реализован в классе команды. Он определяет, что должно быть сделано
        при выполнении команды.
        """
        pass