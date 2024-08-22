from payment_methods import PaymentProcessor
from discounts import PercentageDiscount
from logger import TransactionLogger
from currency_converter import CurrencyConverter

def main():
    """
    Main function to demonstrate payment processing with discounts and currency conversion.
    """
    payment_processor = PaymentProcessor()
    discount = PercentageDiscount(10)  # 10% discount
    logger = TransactionLogger()
    converter = CurrencyConverter()

    amount_in_usd = 100
    discount_amount = discount.apply(amount_in_usd)
    print(f"Amount after discount: {discount_amount}")

    amount_in_ils = converter.convert(discount_amount, 'USD', 'ILS')
    print(f"Amount in ILS: {amount_in_ils}")

    payment_processor.process_payment(amount_in_ils, 'CreditCard')
    logger.log_transaction(amount_in_ils, 'CreditCard')

if __name__ == "__main__":
    main()
