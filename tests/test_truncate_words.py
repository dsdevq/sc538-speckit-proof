import pytest
from truncate_words import truncate_words


class TestNoTruncation:
    def test_fewer_words_than_limit(self):
        assert truncate_words("hello world", 5) == "hello world"

    def test_exactly_max_words(self):
        assert truncate_words("one two three", 3) == "one two three"

    def test_single_word_within_limit(self):
        assert truncate_words("word", 10) == "word"

    def test_empty_string(self):
        assert truncate_words("", 5) == ""


class TestTruncation:
    def test_truncates_to_max_words(self):
        result = truncate_words("one two three four five", 3)
        assert result == "one two three…"

    def test_truncation_appends_ellipsis(self):
        assert truncate_words("a b c d", 2) == "a b…"

    def test_single_word_limit(self):
        assert truncate_words("hello beautiful world", 1) == "hello…"


class TestWhitespaceNormalization:
    def test_leading_trailing_spaces(self):
        assert truncate_words("  hello world  ", 5) == "hello world"

    def test_multiple_spaces_between_words(self):
        assert truncate_words("one   two   three", 2) == "one two…"

    def test_tabs_and_newlines(self):
        assert truncate_words("one\ttwo\nthree", 3) == "one two three"

    def test_mixed_whitespace_with_truncation(self):
        result = truncate_words("  word1   word2   word3   word4  ", 2)
        assert result == "word1 word2…"


class TestNonPositiveMaxWords:
    def test_zero_returns_empty(self):
        assert truncate_words("hello world", 0) == ""

    def test_negative_returns_empty(self):
        assert truncate_words("hello world", -1) == ""

    def test_large_negative_returns_empty(self):
        assert truncate_words("a b c", -100) == ""

    def test_zero_with_empty_string(self):
        assert truncate_words("", 0) == ""
