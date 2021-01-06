### 695. Max Area of Island

Given a non-empty 2D array `grid` of 0's and 1's, an **island** is a group of `1`'s (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

**Example 1:**

```
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
```

Given the above grid, return `6`. Note the answer is not 11, because the island must be connected 4-directionally.

**Example 2:**

```
[[0,0,0,0,0,0,0,0]]
```

Given the above grid, return `0`.

**Note:** The length of each dimension in the given `grid` does not exceed 50.



**Submission:**

- Python

```python
# Runtime: 140 ms, faster than 89.86% of Python3 online submissions for Max Area of Island.
# Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Max Area of Island.


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m * n == 0:
            return 0
        
        area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = max(area, self.helper(grid, i, j))
        return area
      
    def helper(self, grid: List[List[int]], x: int, y:int):
        if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y]==0:
            return 0
        grid[x][y] = 0
        return 1 + self.helper(grid, x - 1, y) + self.helper(grid, x + 1, y) + \
    self.helper(grid, x, y - 1) + self.helper(grid, x, y + 1)
```



- C++

```c++

```



- Java

```java

```



​	