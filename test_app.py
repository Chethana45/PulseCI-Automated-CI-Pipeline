"""
Unit tests for PulseCI app.py module using Pytest.
Covers normal, boundary, and invalid input test cases.
"""

import pytest
from app import calculate_discount, calculate_total_price, validate_number


# =====================================================================
# 1. NORMAL CASES
# =====================================================================

def test_calculate_discount_normal():
    """Test standard discount calculation on a normal price."""
    # $100 with 20% discount = $20 discount
    assert calculate_discount(100.0, 20.0) == 20.0


def test_calculate_total_price_normal():
    """Test full calculation: unit price, quantity, discount, and tax."""
    # Unit price $50, quantity 2 = $100 subtotal
    # 10% discount = $10 discount -> $90 discounted subtotal
    # 10% tax on $90 = $9 tax -> final total = $99.00
    total = calculate_total_price(unit_price=50.0, quantity=2, discount_percent=10.0, tax_rate=10.0)
    assert total == 99.00


# =====================================================================
# 2. BOUNDARY CASES
# =====================================================================

def test_calculate_discount_zero_percent():
    """Boundary test: 0% discount should result in 0.0 discount amount."""
    assert calculate_discount(150.0, 0.0) == 0.0


def test_calculate_discount_full_hundred_percent():
    """Boundary test: 100% discount should equal the full price."""
    assert calculate_discount(250.0, 100.0) == 250.0


def test_calculate_total_price_minimum_quantity_and_zero_tax():
    """Boundary test: Minimum valid quantity (1) with 0% discount and 0% tax."""
    total = calculate_total_price(unit_price=19.99, quantity=1, discount_percent=0.0, tax_rate=0.0)
    assert total == 19.99


# =====================================================================
# 3. INVALID INPUT & ERROR CASES
# =====================================================================

def test_calculate_discount_exceeding_max_percentage():
    """Invalid case: Discount percentage greater than 100% must raise ValueError."""
    with pytest.raises(ValueError, match="Discount percentage cannot exceed 100%"):
        calculate_discount(100.0, 105.0)


def test_calculate_total_price_negative_unit_price():
    """Invalid case: Negative unit price must raise ValueError."""
    with pytest.raises(ValueError, match="'unit_price' cannot be less than 0.01"):
        calculate_total_price(unit_price=-5.0, quantity=2)


def test_calculate_total_price_zero_quantity():
    """Invalid case: Quantity less than 1 must raise ValueError."""
    with pytest.raises(ValueError, match="'quantity' must be at least 1"):
        calculate_total_price(unit_price=10.0, quantity=0)


def test_validate_number_non_numeric_type():
    """Invalid case: Passing a string or boolean instead of a number must raise TypeError."""
    with pytest.raises(TypeError, match="must be a valid number"):
        validate_number("free", "price")
