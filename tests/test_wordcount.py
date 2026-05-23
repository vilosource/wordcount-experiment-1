import wordcount


def test_count_words_basic():
    assert wordcount.count_words("hello world") == 2
    assert wordcount.count_words("one two three four") == 4


def test_count_words_empty():
    assert wordcount.count_words("") == 0


def test_count_words_whitespace_collapse():
    assert wordcount.count_words("  a  b  ") == 2
