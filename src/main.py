from payment_methods import PaymentProcessor
from discounts import PercentageDiscount
from logger import TransactionLogger
from currency_converter import CurrencyConverter

def main():
    """
    Main function to demonstrate payment processing with discounts and currency conversion.
    """
    payment_processor = PaymentProcessor()
    discount = PercentageDiscount(30)  # 30% discount
    logger = TransactionLogger()
    converter = CurrencyConverter()

    amount_in_usd = 150
    discount_amount = discount.apply(amount_in_usd)
    amount_after_discount = discount_amount

    amount_in_ils = converter.convert(amount_after_discount, 'USD', 'ILS')

    payment_processor.process_payment(amount_in_ils, 'CreditCard')

    logger.log_transaction(amount_in_ils, 'CreditCard')

if __name__ == "__main__":
    main()
