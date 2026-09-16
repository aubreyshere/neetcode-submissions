class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        rem = 0

        for i in range(len(nums)+1):
            rem = rem ^ i

        for num in nums:
            rem = rem ^ num
        
        return rem
        

        