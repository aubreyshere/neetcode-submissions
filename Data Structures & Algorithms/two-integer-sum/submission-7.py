class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            diff = target - num
            if diff in nums and nums.index(diff) != index:
                answer = [index, nums.index(diff)]
                answer.sort()
                return answer
        