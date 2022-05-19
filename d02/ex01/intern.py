class Intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name.") -> None:
        self.name = name

    class Coffee:
        def __str__(self) -> str:
            return "This is the worst coffee you ever tasted."

    def __str__(self) -> str:
        return self.name

    def work(self) -> str:
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self) -> Coffee():
        return Intern.Coffee()


def test():
    intern1 = Intern()
    intern2 = Intern("Max")
    print(intern1)
    print(intern2)
    try:
        intern1.work()
    except Exception as e:
        print(e)
    print(intern2.make_coffee())


if __name__ == "__main__":
    test()
