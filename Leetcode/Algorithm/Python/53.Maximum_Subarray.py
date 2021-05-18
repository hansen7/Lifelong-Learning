# -*- coding: utf-8 -*-
# @Author: Hanchen Wang
# @Date:   2020-11-24 04:56:54
# @Last Modified by:   Hanchen Wang
# @Last Modified time: 2021-05-18 08:25:25

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        # ref: https://leetcode.com/problems/maximum-subarray/discuss/\
        # 20193/DP-solution-and-some-thoughts

        if nums is None: return 0

        max_sum = nums[0]
        max_sub_sum = nums[0]
        
        for num in nums[1:]:
            max_sub_sum = max_sub_sum + num if max_sub_sum > 0 else num
            max_sum = max(max_sum, max_sub_sum)
        return max_sum

