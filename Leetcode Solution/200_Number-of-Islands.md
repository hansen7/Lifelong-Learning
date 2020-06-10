### 200. Number of Islands

Given a 2d grid map of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**

```
Input:
11110
11010
11000
00000

Output: 1
```

**Example 2:**

```
Input:
11000
11000
00100
00011

Output: 3
```

**Submission:**

- Python

```python
# Runtime: 192 ms, faster than 12.02% of Python3 online submissions for Number of Islands.
# Memory Usage: 14 MB, less than 30.77% of Python3 online submissions for Number of Islands.


class Solution:
    def _numIslands(self, grid: List[List[str]], x: int, y: int, visited: List[List[int]]):
        neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def inArea(x:int, y:int):
            return x>=0 and x<len(grid) and y>= 0 and y < len(grid[0])
        
        visited[x][y] = True
        
        for i in range(4):
            x_ = x + neighbors[i][0]
            y_ = y + neighbors[i][1]
            if inArea(x_, y_) and not visited[x_][y_] and grid[x_][y_] == '1':
                self._numIslands(grid, x_, y_, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = list()
        for val in grid:
            t = list()
            for _ in val:
                t.append(False)
                
            visited.append(t)
        count = 0
        
        for i, val in enumerate(grid):
            for j, _ in enumerate(val):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    self._numIslands(grid, i, j, visited)
                    
        return count

"""这个问题比上一个问题特殊，我们没法针对问题得到先验知识，所以我们无法在算法的初始对算法进行优化。难道就没什么优化了吗？有。我们不使用visited记录访问过的元素，而是通过对已访问过的元素直接赋0的方式，因为我们知道已访问过的元素，我们不会再访问了。这是一步非常强力的优化。"""

"""
Runtime: 128 ms, faster than 97.98% of Python3 online submissions for Number of Islands.
Memory Usage: 13.7 MB, less than 80.34% of Python3 online submissions for Number of Islands.
"""
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
            
        result = 0
        m, n = len(grid), len(grid[0])
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    result += 1
                    self._numIslands(grid, row, col)
                    
        return result

    def _numIslands(self, grid, r, c):
        grid[r][c] = '0'
        if 0 < r and grid[r - 1][c] == '1':
            self._numIslands(grid, r - 1,c)

        if 0 < c and grid[r][c - 1] == '1':
            self._numIslands(grid, r, c - 1)

        if c < len(grid[0]) -1 and grid[r][c + 1] =='1':
            self._numIslands(grid, r, c + 1)

        if r < len(grid) - 1 and grid[r + 1][c] == '1':
            self._numIslands(grid, r + 1, c)
        """很多人注意到了我上面没有使用for i in range(4)这种写法，
        实际上我在之前的问题c++版本中也是采用了上面这种写法。为什么呢？因为这样更快。"""
        
        
# 同样的，对于递归解决的问题，我们都应该思考一下怎么通过迭代去解决。
# 我们只要将self._numIslands写成迭代形式即可

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
            
        result = 0
        m, n = len(grid), len(grid[0])

        def _numIslands(grid, r, c):
            if grid[r][c] != '1':
                return 

            stack = list()
            stack.append((r, c))
            while stack:
                x, y  = stack.pop()
                if grid[x][y] != '1':
                    continue

                grid[x][y] = '0'
                directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                for d in directions:
                    nr = x + d[0]
                    nc = y + d[1]
                    if 0 <= nr < m and 0 <= nc < n:
                        stack.append((nr, nc))

        for row in range(m):
            for col in range(n):
                if grid[row][col] == '1':
                    result += 1
                    _numIslands(grid, row, col)
                    
        return result
```



- C++

```c++

```



- Java

```java

```



​	