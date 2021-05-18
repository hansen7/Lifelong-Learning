# -*- coding: utf-8 -*-
# @Author: Hanchen Wang
# @Date:   2020-11-24 04:56:54
# @Last Modified by:   Hanchen Wang
# @Last Modified time: 2021-05-18 09:16:45


class Solution:
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # recursion, time limit exceeded
        n_steps = len(triangle)  # depth

        def minsum(i: int, j: int) -> int:
            # the minimum sum of the path 
            # from triangle[i][j] to the bottom
            if i == n_steps - 1:  # the bottom row
                return triangle[i][j]
            return min(minsum(i+1, j), minsum(i+1,j+1)) + triangle[i][j]

        return minsum(0, 0)


    def minimumTotal(self, triangle: List[List[int]]) -> int:

        # traceback, dynamic programming
        # space complexity: O(n**2)

        depth = len(triangle)
        # if depth == 0: return 0

        minsum = [[0] * depth for i in range(depth)]
        minsum[depth-1] = triangle[depth-1]  # bottom

        # fill the lower triangle of dp
        for i in range(depth-2, -1, -1):  # depth-2, ..., 1, 0
            for j in range(i+1):  # 0, 1, ..., i
                minsum[i][j] = min(minsum[i+1][j], minsum[i+1][j+1]) + triangle[i][j]

        return minsum[0][0]
        

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # essentially also traceback, save some space, O(n)

        depth = len(triangle)
        # if depth == 0: return 0

        minsum = triangle[-1]  # a 1-D list of length n
        for i in range(depth-2, -1, -1):
            for j in range(i+1):
                minsum[j] = min(minsum[j], minsum[j+1]) + triangle[i][j]

        return minsum[0]

