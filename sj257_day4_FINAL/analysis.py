''' Goal is to use list comprehensions for fast, easy data analysis.

List comprehension:
    [ <expr> for <var> in <iterable> if <cond> ]

Suggestions to improve your life.

Separate a big problem into smaller problems:
    1) ETL -- Extract, Transform, Load (acquire)     Hunter/Gatherer part of your brain.
    2) Data Analysis                                 Right brain (you went to school for this).
    3) Output formatting                             Left brain aesthetic and artist.

For analysis, start with projections (this is almost never what you want, but it is a great stepping stone).
    In math, a projection is reducing dimensionality.  Shine a light on a person (3-D) gives a shadow (2-D)
    In database theory, a projection is subset of a tuple:
        (name, age, location, education) -> (age, location)
        (name, age, location, education) -> (age)        

'''

from portfolio import parse_trades
from pprint import pp

port = parse_trades('data/stocks.txt')
pp(port)

print('\nProjections:')
print([trade.symbol for trade in port])
print([trade.shares for trade in port])
print([trade.price for trade in port])
print([(trade.shares, trade.price) for trade in port])

print('\nEnglish:  Tell me how many shares of Cisco you have purchased cumulatively in all your stock trades to date?')
print('Trader: What is your position is CSCO?')
print('SELECT SUM(shares) FROM Port WHERE symbol = "CSCO";')
cisco_position = sum([trade.shares for trade in port if trade.symbol == 'CSCO'])
print(f'The CSCO position is {cisco_position} shares.')

print('\nEnglish:  What are all the companies you have ever traded, listed alphabetically without duplicates?')
print('Trader: What symbols to you trade?')
print('SELECT DISTINCT symbol FROM Port ORDER BY symbol;')
symbols = sorted(set([trade.symbol for trade in port]))
print('Symbols traded to date:', ', '.join(symbols))

print('\nEnglish:  Cumulatively, how much money have you invested in all of your stock trades to date?')
print('Trader:  What is the cost basis of the portfolio?')
print('SELECT SUM(shares * price) FROM Port;')
cost_basis = sum([trade.shares * trade.price for trade in port])
print(f'Cost basis: ${cost_basis:,.2f}')

print("\nEnglish: Cumulatively what are all of your stock trades worth in today's market?")
print('Trader:  What is the market value of the portfolio?')
print('''\
SELECT SUM(Port.shares * CurrentPrices.price)
FROM Port, CurrentPrices
WHERE Port.symbol = CurrentPrices.symbol;
''')
current_prices = dict(CSCO=41.41, MSFT=125.21, ANTM=156.78, IBM=22.45, GOOG=972.51)
market_value = sum([trade.shares * current_prices[trade.symbol] for trade in port])
print(f'Market value: ${market_value:,.2f}')

# What percentage of the portfolio is in health care?
# Do any trades exceed the trader limit of $40,000?


