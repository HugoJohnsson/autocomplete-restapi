from .node import Node

# Represents a PrefixTree, holds all the insert and search methods
class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, phrase, current_node = None, index = 0):
        if len(phrase) < 2: # Phrase not long enough
            return False

        if not current_node: # First time called
            current_node = self.root

        if len(phrase) == index:
            # Is on last Node / character
            current_node.is_end = True
            current_node.phrase = phrase
            return

        current_char = phrase[index]
        new_node = current_node.children.get(current_char)

        if not new_node: # Current node does not have a child with the current character
            # Create new Node and add it to the current node's children
            new_node = Node()
            current_node.children[current_char] = new_node
        
        # Recursively call insert again with the new child node and index + 1 to get the next character
        self.insert(phrase, new_node, index + 1)

    def find_sub_tree(self, prefix, current_node = None, index = 0):
        if len(prefix) == index: # if the length of the prefix is 0 we just return None the very first time the function gets called
            return current_node

        if not current_node: # First time called
            current_node = self.root

        current_char = prefix[index]
        next_node = current_node.children.get(current_char)

        if not next_node: #
            return None
        
        return self.find_sub_tree(prefix, next_node, index + 1)

        
        