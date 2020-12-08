# autocomplete-restapi
Service providing autocompletions based on a prefix.

**How it works**

The basic part of this project is the Prefix Tree data structure (Trie, https://en.wikipedia.org/wiki/Trie),
which is held in memory. In my implementation every node has a children map (Python Dictionary) where the key is 
a specific character and the value is another node. A node also has an "is_end" flag which represents if the current
node is the end of a word as well as a "phrase" which for the "end of word" nodes contains the entire word. I store
the entire phrase on those nodes because when we want to find words matching a prefix we traverse the tree,
and when we hit an "end of word" node we just add the phrase to the result, super efficient!

A simple web service / API has been swith the Flask (https://flask.palletsprojects.com/en/1.1.x/) web application
framework. While the application is running only one instance of the Prefix Tree is maintained and on startup
it loads english words into the Prefix Tree from the database which is simply a large TXT file (words.txt).
I also setup a caching layer with Redis (https://redis.io), every prefix searched for that generates a result with matching
phrases is cached.

All in all it's a very simple application, it is definitely not production ready.
For example, the Flask app has not been setup to run behind a WSGI server and the caching logic could be alot more sophisticated
with proper cache invalidation etc.

**Setup**

You can easily run the application with docker-compose. Just make sure you have Docker and docker-compose installed on your machine.
1. Clone the repo.
2. Run `docker-compose build`
3. Run `docker-compose up`
4. Ready to go!
