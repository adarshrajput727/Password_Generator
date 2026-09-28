"""Secure password generation logic."""

import secrets
import random

from config import DIGITS, LOWERCASE_LETTERS, SYMBOLS, UPPERCASE_LETTERS
from validator import validate_composition


def _secure_choice(characters: str) -> str:
    """Return one cryptographically secure random character."""
    return secrets.choice(characters)


def generate_password(
    letters: int,
    symbols: int,
    numbers: int,
    uppercase: int = 0,
) -> str:
    """Generate and securely shuffle a password with requested composition."""
    validate_composition(letters, symbols, numbers, uppercase)

    characters = (
        [_secure_choice(LOWERCASE_LETTERS) for _ in range(letters)]
        + [_secure_choice(SYMBOLS) for _ in range(symbols)]
        + [_secure_choice(DIGITS) for _ in range(numbers)]
        + [_secure_choice(UPPERCASE_LETTERS) for _ in range(uppercase)]
    )

    # SystemRandom uses the OS-backed secure random source for shuffling.
    random.SystemRandom().shuffle(characters)
    return "".join(characters)


def generate_from_length(
    length: int,
    include_lowercase: bool = True,
    include_uppercase: bool = True,
    include_numbers: bool = True,
    include_symbols: bool = True,
) -> str:
    """Generate a password from a requested total length and character groups."""
    groups = []
    if include_lowercase:
        groups.append(LOWERCASE_LETTERS)
    if include_uppercase:
        groups.append(UPPERCASE_LETTERS)
    if include_numbers:
        groups.append(DIGITS)
    if include_symbols:
        groups.append(SYMBOLS)

    if not groups:
        raise ValueError("At least one character group must be enabled.")
    if length < len(groups):
        raise ValueError(
            "Length must be at least the number of enabled character groups."
        )

    password = [_secure_choice(group) for group in groups]
    combined = "".join(groups)
    password.extend(_secure_choice(combined) for _ in range(length - len(groups)))
    random.SystemRandom().shuffle(password)
    return "".join(password)


def generate_multiple(
    count: int,
    length: int,
    include_lowercase: bool = True,
    include_uppercase: bool = True,
    include_numbers: bool = True,
    include_symbols: bool = True,
) -> list[str]:
    """Generate multiple passwords using the length-based generator."""
    if count < 1 or count > 50:
        raise ValueError("Number of passwords must be between 1 and 50.")

    return [
        generate_from_length(
            length,
            include_lowercase,
            include_uppercase,
            include_numbers,
            include_symbols,
        )
        for _ in range(count)
    ]
