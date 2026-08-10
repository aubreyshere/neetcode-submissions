class PrefixTree:

    def __init__(self):
        self.endValid = False
        self.childNodes = {}        

    def insert(self, word: str) -> None:
        currentTree = self

        for l in word:
            if l not in currentTree.childNodes:
                currentTree.childNodes[l] = PrefixTree()

            currentTree = currentTree.childNodes[l]

        currentTree.endValid = True


    def search(self, word: str) -> bool:
        currentTree = self

        for l in word:
            if l in currentTree.childNodes:
                currentTree = currentTree.childNodes[l]
            else:
                return False

        if currentTree.endValid == True:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        currentTree = self

        for l in prefix:
            if l in currentTree.childNodes:
                currentTree = currentTree.childNodes[l]
            else:
                return False

        return True
        
        