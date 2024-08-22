class PercentageDiscount:
    """
    Applies a percentage-based discount to an amount.
    """
    def __init__(self, percentage):
        self.percentage = percentage

    def apply(self, amount):
        """
        Apply the discount to the given amount.
        :param amount: Original amount.
        :return: Amount after discount.
        """
        return amount * (1 - self.percentage / 100)

class FixedAmountDiscount:
    """
    Applies a fixed-amount discount to an amount.
    """
    def __init__(self, amount):
        self.amount = amount

    def apply(self, amount):
        """
        Apply the discount to the given amount.
        :param amount: Original amount.
        :return: Amount after discount.
        """
        return amount - self.amount
