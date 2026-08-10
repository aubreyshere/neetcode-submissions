class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tracker = {}
        longest = 0
        longestFreq = 0
        left = 0

        for i in range(len(s)):
            tracker[s[i]] = 1 + tracker.get(s[i], 0)
            longestFreq = max(longestFreq, tracker[s[i]])

            while i - left + 1  - longestFreq > k:
                tracker[s[left]] -= 1
                left += 1

            longest = max(longest, i - left + 1)

        return longest

            
            
        