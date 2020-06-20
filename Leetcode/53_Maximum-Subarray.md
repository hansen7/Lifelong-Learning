### 53. Maximum Subarrray

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Follow up:**

If you have figured out the O(*n*) solution, try coding another solution using the divide and conquer approach, which is more subtle.

**Submission:**

- Python

```python
'''Dynamic Programming
ref: https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts'''
class Solution:
    '''Runtime: 60 ms, faster than 94.35% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.6 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        
        max_sum = nums[0]
        max_sub_sum = nums[0]
        
        for num in nums[1:]:
            max_sub_sum = max_sub_sum + num if max_sub_sum > 0 else num
            max_sum = max(max_sum, max_sub_sum)
        return max_sum
    
    
'''Divide and Conquer 分而治之'''
class Solution:
    '''Runtime: 120 ms, faster than 5.03% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.6 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.
    '''
    # Find the maximum possible sum in 
    # arr[] auch that arr[m] is part of it 
    def maxCrossingSum(self, arr, l, m, h) : 
      
        # Include elements on left of mid. 
        sm, left_sum = 0, -10000
      
        for i in range(m, l-1, -1) : 
            sm = sm + arr[i] 
          
            if sm > left_sum: 
                left_sum = sm 
      
      
        # Include elements on right of mid 
        sm, right_sum = 0, -1000
        
        for i in range(m + 1, h + 1) : 
            sm = sm + arr[i] 
          
            if sm > right_sum: 
                right_sum = sm 
      
  
        # Return sum of elements on left and right of mid 
        return left_sum + right_sum; 

    def maxSubArraySum(self, arr, l, h): 
      
        # Base Case: Only one element 
        if (l == h) : 
            return arr[l] 
  
        # Find middle point 
        m = (l + h) // 2

        # Return maximum of following three possible cases 
        # a) Maximum subarray sum in left half 
        # b) Maximum subarray sum in right half 
        # c) Maximum subarray sum such that the  
        #     subarray crosses the midpoint  
        return max(self.maxSubArraySum(arr, l, m), 
                   self.maxSubArraySum(arr, m+1, h), 
                   self.maxCrossingSum(arr, l, m, h))
    
    def maxSubArray(self, nums: List[int]) -> int:
        return self.maxSubArraySum(nums, 0, len(nums) - 1) 
        
```



- C++

```c++

```



- Java

```java

```



​	