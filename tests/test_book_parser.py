import pytest
from book_parser.book_parser import PrefixTreeNode


@pytest.fixture
def prefix_tree_root():
    return PrefixTreeNode()


def test_add_word_occurrence(prefix_tree_root):
    assert prefix_tree_root.add_word_occurrence('hello').count == 1
    assert prefix_tree_root.add_word_occurrence('hello').count == 2
    assert prefix_tree_root.add_word_occurrence('hello').count == 3


def test_PrefixTreeNode():
    ptn = PrefixTreeNode()
    ptn.add_word_occurrence('hello')
    ptn.add_word_occurrence('hell')
    ptn.add_word_occurrence('hi')
    assert 1 == 1
