#! /usr/bin/python3
# docstring

def apply_discount(price: int, discount: float = 0.0) -> int:
    """Apply Discount Percent and Calculate Final Price"""
    final_price = int(price * (1 - discount))
    assert 0 < final_price <= price, "Why this AssertionError never Raised!"

    return final_price


# and this is the optimization of the above code:
def optimize_apply_discount(price: int, discount: float = 0.0) -> int:
    """
    Apply Discount Percent and Calculate Final Price
    if discount > 1.0: the final price will be zero
    """
    final_price = max(int(price * (1 - discount)), 0)
    if not (0 < final_price <= price):
        raise ValueError("the final price is not in the range")

    return final_price


print(apply_discount(100, 1.2))
