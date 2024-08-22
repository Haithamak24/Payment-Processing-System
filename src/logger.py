class TransactionLogger:
    """
    Logs transaction details to the console.
    For a real application, consider using Python's logging module.
    """
    def log_transaction(self, amount, method):
        """
        Log the transaction details.
        :param amount: Amount processed.
        :param method: Payment method used.
        """
        print(f"Transaction logged: {amount} ILS paid using {method}.")
