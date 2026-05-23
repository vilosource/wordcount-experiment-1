"""wordcount — a tiny text-stats library."""


def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in `text`."""
    return len(text.split())


def count_lines(text: str) -> int:
    """Return the number of lines in `text`.

    A trailing newline does not create a phantom line.
    """
    if not text:
        return 0
    return text.count("\n") + (0 if text.endswith("\n") else 1)
