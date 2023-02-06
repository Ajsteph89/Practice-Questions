# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



prices = [2, 4, 1]


def profit(prices):
        res = 0
        l = 0
        for x in range(1, len(prices)):
            if prices[x] < prices[l]:
                l = x
            # determines if existing result or the new calc is higher
            res = max(res, prices[x] - prices[l])
        return res

print(profit(prices))
