class CurrencyConverter:
    """
    Provides currency conversion functionalities.
    Uses fixed exchange rates for simplicity.
    """
    def __init__(self):
        self.exchange_rates = {
            "ILS": 1.0,
            "USD": 3.75,
            "EUR": 4.00,
            "GBP": 4.50
        }

    def convert(self, amount, from_currency, to_currency):
        """
        Convert amount from one currency to another.
        :param amount: Amount to convert.
        :param from_currency: Currency to convert from.
        :param to_currency: Currency to convert to.
        :return: Converted amount.
        """
        if from_currency == to_currency:
            return amount
        if from_currency in self.exchange_rates and to_currency in self.exchange_rates:
            amount_in_ils = amount * (self.exchange_rates["ILS"] / self.exchange_rates[from_currency])
            result = amount_in_ils * (self.exchange_rates[to_currency] / self.exchange_rates["ILS"])
            return result
        else:
            raise ValueError("Unsupported currency")
