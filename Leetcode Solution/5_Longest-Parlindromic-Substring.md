### 5. Longest Palindromic Substring

**Description**:

​	Given a string ``s``, find the longest palindromic substring in ``s``. You may assume that the maximum length of s is 1000.

**Example1:**

```markdown
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

**Example2**:

    Input: "cbbd"
    Output: "bb"
**Submission:**

- Python

```python
class Solution:
    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Here we assume s is not None, this method exceeds the time limit

        max_length = 0

        longest_begin = longest_end = None

        for slow_pt in range(len(s)):
            for fast_pt in range(slow_pt, len(s)):
                str = s[slow_pt:fast_pt+1]
                if str == str[::-1] and (fast_pt - slow_pt) > max_length:
                    max_length = fast_pt - slow_pt
                    longest_begin = slow_pt
                    longest_end = fast_pt + 1

        if longest_begin is None:
            try:
                return s[0]
            except IndexError:
                return s
        else:
            return s[longest_begin:longest_end]

    # This solution I didn't finish, due to some index error, really annoying
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Here we assume s is not None

        max_length = 0

        longest_begin = longest_end = None

        for slow_pt in range(len(s)):
            for fast_pt in range(slow_pt, (len(s)+slow_pt)//2 + 1):
                str1 = s[slow_pt:fast_pt]
                str2 = s[fast_pt-1:2*fast_pt-slow_pt-1]
                if str1 == str2[::-1] and (fast_pt - slow_pt) >= max_length:
                    max_length = fast_pt - slow_pt
                    longest_begin = slow_pt
                    longest_end = 2 * fast_pt - slow_pt - 1

        if longest_begin is None:
            try:
                return s[0]
            except IndexError:
                return s
        else:
            return s[longest_begin:longest_end]

    # beats 94.43%
    def longestPalindrome3(self, s):
        # Manacher algorithm
        #http://en.wikipedia.org/wiki/Longest_palindromic_substring
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        # we will choose the each element of center
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i])
            # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen)//2: (centerIndex + maxLen)//2]





'''
Test Part
'''

str1 = 'aabbaa'

str2 = 'cbbd'

str3 = "ac"

str4 = ''

solve = Solution()

if __name__ == '__main__':
    print(solve.longestPalindrome3(str2))
```



- C++

```c++

```



- Java

```java

```



​	