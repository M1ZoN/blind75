# https://leetcode.com/problems/binary-search/

def search(nums, target):
    mmax = len(nums) - 1
    mmin = 0

    while mmin <= mmax:
        mid = (mmax + mmin) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            mmax = mid - 1
        else:
            mmin = mid + 1
    return -1

print(search([-1,0,5], 5))