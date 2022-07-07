# Two Sum

Date Created: July 1, 2022 5:08 PM
Difficulty: Easy
Due Date: July 1, 2022
Status: Completed
Week #: Week 1

# Description

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

# Solution

```python
def twoSum(nums, target):
    seen = {}
    
    for idx, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], idx]
        seen[num] = idx
```