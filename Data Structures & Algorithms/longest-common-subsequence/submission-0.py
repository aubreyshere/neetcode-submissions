class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memory = {}
        length1 = len(text1)
        length2 = len(text2)

        # Explore and log longest subsequences.
        def dfs(i: int, j: int) -> int:
            if (i, j) in memory:
                return memory[(i,j)]
            elif i == length1 or j == length2:
                return 0

            curMax = 0
            temp = i
            while temp < length1:
                if text1[temp] == text2[j]:
                    curMax = max(curMax, dfs(temp+1, j+1) + 1)
                    break
                temp += 1
            curMax = max(curMax, dfs(i, j+1))
            memory[(i, j)] = curMax
            return curMax 

        return dfs(0, 0)