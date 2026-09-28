"""Output formatting functions for the command-line interface."""


def print_banner() -> None:
    print("=" * 58)
    print("           PYTHON PASSWORD GENERATOR")
    print("=" * 58)
    print("Secure CLI project for generating and analysing passwords.")
    print()


def print_password(password: str, analysis: dict) -> None:
    print("-" * 58)
    print(f"Generated password : {password}")
    print(
        f"Strength            : {analysis['label']}"
    )
    print(
        f"Length              : {analysis['length']}"
    )
    print(
        f"Approx. entropy     : {analysis['entropy_bits']} bits"
    )
    print("-" * 58)


def print_help() -> None:
    print("Options:")
    print("  1. Generate a password by character counts")
    print("  2. Generate a password by total length")
    print("  3. Generate multiple passwords")
    print("  4. Analyse an existing password")
    print("  5. Exit")
