# 278. First Bad Version

Date Created: July 6, 2022 5:36 PM
Difficulty: Easy
Due Date: July 10, 2022
Status: Next Up
Week #: Week 2

# Description

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

**Example 1:**

```
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

```

**Example 2:**

```
Input: n = 1, bad = 1
Output: 1
```

# Solution

```python
def isBadVersion(n, b):
    return n >= b

class Solution:
    def firstBadVersion(self, n: int, b) -> int:
        my_min = 1
        my_max = n
        mid = n // 2
        
        while my_min <= my_max:
            if isBadVersion(mid, b):
                my_max = mid - 1
                mid = (my_max + my_min) // 2
            else:
                my_min = mid + 1
                mid = (my_max + my_min) // 2
        return mid + 1
                
Solution().firstBadVersion(2, 2)
```