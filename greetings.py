"""Ask for a name and display a friendly greeting."""


def main():
    name = input("What is your name? ").strip()
    if name:
        print(f"Hello, {name}! Welcome to Python programming!")
    else:
        print("Hello, friend! Welcome to Python programming!")


if __name__ == "__main__":
    main()
