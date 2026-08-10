class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        search = set(nums)
        longest = 0

        for i in nums:
            if i - 1 not in search:
                length = 1
                while i + length in search:
                    length += 1
                longest = max(length, longest)
        
        return longest
        
                
