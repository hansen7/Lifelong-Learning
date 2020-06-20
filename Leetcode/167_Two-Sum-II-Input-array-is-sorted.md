### 167. Two Sum II - Input array is sorted

**Description**:

​	Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

​	The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

**Note:**

- Your returned answers (both index1 and index2) are not zero-based.
- You may assume that each input would have exactly one solution and you may not use the same element twice.
  Example:



**Example:**

```reStructuredText
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```





*Since Solution for Q1 are also applicable for this Prob, so they won't be listed here.*

**Submission:**

- Python

```python

class Solution:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    # From twoSum1() to twoSum6(), since they are applicable for Q1, they also work for this
    # Rum Time Limit Exceeded
    def binarySearch_iterative(self, alist, item):
        found = False
        first, last = 0, len(alist) - 1
        if len(alist) == 0:
            raise ValueError('The List has no element')
        else:
            while first <= last and not found:
                midpoint = (first + last) // 2
                if alist[midpoint] == item:
                    found = True
                elif item < alist[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1

        if found:
            return midpoint
        else:
            return None

    def binarySearch_recursive(self, arr, elem, start=0, end=None):
        if end is None:
            end = len(arr) - 1
        if start > end:
            return None

        mid = (start + end) // 2
        if elem == arr[mid]:
            return mid
        if elem < arr[mid]:
            return self.binarySearch_recursive(arr, elem, start, mid - 1)
        # elem > arr[mid]
        return self.binarySearch_recursive(arr, elem, mid + 1, end)



    #slow_p遍历数组每个元素，fast_p进行对slow_p之后的数组进行二分搜索
    def twoSum1(self, nums, target):
        # runtime 996ms, beat 1.25%!!!
        for slow_p in range(len(nums)):
            residue = target - nums[slow_p]
            fast_p = self.binarySearch_iterative(nums[slow_p+1:], residue)
            if fast_p is not None:
                return [slow_p + 1, fast_p + slow_p + 2]


    def twoSum2(self, nums, target):
        # runtime 1008ms, more slower!!!
        for slow_p in range(len(nums)):
            residue = target - nums[slow_p]
            fast_p = self. binarySearch_recursive(nums[slow_p+1:], residue)
            if fast_p is not None:
                return [slow_p + 1, fast_p + slow_p + 2]

    ## Two Pointers
    def twoSum3(self, nums, target):
        # 48ms, beats 45.37%
        head, tail = 0, len(nums) - 1
        while nums[head] + nums[tail] != target:
            if nums[head] + nums[tail] < target:
                head += 1
            else:
                tail -= 1
        return [head+1, tail+1]

    def twoSum4(self, nums, target):
        # 36ms, beats 99.90% !!!!!!!!!
        # 相比与twoSum3(),我觉得主要提升就是因为少做了一次加法运算
        head, tail = 0, len(nums) - 1
        while head < tail:
            sum = nums[head] + nums[tail]
            if  sum == target:
                return [head+1, tail+1]
            elif sum < target:
                head += 1
            else:
                tail -= 1



'''Test Code'''
nums = [221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997]
target = 542


solve = Solution()
print(solve.twoSum2(nums, target))
```



- C++

```c++
#include <iostream>
#include <vector>
using namespace std;



class Solution {
public:

// O(nlgn)
    vector<int> twoSum1(vector<int>& numbers, int target) {
        for (int i = 0; i < numbers.size(); ++i) {
            int t = target - numbers[i], left = i + 1, right = numbers.size();
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (numbers[mid] == t) return {i + 1, mid + 1};
                else if (numbers[mid] < t) left = mid + 1;
                else right = mid;
            }
        }
        return {};
    }


// O(n), Runtime 4ms, beats 98.86% !!!
    vector<int> twoSum2(vector<int>& numbers, int target) {
        int l = 0, r = numbers.size() - 1;
        while (l < r) {
            int sum = numbers[l] + numbers[r];
            if (sum == target) return {l + 1, r + 1};
            else if (sum < target) ++l;
            else --r;
        }
        return {};
    }
};


int main(){
    return 0;
}
```



- Java (Save for later)

```java
// Slow-pointer for iteration loop, Fast-pointer using binary search for the residue in the following list.

//    Slow Fast 
//      |   |
//      2,  7,  11,	15,	19,	21
//			|-Binary Search-|

public class Solution {
    public int[] twoSum1(int[] numbers, int target) {
        int[] res = new int[] {-1,-1};
        if (numbers.length < 2) { return res; }
        int slow = 0;
        while (slow < numbers.length-1 && numbers[slow] <= target) {
            int remain = target - numbers[slow];
            int lo = slow+1, hi = numbers.length-1;
            while (lo <= hi) {
                int mid = lo + (hi - lo) / 2;
                int median = numbers[mid];
                if (median < remain) {
                    lo = mid+1;
                } else if (median > remain) {
                    hi = mid-1;
                } else { // median == remain
                    res[0] = slow+1; res[1] = mid+1;
                    return res; // find target
                }
            }
            slow++;
        }
        return res; // do not find target
    }
//runtime 1ms, beats 71.37%    
public int[] twoSum2(int[] numbers, int target) {
        int[] res = new int[] {-1,-1};
        if (numbers.length < 2) { return res; }
        int lo = 0, hi = numbers.length-1;
        while (lo < hi) {
            int sum = numbers[lo] + numbers[hi];
            if (sum < target) {
                lo++;
            } else if (sum > target) {
                hi--;
            } else { // sum == target [FIND!!!]
                res[0] = lo+1; res[1] = hi+1;
                break;
            }
        }
        return res;
    }
}
```



​	