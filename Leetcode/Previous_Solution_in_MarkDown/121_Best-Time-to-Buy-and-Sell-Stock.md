### 121. Best Time to Buy and Sell Stock

**Description**:

​	Say you have an array for which the *i*th element is the price of a given stock on day *i*.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

**Example 1:**

```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```

**Example 2:**

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```



**Submission:**

- Python

```python
class Solution:
  	# Time Limited Exceeded
		def maxProfit(self, prices: List[int]) -> int:
        
        total_profit = 0
        for i in range(len(prices)-1):
            for j in range(len(prices)-i-1):
                total_profit = prices[i+j+1] - prices[i] if (prices[i+j+1] - prices[i] > total_profit) else total_profit
                # total_profit = max(prices[i:]) - prices[i] if (max(prices[i:]) - prices[i]) > total_profit else total_profit
                
        return total_profit
      
   
    
    
    # beats 98.14% in runtime, 83.91% in memory
    def maxProfit(self, prices: List[int]) -> int:
        
        # exception handler
        if len(prices) <= 0:
            return 0
        
        # dynamic programming
        dp0 = [0, 0]
        dp1 = [-prices[0], 0]

        for i in range(len(prices)):
            tmp = dp1[0]
            dp1[0] = max(dp1[0], -prices[i])
            dp0[1] = max(dp0[1], tmp + prices[i]) # 保持 or 卖出
                
        return dp0[1]
      
'''
我们来考虑更普遍的情况：可买卖k次(但好像一个implicit的假设是最多只能持有一手,这一点在122中提到了)。动态规划的关键在于状态以及状态转移方程如何定义，首先考虑影响状态的变量：
	- 当前处于第几天
	- 已经交易的次数
	- 手头是否持有股票

即根据手头是否持有股票，我们定义两个二维数组来定义状态：

	dp0[i][j]: 第i天结束，已有j次买+卖，手头没有股票时的最大利润
	dp1[i][j]: 第i天结束，已有j次买+卖，手头有股票时的最大利润
	
	因此，dp0[0][j]对于所有j都要初始化为0，而dp1[0][j]对于所有j都要初始化为-prices[i]。
	如果我们将dp0所有值都求出来了，那么很明显dp0[n-1][k]就是在最后一天结束时已进行k次交易且手头无股票时的最大收益，也即返回结果。
	
	先看初始状态：
		当 i == 0 and j >= 0: dp0[0][j] = 0, dp1[0][j] = -prices[0];
		当 i > 0 and j == 0: dp0[i][0] = 0, dp1[i][0] = max(dp1[i-1][0], -prices[i]); # 考虑价格最低时的时候买进持有
		
	再来考虑状态转移方程，当i>0且j>0时有：
		dp0[i][j] = max(dp0[i-1][j], dp1[i-1][j-1] + prices[i]) # 保持 or 卖出
		dp1[i][j] = max(dp1[i-1][j], dp0[i-1][j]   - prices[i]) # 保持 or 买入
		
	有了状态定义和转移方程，剩下就好办了，接下来我们试着对具体问题具体分析
	
        对于121这道题目，因为比较简单, dp的过程能够更加简洁：
            定义dp[i]代表”在第i天卖出时的最大获益”，则dp[i]的值该如何得到？根据在哪一天买入我们可以分成两种情况：
                - 在第i天买入在第i天卖出；
                - 在第i天前某一天买入在第i天卖出；

            对于第1种情况，即在同一天买入卖出，获益0；对于第2种情况，因为dp[i-1]代表在第i-1天卖出时的最大获益，那如果我在第i-1天不卖而是在第i天卖不就是这种情况下的最大获益吗，此时获益为dp[i-1] + prices[i] - prices[i-1]。所以状态转移方程为：
                dp[i] = max(0, dp[i-1] + prices[i] - prices[i-1])

		有一个小问题是，是在loop中实时比较和更新Global Optimum(==max(dp))更快，还是到最后用max(dp)更快呢？
		简单做一下实验：
		
		runtime -> 60/64 ms, memory -> 13.9/14.0 MB
		def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) <= 0:
            return 0
        
        dp = [0] * len(prices)

        for i in range(1, len(prices)):
            dp[i] = max(0, dp[i-1] + prices[i] - prices[i-1])
                
        return max(dp)
     
    runtime ~ 70 ms, memory -> 13.6/8/9 MB
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) <= 0:
            return 0
        
        dp = [0] * len(prices)
        max_p = 0

        for i in range(1, len(prices)):
            dp[i] = max(0, dp[i-1] + prices[i] - prices[i-1])
            max_p = max(max_p, dp[i])
        
        return max_p
        
        
   最后比较的solution的runtime更少，但是可能会用更多的空间
   '''
```



- C++

```c++

```



- Java

```java

```



​	