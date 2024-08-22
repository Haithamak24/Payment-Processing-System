from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    """
    Abstract base class for different payment methods.
    Defines a common interface for processing payments.
    """
    @abstractmethod
    def pay(self, amount):
        """
        Process the payment for the given amount.
        :param amount: The amount to be paid.
        """
        pass
