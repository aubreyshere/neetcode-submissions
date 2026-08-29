class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memory = {0}
        tracker = {}
        length = len(s)

        for word in wordDict:
            tracker[word] = len(word)

        for i in range(length):
            if i in memory:
                for word in tracker:
                    j = tracker[word]
                    if s[i:i+j] == word:
                        memory.add(i+j)

        if length in memory:
            return True
        return False
                    
