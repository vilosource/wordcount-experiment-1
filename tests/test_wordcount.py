import wordcount


def test_count_words_basic():
    assert wordcount.count_words("hello world") == 2
    assert wordcount.count_words("one two three four") == 4


def test_count_words_empty():
    assert wordcount.count_words("") == 0


def test_count_words_whitespace_collapse():
    assert wordcount.count_words("  a  b  ") == 2


def test_count_lines_basic():
    assert wordcount.count_lines("") == 0
    assert wordcount.count_lines("hello") == 1


def test_count_lines_multiple():
    assert wordcount.count_lines("a\nb\nc") == 3
    assert wordcount.count_lines("a\nb\nc\n") == 3


def test_count_lines_empty_line():
    assert wordcount.count_lines("\n") == 1
