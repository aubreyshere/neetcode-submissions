class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        pointer1 = 0
        pointer2 = 0
        current = set()

        while pointer2 < len(s):
            if s[pointer2] in current:
                # move pointer 1 to last val and pop values
                current.remove(s[pointer1])
                pointer1 +=1
            else:
                current.add(s[pointer2])
                longest = max(longest, len(current))
                pointer2 += 1

        return longest
            


