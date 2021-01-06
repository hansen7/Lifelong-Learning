# -*- coding: utf-8 -*-
# @Author: Hanchen Wang
# @Date:   2021-01-06 12:47:43
# @Last Modified by:   Hanchen Wang
# @Last Modified time: 2021-01-06 12:53:17


class Solution:
    
    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        """ almost same to twoSum3 in 1_two-sum.py """
        # nums_index = [(v, index) for index, v in enumerate(numbers)]
        head, tail = 0, len(numbers) - 1
        while head < tail:
            curr = numbers[head] + numbers[tail]
            if curr == target:
                return head + 1, tail + 1
            elif curr < target:
                head += 1
            else:
                tail -= 1
