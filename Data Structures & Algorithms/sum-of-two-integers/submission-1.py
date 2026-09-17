class Solution:
    def getSum(self, a: int, b: int) -> int:
        num = 0
        carry = 0

        for i in range(32):
            bit = (a >> i & 1) ^ (b >> i & 1) ^ carry
            carry = (a >> i & 1)  & ((b >> i & 1) | carry) | (b >> i & 1) & carry
            num = num | (bit << i)
        
        if num & 0x80000000:
            num = ~(num ^ 0xFFFFFFFF)
        
        return num