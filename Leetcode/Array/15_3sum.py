# -*- coding: utf-8 -*-
# @Author: Hanchen Wang
# @Date:   2021-01-06 13:40:04
# @Last Modified by:   Hanchen Wang
# @Last Modified time: 2021-01-06 14:27:09

class Solution:

    # def threeSum1(self, nums: List[int]) -> List[List[int]]:
    def threeSum1(self, nums):
        """ 3sum = 1 + 2sum """
        target = 0
        nums.sort()
        result = list()
        if len(nums) < 3: return result

        for idx in range(len(nums) - 2):
            if nums[idx] > (target//3 + 1): 
                return result
            elif (nums[idx] == nums[idx-1]) and (idx > 0):  # remove redundants
                continue
            twosum_ = self.twoSum(nums[idx+1:], target - nums[idx])
            if twosum_: result += twosum_
        return result

    # def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
    def twoSum(self, nums, target):
        """ in 167_two-sum-ii.py """
        head, tail, result = 0, len(nums) - 1, list()
        while head < tail:
            curr = nums[head] + nums[tail]
            if curr == target:
                if [-target, nums[head], nums[tail]] not in result:
                    result.append([-target, nums[head], nums[tail]])
                head += 1
            elif curr < target:
                head += 1
            else:
                tail -= 1
            return result if len(result) else None


if __name__ == "__main__":

    test_case = [0, 0, 0]
    expect_ans = [[0, 0, 0]]
    solver = Solution()
    print(solver.threeSum1(test_case))
    print(solver.threeSum1(test_case) == expect_ans)
