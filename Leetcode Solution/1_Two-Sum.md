### 1. Two Sum

**Description**:

​	Given any array of integers, return indices of the two number such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.



**Example:**

```
Given nums = [2, 7, 11, 15], target = 9, 
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
```



**Submission:**

- Python

```python
class Solution:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Rum Time Limit Exceeded
    def twoSum1(self, nums, target):
        for idx in range(len(nums)):
            for j in range(1, len(nums)-idx):
                if nums[j+idx] + nums[idx] == target:
                    return [idx, j+idx]

    def twoSum2(self, nums, target):
        # hash 1, not that efficiently
        hash_nums = {}
        for index, num in enumerate(nums):
            try:
                hash_nums[num].append(index)
            except KeyError:
                hash_nums[num] = [index]

        for index, num in enumerate(nums):
            try:
                candidate = hash_nums[target - num]
                if target == 2*num:
                    if len(candidate) > 1:
                        # there might be at most two identified numbers in the list
                        return candidate
                    else:
                        continue
                else:
                    return [index, candidate[0]]
            except KeyError:
                pass

    def twoSum3(self, nums, target):
        # hash 2, a little bit better than twoSum2()
        hash_nums = {}
        for index, num in enumerate(nums):
            residue = target - num
            try:
                #check whether residue has appeared in the previous list
                hash_nums[residue]
                return [hash_nums[residue], index]
            except KeyError:
                hash_nums[num] = index

    def twoSum4(self, nums, target):
        # not as good as twoSum3
        nums_index = [(v, index) for index, v in enumerate(nums)]
        # store as a list to use their built-in sort() method
        nums_index.sort()

        #begin and end for the sorted list
        begin, end = 0, len(nums) - 1
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]
            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr < target:
                begin += 1
            else:
                end -= 1

    def twoSum5(self, nums, target):
        # This is the fastest, runtime beats 69.73%, Time Complexity O(N)
        # But not applicable if there is one more solution
        hash_nums = {}
        for idx, num in enumerate(nums):
            if target - num in hash_nums:
                return [hash_nums[target - num], idx]
            hash_nums[num] = idx

    def twoSum6(self, nums, target):
        # Basically use the built-in method .index() of list
        # Super Super SLOW!!!
        for i in nums:
            j = target - i
            tmp_nums = nums[nums.index(i) + 1:]
            if j in tmp_nums:
                return [nums.index(i), nums.index(i) + 1 + tmp_nums.index(j)]


'''Test Code'''
nums = [3, 2, 4]
target = 6

solve = Solution()
print(solve.twoSum6(nums, target))
```



- C++

```c++
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target){
        unordered_map<int, int> lookup;
        for (int i = 0; i < nums.size(); ++i) {
            if (lookup.count(target - nums[i])) {
                return {lookup[target - nums[i]], i};
            }
            lookup[nums[i]] = i;
        }
        return {};
    }
};

int main(){
    return 0;
}
```



- Java

```java
public class Solution {
    // example in leetcode book
    public int[] twoSum1(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int x = nums[i];
            if (map.containsKey(target - x)) {
                return new int[]{map.get(target - x), i};
            }
            map.put(x, i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}

public static int[] twoSum2(int[] nums, int target) {
    if (nums.length < 2) {
        throw new IllegalArgumentException();
    }
    Map<Integer,Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int diff = target - nums[i];
        if (map.containsKey(diff)) {
            return new int[] {map.get(diff),i};
        }
        map.put(nums[i],i);
    }
    return new int[] {0,0};
}

```



​	