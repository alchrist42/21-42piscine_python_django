import sys

STATES = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}
CAPITAL_CITIES = {"OR": "Salem", "AL": "Montgomery", "NJ": "Trenton", "CO": "Denver"}


def func_city(city):
    capital = CAPITAL_CITIES.get(STATES.get(city), "Unknown state")
    print(capital)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        func_city(sys.argv[1])
