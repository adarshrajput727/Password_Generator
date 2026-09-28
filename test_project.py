"""Validation tests for the core project modules."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from generator import generate_from_length, generate_password, generate_multiple
from strength import analyze_password
from validator import validate_count


def test_validate_count():
    assert validate_count("5", "letters", 0, 10) == 5


def test_generate_by_counts():
    password = generate_password(3, 2, 2, 2)
    assert len(password) == 9
    assert sum(c.islower() for c in password) == 3
    assert sum(c.isupper() for c in password) == 2
    assert sum(c.isdigit() for c in password) == 2
    assert sum(not c.isalnum() for c in password) == 2


def test_generate_by_length():
    password = generate_from_length(16)
    assert len(password) == 16


def test_generate_multiple():
    passwords = generate_multiple(5, 12)
    assert len(passwords) == 5
    assert all(len(password) == 12 for password in passwords)


def test_strength_analysis():
    result = analyze_password("Abcd!1234xyz")
    assert result["length"] == 12
    assert result["categories_used"] == 4


if __name__ == "__main__":
    test_validate_count()
    test_generate_by_counts()
    test_generate_by_length()
    test_generate_multiple()
    test_strength_analysis()
    print("All tests passed.")
