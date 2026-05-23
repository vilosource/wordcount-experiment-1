"""wordcount — a tiny text-stats library."""


def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in `text`."""
    return len(text.split())


def count_lines(text: str) -> int:
    """Return the number of lines in `text` (trailing newline does not add a line)."""
    stripped = text.rstrip('\n')
    if not stripped:
        return len(text) > 0
    return stripped.count('\n') + 1
