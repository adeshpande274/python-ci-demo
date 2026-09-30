def calculate_total(amount, tax_rate):
    """Return the amount after adding tax."""
    if amount < 0:
        raise ValueError("amount cannot be negative")
    if tax_rate < 0:
        raise ValueError("tax rate cannot be negative")

    return round(amount * (1 + tax_rate / 100), 2)


if __name__ == "__main__":
    total = calculate_total(100, 18)
    print(f"Total with tax: {total:.2f}")
