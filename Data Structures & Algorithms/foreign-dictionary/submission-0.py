from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # prerequistite for ..
        adj = {}
        # of prereqs left
        inDeg = {}

        for word in words:
            for c in word:
                adj[c] = set()
        
        for c in adj:
            inDeg[c] = 0

        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            len1, len2 = len(word1), len(word2)

            if len1 > len2 and word1[:len2] == word2:
                return ""
            
            for j in range(min(len1,len2)):
                if word1[j] != word2[j]:
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        inDeg[word2[j]] += 1
                    break
        
        q = deque()
        res = []
        for c in inDeg:
            if inDeg[c] == 0:
                q.append(c)

        while q:
            char = q.popleft()
            res.append(char)
            for c in adj[char]:
                inDeg[c] -= 1
                if not inDeg[c]:
                    q.append(c)
        
        if len(res) != len(inDeg):
            return ""
        return "".join(res)
