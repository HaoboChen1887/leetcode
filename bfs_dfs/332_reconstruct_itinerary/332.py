from collections import defaultdict
import heapq
class Solution:
    # this is a dfs problem 
    # we use a dict to build connections between airports 
    # we maintain the alphabnatical order when there are 
    # multiple routes from the same airpot by using a minheap 
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        m = defaultdict(list)
        for ticket in tickets:
            heapq.heappush(m[ticket[0]], ticket[1])
        dfs(m, "JFK", res)
        return reversed(res)
    
def dfs(m, depart, res):
    while m[depart]:
        arrival = m[depart][0]
        heapq.heappop(m[depart])
        dfs(m, arrival, res)
    res.append(depart)
        
        