"""A simple calculator. Run with: python calculator.py"""


def calculate(first, operator, second):
    """Calculate a result using +, -, *, or /."""
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ValueError("Cannot divide by zero.")
        return first / second
    raise ValueError("Please choose +, -, *, or /.")


def main():
    print("Simple Calculator")
    print("Type q at any prompt to quit.")
    while True:
        try:
            first = input("First number: ").strip()
            if first.lower() == "q":
                break
            operator = input("Operation (+, -, *, /): ").strip()
            if operator.lower() == "q":
                break
            second = input("Second number: ").strip()
            if second.lower() == "q":
                break
            result = calculate(float(first), operator, float(second))
            print(f"Result: {result:g}\n")
        except ValueError as error:
            print(f"Error: {error}\n")
        except (EOFError, KeyboardInterrupt):
            print()
            break


if __name__ == "__main__":
    main()
