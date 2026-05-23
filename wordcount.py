"""wordcount — a tiny text-stats library."""


def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in `text`."""
    return len(text.split())


def count_lines(text: str) -> int:
    """Return the number of lines in `text`.

    A trailing newline does not add a phantom line.
    """
    stripped = text.rstrip('\n')
    if not stripped:
        return 1 if text else 0
    return len(stripped.split('\n'))
