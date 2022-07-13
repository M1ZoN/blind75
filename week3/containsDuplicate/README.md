# 217. Contains Duplicate

Difficulty: Easy

# Description

Given an integer array ```nums```, return ```true``` if any value appears **at least twice** in the array, and return ```false``` if every element is distinct.

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: true
```

**Example 2:**

```
Input: nums = [1,2,3,4]
Output: false
```

**Example 3:**

```
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

# Solution

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        
        for i in nums:
            if i not in hm:
                hm[i] = 1
            else:
                return True
            
        return False


# Or a soluting using set:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_elems = len(nums)
        num_unique_elems = len(set(nums))

        return num_elems > num_unique_elems
