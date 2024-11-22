import unittest
from exceptions.out_of_stock_error import OutOfStockError
from exceptions.payment_processing_error import PaymentProcessingError
from exceptions.delivery_error import DeliveryError
from handlers.stock_check_handler import StockCheckHandler
from handlers.payment_processor_handler import PaymentProcessorHandler
from handlers.delivery_handler import DeliveryHandler
from handlers.order_handler import OrderHandler
from commands.process_order_command import ProcessOrderCommand


class TestOrderProcessing(unittest.TestCase):
    """
    Тестирование процесса обработки заказа в интернет-магазине, включая проверку наличия товара,
    обработку платежа и доставку. Также включает проверку работы цепочки обязанностей с исключениями.
    """

    def setUp(self):
        """
        Настроим начальные данные для тестов: заказы с разными статусами (в наличии, недостаточно средств, неверный адрес).
        """
        self.order_in_stock = {
            "item": "Ручка",
            "payment": 100,
            "address": "Революционная, 21",
        }
        self.order_out_of_stock = {
            "item": "Линейка",
            "payment": 100,
            "address": "Революционная, 21",
        }
        self.order_insufficient_funds = {
            "item": "Ручка",
            "payment": 30,
            "address": "Революционная, 21",
        }
        self.order_invalid_address = {
            "item": "Ручка",
            "payment": 100,
            "address": "Неизвестный адрес",
        }

    def test_check_stock_success(self):
        """
        Проверка успешной обработки наличия товара на складе.
        В случае успешного выполнения ошибки не будет.
        """
        stock_check_handler = StockCheckHandler()
        stock_check_handler.handle(self.order_in_stock)

    def test_check_stock_failure(self):
        """
        Проверка ошибки при отсутствии товара на складе.
        Ожидается исключение OutOfStockError.
        """
        stock_check_handler = StockCheckHandler()
        with self.assertRaises(OutOfStockError):
            stock_check_handler.handle(self.order_out_of_stock)

    def test_process_payment_success(self):
        """
        Проверка успешной обработки платежа.
        В случае успешного выполнения ошибки не будет.
        """
        payment_processor_handler = PaymentProcessorHandler()
        payment_processor_handler.handle(self.order_in_stock)

    def test_process_payment_failure(self):
        """
        Проверка ошибки при недостаточности средств для выполнения платежа.
        Ожидается исключение PaymentProcessingError.
        """
        payment_processor_handler = PaymentProcessorHandler()
        with self.assertRaises(PaymentProcessingError):
            payment_processor_handler.handle(self.order_insufficient_funds)

    def test_delivery_success(self):
        """
        Проверка успешной доставки товара.
        В случае успешного выполнения ошибки не будет.
        """
        delivery_handler = DeliveryHandler()
        delivery_handler.handle(self.order_in_stock)

    def test_delivery_failure(self):
        """
        Проверка ошибки при неверном адресе для доставки.
        Ожидается исключение DeliveryError.
        """
        delivery_handler = DeliveryHandler()
        with self.assertRaises(DeliveryError):
            delivery_handler.handle(self.order_invalid_address)

    def test_process_order_command_success(self):
        """
        Проверка успешного выполнения всей цепочки обработчиков (проверка наличия товара, обработка платежа, доставка).
        Ожидается, что не возникнет ошибок.
        """
        order_handler = OrderHandler()
        stock_check_handler = StockCheckHandler()
        payment_processor_handler = PaymentProcessorHandler()
        delivery_handler = DeliveryHandler()

        order_handler.set_next(stock_check_handler).set_next(
            payment_processor_handler
        ).set_next(delivery_handler)

        command = ProcessOrderCommand(order_handler, self.order_in_stock)
        try:
            command.execute()
        except Exception as e:
            self.fail(f"Unexpected exception raised: {e}")

    def test_process_order_command_failure(self):
        """
        Проверка, что выбрасываются исключения при ошибках в цепочке обработчиков.
        Ожидается исключение при наличии ошибок на любом из этапов (отсутствие товара, недостаточно средств или неверный адрес).
        """
        order_handler = OrderHandler()
        stock_check_handler = StockCheckHandler()
        payment_processor_handler = PaymentProcessorHandler()
        delivery_handler = DeliveryHandler()

        order_handler.set_next(stock_check_handler).set_next(
            payment_processor_handler
        ).set_next(delivery_handler)

        # Тест на отсутствие товара
        command = ProcessOrderCommand(order_handler, self.order_out_of_stock)
        with self.assertRaises(OutOfStockError):
            command.execute()

        # Тест на недостаточность средств
        command = ProcessOrderCommand(order_handler, self.order_insufficient_funds)
        with self.assertRaises(PaymentProcessingError):
            command.execute()

        # Тест на неверный адрес
        command = ProcessOrderCommand(order_handler, self.order_invalid_address)
        with self.assertRaises(DeliveryError):
            command.execute()


if __name__ == "__main__":
    unittest.main()
