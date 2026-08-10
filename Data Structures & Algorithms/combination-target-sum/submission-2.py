class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        answer = []
        
        def sumAllItems(minIndex: int, remainder: int, curNums: []) -> None:

            if remainder == 0:
                answer.append(curNums)
                return
            elif remainder < 0:
                return

            while minIndex < length:
                sumAllItems(minIndex, remainder - nums[minIndex], curNums + [nums[minIndex]])
                minIndex += 1
            return

        sumAllItems(0, target, [])

        return answer

            



        