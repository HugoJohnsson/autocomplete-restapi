# Represents a node in the prefix three
class Node:
    def __init__():
        self.children = dict() # Map of characters to other Nodes
        self.is_end = False # "End of word" - True if the node is the last representing a word
        self.word = "" # Stores the entire word for faster results when trying to get all matching words in the tree

    def get_children():
        return self.children