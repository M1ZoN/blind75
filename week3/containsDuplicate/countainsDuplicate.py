# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        
        for i in nums:
            if i not in hm:
                hm[i] = 1
            else:
                return True
            
        return False