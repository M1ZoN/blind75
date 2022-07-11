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

# 1 = 1
# 2 = 1 1, 2
# 3 = 1 1 1, 1 2, 2 1
# 4 = 1 1 1 1, 2 1 1, 1 2 1, 1 1 2