# -*- coding: utf-8 -*-
# @Author: Hanchen Wang
# @Date:   2021-01-06 10:44:10
# @Last Modified by:   Hanchen Wang
# @Last Modified time: 2021-01-06 12:42:29


class Solution:

    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        """hash, basic"""

        # generate a hash table, O(n)
        hash_nums = dict()
        for index, num in enumerate(nums):
            try:
                hash_nums[num].append(index)
            except KeyError:
                hash_nums[num] = [index]

        # loop within the table, O(n)
        for index, num in enumerate(nums):
            try:
                candidate = hash_nums[target - num]
                if target == 2 * num:
                    if len(candidate) > 1:
                        # candidate1 = candidate2 = target/2
                        # yet numbers are assumed to be unique as described
                        # the site still contains test examples such as: [3,2,4], 6
                        return candidate
                    else:
                        continue
                else:
                    return [index, candidate[0]]
            except KeyError:
                pass

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """a better hash"""

        # generate and search within a hash table simultaneously, O(n)
        hash_nums = dict()
        for index, num in enumerate(nums):
            residue = target - num
            try:
                hash_nums[residue]
                return [hash_nums[residue], index]
            except KeyError:
                hash_nums[num] = index

    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        ''' still hash, dual pointers, also for two sum ii '''

        # a slightly different way for creating a hash table
        nums_index = [(v, index) for index, v in enumerate(nums)]
        nums_index.sort()

        # dual pointers instead for looping
        head, tail = 0, len(nums) - 1
        while head < tail:
            curr = nums_index[head][0] + nums_index[tail][0]
            if curr == target:
                return [nums_index[head][1], nums_index[tail][1]]
            elif curr < target:
                head += 1
            else:
                tail -= 1

    def twoSum4(self, nums: List[int], target: int) -> List[int]:
        """fateset, similar to twoSum2"""
        hash_nums = {}
        for idx, num in enumerate(nums):
            if target - num in hash_nums:
                return [hash_nums[target - num], idx]
            hash_nums[num] = idx

    def twoSum5(self, nums: List[int], target: int) -> List[int]:
        """try .index(),
        https://docs.python.org/3/tutorial/datastructures.html#more-on-lists"""
        for i in nums:
            j = target - i
            tmp_nums = nums[nums.index(i) + 1:]
            if j in tmp_nums:
                return [nums.index(i), nums.index(i) + 1 + tmp_nums.index(j)]
