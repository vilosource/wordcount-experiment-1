"""wordcount — a tiny text-stats library."""


def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in `text`."""
    return len(text.split())


def count_lines(text: str) -> int:
    """Return the number of lines in `text`.

    Trailing newline does not add a phantom line.
    """
    if not text:
        return 0
    newline_count = text.count("\n")
    if newline_count == 0:
        return 1
    if text.endswith("\n"):
        return newline_count
    return newline_count + 1
