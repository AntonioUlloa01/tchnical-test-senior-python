def products_order(products):
    inventory = {
        'apple': 10,
        'banana': 5,
        'orange': 8,
        'grape': 15,
        'kiwi': 3
    }

    products_order_total = 0

    for product, quantity in products.items():

        if inventory.get(product) is None:
            print(f"Error: {product} not found in inventory")
            return f"Error: {product} not found in inventory"

        if quantity > inventory[product]:
            print(f"Error: Not enough {product}s in stock!")
            return f"Error: Not enough {product}s in stock!"

        products_order_total += quantity * 5
        inventory[product] -= quantity

    for item, stock in inventory.items():
        print(f"{item}: {stock} in stock")
