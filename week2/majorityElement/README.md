# 169. Majority Element

Date Created: July 6, 2022 5:53 PM
Difficulty: Easy
Due Date: July 13, 2022
Status: Next Up
Week #: Week 2

# Description

Given an array `nums` of size `n`, return *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1:**

```
Input: nums = [3,2,3]
Output: 3

```

**Example 2:**

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

# Solution

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}

        for i in nums:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1

        m = 1
        res = nums[0]

        for i in hm:
            if hm[i] > m:
                m = hm[i]
                res = i

        return res
```