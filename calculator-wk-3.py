def calculate_discount(price, discount_percent):
    """
    Calculate the discounted price given the original price and discount percentage.

    :param price: Original price of the item
    :param discount_percent: Discount percentage to apply
    :return: Discounted price
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else: return price
    # Calculate the discount amount and apply it to the price

price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20:
    print(f"Discount applied! The final price is: {final_price}")
else:
    print(f"No discount applied. The price remains: {final_price}")
    