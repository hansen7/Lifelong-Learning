### 50. Pow(x, n)

Implement pow(*x*, *n*), which calculates *x* raised to the power *n* (xn).

**Example 1:**

```
Input: 2.00000, 10
Output: 1024.00000
```

**Example 2:**

```
Input: 2.10000, 3
Output: 9.26100
```

**Example 3:**

```
Input: 2.00000, -2
Output: 0.25000
Explanation: 2^{-2} = 1/2^2 = 1/4 = 0.25
```

**Note:**

- -100.0 < *x* < 100.0
- *n* is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]

**Submission:**

- Python

```python
# n有可能是正数或者负数，分开计算。

# 用递归的做法讲复杂度降到O（logn）。

# Runtime: 28 ms, faster than 87.81% of Python3 online submissions for Pow(x, n).
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Pow(x, n).
class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0: return 1
        # if n == 1: return x

        if n > 0:
            if n%2:
                temp = self.myPow(x, (n-1)/2)
                return temp * temp * x
            else:
                temp = self.myPow(x, n/2)
                return temp * temp
        else:
            #if n%2:
            #    temp = self.myPow(x, abs((n+1)/2))
            #    return 1./(temp * temp * x)
            #else:
            #    temp = self.myPow(x, abs(n/2))
            #    return 1./(temp * temp)
            return 1./self.myPow(x, -n)
        
```



- C++

```c++

```



- Java

```java

```



​	