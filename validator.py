"""Input validation and normalization utilities."""

from config import MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH


def validate_count(value: str, field_name: str, minimum: int = 0, maximum: int = 128) -> int:
    """Validate a non-negative integer entered by the user."""
    try:
        number = int(value)
    except ValueError as exc:
        raise ValueError(f"{field_name} must be a whole number.") from exc

    if number < minimum or number > maximum:
        raise ValueError(
            f"{field_name} must be between {minimum} and {maximum}."
        )
    return number


def validate_password_length(length: int) -> int:
    """Validate the requested password length."""
    if not MIN_PASSWORD_LENGTH <= length <= MAX_PASSWORD_LENGTH:
        raise ValueError(
            f"Password length must be between {MIN_PASSWORD_LENGTH} "
            f"and {MAX_PASSWORD_LENGTH}."
        )
    return length


def validate_composition(
    letters: int,
    symbols: int,
    numbers: int,
    uppercase: int,
) -> None:
    """Ensure requested character counts form a valid password."""
    counts = [letters, symbols, numbers, uppercase]
    if any(count < 0 for count in counts):
        raise ValueError("Character counts cannot be negative.")

    total = sum(counts)
    if total == 0:
        raise ValueError("At least one character must be requested.")
