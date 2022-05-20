from portfolio import parse_trades
from pprint import pp

port = parse_trades('data/stocks.txt')
pp(port)

print('\nProjections')

print([(trade.shares, trade.price) for trade in port])

cisco_position = sum([trade.shares for trade in port if trade.symbol == 'CSCO'])

symbols = sorted(set([trade.symbol for trade in port]))
print('Symbols trade to date:', ', ' .join(symbols))

cost_basis = sum([trade.shares * trade.price for trade in port])
print(f'Cost basis: ${cost_basis:,.2f}')

current_prices = dict(CSCO=41.41, MSFT=125.21, ANTM=156.78, IBM=22.45, GOOG=972.51)

market_value = sum([trade.shares * current_prices[trade.symbol] for trade in port])
print(f'Market Value: ${market_value:,.2f}')


