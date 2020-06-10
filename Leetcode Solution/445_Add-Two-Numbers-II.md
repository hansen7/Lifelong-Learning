### 445. Add Two Numbers II

**Description**:

​	You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

​	You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Follow up:**

​	What if you cannot modify the input lists? In other words, reversing the lists is not allowed.



**Example:**

```
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
```



**Submission:**

- Python

```python
# Definition for singly-linked list.
# For more info on ListNode with Python, see here: https://stackabuse.com/python-linked-lists/ or
# https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print(self):
        if self.val is None:
            print('This is an empty ListNode.')
        else:
            list_ = [self.val]
            while self.next:
                self = self.next
                list_.append(self.val)
            print(list_)

class Solution:
    # Beats 94.38%
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        l1, l2 is two pointers that point at the beginning of the ListNodes
        """


        # head_ is the node that has a val = 0, and points at the beginning of the ListNode
        return self.span_(self.pave_(l1) + self.pave_(l2))

    def pave_(self, ListNode):
        if ListNode.val is None:
            return None
        else:
            number = ListNode.val
            while ListNode.next:
                ListNode = ListNode.next
                number = number*10 + ListNode.val
            return number

    def span_(self, Number):
        if Number is None:
            return None
        else:
            head_ = ListNode(0)
            current = head_
            str_ = str(Number)
            for idx in range(len(str_)):
                current.next = ListNode(int(str_[idx]))
                current = current.next
            return head_.next





'''Test Code'''


node1, node2, node3, node4 = ListNode(7), ListNode(2), ListNode(4), ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4
node_1 = node1
del node1, node2, node3, node4

node1, node2, node3 = ListNode(5), ListNode(6), ListNode(4)
node1.next = node2
node2.next = node3
node_2 = node1
del node1, node2, node3

solve = Solution()
node_1.print()
node_2.print()
solve.addTwoNumbers(node_1, node_2).print()
```



- C++

```c++

```



- Java

```java

```



​	