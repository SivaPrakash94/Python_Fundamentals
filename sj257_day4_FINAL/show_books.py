'Goal:  Learn JSON parsing and to practice dictionary data analysis'

import json

with open('data/books.json') as f:
    catalog = json.load(f)

print('Task 1: Determine how many books are in the catalog')
print(len(catalog))

print('\nTask 2: Is bk152 in the catalog?')
print('bk152' in catalog)

print('\nTask 3: Nicely display all the book identifiers')
for book_id in sorted(catalog):
    print(book_id)

print('\nTask 4: Show all the book titles')
for book in catalog.values():
    print(book['title'])

print('\nTask 5: Author, an arrow, publish date for bk105')
book = catalog['bk105']
print(f"{book['author']} \N{rightwards arrow} {book['publish_date']}")

print('\nTask 6: Author, an arrow and price for the computer books')
for book in catalog.values():
    if book['genre'].casefold() == 'computer':
        print(f"{book['author']} \N{rightwards arrow} ${book['price']:.2f}")

print('\nTask 7: Show tags and tag values for bk107')
for tag, tag_value in catalog['bk107'].items():
    print(tag.upper())
    print(tag_value)
    print()
