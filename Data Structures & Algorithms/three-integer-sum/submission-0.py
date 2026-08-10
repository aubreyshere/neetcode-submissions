class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()
        result = []

        for i in range(len(nums)):
            pointer1 = i + 1
            pointer2 = len(nums) - 1

            while True:

                if pointer1 >= pointer2:
                    break
                
                if nums[i] + nums[pointer1] + nums[pointer2] > 0:
                    pointer2 -= 1
                
                elif nums[i] + nums[pointer1] + nums[pointer2] < 0:
                    pointer1 += 1

                elif nums[i] + nums[pointer1] + nums[pointer2] == 0:
                    answer.add((nums[i], nums[pointer1], nums[pointer2]))
                    pointer1 += 1
                    pointer2 -= 1

        for item in answer:
            result.append(list(item))

        return result