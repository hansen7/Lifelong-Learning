### 283. Move Zeroes

Given an array `nums`, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Example:** 

```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

**Note**:

1. You must do this **in-place** without making a copy of the array.
2. Minimize the total number of operations.



**Submission**

- Python

```python
class Solution:
	'''
	Runtime: 288 ms, faster than 9.44% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.1 MB, less than 5.97% of Python3 online submissions for Move Zeroes.'''
	def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        
        for idx in range(len(nums) - 1):
            if nums[idx] == 0:
                for jdx in range(idx, len(nums)):
                    if nums[jdx] != 0:
                        break
                nums[idx] = nums[jdx]
                nums[jdx] = 0
    

    
class Solution:
    '''Runtime: 44 ms, faster than 90.65% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.1 MB, less than 5.97% of Python3 online submissions for Move Zeroes.'''

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
                
        count, n = 0, len(nums) # Count of non-zero elements 
      
        # Traverse the array. If element  
        # encountered is non-zero, then 
        # replace the element at index 
        # 'count' with this element 
        for i in range(n): 
            if nums[i] != 0: 

                # here count is incremented 
                nums[count] = nums[i] 
                count += 1

        # Now all non-zero elements have been 
        # shifted to front and 'count' is set 
        # as index of first 0. Make all  
        # elements 0 from count to end. 
        while count < n: 
            nums[count] = 0
            count += 1
        
```



- C++

```c++

```



- Java

```java

```



​	