### 122. Best Time to Buy and Sell Stock II

**Description**:

​	Say you have an array for which the *i*th element is the price of a given stock on day *i*.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

**Note:** You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

**Example 1:**

```
Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
```

**Example 2:**

```
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
```

**Example 3:**

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```


**Submission**

- Python

```python
class Solution:      
    # Memory Limit Exceeded
    def maxProfit(self, prices: List[int]) -> int:
    		# exception handler
        if len(prices) <= 0:
            return 0
        
        n = len(prices)
        dp0 = [[0] * n for i in range(n)]
        dp1 = [[0] * n for i in range(n)]
        # dp1[0][0:n] = -prices[0]

        for i in range(n):
            dp1[0][i] = -prices[0]
        for i in range(1,n):
            dp1[i][0] = max(dp1[i-1][0], -prices[i])
        
        for i in range(1, n):
            for j in range(n):
                dp0[i][j] = max(dp0[i-1][j], dp1[i-1][j-1] + prices[i])
                dp1[i][j] = max(dp1[i-1][j], dp0[i-1][j]   - prices[i])
                
        return max(max(dp0))
    
    # beats 99% in runtime, 48% in memory
    def maxProfit(self, prices: List[int]) -> int:
        
        # exception handler
        if len(prices) <= 0:
            return 0
        
        n = len(prices)
        dp0 = [0] * n
        # dp1 = [-prices[0]] + [0] * (n-1)
        dp1 = [0] * n
        dp1[0] = -prices[0]
        
        for i in range(1, n):
            dp0[i] = max(dp0[i-1], dp1[i-1] + prices[i])
            dp1[i] = max(dp1[i-1], dp0[i-1] - prices[i])
                
        return dp0[-1]
      
'''
接121的分析，DP might be the best solution for this:
	https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/
'''
```



- C++

```c++

```



- Java

```java

```



​	