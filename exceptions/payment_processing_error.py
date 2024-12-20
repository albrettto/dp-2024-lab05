class PaymentProcessingError(Exception):
    """
    Исключение, возникающее при ошибках обработки платежа.

    Это исключение возникает, если платеж не может быть обработан, например, из-за недостаточности средств
    на счете или других проблем с процессом оплаты.
    """

    default_message = (
        "Сбой в обработке платежа произошел из-за недостаточности средств."
    )

    def __init__(self, message: str | None):
        """
        Инициализирует исключение с переданным сообщением или сообщением по умолчанию.

        Аргументы:
            message (str | None): Сообщение для исключения. Если не передано, используется сообщение по умолчанию.
        """
        super().__init__(message or self.default_message)
