class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        if length == 0:
            return []
        rArr = []
        lArr = [1]* length
        result = []
        

        for i in range(length):
            if i == 0:
                rArr.append(1)
            else:
                rArr.append(rArr[i-1] * nums[i-1])
                lArr[length - i - 1] = (lArr[length - i] * nums[length-i])

        print(lArr)
        print(rArr)
        for i in range(length):
            result.append(rArr[i] * lArr[i])
        return result