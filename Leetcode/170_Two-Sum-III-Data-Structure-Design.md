### 170. Two Sum III - Data Structure Design

**Description**:

​	Design and implement a TwoSum class. It should support the following operations:add and find.

**Note:**

- add - Add the number to an internal data structure.
- find - Find if there exists any pair of numbers which sum is equal to the value.

**Example:**

```reStructuredText
add(1); add(3); add(5);
find(4) -> true
find(7) -> falses
```



**Submission:**

- Python

```python
class TwoSum1(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.internal = []
        self.dic = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.internal.append(number)
        if number in self.dic:
            # more than once
            self.dic[number] = True
            return
        # once
        self.dic[number] = False

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for v in self.internal:
            if value - v in self.dic:
                if v << 1 == value and not self.dic[v]:
                    continue
                return True
        return False
```



- C++

```c++
class TwoSum {
public:
    void add(int number) {
        ++m[number];
    }
    bool find(int value) {
        for (auto a : m) {
            int t = value - a.first;
            if ((t != a.first && m.count(t)) || (t == a.first && a.second > 1)) {
                return true;
            }
        }
        return false;
    }
private:
    unordered_map<int, int> m;
};
```



- Java (Save for later)

```java

```



​	