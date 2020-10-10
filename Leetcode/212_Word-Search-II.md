### 212. Word Search II

**Description:**

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

**Example1:**

```markdown
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
```



**Note:**

1. All inputs are consist of lowercase letters `a-z`.
2. The values of `words` are distinct.



**Submission:**

- Python

```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return []
        m, n = len(board), len(board[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        tree = Trie()
        for word in words:
            tree.insert(word)
        words = set(words)
        
        res = set()
        
        def dfs(x0, y0, node, tmpword):
            visited.add((x0, y0))
            for k in range(4):
                x = x0 + dx[k]
                y = y0 + dy[k]
                
                if 0 <= x < m and 0 <= y < n and board[x][y] in node and (x, y) not in visited:
                    visited.add((x, y))
                    dfs(x, y, node[board[x][y]], tmpword + board[x][y])
                    visited.remove((x,y))
                    
            if tmpword in words:
                res.add(tmpword)
                return
                
        for i in range(m):
            for j in range(n):
                if board[i][j] in tree.root:
                    visited = set((i, j))
                    dfs(i, j, tree.root[board[i][j]], board[i][j])
        return list(res)
            
        
class Trie:
    """"""
    def __init__(self):
        """initialise the data structure"""
        self.root = {}
        
    def insert(self, word):
        """inserts a word into the trie"""
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node['end'] = True
        
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]           
        return True
    
```



- C++

```c++

```



- Java

```java

```



​	