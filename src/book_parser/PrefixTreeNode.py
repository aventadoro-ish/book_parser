from __future__ import annotations

from dataclasses import dataclass, field


@ dataclass
class WordData:
    count: int = 0

    @property
    def is_word_end(self) -> bool:
        return self.count > 0


@dataclass
class PrefixTreeNode:
    letter: str
    parent: PrefixTreeNode | None = None
    word_data: WordData = field(default_factory=WordData)
    children: dict[str, PrefixTreeNode] = field(default_factory=dict)

    def __post_init__(self):
        if len(self.letter) > 1:
            raise ValueError(f'{self.letter=} must be a single character.')

    def add_word_occurrence(self, word: str | list[str]) -> PrefixTreeNode:
        """
        Traverses the tree, adding nodes if needed.
        Increments self.word_data.count
        :param word: words to add occurrence of
        :type word: str | list[str]
        :return: node corresponding to the last letter
        :rtype: PrefixTreeNode
        """
        try:
            first_letter = word[0]
            if first_letter not in self.children:
                self.children[first_letter] = \
                    PrefixTreeNode(first_letter, self)

            return self.children[first_letter].add_word_occurrence(word[1:])

        except IndexError:
            # end of word reached
            self.word_data.count += 1
            return self

    def add_multiple_word_occurrences(
            self, words: list[str]) -> list[PrefixTreeNode]:

        return_list = []
        for word in words:
            return_list.append(self.add_word_occurrence(word))

        return return_list

    def __getitem__(self, word: str) -> PrefixTreeNode:
        if len(word) == 0:
            return self

        return self.children[word[0]][word[1:]]

    def get_children_str(self) -> str:
        return ''.join([x for x in self.children.keys()])

    def get_prefix(self) -> str:
        if self.parent is None:
            return ''

        return self.parent.get_prefix() + self.letter

    def __str__(self) -> str:
        return f'PTN({self.get_prefix()}, ' \
               f'"{self.get_children_str()}", ' \
               f'{self.word_data.count})'

    @property
    def n_words(self):
        count = self.word_data.count

        for child in self.children.values():
            count += child.n_words

        return count

    @property
    def n_unique_words(self):
        count = 1 if self.word_data.count > 0 else 0
        for child in self.children.values():
            count += child.n_unique_words

        return count
