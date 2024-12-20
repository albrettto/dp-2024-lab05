class DeliveryError(Exception):
    """
    Исключение, возникающее при ошибке доставки.

    Это исключение возникает в случае, если доставка не может быть выполнена
    из-за отсутствующего или неправильного адреса доставки.
    """

    default_message = "Доставка не удалась из-за отсутствия адреса."

    def __init__(self, message: str | None = None):
        """
        Инициализирует исключение с переданным сообщением или сообщением по умолчанию.

        Аргументы:
            message (str | None): Сообщение для исключения. Если не передано, используется сообщение по умолчанию.
        """
        super().__init__(message or self.default_message)
