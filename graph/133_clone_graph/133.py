from collections import deque
class Solution:
    # bfs
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        m = {}
        newNode = Node(node.val)
        m[node] = newNode
        q = deque([node])
        while q:
            curr = q.popleft()
            for nb in curr.neighbors:
                if nb not in m:
                    m[nb] = Node(nb.val)
                    q.append(nb)
                m[curr].neighbors.append(m[nb])
        return newNode
    
    # dfs, use a map to record which nodes has been cloned
#    def cloneGraph(self, node: 'Node') -> 'Node':
#        self.m = {}
#        return self.clone(node)
#    
#    def clone(self, node):
#        if not node:
#            return None
#        if node.val in self.m:
#            return self.m[node.val]
#        newNode = Node(node.val, [])
#        self.m[newNode.val] = newNode
#        for nb in node.neighbors:
#            newNode.neighbors.append(self.clone(nb))
#        return newNode
        