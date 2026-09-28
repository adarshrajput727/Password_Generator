"""Small reusable helper functions."""


def read_int(prompt: str, minimum: int = 0, maximum: int = 128) -> int:
    """Read and validate an integer from the terminal."""
    from validator import validate_count

    while True:
        value = input(prompt).strip()
        try:
            return validate_count(value, "Input", minimum, maximum)
        except ValueError as error:
            print(f"Invalid input: {error}")


def read_yes_no(prompt: str, default: bool = True) -> bool:
    """Read a yes/no response with a default value."""
    suffix = " [Y/n]: " if default else " [y/N]: "
    while True:
        answer = input(prompt + suffix).strip().lower()
        if not answer:
            return default
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please enter y/yes or n/no.")
