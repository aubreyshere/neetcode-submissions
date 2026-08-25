class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.simple(nums[1:]), self.simple(nums[:-1]))
        
    def simple(self, nums) -> int:
        one, two, three = 0, 0, 0

        for i in range(len(nums)):
            temp = one
            one = max(two, three) + nums[i]

            three = two
            two = temp

        return max(one, two)