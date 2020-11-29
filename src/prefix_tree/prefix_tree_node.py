class _PrefixTreeNode:
    """
        Represents a node in the prefix three

        ...

        Attributes
        ----------
        children : dict
            represents the child nodes with a map of characters to other PrefixTreeNode 
        is_end : bool
            is True if node represents the end of a phrase
        phrase : string
            stores the entire phrase if node has "is_end" set to True to simplify
            the process when trying to get all matching phrases in the tree
        
        """

    def __init__(self):
        self.children = dict()
        self.is_end = False
        self.phrase = ""