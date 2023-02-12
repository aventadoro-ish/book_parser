from __future__ import annotations
from book_parser.PrefixTreeNode import PrefixTreeNode


class BookParser:
    def __init__(self, text=''):
        self.root = PrefixTreeNode('')
        self.n_punctuation_symbols = 0

        if len(text) > 0:
            self.add_data_from_text(text)

    def add_data_from_text(self, text: str) -> int:
        """
        Adds all word occurrences form text
        Updates self.root, self.n_commas, self.n_dots
        :param text: text to be added
        :type text: str
        :return: number of words processed
        :rtype: int
        """
        current_word = ''
        n_words = 0

        while len(text) > 0:
            char = text[0]

            if char.isalpha():
                current_word += char
            elif char in ' ,.!?\n':
                self.n_punctuation_symbols += 1

                if len(current_word) > 0:
                    self.root.add_word_occurrence(current_word)
                    current_word = ''
                    n_words += 1

            # TODO: numbers support

            text = text[1:]

        return n_words
