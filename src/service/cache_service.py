from redis import Redis

class CacheService:
    """
    Singleton service for interacting with our cache (Redis).
    ...

    Attributes
    ----------
    conn : Redis
        holds the redis connection object
        
    """
    def __init__(self):
        self.conn = Redis(
            host='redis',
            port=6379,
            password=''
        )

    def get_cached_phrases(self, prefix):
        """
        Gets all matched phrases for the given prefix,
        if the does not exist we just return an empty list.

        Args:
            prefix ([string])

        Returns:
            [list[string]]
        """

        result = self.conn.zrange(prefix, 0, -1)
        result = [b.decode() for b in result]

        return result

    def insert(self, prefix, matching_phrases):
        """
        Inserts a list of matching phrases into our cache
        as a Redis Sorted Set (ZRANGE).

        Args:
            prefix ([string])
            matching_phrases ([list[string]])
        """

        self.conn.zadd(prefix, self._constructPhrasesDictFromList(matching_phrases))

    def _constructPhrasesDictFromList(self, phrases):
        result = {}

        for phrase in phrases:
            result[phrase] = 1

        return result

        

cache_service = CacheService()