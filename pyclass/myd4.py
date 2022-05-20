from typing import NamedTuple
from pprint import pprint
import csv

class Trade(NamedTuple):
    symbol: str
    shares: int
    price: float

def parse_trades(filename ):
    "Parse a CSV file of stock trades into a list of Trade objects"
    trades = []
    with open(filename) as f:
        for symbol, shares, price in csv.reader(f):
            trade = Trade(symbol, int(shares), float(price))
            #print(trade)
            trades.append(trade)

    return trades

    #print(trades)       
    #pprint(trades)

if __name__ == '__main__':
    portfolio = parse_trades('data/stocks.txt')
    pprint(portfolio)
    
