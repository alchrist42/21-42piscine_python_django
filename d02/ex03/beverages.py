class HotBeverage:
    def __init__(
        self, price=0.30, name="hot beverage", desc="Just some hot water in a cup."
    ):
        self.price = price
        self.name = name
        self.desc = desc

    def description(self) -> str:
        return self.desc

    def __str__(self) -> str:
        return f"name : {self.name}\nprice: {self.price:0.2f}\ndescription: {self.desc}"


class Coffee(HotBeverage):
    def __init__(
        self, price=0.40, name="coffee", desc="A coffee, to stay awake."
    ) -> None:
        super().__init__(price=price, name=name, desc=desc)


class Tea(HotBeverage):
    def __init__(
        self, price=0.30, name="tea", desc="Just some hot water in a cup."
    ) -> None:
        super().__init__(price=price, name=name, desc=desc)


class Chocolate(HotBeverage):
    def __init__(
        self, price=0.50, name="chocolate", desc="Chocolate, sweet chocolate..."
    ) -> None:
        super().__init__(price=price, name=name, desc=desc)


class Cappuccino(HotBeverage):
    def __init__(
        self, price=0.45, name="cappuccino", desc="Un po’ di Italia nella sua tazza!"
    ) -> None:
        super().__init__(price=price, name=name, desc=desc)


def test():
    print(HotBeverage())
    print(Coffee())
    print(Tea())
    print(Chocolate())
    print(Cappuccino())


if __name__ == "__main__":
    test()
