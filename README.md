Payment Processing System
Project Overview
This project implements a basic payment processing system with support for multiple payment methods, currency conversion, and discounts. It includes:

Payment Methods: Credit Card, PayPal, Cryptocurrency
Currency Conversion: Converts amounts between different currencies using fixed exchange rates
Discounts: Applies percentage-based and fixed amount discounts
Transaction Logging: Logs transaction details to the console
Setup Instructions
Prerequisites
Python 3.12.5 installed on your machine.
Installation
Clone the Repository

git clone https://github.com/Haithamak24/payment-processing-system.git
Navigate to the Project Directory

cd payment-processing-system
No Additional Dependencies: This project does not require any external libraries beyond Python’s standard library.

Usage
Run the Main Script

To run the payment processing system, execute the main.py script:
python src/main.py
Project Flow

Discount Application: A 10% discount is applied to the initial amount (100 USD).
Currency Conversion: The discounted amount is converted from USD to ILS and also from GBP and EUR to ILS, also vice versa is true.
Payment Processing: The converted amount is processed using the Credit Card or PayPal or Cryptocurrency payment method.
Logging: The transaction details are logged to the console.
Design Decisions
Abstract Base Class (PaymentMethod): Used to define a common interface for different payment methods, adhering to the Open/Closed Principle. This allows for easy extension with new payment methods.
Currency Conversion: Implemented with fixed exchange rates for simplicity. In a real-world scenario, you might use a dynamic service for real-time rates.
Discounts: Separate classes for percentage and fixed amount discounts, following the Single Responsibility Principle.
Logger: Basic console logging is used. For production, consider using Python’s logging module for more advanced logging features.
Modular Structure: Code is organized into separate modules for payment methods, currency conversion, discounts, and logging to improve maintainability and readability.
Testing
No automated tests are provided with this project. To test the functionality:

Run the main.py Script: Check the console output for the expected transaction processing and logging behavior.
Modify and Extend: Feel free to modify the code to add new features or methods, and verify their functionality by running the script.

also, I'd love to hear your comments, and thoughts about my project!
Thanks for passing by!
