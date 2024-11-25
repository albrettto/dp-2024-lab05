from commands.process_order_command import ProcessOrderCommand
from handlers.stock_check_handler import StockCheckHandler
from handlers.order_handler import OrderHandler
from handlers.payment_processor_handler import PaymentProcessorHandler
from handlers.delivery_handler import DeliveryHandler
from exceptions.out_of_stock_error import OutOfStockError
from exceptions.payment_processing_error import PaymentProcessingError
from exceptions.delivery_error import DeliveryError


# Пример заказа с товаром, платежом и адресом
order = {"item": "Ручка", "payment": 100, "address": "Революционная, 21"}

# Создание цепочки обработчиков
stock_check_handler = StockCheckHandler()  # Проверка наличия товара на складе
payment_processor_handler = PaymentProcessorHandler()  # Обработка платежа
delivery_handler = DeliveryHandler()  # Доставка товара
order_handler = OrderHandler()  # Обработчик общего заказа (начальная точка)

# Настройка цепочки обработчиков: сначала проверка товара, затем обработка платежа и доставка
order_handler.set_next(stock_check_handler).set_next(
    payment_processor_handler
).set_next(delivery_handler)

try:
    # Создаем команду, которая будет выполнять всю цепочку обработчиков
    command = ProcessOrderCommand(order_handler, order)
    command.execute()  # Выполняем команду (обработку заказа)
except (OutOfStockError, PaymentProcessingError, DeliveryError) as e:
    # В случае возникновения ошибки в процессе выполнения цепочки, обрабатываем ее
    print(f"Обработчик ошибок: {e}")
