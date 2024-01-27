# I have tried just about everything but my solution is not being accepted
# by check50.
"""
s = 0
while s < 50:
    print(f"Amount Due: {50 - s}")
    coin = int(input("Insert Coin: "))
    if coin not in [25, 10, 5]:
        continue
    s += coin

print(f"Change Owed: {max(s - 50, 0)}")
"""

# https://stackoverflow.com/questions/76821895/coke-machine-cs50-pset2-problem-2-while-loop-issue

amount_due = 50
coins = [5, 10, 25]

while amount_due > 0:
    print(f"Amount Due: {amount_due}")

    coin = int(input("Insert Coin: "))

    if coin in coins:
        amount_due -= coin

print(f"Change Owed: {abs(amount_due)}")
