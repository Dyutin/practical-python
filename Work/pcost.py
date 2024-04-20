# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):
    f = open(filename, 'rt')
    next(f)
    cost = 0.0
    for line in f:
        try:
            row = line.split(',')
            cost += int(row[1])*float(row[2])
        except ValueError:
            print("Bad Row", line)
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'

tcost = portfolio_cost(filename)
print("Total cost ", tcost)

