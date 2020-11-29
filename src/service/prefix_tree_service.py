from prefix_tree.prefix_tree import PrefixTree
from service.cache_service import cache_service

class PrefixTreeService:
    """
    Singleton service for interacting with the underlying
    prefix tree data structure.

    ...

    Attributes
    ----------
    prefix_tree : PrefixTree
        holds the prefix tree data structure
    cache_service : CacheService
        holds the CacheService singleton instance
    """

    def __init__(self, cache_service):
        self.prefix_tree = PrefixTree()
        self.cache_service = cache_service

        self.prefix_tree.insert("hej")
        self.prefix_tree.insert("hejsan")

    def get_matching_phrases(self, prefix):
        """
        Returns an array of matching phrases by
        first checking if we have it stored in our cache.
        If there's a cache miss we get the phrases from the
        PrefixTree, cache it and return the results.

        Args:
            prefix ([string]): [the prefix we want to find matching phrases for]

        Returns:
            [list[string]]: [list of all matching phrases]
        """

        result = self.cache_service.get_cached_phrases(prefix)

        if not result: # Cache miss
            result = self.prefix_tree.find_matching_phrases(prefix)
            self.cache_service.insert(prefix, result)

        return result

    def insert(self, phrase):
        self.prefix_tree.insert(phrase)
    


prefix_tree_service = PrefixTreeService(cache_service)