# pcost.py
#
# Exercise 1.27

import sys


def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        data = f.readlines()
    total = 0
    for i in data[1:]:
        try:
            stock = float(i.split(',')[-2].strip())
            price = float(i.split(',')[-1].strip())
        except:
            stock = 0
            price = 0

        total += stock * price
    return total


# cost = portfolio_cost(
#     'C:/Users/BAUM/Desktop/practical-python/Work/Data/portfolio.csv')

# cost = portfolio_cost(
#     'C:/Users/BAUM/Desktop/practical-python/Work/Data/missing.csv')


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'C:/Users/BAUM/Desktop/practical-python/Work/Data/portfolio.csv'

cost = portfolio_cost(filename)

print('Total cost: ', cost)
