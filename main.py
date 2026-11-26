"""Monday, Reviewed in One Line — make.fun entry.

Running this program writes the entry line to /output/entry.txt.
A one-line review of Monday, star rating included.
"""

from pathlib import Path

ENTRY_TEXT = (
    "★☆☆☆☆: Arrived uninvited, stayed all day, "
    "and somehow brought Tuesday's problems along with it."
)

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry() -> None:
    """Write the Monday review to the output file as UTF-8."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_entry()

