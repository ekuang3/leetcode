def max_profit_1_transaction(prices):
    """
    Max profit after 1 transaction.

    Time: O(n) where n is length of prices
    Space: O(1)
    """
    max_profit = 0  # Initialize maximum profit to 0
    max_so_far = 0  # Initialize maximum profit so far to 0

    # Iterate through prices starting from the second day
    for i in range(1, len(prices)):
        # Calculate profit change from the previous day
        max_so_far += prices[i] - prices[i-1]  
        
        # If accumulated profit is negative, reset it to 0
        max_so_far = max(0, max_so_far)  
        
        # Update max_profit if max_so_far is greater
        max_profit = max(max_profit, max_so_far)  

    return max_profit

def max_profit_2_transactions(prices):
    """
    Max profit after 2 transactions.
    
    Time: O(n) where n is length of prices
    Space: O(1)
    """
    n = len(prices)
    if n < 2:
        return 0

    # Initialize the buy and sell arrays
    buy1, buy2 = float('-inf'), float('-inf')
    sell1, sell2 = 0, 0

    for price in prices:
        # First transaction: buy at the lowest price or sell for a higher profit
        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)

        # Second transaction: buy with remaining cash or sell for a higher profit
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, buy2 + price)

    return sell2


if __name__=='__main__':

    prices = [7,1,5,3,6,4]
    
    res = max_profit_1_transaction(prices) # 5 b/c 1 & 6
    print(res)

    res = max_profit_2_transactions(prices) # 7 b/c 1 & 5 (4) and 3 & 6 (3) -> 4+3=7
    print(res)

    prices = [7,6,4,3,1]
    
    res = max_profit_1_transaction(prices) # 0
    print(res)

    res = max_profit_2_transactions(prices) # 0
    print(res)