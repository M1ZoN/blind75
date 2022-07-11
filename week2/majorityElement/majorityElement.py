class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}

        for i in nums:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1

        m = 1
        res = nums[0]

        for i in hm:
            if hm[i] > m:
                m = hm[i]
                res = i

        return res