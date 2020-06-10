### 309. Best Time to Buy and Sell Stock with Cooldown

Say you have an array for which the *i*th element is the price of a given stock on day *i*.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

- You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
- After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

**Example:**

```
Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```



**Submission**

- Python

```python
class Solution:
  	# Runtime: 36 ms, faster than 79.96% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
		# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.

    def maxProfit(self, prices: List[int]) -> int:
        n_days = len(prices)
        
        if n_days == 0:
            return 0
        
        dp0 = [0] * n_days
        dp1 = [0] * n_days
        cool_d = [0] * n_days
        dp1[0] = - prices[0]
        
        for i in range(1, n_days):
            dp0[i] = max(dp0[i-1], dp1[i-1] + prices[i])
            dp1[i] = max(dp1[i-1], cool_d[i-1] - prices[i])
            cool_d[i] = max(cool_d[i-1], dp0[i-1])
            
        return dp0[n_days-1]

  
class Solution:
		# Runtime: 32 ms, faster than 93.11% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
		# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.

    def maxProfit(self, prices: List[int]) -> int:
        n_days = len(prices)
        
        if n_days == 0:
            return 0
        
        dp0 = 0
        dp1 = - prices[0]
        cool_d = 0  # no need to cooldown at the beginning
        
        for i in range(1, n_days):
            pre_dp0 = dp0
            dp0 = max(dp0, dp1 + prices[i])
            dp1 = max(dp1, cool_d - prices[i])
            cool_d = max(cool_d, pre_dp0)
            
        return dp0
```



- C++

```c++
int maxProfit(vector<int>& prices) {
    int n = prices.size();
    if(!n) return 0;
    
    // vector<int>dp0(n, 0);
    // vector<int>dp1(n, 0);
    // vector<int>cool(n, 0);
    // dp1[0] = - prices[0]; // i = 0
    // for(int i = 1; i < n; i++){
    //     dp0[i] = max(dp0[i-1], dp1[i-1] + prices[i]); 
    //     dp1[i] = max(dp1[i-1], cool[i-1] - prices[i]);
    //     cool[i] = max(cool[i-1], dp0[i-1]);
    // }
    // return dp0[n-1];
    // 空间优化后:
    int dp0 = 0, dp1 = - prices[0], cool = 0;
    for(int i = 1; i < n; i++){
        int pre_dp0 = dp0;
        dp0 = max(dp0, dp1 + prices[i]);
        dp1 = max(dp1, cool - prices[i]);
        cool = max(cool, pre_dp0);
    }
    return dp0;
}
```



- Java

```java

```



​	