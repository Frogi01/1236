class Pizza:
    def __init__(self):
        self.size = None
        self.crust = None
        self.toppings = []

    def __str__(self):
        toppings = ", ".join(self.toppings)
        return f"Пицца размера {self.size}, с корочкой {self.crust}, с добавками: {toppings}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def set_crust(self, crust):
        self.pizza.crust = crust
        return self

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def get_pizza(self):
        return self.pizza

# Использование строителя для создания объекта
builder = PizzaBuilder()
pizza = builder.set_size("средняя").set_crust("тонкая").add_topping("грибы").add_topping("сыр").get_pizza()
print(pizza)  