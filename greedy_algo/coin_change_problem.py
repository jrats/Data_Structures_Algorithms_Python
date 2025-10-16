def coinChange(amount, coins):
    N = amount
    coins.sort()
    index = len(coins) - 1
    while True:
        val = coins[index]
        if N>=val:
            print(val)
            N=N-val
        if N<val:
            index -=1
        if N==0:
            break

coins = [1,2,5,20,50,100]
coinChange(201, coins)