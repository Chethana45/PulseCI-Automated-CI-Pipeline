"""
PulseCI - Core Application Module
Demonstrates business logic for e-commerce calculations with validation.
"""

from typing import Union


def validate_number(value: Union[int, float], name: str, min_val: float = 0.0) -> float:
    """
    Validates that a numerical input is a float/int and satisfies minimum value constraints.
    """
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError(f"'{name}' must be a valid number (integer or float).")
    if value < min_val:
        raise ValueError(f"'{name}' cannot be less than {min_val}.")
    return float(value)


def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculates the discounted amount from a base price.

    :param price: Original price (must be >= 0)
    :param discount_percent: Discount percentage between 0 and 100
    :return: Discount amount in currency units
    """
    valid_price = validate_number(price, "price", min_val=0.0)
    valid_discount = validate_number(discount_percent, "discount_percent", min_val=0.0)

    if valid_discount > 100.0:
        raise ValueError("Discount percentage cannot exceed 100%.")

    return round((valid_price * valid_discount) / 100.0, 2)


def calculate_total_price(unit_price: float, quantity: int, discount_percent: float = 0.0, tax_rate: float = 0.0) -> float:
    """
    Calculates the final payable price after applying discount and sales tax.

    :param unit_price: Price per unit (> 0)
    :param quantity: Number of items purchased (integer >= 1)
    :param discount_percent: Discount percentage (0 to 100)
    :param tax_rate: Tax percentage (0 to 100)
    :return: Total final price rounded to 2 decimal places
    """
    valid_unit_price = validate_number(unit_price, "unit_price", min_val=0.01)
    
    if not isinstance(quantity, int) or isinstance(quantity, bool):
        raise TypeError("'quantity' must be an integer.")
    if quantity < 1:
        raise ValueError("'quantity' must be at least 1.")

    valid_tax = validate_number(tax_rate, "tax_rate", min_val=0.0)
    if valid_tax > 100.0:
        raise ValueError("Tax rate cannot exceed 100%.")

    subtotal = valid_unit_price * quantity
    discount_amount = calculate_discount(subtotal, discount_percent)
    discounted_subtotal = subtotal - discount_amount
    tax_amount = (discounted_subtotal * valid_tax) / 100.0

    return round(discounted_subtotal + tax_amount, 2)


def main():
    """Application entry point demonstrating calculations."""
    print("=" * 50)
    print(" PulseCI E-Commerce Pricing Engine ")
    print("=" * 50)

    sample_price = 49.99
    sample_qty = 3
    sample_discount = 10.0  # 10%
    sample_tax = 8.5        # 8.5%

    print(f"Item Unit Price    : ${sample_price:.2f}")
    print(f"Quantity           : {sample_qty}")
    print(f"Discount Rate      : {sample_discount}%")
    print(f"Tax Rate           : {sample_tax}%")

    total = calculate_total_price(sample_price, sample_qty, sample_discount, sample_tax)
    print("-" * 50)
    print(f"Final Total Price  : ${total:.2f}")
    print("=" * 50)
    print("[SUCCESS] Application executed cleanly.")


if __name__ == "__main__":
    main()
