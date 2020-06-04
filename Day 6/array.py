def buy_and_sell_stock_once(prices):
    maxProfit, currentMaxValue = 0, 0
    for price in reversed(prices):
        currentMaxValue = max(currentMaxValue, price)
        profit = currentMaxValue - price
        maxProfit = max(profit, maxProfit)
    return maxProfit
print(buy_and_sell_stock_once([12,678,346,345,456,5,43,43,454]))


