def buy_sell_stock(prices):
    buy = float('inf')
    sell = float('-inf')
    for i in range(len(prices)):
        buy = min(buy,prices[i])
        sell = max(sell,prices[i]-buy)
    return sell 
prices = [7,1,5,3,6,4]
print(buy_sell_stock(prices))