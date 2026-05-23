"""wordcount — a tiny text-stats library."""


def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in `text`."""
    return len(text.split())


def count_lines(text: str) -> int:
    """Return the number of lines in `text`."""
    # Empty string has no lines
    if not text:
        return 0
    # Count newline characters
    newline_count = text.count("\n")
    # No newline means single line
    if newline_count == 0:
        return 1
    # Trailing newline doesn't add a phantom line
    if text.endswith("\n"):
        return newline_count
    return newline_count + 1
