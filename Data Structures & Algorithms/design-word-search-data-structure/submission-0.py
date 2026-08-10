class WordDictionary:

    def __init__(self):
        self.end = False
        self.children = {}

    def addWord(self, word: str) -> None:
        current = self

        for l in word:
            if l not in current.children:
                current.children[l] = WordDictionary()

            current = current.children[l]

        current.end = True
        

    def search(self, word: str) -> bool:
        current = self

        for i in range(len(word)):
            if word[i] in current.children:
                current = current.children[word[i]]
            elif word[i] == '.':
                answer = False
                for val in current.children:
                    answer = answer or current.search(val + word[i + 1:])
                return answer
            else:
                return False
        
        return current.end
        
