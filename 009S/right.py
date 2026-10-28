def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


def apply_discount(total, discount):
    """Apply a percentage discount to the total amount."""
    return total * (1 - discount)


def generate_invoice(items, discount):
    total = calculate_total(items)
    final = apply_discount(total, discount)
    return {"total": total, "final": final}
