"""Swap two values. Run with: python swap.py"""


def main():
    first = input("Enter the first value: ")
    second = input("Enter the second value: ")

    print(f"Before swapping: first = {first}, second = {second}")
    first, second = second, first
    print(f"After swapping: first = {first}, second = {second}")


if __name__ == "__main__":
    main()
