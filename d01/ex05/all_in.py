import sys

STATES = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}
CAPITAL_CITIES = {"OR": "Salem", "AL": "Montgomery", "NJ": "Trenton", "CO": "Denver"}


def func_state(city):
    codes = [code for code, capital in CAPITAL_CITIES.items() if city == capital]
    states = [state for state, code in STATES.items() if code in codes]
    if states:
        return states[0]
    return None


def func_city(state):
    return CAPITAL_CITIES.get(STATES.get(state))


def func_all(s):
    names = [arg.strip(" ").title() for arg in s.split(",") if arg.strip(" ")]
    for name in names:
        if func_state(name):
            print(f"{name} is the capital of {func_state(name)}")
        elif func_city(name):
            print(f"{func_city(name)} is the capital of {name}")
        else:
            print(f"{name} is neither a capital city nor a state")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        func_all(sys.argv[1])
