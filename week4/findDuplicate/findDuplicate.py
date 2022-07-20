class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = res = 0
        found = False
        
        while not found:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                found = True
        
        while slow != res:
            res = nums[res]
            slow = nums[slow]
        
        return res