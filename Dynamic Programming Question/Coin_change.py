def coin_change(coins,amount):
    dp = [0] + [float('inf')] * amount 
    for i in range(1,amount+1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i],dp[i-coin] + 1)
    if dp[-1] == float('inf'):
        return -1 
    else:
        return dp[-1]

coins = [1,2,5]
amount = 11
print(coin_change(coins, amount))