class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for index, num in enumerate(nums):
            values[num] = index
        
        for index, num in enumerate(nums):
            diff = target - num
            if diff in values and values[diff] != index:
                return [index, values[diff]]
        return []
        