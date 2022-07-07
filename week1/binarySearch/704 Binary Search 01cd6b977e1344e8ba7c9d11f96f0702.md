# 704. Binary Search

Date Created: July 1, 2022 5:29 PM
Difficulty: Easy
Due Date: July 4, 2022
Status: Completed
Week #: Week 1

# Description

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

```

**Example 2:**

```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```

# Solution

```python
def search(nums, target):
    mmax = len(nums) - 1
    mmin = 0

    while mmin <= mmax:
        mid = (mmax + mmin) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            mmax = mid - 1
        else:
            mmin = mid + 1
    return -1

print(search([-1,0,5], 5))
```