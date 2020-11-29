from .prefix_tree_node import PrefixTreeNode
class PrefixTree:
    """
    Represents a PrefixTree.

    ...

    Attributes
    ----------
    root : PrefixTreeNode
        holds the root node of the prefix tree
    
    """

    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, phrase, current_node = None, index = 0):
        """ 
        Inserts a given phrase to the tree, this is a recursive method.

        Args:
            phrase ([String]): [the phrase to insert]
            current_node ([PrefixTreeNode], optional): [holds the current node when calling itself]. Defaults to None.
            index (int, optional): [index for the current character we are looking at]. Defaults to 0.
        """

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
            new_node = PrefixTreeNode()
            current_node.children[current_char] = new_node
        
        # Recursively call insert again with the new child node and index + 1 to get the next character
        self.insert(phrase, new_node, index + 1)

    def find_matching_phrases(self, prefix):
        """ 
        Returns a list of all matching phrases for the given prefix.

        Args:
            prefix ([String]): [the prefix we want to find matching phrases for]
        """
        def _find_matching_phrases(node, result): # Helper function
            if node.is_end:
                result.append(node.phrase)
                
                if len(node.children) == 0:
                    return

            for char in node.children.keys():
                _find_matching_phrases(node.children[char], result)

            return result


        # Find the subtree (last node) for the given prefix
        sub_tree_root = self.__find_sub_tree(prefix)

        if not sub_tree_root:
            return []

        return _find_matching_phrases(sub_tree_root, [])


    def __find_sub_tree(self, prefix, current_node = None, index = 0):
        """
        Internal helper method for finding the root node of
        the subtree we want to search based on the given prefix.

        Args:
            prefix ([String]): [the prefix we want to find the subtree root node for]
            current_node ([PrefixTreeNode], optional): [holds the current node when calling itself]. Defaults to None.
            index (int, optional): [index for the current character we are looking at]. Defaults to 0.

        Returns:
            [type]: [description]
        """
        if len(prefix) == index: # If the length of the prefix is 0 we just return None the very first time the function gets called
            return current_node

        if not current_node: # First time called
            current_node = self.root

        current_char = prefix[index]
        next_node = current_node.children.get(current_char)

        if not next_node:
            return None
        
        return self.__find_sub_tree(prefix, next_node, index + 1)

        
        