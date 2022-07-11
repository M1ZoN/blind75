# 70. Climbing Stairs

Date Created: July 6, 2022 5:49 PM
Difficulty: Easy
Due Date: July 11, 2022
Status: Next Up
Week #: Week 2

# Description

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

**Example 1:**

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

```

**Example 2:**

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

# Solution

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        step1 = 1
        step2 = 1

        for i in range(n):
            temp = step1 + step2
            step1 = step2
            step2 = temp
        return step1



Solution().climbStairs(6)
```