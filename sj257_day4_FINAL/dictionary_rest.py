

# https://dictionaryapi.dev

from urllib.request import urlopen
from pprint import pp
import json

def define(word, show_synonyms=False):
    "Print out all definitions from wikipedia"
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    with urlopen(url) as f:
        response = json.load(f)
    print(f'Defining: {word}')
    for source in response:
        for meaning in source.get('meanings', []):        # Use get() if "meanings" might not be present
            for definition in meaning['definitions']:     # If meaning['definition'] is an empty list, loop zero times
                print(definition['definition'])
            if show_synonyms:
                synonyms = meaning.get('synonyms', [])
                if synonyms:                              # Skip printing synonyms at all if there aren't any
                    print('Synonyms:', ', '.join(synonyms), '\n')
    print()

if __name__ == '__main__':

    define('love')
    define('marriage', True)

# JsonExtractor(response, '*:source,*:meanings["meaning"],*:definitions['definition']')   # Like XPATH in XML
# Other fun REST APIs:
#    https://owen-wilson-wow-api.herokuapp.com
#    https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets

### API for opening a browser
### https://docs.python.org/3/library/webbrowser.html#module-webbrowser
##kind = input('movie/year/director')
##value = input('value: ')
##wows = owen(kind, value)
### wow:  {'movie': 'Marley and Me', 'year': 2003, link:'www...'}
##webrowser.open(wow['link'])

# What a JSON query language might look like.
"**'meaning'*'definition'[0]"
"**'meaning'*'synonyms'?*"
