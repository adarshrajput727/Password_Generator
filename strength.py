"""Password composition and strength analysis."""

import math
import string


def analyze_password(password: str) -> dict:
    """Return measurable composition information for a password."""
    length = len(password)
    categories = {
        "lowercase": any(c.islower() for c in password),
        "uppercase": any(c.isupper() for c in password),
        "digits": any(c.isdigit() for c in password),
        "symbols": any(c in string.punctuation for c in password),
    }
    categories_used = sum(categories.values())

    # Approximate entropy is based on the size of the character pool.
    pool = 0
    if categories["lowercase"]:
        pool += 26
    if categories["uppercase"]:
        pool += 26
    if categories["digits"]:
        pool += 10
    if categories["symbols"]:
        pool += len(string.punctuation)

    entropy = length * math.log2(pool) if pool else 0.0

    if length < 8 or categories_used <= 1:
        label = "Weak"
    elif length < 12 or categories_used == 2:
        label = "Moderate"
    elif length < 16 or categories_used == 3:
        label = "Strong"
    else:
        label = "Very Strong"

    return {
        "length": length,
        "categories_used": categories_used,
        "entropy_bits": round(entropy, 2),
        "label": label,
        "categories": categories,
    }


def strength_message(analysis: dict) -> str:
    """Create a concise human-readable strength summary."""
    return (
        f"{analysis['label']} | "
        f"Length: {analysis['length']} | "
        f"Categories: {analysis['categories_used']}/4 | "
        f"Approx. entropy: {analysis['entropy_bits']} bits"
    )
