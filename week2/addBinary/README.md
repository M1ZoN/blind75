# 67. Add Binary

Date Created: July 6, 2022 5:53 PM
Difficulty: Easy
Due Date: July 11, 2022
Status: Next Up
Week #: Week 2

# Description

Given two binary strings `a` and `b`, return *their sum as a binary string*.

**Example 1:**

```
Input: a = "11", b = "1"
Output: "100"

```

**Example 2:**

```
Input: a = "1010", b = "1011"
Output: "10101"

```

# Solution

**Converting to int and back**

```python
# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)

        return "{0:b}".format(x + y)
```

