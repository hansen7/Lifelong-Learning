### 923. 3Sum With Multiplicity

**Description:**

​	Given an integer array A, and an integer ``target``, return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == ``target``.

As the answer can be very large, return it modulo 10^9 + 7.

**Example1:**

```markdown
Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
```



**Example2**:

```markdown
Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
```


**Note:**

1. 3 <= A.length <= 3000
2. 0 <= A[i] <= 100
3. 0 <= target <= 300



Submission:**

- Python

```python
import collections

class Solution:
    #beats 92.22%
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        #return a dict, while the keys are the list numbers, and the values are the frequency
        count = collections.Counter(A)
        set_A = set(A)
        list_A = list(set_A)
        list_A.sort()
        res = 0

        for i in range(len(list_A)):
            for j in range(i, len(list_A)):
                c = target - list_A[i] - list_A[j]
                if c >= list_A[j] and c in set_A:
                    if list_A[i] != list_A[j] != c:
                        res += count[list_A[i]] * count[list_A[j]] * count[c]
                    elif list_A[i] == list_A[j] and list_A[j] != c:
                        res += count[c] * self.caculate(count[list_A[i]], 2)
                    elif list_A[j] == c and list_A[i] != list_A[j]:
                        res += count[list_A[i]] * self.caculate(count[list_A[j]], 2)
                    elif list_A[i] == c and list_A[j] != c:
                        res += count[list_A[j]] * self.caculate(count[c], 2)
                    else:
                        res += self.caculate(count[list_A[i]], 3)
        return res % (10 ** 9 + 7)

    def caculate(self, x, i):
        if i == 2:
            return x * (x - 1) / 2
        elif i == 3:
            return x * (x - 1) * (x - 2) / 6

'''Test Code'''

nums = [-1, -1, -2, 2, 2, 3, 4, 5]
target = 0

solution = Solution()
print(solution.threeSumMulti([1,2,2,2,3,4], 5))
#print(solution.twoSum([0,0], target))
```



- C++

```c++

```



- Java

```java

```



​	