class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        maxP = nums[0]

        for num in nums:
            temp = num * curMax
            curMax = max(temp, num * curMin, num)
            curMin = min(temp, num * curMin, num)
            maxP = max(maxP, curMax)

        return maxP
        