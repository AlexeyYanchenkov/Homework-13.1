class Category:
    name = str
    description = str
    product = list
    total_category = 0
    total_unique_products = 0

    def __init__(self, name: str, description: str, product: list):
        self.name = name
        self.description = description
        self.product = product

        Category.total_category +=1
        Category.total_unique_products += len(product)


class Product:
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
