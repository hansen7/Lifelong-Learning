### 2. Add Two Numbers

**Description**:

​	You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



**Example:**

```
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
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
            list_ = [self.val];
            while self.next:
                self = self.next
                list_.append(self.val)
            print(list_)

class Solution:
    # Beats 86.58%
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        l1, l2 is two pointers that point at the beginning of the ListNodes
        """
        # 'current' -> value for current digit
        # 'carry' -> carry for next digit

        # beginning
        head_ = ListNode(0)
        current, carry = head_, 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            carry, val = val//10, val%10
            # carry, val = divmod(val, 10)
            # if we use the built-in func: divmod(x, y), which returns the tuple (x//y, x%y), the programme will be slower
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        # head_ is the node that has a val = 0, and points at the beginning of the ListNode
        return head_.next





'''Test Code'''

node1, node2, node3 = ListNode(2), ListNode(4), ListNode(3)
node2.next = node3
node1.next = node2
node_1 = node1
del node1, node2, node3

node1, node2 = ListNode(5), ListNode(6)
node1.next = node2
node_2 = node1
del node1, node2

solve = Solution()
node_1.print()
node_2.print()
solve.addTwoNumbers1(node_1, node_2).print()
```



- C++

```c++

```



- Java

```java

```



​	