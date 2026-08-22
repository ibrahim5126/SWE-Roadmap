"""
Day 1 — Command-line Calculator

Supports +, -, *, / with proper input validation and division-by-zero
handling. Loops until the user chooses to quit, instead of running once
and dying like a tutorial script.
"""

OPERATORS = {"+", "-", "*", "/"}


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def calculate(operator, a, b):
    """Dispatch to the right operation. Raises ValueError for a bad operator."""
    if operator == "+":
        return add(a, b)
    if operator == "-":
        return subtract(a, b)
    if operator == "*":
        return multiply(a, b)
    if operator == "/":
        return divide(a, b)
    raise ValueError(f"Unsupported operator: {operator!r}")


def get_number(prompt):
    """Keep asking until the user gives a valid float."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print(f"'{raw}' isn't a valid number. Try again.")


def get_operator():
    while True:
        op = input(f"Enter an operator ({', '.join(sorted(OPERATORS))}): ").strip()
        if op in OPERATORS:
            return op
        print(f"'{op}' isn't a supported operator.")


def main():
    print("Simple CLI Calculator — Ctrl+C or 'q' to quit.\n")

    while True:
        first_input = input("\nFirst number (or 'q' to quit): ").strip()
        if first_input.lower() == "q":
            print("Goodbye.")
            break

        try:
            number_1 = float(first_input)
        except ValueError:
            print(f"'{first_input}' isn't a valid number. Try again.")
            continue

        operator = get_operator()
        number_2 = get_number("Second number: ")

        try:
            result = calculate(operator, number_1, number_2)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            continue

        print(f"{number_1} {operator} {number_2} = {result}")


if __name__ == "__main__":
    main()
