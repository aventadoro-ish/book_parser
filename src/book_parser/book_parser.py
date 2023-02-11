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
    letter: str = ''
    word_data: WordData = field(default_factory=WordData)
    parent: PrefixTreeNode | None = None
    children: dict[str, PrefixTreeNode] = field(default_factory=dict)

    def add_word_occurrence(self, word: str) -> WordData:
        """
        Traverses the tree, creating nodes as needed, increments
        self.WordData.count on the last node
        :param word: word to add occurrence of
        :type word: str
        :return: this word's data
        :rtype: WordData
        """
        try:
            first_char = word[0]
            if first_char not in self.children:
                self.children[first_char] = \
                    PrefixTreeNode(first_char, parent=self)

            return self.children[first_char].add_word_occurrence(word[1:])

        except IndexError:
            self.word_data.count += 1
            print('*', self.get_prefix(), self.word_data.count)
            return self.word_data

    def print_tree(self):
        if self.word_data.is_word_end:
            print(self.get_prefix())

        for child_letter, child in self.children.items():
            child.print_tree()

    def get_prefix(self) -> str:
        current_node = self
        prefix = ''

        while current_node.parent is not None:
            prefix = current_node.letter + prefix
            current_node = current_node.parent

        return prefix

    def __getitem__(self, word: str) -> PrefixTreeNode:
        """
        Returns node of the tree corresponding to the word provided, regardless
        if it is a valid word or not.
        :param word: search for this word
        :type word: str
        :return: node of the given word
        :rtype: PrefixTreeNode
        :raise IndexError
        """
        if len(word) == 0:
            print('**', self.get_prefix())
            return self

        return self[word[1:]]


def main():
    ptn = PrefixTreeNode()
    ptn.add_word_occurrence('hello')
    ptn.add_word_occurrence('hell')
    ptn.add_word_occurrence('hi')

    print(ptn['hello'].word_data.count)

    print(ptn.children['h'].children.keys())
    ptn.print_tree()


if __name__ == '__main__':
    main()
