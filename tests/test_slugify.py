import pytest
from slugify import slugify


class TestBasicAscii:
    def test_simple_words(self):
        assert slugify("Hello World") == "hello-world"

    def test_already_lowercase(self):
        assert slugify("hello world") == "hello-world"

    def test_uppercase(self):
        assert slugify("UPPER CASE") == "upper-case"

    def test_single_word(self):
        assert slugify("python") == "python"

    def test_numbers(self):
        assert slugify("Python 3") == "python-3"

    def test_multiple_spaces(self):
        assert slugify("hello   world") == "hello-world"

    def test_tabs_and_newlines(self):
        assert slugify("hello\t\nworld") == "hello-world"


class TestUnicode:
    def test_accented_e(self):
        assert slugify("café") == "cafe"

    def test_naive_with_diaeresis(self):
        assert slugify("naïve") == "naive"

    def test_umlaut(self):
        assert slugify("über") == "uber"

    def test_mixed_accents(self):
        assert slugify("Café naïve") == "cafe-naive"

    def test_spanish_tilde(self):
        assert slugify("Señor") == "senor"

    def test_french_phrase(self):
        assert slugify("résumé") == "resume"

    def test_nordic_characters(self):
        assert slugify("Ångström") == "angstrom"


class TestPunctuation:
    def test_comma(self):
        assert slugify("hello, world") == "hello-world"

    def test_exclamation(self):
        assert slugify("hello, world!") == "hello-world"

    def test_period(self):
        assert slugify("end.of.line") == "endofline"

    def test_slash(self):
        assert slugify("path/to/file") == "pathtofile"

    def test_apostrophe(self):
        assert slugify("it's a test") == "its-a-test"

    def test_ampersand(self):
        assert slugify("rock & roll") == "rock-roll"

    def test_at_sign(self):
        assert slugify("user@example.com") == "userexamplecom"

    def test_all_punctuation(self):
        assert slugify("!@#$%^&*()") == ""


class TestHyphens:
    def test_existing_hyphen_preserved(self):
        assert slugify("well-known") == "well-known"

    def test_repeated_hyphens_collapsed(self):
        assert slugify("über--cool") == "uber-cool"

    def test_many_hyphens(self):
        assert slugify("a---b----c") == "a-b-c"

    def test_leading_hyphen_stripped(self):
        assert slugify("-hello") == "hello"

    def test_trailing_hyphen_stripped(self):
        assert slugify("hello-") == "hello"

    def test_hyphen_from_punctuation_collapse(self):
        assert slugify("one, , ,two") == "one-two"


class TestEdgeCases:
    def test_empty_string(self):
        assert slugify("") == ""

    def test_whitespace_only(self):
        assert slugify("   ") == ""

    def test_idempotent(self):
        slug = slugify("Hello, World!")
        assert slugify(slug) == slug

    def test_digits_only(self):
        assert slugify("12345") == "12345"

    def test_mixed_unicode_and_punctuation(self):
        assert slugify("Ångström & naïve, café!") == "angstrom-naive-cafe"
