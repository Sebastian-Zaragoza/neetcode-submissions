"""
Elements
prices - integer array

Tasks
You may choose a single day to buy a NeetCoin 
and choose a different day in the future to sell it

*Return the maximum profit you can achieve
*If there are not transactions, return 0

Observations
prices[i] - price of NeetCoin on the ith day

In summary
Return the maximum profit obtained to buy a NeetCoin choosing a single day and sell it in other day
If there is not profit, return 0

Observations
What if does array contain duplicates?
If all of them are the same, return 0

What if the array is empty?
If the array is empty, return 0

What would happen if the evaluating process doesnt find a number greater than the minimum?
If its true, return 0

How would I solve this intuitively?
1. Initialize a container to store the temporal profit
2. Initialize a pointer to evaluate element by element
3. Check if the element is less than the actual minimum
    3.1. If its true, change the old minimum value to the new one
    3.2. If its false, compute the difference
4. Once the difference is calculated, store this
5. Repeat the process with the rest of values
6. Return the profit found

What time complexity be?
O(n)

What space complexity be?
O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = float('inf')
        for price in prices:
            if price < minimum:
                minimum = price
                continue
            profit = max(profit, price - minimum)
        return profit            






