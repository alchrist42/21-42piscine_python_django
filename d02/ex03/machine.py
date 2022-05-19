from random import random, choice
from beverages import HotBeverage, Coffee, Tea, Cappuccino, Chocolate

class CoffeeMachine:
    def __init__(self) -> None:
        self.cupt_to_repair = 10

    class EmptyCup(HotBeverage):
        def __init__(
            self, price=0.90, name="empty cup", desc="An empty cup?! Gimme my money back!"
        ) -> None:
            super().__init__(price=price, name=name, desc=desc)
    
    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.cupt_to_repair = 10
        print("Machine has been repaired")

    def serve(self, tip: HotBeverage) -> HotBeverage:
        if self.cupt_to_repair <= 0:
            raise self.BrokenMachineException()
        # prepair drink
        self.cupt_to_repair -= 1
        if random() < 0.8:
            return tip()
        else:
            return self.EmptyCup()

def test():
    coffeeMachine = CoffeeMachine()
    for _ in range(22):
        try:
            print(coffeeMachine.serve(choice(
                [Coffee, Tea, Cappuccino, Chocolate])))
            print()
        except CoffeeMachine.BrokenMachineException as e:
            print("ERROR:", e)
            coffeeMachine.repair()


if __name__ == '__main__':
    test()