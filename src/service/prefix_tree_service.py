from prefix_tree.prefix_tree import PrefixTree

class PrefixTreeService:
    """
    Singleton service for interacting with the underlying
    prefix tree data structure.

    ...

    Attributes
    ----------
    prefix_tree : PrefixTree
        holds the prefix tree data structure
    
    """

    def __init__(self):
        self.prefix_tree = PrefixTree()
        self.prefix_tree.insert("hugo")
        self.prefix_tree.insert("hej")

    def get_matching_phrases(self, prefix):
        """[summary]

        Args:
            prefix ([string]): [the prefix we want to find matching phrases for]

        Returns:
            [list[string]]: [list of all matching phrases]
        """
        return self.prefix_tree.find_matching_phrases(prefix)
    


prefix_tree_service = PrefixTreeService()