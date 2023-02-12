import re

import pytest
from book_parser.BookParser import BookParser

TEST_TEXT = \
    """Hello, my name is Matvey, and this is sample text for my book parser.
Sample text is used during testing of BookParser class.
"""


@pytest.fixture
def empty_book_parser() -> BookParser:
    return BookParser()


@pytest.fixture
def text_filled_book_parser() -> BookParser:
    return BookParser(TEST_TEXT)


def test_empty_init(empty_book_parser):
    bp = empty_book_parser
    assert bp.n_punctuation_symbols == 0
    assert bp.root.n_words == 0
    assert bp.root.n_unique_words == 0


def test_add_data_from_text(empty_book_parser):
    bp = empty_book_parser

    words = []
    for word in re.split('[ ,.!?\n]', TEST_TEXT):
        if len(word) > 0:
            words.append(word)

    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    assert bp.add_data_from_text(TEST_TEXT) == len(words)

    assert bp.root.n_words == len(words)
    assert bp.root.n_unique_words == len(unique_words)


def test_text_init(text_filled_book_parser):
    bp = text_filled_book_parser

    words = []
    for word in re.split('[ ,.!?\n]', TEST_TEXT):
        if len(word) > 0:
            words.append(word)

    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    assert bp.root.n_words == len(words)
    assert bp.root.n_unique_words == len(unique_words)
    assert False
