# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



prices = [2, 4, 1]


def profit(prices):
    sub = []
    for i in range(len(prices)-1):
        if prices[i] < prices[i+1]:
            sub.append(prices[i])
    
    smallest = sub[0]
    sell = prices[prices.index(smallest):]
    print(sell)
    largest = max(sell)
    if largest > smallest:
        return largest-smallest
    else:
        return 0


print(profit(prices))
