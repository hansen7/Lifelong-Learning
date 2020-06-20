### 67. Add Binary

**Description**:

​	Given two binary strings, return their sum (also a binary string).

​	The input strings are both non-empty and contains only characters 1 or 0.

**Example:**

```markdown
Input: a = "11", b = "1"
Output: "100"

Input: a = "11", b = "1"
Output: "100"
```



**Submission:**

- Python

```python
class Solution:
    """
        :type a: str
        :type b: str
        :rtype: str
    """

    # beats 6.53%, not quick
    def addBinary(self, a, b):
        return str(bin(int(a, base=2) + int(b, base=2))).replace('0b', '')

    # beats 36.30%
    def addBinary2(self, a, b):
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        carry = 0
        result = ''

        for idx in range(max_len-1, -1, -1):
            curr = carry
            if a[idx] == '1':
                curr += 1
            if b[idx] == '1':
                curr += 1
            curr, carry = curr % 2, curr // 2
            result = str(curr) + result
        if carry:
            result = '1' + result
        return result

    # beats 92.69%, the variate a lot
    def addBinary3(self, x, y):

        max_len = max(len(x), len(y))

        x = x.zfill(max_len)
        y = y.zfill(max_len)

        result = ''
        carry = 0

        for i in range(max_len-1, -1, -1):
            curr = carry
            curr += 1 if x[i] == '1' else 0
            curr += 1 if y[i] == '1' else 0
            result = ('1' if curr % 2 == 1 else '0') + result
            carry = 0 if curr < 2 else 1

        if carry:
            result = '1' + result

        return result

'''Test Code'''
a, b = '1001', '101'
a, b = '1', '11'
solve = Solution()
print(solve.addBinary2(a, b))
```



- C++

```c++

```



- Java

```java

```



​	