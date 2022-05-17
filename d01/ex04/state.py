import sys

STATES = {"Oregon": "OR", "Alabama": "AL", "New Jersey": "NJ", "Colorado": "CO"}
CAPITAL_CITIES = {"OR": "Salem", "AL": "Montgomery", "NJ": "Trenton", "CO": "Denver"}


def func_state(city):
    codes = [code for code, capital in CAPITAL_CITIES.items() if city == capital]
    states = [state for state, code in STATES.items() if code in codes]
    ans = ", ".join(states)
    print(ans or "Unknown capital city")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        func_state(sys.argv[1])
