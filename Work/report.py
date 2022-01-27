# report.py
#
# Exercise 2.4

import sys
import csv


def read_portfolio(filename):
    with open(filename, 'rt') as f:
        data = f.readlines()
    portfolio = []
    for i in data[1:]:
        temp = {}
        i = i.split(',')
        temp['name'] = i[0].replace('"', '')
        temp['shares'] = int(i[1])
        temp['price'] = float(i[2])
        portfolio.append(temp)
    return portfolio


def read_prices(filename):
    f = open(filename, 'r')
    rows = csv.reader(f)

    temp = {}
    for row in rows:
        try:
            temp[row[0]] = row[1]
        except:
            pass

    return temp


# cost = portfolio_cost(
#     'C:/Users/BAUM/Desktop/practical-python/Work/Data/portfolio.csv')

# cost = portfolio_cost(
#     'C:/Users/BAUM/Desktop/practical-python/Work/Data/missing.csv')


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'C:/Users/BAUM/Desktop/practical-python/Work/Data/portfolio.csv'

if len(sys.argv) == 2:
    filename2 = sys.argv[1]
else:
    filename2 = 'C:/Users/BAUM/Desktop/practical-python/Work/Data/prices.csv'

portfolio = read_portfolio(filename)
prices = read_prices(filename2)

print('portfolio : ', portfolio)
print('prices : ', prices)

my_fund = 0
for i in portfolio:
    my_fund += i['shares'] * i['price']
print('past_profit: ', my_fund)

now_fund = 0
for i in portfolio:
    now_fund += i['shares'] * float(prices[i['name']])
print('current_profit: ', now_fund)

print('profit: ', round(now_fund - my_fund))
