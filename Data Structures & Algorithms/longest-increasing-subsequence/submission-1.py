class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tracker = {}
        maxLen = 0
        length = len(nums)

        def dfs(i: int) -> int:
            if i in tracker:
                return tracker[i]
            
            ind = i + 1
            tracker[i] = 1
            while ind < length:
                if nums[ind] > nums[i]:
                    tracker[i] = max(tracker[i], dfs(ind) + 1)

                ind += 1

            return tracker[i]
            

        for i in range(len(nums)):
            if i not in tracker:
                maxLen = max(dfs(i), maxLen)

        return maxLen
        