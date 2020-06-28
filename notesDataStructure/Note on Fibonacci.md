先简要回顾Fibonacci数列的递推公式，由Fibonacci数列的定义可得

![image-20180806161157351](/var/folders/c_/q1g90c_s3d712_h2cljszmx40000gp/T/abnerworks.Typora/image-20180806161157351.png)

又有

![image-20180806161542742](/var/folders/c_/q1g90c_s3d712_h2cljszmx40000gp/T/abnerworks.Typora/image-20180806161542742.png)

![image-20180806161834349](/var/folders/c_/q1g90c_s3d712_h2cljszmx40000gp/T/abnerworks.Typora/image-20180806161834349.png)

如此一来，计算斐波那契数列的问题就转化为了求Q的n−1次幂的问题。我们使用矩阵快速幂的方法来达到O(log(n))O(log⁡(n))的复杂度。借助分治的思想，快速幂采用以下公式进行计算：![image-20180806162325421](/var/folders/c_/q1g90c_s3d712_h2cljszmx40000gp/T/abnerworks.Typora/image-20180806162325421.png)



采用递归可以在Python中快速实现上速算法：

```python
def Fibonacci_matrix(n):
    def mul(a, b):
        return ((a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]),
                (a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]))

    def power(x, n):
        if n == 1:
            return x
        ans = power(mul(x, x), n / 2)
        if n % 2:
            ans = mul(x, ans)
        return ans

    if n == 0:
        return 0
    if n == 1:
        return 1
    q = ((1, 1), (1, 0))
    return power(q, n - 1)[0][0]
```

上述程序中`mul`函数执行两个2×2矩阵的乘法，`power`函数递归计算矩阵的快速幂。为了进一步提高效率，我们修改`power`函数舍弃递归转而采用循环来计算快速幂。修改后的Python代码如下：

```python
def Fibonacci_matrix_iteration(n):
    def mul(a, b):
        return ((a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]),
                (a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]))

    def power(x, n):
        if n == 1:
            return x
        y = ((1, 0), (0, 1))
        while n > 1:
            if n % 2:
                y = mul(x, y)
            x = mul(x, x)
            n /= 2
        return mul(x, y)

    if n == 0:
        return 0
    if n == 1:
        return 1
    q = ((1, 1), (1, 0))
    return power(q, n - 1)[0][0]
```

升级递归算法

对于斐波那契数列，我们还有以下这样的递推公式：

![image-20180806164000973](/var/folders/c_/q1g90c_s3d712_h2cljszmx40000gp/T/abnerworks.Typora/image-20180806164000973.png)

```python
def Fibonacci_recursion_fast(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    k = (n + 1) / 2 if n % 2 else n / 2
    fib_k = Fibonacci_recursion_fast(k)
    fib_k_1 = Fibonacci_recursion_fast(k - 1)
    return fib_k**2 + fib_k_1**2 if n % 2 else (2 * fib_k_1 + fib_k) * fib_k
```

