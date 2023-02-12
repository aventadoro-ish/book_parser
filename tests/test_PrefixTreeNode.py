import pytest
from book_parser.PrefixTreeNode import PrefixTreeNode, WordData


@pytest.fixture
def empty_prefix_tree_root():
    return PrefixTreeNode('')


@pytest.fixture
def filled_prefix_tree():
    # TODO: update using new methods
    root = PrefixTreeNode('')
    root.add_word_occurrence('hello')
    root.add_word_occurrence('hi')
    root.add_word_occurrence('boom')
    root.add_word_occurrence('boot')
    return root


def test_word_data():
    wd = WordData()
    assert wd.is_word_end is False
    assert wd.count == 0

    wd.count += 1
    assert wd.is_word_end is True
    assert wd.count == 1


def test_add_word_occurrence(empty_prefix_tree_root):
    root = empty_prefix_tree_root
    assert root.add_word_occurrence('hello').word_data.count == 1
    assert root.add_word_occurrence('hello').word_data.count == 2

    assert root.add_word_occurrence('hi').word_data.count == 1


def test_add_multiple_word_occurrences(empty_prefix_tree_root):
    root = empty_prefix_tree_root
    words = ['hello', 'hi', 'boom', 'boom', 'box']
    ret_lst = root.add_multiple_word_occurrences(words)
    ret_lst_count = [x.word_data.count for x in ret_lst]

    assert len(ret_lst) == 5
    assert ret_lst_count == [1, 1, 2, 2, 1]


def test_get_item(filled_prefix_tree):
    root = filled_prefix_tree
    assert root['hello'].word_data.is_word_end is True
    assert root['hello'].word_data.count == 1

    assert root['hi'].word_data.is_word_end is True
    assert root['hi'].word_data.count == 1

    assert root['boom'].word_data.is_word_end is True
    assert root['boom'].word_data.count == 1

    assert root['boom'].word_data.is_word_end is True
    assert root['boot'].word_data.count == 1


def test_post_init():
    with pytest.raises(ValueError):     # letter too long missing
        PrefixTreeNode('letter')


def test_get_children_str(filled_prefix_tree):
    root = filled_prefix_tree
    assert root.get_children_str() == 'hb'
    assert root['h'].get_children_str() == 'ei'


def test_get_prefix(filled_prefix_tree):
    root = filled_prefix_tree
    assert root.get_prefix() == ''
    assert root['hello'].get_prefix() == 'hello'


def test_str(filled_prefix_tree):
    root = filled_prefix_tree
    assert str(root) == 'PTN(, "hb", 0)'
    assert str(root['hello']) == 'PTN(hello, "", 1)'


def test_usage():
    root = PrefixTreeNode('')
    words = 'Hello my name is Matvey and this is a sample sentence'
    root.add_multiple_word_occurrences(words.split(' '))

    assert root['is'].word_data.count == 2

    new_words = 'Matvey is a cool person'
    root.add_multiple_word_occurrences(new_words.split(' '))

    assert root['Matvey'].word_data.is_word_end is True

    with pytest.raises(KeyError):
        root['hypotenuse']  # word not in the tree


def test_n_words(filled_prefix_tree):
    assert filled_prefix_tree.n_words == 4


def test_n_unique_words(filled_prefix_tree):
    assert filled_prefix_tree.n_unique_words == 4
