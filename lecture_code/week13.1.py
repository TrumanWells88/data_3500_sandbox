# web json APIs

import json
import requests

url = "https://v2.jokeapi.dev/joke/Programming"

request = requests.get(url)

#  print(request)

# print requests
dictionary = json.loads(request.text)
print(dictionary)

new_url = 'https://api.datamuse.com/words?rel_trg=cow'
