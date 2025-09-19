def get_odds():
    odd = 1
    while True:
        yield odd
        odd = odd + 2

odds = get_odds()

def pi_series():
    summation = 0
    index = 0 # index is not required, ı want to see the position
    while True:
        if index % 2 == 0:
            summation += 1 / next(odds)
        else:
            summation += (-1) / next(odds)
        yield summation
        index += 1


pi_sum = pi_series()

for x in range(1000000):
    print(next(pi_sum) * 4)
