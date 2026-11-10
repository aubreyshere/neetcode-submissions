class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        prev = 0
        cur = 1

        while cur < len(nums):
            if nums[prev] == nums[cur]:
                return nums[prev]
            prev += 1
            cur += 1