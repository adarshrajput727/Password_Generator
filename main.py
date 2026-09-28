"""Entry point for the VITyarthi Python Password Generator."""

from pathlib import Path
import sys

SRC_DIR = Path(__file__).resolve().parent / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from cli import run


if __name__ == "__main__":
    run()
