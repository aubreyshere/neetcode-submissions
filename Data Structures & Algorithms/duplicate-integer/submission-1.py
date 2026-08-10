class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        modified = set(nums)
        
        if len(nums) == len(modified):
            return False
        else: 
            return True
        
        