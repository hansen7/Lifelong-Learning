### 653. Two Sum IV - Input is a BST

**Description**:

​	Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

**Example1:**

```markdown
**Input**: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

**Output**: True
```

**Example2:**

```markdown
**Input**: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

**Output**: True
```
**Submission:**

- Python

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# beats 34.69%, 先变成set，再在set中进行搜索
class Solution1(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.dset = set()
        self.traverse(root)
        for n in self.dset:
            if k - n != n and k - n in self.dset:
                return True
        return False

    def traverse(self, root):
        if not root: return
        self.dset.add(root.val)
        self.traverse(root.left)
        self.traverse(root.right)


# beats 72.19%, 这个其实还是比上一个方法快很多的
class Solution2(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.root = root
        self.k = k
        return self.findNumber(root)

    def findNumber(self, root):
        if not root:
            return False
        node = self.root
        n = self.k - root.val
        if n != root.val:
            while node:
                if node.val == n:
                    return True
                if n > node.val:
                    node = node.right
                else:
                    node = node.left
        return self.findNumber(root.left) or self.findNumber(root.right)
```



- C++

```c++
class TwoSum {
public:
    void add(int number) {
        ++m[number];
    }
    bool find(int value) {
        for (auto a : m) {
            int t = value - a.first;
            if ((t != a.first && m.count(t)) || (t == a.first && a.second > 1)) {
                return true;
            }
        }
        return false;
    }
private:
    unordered_map<int, int> m;
};
```



- Java (Save for later)

```java

```



​	