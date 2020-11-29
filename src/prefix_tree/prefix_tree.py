from .node import Node

# Represents a PrefixTree, holds all the insert and search methods
class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert_prefix(self, word):
        def _insert_prefix(word, current_node, index):
            if len(word) == index:
                current_node.is_end = True
                current_node.word = word
                return

            current_char = word[index]
            new_node = current_node.children.get(current_char)

            if not new_node:
                new_node = Node()
                current_node.children[current_char] = new_node
            
            _insert_prefix(word, new_node, index + 1)

        _insert_prefix(word, self.root, 0)