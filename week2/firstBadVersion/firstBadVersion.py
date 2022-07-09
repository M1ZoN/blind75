# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

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