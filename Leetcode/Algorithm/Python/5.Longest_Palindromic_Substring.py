# -*- coding: utf-8 -*-
# @Author: Hanchen Wang
# @Date:   2020-11-24 04:56:54
# @Last Modified by:   Hanchen Wang
# @Last Modified time: 2021-05-18 08:00:12

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        # dual pointers
        # time limit exceeded
        
        max_len = 0
        head = tail = None

        for slow_pt in range(len(s)):
            for fast_pt in range(slow_pt, len(s)):
                str_ = s[slow_pt:fast_pt+1]
                if str_ == str_[::-1] and (fast_pt - slow_pt) > max_len:
                    max_len = fast_pt - slow_pt
                    head, tail = slow_pt, fast_pt
        if head is None:
            return s[0] if s else None
        return s[head:tail+1] 


    def longestPalindrome2(self, s: str) -> str:
        # Manacher algorithm, not well understand,  most efficient
        # http://en.wikipedia.org/wiki/Longest_palindromic_substring
        # first is transformation, e.g., s = 'abba' -> '^#a#b#b#a#$'
        # ^ and $ signs are sentinels appended to each end to avoid bounds checkings

        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0

        # we will choose the each element of center
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i])
            # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen)//2: (centerIndex + maxLen)//2]


    def longestPalindrome3(self, s: str) -> str:

        n = len(s)
        result = ''
        dp = [[False] * n] * n  
        # dp[i, j] == True -> s[i:j+1] is a Palindrome
        
        for i in reversed(range(n)):  # n-1, ..., 1, 0
            dp[i][i] = True  # same as first if in below
            
            for j in range(i, n):    
                # if i == j:  # diagonal
                #     dp[i][j] = True
                
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] if i+1 <= j-1 else True
                
                if dp[i][j] and j+1-i > len(result):  # update result
                    result = s[i:j+1]
        return result 

