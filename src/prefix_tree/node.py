# Represents a node in the prefix three
class Node:
    def __init__(self):
        self.children = dict() # Map of characters to other Nodes
        self.is_end = False # "End of word" - True if the node is the last representing a word
        self.phrase = "" # Stores the entire phrase for faster results when trying to get all matching phrases in the tree