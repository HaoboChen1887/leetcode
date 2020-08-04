from collections import deque
class Solution:
    # build a graph from the tree
    # during each iteration, remove all edges linked to leaf nodes
    # remove leafs nodes until there are less than or equal to two nodes in the graph
    # the remaining two nodes are the answer
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        res = []
        adj = [set() for _ in range(n)]
        q = deque()
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        
        for i in range(n):
            if len(adj[i]) == 1:
                q.append(i)
        while n > 2:
            size = len(q)
            n -= size
            for i in range(size):
                t = q.popleft()
                for a in adj[t]:
                    adj[a].remove(t)
                    if len(adj[a]) == 1:
                        q.append(a)
        while q:
            res.append(q.popleft())
        return res