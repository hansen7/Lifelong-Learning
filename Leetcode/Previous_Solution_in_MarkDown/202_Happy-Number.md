### 202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

**Example:** 

```
Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
```

**Submission**

- Python

```python
class Solution:
	'''
	Runtime: 28 ms, faster than 88.07% of Python3 online submissions for Happy Number. 
	Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions for Happy Number.'''
	def isHappy(self, n: int) -> bool:
        slow = n
        fast = n 
        while True:       
            # move slow number by one iteration 
            slow = self.numSquareSum(slow)       
            # move fast number by two iteration 
            fast = self.numSquareSum(self.numSquareSum(fast)); 
            
            if slow == fast: 
				break
  
        # if both number meet at 1,  then return true 
        return (slow == 1)
    
    def numSquareSum(self, n): 
        squareSum = 0
        while n: 
            squareSum += (n%10) ** 2
            n = int(n/10)
        return squareSum
    

    
class Solution:
    '''Runtime: 24 ms, faster than 96.98% of Python3 online submissions for Happy Number.
Memory Usage: 13.7 MB, less than 5.26% of Python3 online submissions for Happy Number.'''
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            if n in s: 
                return False
            s.add(n)
            # n = sum([int(i) ** 2 for i in str(n)]) -> 32 ms
            n = sum(map(lambda x:int(x)**2, str(n)))
        
        return True
```



- C++

```c++

```



- Java

```java

```



​	