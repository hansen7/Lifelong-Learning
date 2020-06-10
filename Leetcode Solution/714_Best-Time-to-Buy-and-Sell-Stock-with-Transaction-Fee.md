### 309. Best Time to Buy and Sell Stock with Cooldown

Your are given an array of integers `prices`, for which the `i`-th element is the price of a given stock on day `i`; and a non-negative integer `fee` representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

**Example 1:**

```
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9

The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
```



**Note:**

`0 < prices.length <= 50000`.

`0 < prices[i] < 50000`.

`0 <= fee < 50000`.



**Submission**

- Python

```python
class Solution:
  	# Runtime: 776 ms, faster than 68.14% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
		# Memory Usage: 19.4 MB, less than 12.50% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n_days = len(prices)
        
        if n_days == 0:
            return 0
        
        dp0, dp1 = 0, -prices[0]
        
        for i in range(1, n_days):
            pre_dp0 = dp0
            dp0 = max(dp0, dp1 + prices[i] - fee)
            dp1 = max(dp1, pre_dp0 - prices[i])
            
        return dp0
```



- C++

```c++

```



- Java

```java

```



​	