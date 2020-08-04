from collections import defaultdict
class Solution:
    # this problem can be modeled as a 'find a path problem'.
    # We need to find a path which matches the query
    # we build a graph with the given equations and their reciprocals, and store values in a dict
    # for each query, we need a set to record which variables we have visited
    # for each unvisited variable, we check if it is in the graph
    # if we reach the denominator, we return the value and multiply it to the result
    m = defaultdict(dict)
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        res = []
        for i, eq in enumerate(equations):
            self.m[eq[0]][eq[1]] = values[i]
            self.m[eq[1]][eq[0]] = 1 / values[i]
        
        for query in queries:
            visited = set()
            t = self.helper(query[0], query[1], visited)
            res.append(t if t > 0.0 else -1)
        return res
    
    def helper(self, nom, denom, visited):
        if denom in self.m[nom]:
            return self.m[nom][denom]
        for a in self.m[nom]:
            if a in visited:
                continue
            visited.add(a)
            t = self.helper(a, denom, visited)
            if t > 0.0:
                return t * self.m[nom][a]
        return -1.0 
        