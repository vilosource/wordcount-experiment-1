"""wordcount — a tiny text-stats library."""


def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in `text`."""
    return len(text.split())


def count_lines(text: str) -> int:
    """Return the number of lines in `text`."""
    if not text:
        return 0
    stripped = text.rstrip('\n')
    return len(stripped.split('\n')) if stripped else 1
