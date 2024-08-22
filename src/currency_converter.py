class CurrencyConverter:
    """
    Converts amounts between different currencies based on exchange rates.
    """
    def __init__(self):
        # Exchange rates are for 1 unit of each currency to USD
        self.exchange_rates = {
            "USD": 1.0,       # Base currency
            "ILS": 1 / 3.75,  # 1 USD = 3.75 ILS => 1 ILS = 1 / 3.75 USD
            "EUR": 1 / 1.1,   # Example conversion rates
            "GBP": 1 / 1.2
        }

    def convert(self, amount, from_currency, to_currency):
        """
        Convert the amount from one currency to another.
        :param amount: Amount to convert.
        :param from_currency: Currency to convert from.
        :param to_currency: Currency to convert to.
        :return: Converted amount.
        """
        if from_currency == to_currency:
            return amount

        if from_currency in self.exchange_rates and to_currency in self.exchange_rates:
            # Convert amount to base currency (USD)
            amount_in_base_currency = amount * self.exchange_rates[from_currency]
            print(f"Amount in base currency (USD): {amount_in_base_currency}")

            # Convert from base currency (USD) to target currency
            result = amount_in_base_currency / self.exchange_rates[to_currency]
            print(f"Conversion result: {result}")

            return result
        else:
            raise ValueError("Unsupported currency")
