class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memory = {}
        lastInd = len(nums) - 1

        def dfs(i) -> bool:
            if i in memory:
                return memory[i]
            elif i == lastInd:
                return True
            
            answer = False
            for ind in range(nums[i]):
                answer = answer or dfs(i + ind + 1)

            memory[i] = answer
            return answer            

        return dfs(0)