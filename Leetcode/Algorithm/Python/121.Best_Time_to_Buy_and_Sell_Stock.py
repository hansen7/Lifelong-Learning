# -*- coding: utf-8 -*-
# @Author: Hanchen Wang
# @Date:   2020-11-24 04:56:54
# @Last Modified by:   Hanchen Wang
# @Last Modified time: 2021-05-18 10:12:39


class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        # quite inefficient
        num_days = len(prices)
        # dp = [0] * num_days
        dp = 0
        max_profit = 0

        for i in range(1, num_days):
            # dp[i] = max(dp[i-1] + prices[i] - prices[i-1], 0)
            dp = max(dp + prices[i] - prices[i-1], 0)
            max_profit = max(max_profit, dp)
            
        return max_profit
        # return max(dp)

    def maxProfit(self, prices: List[int]) -> int:

        num_days = len(prices)
        if num_days <= 1: return 0

        dp0 = [0, 0]
        dp1 = [-prices[0], 0]

        for i in range(len(prices)):
            tmp = dp1[0]
            dp1[0] = max(dp1[0], -prices[i])
            dp0[1] = max(dp0[1], tmp + prices[i]) # 保持 or 卖出
                
        return dp0[1]

        """ 
        我们来考虑更普遍的情况：可买卖k次。

        动态规划的关键在于状态以及状态转移方程如何定义，首先考虑影响状态的变量：
            - 当前处于第几天
            - 已经交易的次数
            - 手头是否持有股票

        根据手头是否持有股票，我们定义两个二维数组来定义状态：
            dp0[i][j]: 第i天结束，已有j次买+卖，手头没有股票时的最大利润
            dp1[i][j]: 第i天结束，已有j次买+卖，手头有股票时的最大利润

        因此，初始化过程为 dp0[0][:] = 0，dp1[i][:] = -prices[i]
        如果我们将dp0所有值都求出来了，那么很明显dp0[n-1][k]
        就是在最后一天结束时已进行k次交易且手头无股票时的最大收益，也即返回结果

        先看初始状态：
            i == 0 and j >= 0:
                dp0[0][j] = 0
                dp1[0][j] = -prices[0];
            
            i > 0 and j == 0:
                dp0[i][0] = 0
                dp1[i][0] = max(dp1[i-1][0], -prices[i]); # 价格最低时的时候买进

        再来考虑状态转移方程，当i>0且j>0时有：
            dp0[i][j] = max(dp0[i-1][j], dp1[i-1][j-1] + prices[i]) # 保持 or 卖出
            dp1[i][j] = max(dp1[i-1][j], dp0[i-1][j]   - prices[i]) # 保持 or 买入

        对于121这道题目，因为比较简单, dp的过程能够更加简洁：
        定义dp[i]代表”在第i天卖出时的最大获益”，则dp[i]的值该如何得到？根据在哪一天买入我们可以分成两种情况：
            - 在第i天买入在第i天卖出；
            - 在第i天前某一天买入在第i天卖出；
            
        对于第1种情况，即在同一天买入卖出，获益0；
        对于第2种情况，因为dp[i-1]代表在第i-1天卖出时的最大获益，
        那如果我在第i-1天不卖而是在第i天卖不就是这种情况下的最大获益吗，
        此时获益为dp[i-1] + prices[i] - prices[i-1]。
        所以状态转移方程为：
            dp[i] = max(0, dp[i-1] + prices[i] - prices[i-1]) """
