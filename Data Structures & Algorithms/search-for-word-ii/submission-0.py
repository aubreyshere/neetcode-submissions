class Trie:

    def __init__(self):
        self.end = False
        self.i = -1
        self.children = {}

    def addWord(self, word: str, index: int) -> None:
        current = self

        for l in word:
            if l not in current.children:
                current.children[l] = Trie()

            current = current.children[l]

        current.i = index
        current.end = True
        
        return current.end

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        search = Trie()
        rows = len(board)
        cols = len(board[0])
        result = set()
        used = set()

        def exploreBoard(r: int, c: int, node) -> None:
            if not (0 <= r < rows and 0 <= c < cols) or (r, c) in used or board[r][c] not in node.children:
                return

            node = node.children[board[r][c]]

            if node.end:
                result.add(words[node.i])

            used.add((r,c))
            exploreBoard(r-1, c, node)
            exploreBoard(r+1, c, node)
            exploreBoard(r, c-1, node)
            exploreBoard(r, c+1, node)
            used.remove((r,c))

            return

        for index, word in enumerate(words):
            search.addWord(word, index)

        for r in range(rows):
            for c in range(cols):
                exploreBoard(r,c, search)

        return list(result)