# https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums):
    
    maxSum = nums[0]
    curSum = 0

    for i in nums:
        if curSum < 0:
            curSum = 0
        curSum += i
        maxSum = max(maxSum, curSum)
    return maxSum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))