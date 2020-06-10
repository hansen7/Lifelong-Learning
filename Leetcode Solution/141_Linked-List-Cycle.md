### 141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer `pos` which represents the position (0-indexed) in the linked list where tail connects to. If `pos`is `-1`, then there is no cycle in the linked list.

**Example 1:**

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

**Example 2:**

```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

**Example 3:**

```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

**Submission**

- Python

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    '''Runtime: 48 ms, faster than 62.59% of Python3 online submissions for Linked List Cycle.
Memory Usage: 17.3 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
    '''
        
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        if head is not None:
            temp = head.next
        
            while temp:
                if (temp in s): 
                    return True
            
                s.add(temp) 
                temp = temp.next
        return False
    
    

class Solution:
    '''
       Runtime: 48 ms, faster than 62.59% of Python3 online submissions for Linked List Cycle.
Memory Usage: 16.9 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
'''
    def hasCycle(self, head: ListNode) -> bool:

        if head and head.next is not None:
            temp = head.next
            fast_temp = temp.next
        
            while temp and fast_temp:
                if temp.val == fast_temp.val: 
                    return True
                temp = temp.next

                if fast_temp.next == None:
                    return False
                fast_temp = fast_temp.next.next
            
        return False
```



- C++

```c++

```



- Java

```java

```



​	