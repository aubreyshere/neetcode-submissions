class DSU:

    def __init__(self, n):
        self.parent = list(range(n))

    def findParent(self, x) -> int:
        if self.parent[x] == x:
            return x
        return self.findParent(self.parent[x])

    def union(self, x, y) -> bool:
        xLeader = self.findParent(x)
        yLeader = self.findParent(y)

        if xLeader != yLeader:
            self.parent[yLeader] = xLeader
            return True
        return False

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = DSU(n)
        if len(edges) != n - 1:
            return False

        for edge in edges:
            if not tree.union(edge[0], edge[1]):
                return False

        return True
