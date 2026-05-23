"""wordcount — a tiny text-stats library."""


def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in `text`."""
    return len(text.split())


def count_lines(text: str) -> int:
    """Return the number of lines in `text`."""
    if not text:
        return 0
    parts = text.split("\n")
    return len(parts) - 1 if parts[-1] == "" else len(parts)
