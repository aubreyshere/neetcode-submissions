class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        curSum = 0

        for num in nums:
            if num > curSum and curSum < 0:
                curSum = num
            else:
                curSum += num
            maxSum = max(maxSum, curSum)

        return maxSum