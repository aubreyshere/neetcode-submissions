class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[right] < nums[mid] and nums[right] >= target:
                left = mid + 1
            elif target < nums[mid] or (nums[left] > nums[mid] and nums[left] <= target):
                right = mid - 1
            else:
                left = mid + 1
                

        return -1
