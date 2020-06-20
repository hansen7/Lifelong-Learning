### 3. Longest Substring Without Repeating Characters

**Description**:

​	Given a string, find the length of the longest substring without repeating characters.



**Example 1**:

```markdown
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
```

**Example 2:**

```markdown
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**

```markdown
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence or a substring
```



**Submission:**

- Python

```python
class Solution:
    # runtime beats 5.31%, O(n)
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mostlength = 1

        if len(s) < 2:
            return len(s)

        for idx in range(len(s)-1):
            count_ = 1
            set_ = set(s[idx])
            for jdx in range(1, len(s[idx:])):
                #if len(s[idx:]) <= mostlength:
                #   break
                if s[idx + jdx] not in set_:
                    count_ += 1
                    set_.add(s[idx + jdx])
                    mostlength = count_ if count_ > mostlength else mostlength
                else:
                    #mostlength = count_ if count_ > mostlength else mostlength
                    break

        return mostlength


    # beats 89.84%
    def lengthOfLongestSubstring1(self, s):
        longest, start, visited = 0, 0, [False] * 256
        for i, char in enumerate(s):

            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1

            else:
                visited[ord(char)] = True

            longest = max(longest, i - start + 1)
        return longest

    # This solution is around to beat 50%
    def lengthOfLongestSubstring2(self, s):
        # Time Complexity -> O(n)
        # char_dict is save as {'s[idx]': idx, ...}
        # start -> the beginning of the substring
        max_length, start, char_dict = 0, 0, {}
        # The enumerate index starts from (1, s[0]), (2, s[1])...
        # so there are two pointers, idx and start
        for idx, char in enumerate(s, 1):
            # dict.get() -> if exist, return the value, else return -1
            # so if s[idx-1] is not in the dict, so the start won't be updated
            # othewise the start will be updated
            if char_dict.get(char, -1) >= start:
                start = char_dict[char]
            # add/update the idx for the char in the dict
            char_dict[char] = idx
            max_length = max(max_length, idx - start)
        return max_length


'''
Test Code
'''

str1 = 'ABAAACB'
solution = Solution()
print(solution.lengthOfLongestSubstring2(str1))
```



- C++

```c++

```



- Java

```java

```



​	