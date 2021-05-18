### 120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```

The minimum path sum from top to bottom is `11` (i.e., **2** + **3** + **5** + **1** = 11).

**Note:**

Bonus point if you are able to do this using only *O*(*n*) extra space, where *n* is the total number of rows in the triangle.



**Submission:**

- Python

```python
class Solution:
  	# Time limit exceeded -> recursion
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n_steps = len(triangle)
        
        def minsum(i:int, j:int) -> int:
            if i == n_steps-1:
                return triangle[i][j]
            return min(minsum(i+1, j), minsum(i+1,j+1)) + triangle[i][j]
        
        return minsum(0,0)
      
  
    # Runtime: 52 ms, faster than 95.65% of Python3 online submissions for Triangle.
	# Memory Usage: 14.1 MB, less than 20.00% of Python3 online submissions for Triangle.
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n_steps = len(triangle)       
        if n_steps == 0:
            return 0
        
        # n_steps * n_steps array
        minsum = [[0] * n_steps for i in range(n_steps)]
        minsum[n_steps-1] = triangle[n_steps-1]
        
        for i in range(n_steps-2, -1, -1):
            for j in range(i+1):
                minsum[i][j] = min(minsum[i+1][j], minsum[i+1][j+1]) + triangle[i][j]
        
        return minsum[0][0]
    
		# Runtime: 52 ms, faster than 95.65% of Python3 online submissions for Triangle.
		# Memory Usage: 13.4 MB, less than 86.67% of Python3 online submissions for Triangle.
    # optimise for the space usage
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        n_steps = len(triangle)       
        if n_steps == 0:
            return 0
        
        # n_steps array
        minsum = triangle[-1]
        
        for i in range(n_steps-2, -1, -1):
            for j in range(i+1):
                minsum[j] = min(minsum[j], minsum[j+1]) + triangle[i][j]

        return minsum[0]
      
```



- C++

```c++

```



- Java

```java

```



​	