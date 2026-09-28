"""Interactive command-line interface."""

from formatter import print_banner, print_help, print_password
from generator import generate_from_length, generate_multiple, generate_password
from strength import analyze_password, strength_message
from utils import read_int, read_yes_no
from validator import validate_password_length


def generate_by_counts() -> None:
    print("\n--- Generate by Character Counts ---")
    letters = read_int("Lowercase letters: ", 0, 128)
    uppercase = read_int("Uppercase letters: ", 0, 128)
    symbols = read_int("Symbols: ", 0, 128)
    numbers = read_int("Numbers: ", 0, 128)

    total = letters + uppercase + symbols + numbers
    validate_password_length(total)
    password = generate_password(letters, symbols, numbers, uppercase)
    print_password(password, analyze_password(password))


def generate_by_length() -> None:
    print("\n--- Generate by Total Length ---")
    length = read_int("Password length (4-128): ", 4, 128)
    lower = read_yes_no("Include lowercase letters?", True)
    upper = read_yes_no("Include uppercase letters?", True)
    numbers = read_yes_no("Include numbers?", True)
    symbols = read_yes_no("Include symbols?", True)

    password = generate_from_length(length, lower, upper, numbers, symbols)
    print_password(password, analyze_password(password))


def generate_batch() -> None:
    print("\n--- Generate Multiple Passwords ---")
    count = read_int("How many passwords (1-50)? ", 1, 50)
    length = read_int("Password length (4-128): ", 4, 128)
    passwords = generate_multiple(count, length)

    print("-" * 58)
    for index, password in enumerate(passwords, start=1):
        print(f"{index:>2}. {password}")
    print("-" * 58)


def analyse_existing() -> None:
    print("\n--- Password Strength Analysis ---")
    password = input("Enter password to analyse: ")
    if not password:
        print("Password cannot be empty.")
        return
    print(strength_message(analyze_password(password)))


def run() -> None:
    print_banner()
    while True:
        print_help()
        choice = input("\nChoose an option: ").strip()

        try:
            if choice == "1":
                generate_by_counts()
            elif choice == "2":
                generate_by_length()
            elif choice == "3":
                generate_batch()
            elif choice == "4":
                analyse_existing()
            elif choice == "5":
                print("Thank you for using the Password Generator.")
                break
            else:
                print("Please choose an option from 1 to 5.")
        except ValueError as error:
            print(f"Error: {error}")

        print()


if __name__ == "__main__":
    run()
