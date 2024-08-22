from abstract_classes import PaymentMethod

class CreditCard(PaymentMethod):
    """
    Payment method for Credit Card.
    """
    def pay(self, amount):
        """
        Process payment via credit card.
        :param amount: Amount to be paid.
        """
        print(f"Processing credit card payment of {amount} ILS")

class PayPal(PaymentMethod):
    """
    Payment method for PayPal.
    """
    def pay(self, amount):
        """
        Process payment via PayPal.
        :param amount: Amount to be paid.
        """
        print(f"Processing PayPal payment of {amount} ILS")

class Cryptocurrency(PaymentMethod):
    """
    Payment method for Cryptocurrency.
    """
    def pay(self, amount):
        """
        Process payment via cryptocurrency.
        :param amount: Amount to be paid.
        """
        print(f"Processing crypto payment of {amount} ILS")

class PaymentProcessor:
    """
    Handles the processing of payments using various methods.
    """
    def __init__(self):
        self.methods = {
            'CreditCard': CreditCard(),
            'PayPal': PayPal(),
            'Crypto': Cryptocurrency()
        }

    def process_payment(self, amount, method):
        """
        Process the payment using the specified method.
        :param amount: Amount to be paid.
        :param method: Payment method to use.
        """
        if method in self.methods:
            self.methods[method].pay(amount)
        else:
            raise ValueError(f"Payment method {method} not supported.")
