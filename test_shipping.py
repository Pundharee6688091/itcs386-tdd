# test_shipping.py
import pytest

from shipping import shipping_fee


# Rule 1: the weight must be more than 0 kg.
# Bug: breaks Rule 1. Exactly 0 kg is accepted (the code checks < 0, not <= 0).
@pytest.mark.parametrize("weight", [0, -0.5, -3])
def test_weight_not_more_than_zero_is_rejected(weight):
    with pytest.raises(ValueError, match="more than 0"):
        shipping_fee(weight)


# Rule 2: up to 1 kg costs 40 baht.
# Bug: breaks Rule 2. Exactly 1 kg costs 60, not 40 (the code checks < 1, not <= 1).
@pytest.mark.parametrize("weight", [0.1, 0.5, 1])
def test_up_to_1_kg_costs_40(weight):
    assert shipping_fee(weight) == 40


# Rule 3: more than 1 kg and up to 5 kg costs 60 baht.
@pytest.mark.parametrize("weight", [1.01, 3, 5])
def test_more_than_1_up_to_5_kg_costs_60(weight):
    assert shipping_fee(weight) == 60


# Rule 4: more than 5 kg costs 60 + 10 for every started kg above 5.
# Bug: breaks Rule 4. A part kilogram is rounded down instead of counted as
# started (int() cuts off the decimal, so 5.2 kg costs 60 instead of 70).
@pytest.mark.parametrize("weight, expected", [
    (5.2, 70),   # example from the docstring
    (5.01, 70),  # just above the 5 kg boundary
    (6, 70),     # exactly one extra kilogram
    (6.5, 80),   # second kilogram started
    (10, 110),   # five whole extra kilograms
])
def test_more_than_5_kg_adds_10_per_started_kg(weight, expected):
    assert shipping_fee(weight) == expected
