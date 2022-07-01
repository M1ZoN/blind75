def twoSum(nums, target):
    seen = {}
    
    for idx, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], idx]
        seen[num] = idx

print([2, 7, 11, 15], 9)