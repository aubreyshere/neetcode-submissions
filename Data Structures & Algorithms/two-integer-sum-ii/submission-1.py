class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = len(numbers) - 1

        while (True):
            if numbers[pointer2] + numbers[pointer1] > target:
                pointer2 -= 1
                continue
            if numbers[pointer2] + numbers[pointer1] < target:
                pointer1 += 1
                continue
            if numbers[pointer2] + numbers[pointer1] == target:
                return [pointer1 + 1, pointer2 + 1]
