"""Convert temperatures between Celsius and Fahrenheit.

Run with: python temperature.py
"""


def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    try:
        choice = input("Choose 1 or 2: ").strip()
        if choice not in ("1", "2"):
            print("Please choose 1 or 2.")
            return

        temperature = float(input("Enter the temperature: "))
        if choice == "1":
            result = temperature * 9 / 5 + 32
            print(f"{temperature:g} °C = {result:g} °F")
        else:
            result = (temperature - 32) * 5 / 9
            print(f"{temperature:g} °F = {result:g} °C")
    except ValueError:
        print("Please enter a valid number for the temperature.")
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
