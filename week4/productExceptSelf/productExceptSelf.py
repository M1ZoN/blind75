class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftArr = [1 for _ in nums]
        rightArr = [1 for _ in nums]
        answer = [1 for _ in nums]
        
        for i in range(len(nums)):
            if i == 0:
                leftArr[i] = nums[0]
            else:
                leftArr[i] = leftArr[i - 1] * nums[i]
                
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                rightArr[i] = nums[i]
            else:
                rightArr[i] = nums[i] * rightArr[i + 1]
        
        for i in range(len(nums)):
            if i == 0 and i + 1 < len(nums):
                answer[i] = rightArr[i + 1]
            elif i == len(nums) - 1 and i - 1 >= 0:
                answer[i] = leftArr[i - 1]
            else:
                answer[i] = leftArr[i - 1] * rightArr[i + 1]
        return answer