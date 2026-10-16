"""Print FizzBuzz for numbers 1 through 100.

Run with: python fizzbuzz.py
"""


def main():
    for number in range(1, 101):
        if number % 15 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


if __name__ == "__main__":
    main()
