def maxProfit(prices):
    
    # if the array is empty
    if len(prices) == 0:
        return 0

    # declare our variables
    min_price = prices[0]
    max_profit = 0

    for p in prices:
        # check if we have a new max profit
        if p - min_price > max_profit:
            max_profit = p - min_price

        # check if we have a new min profit
        if p < min_price:
            min_price = p

    return max_profit
