import json
with open('data/books.json') as f:
    catalog = json.load(f)
print(json.__doc__)
