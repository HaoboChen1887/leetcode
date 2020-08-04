import heapq
class Solution:
    # first use a list to break input into left and right edges
    # left edges' height are stored as negative numbers
    # sort the points by their x-pos to ensure a inorder scan
    # push 0 to the hp to make sure all right edges can be added to res
    # we use heapq to build a max heap of heights, so we need to store heights as negative values
    # we scan through all points in h
    # when we encounter a point whose height is negative, we know it's left edge
    # we add it's height to max heap
    # now we peek the heap top, since max heap maintains in a way such that the top item is max
    # we know that if in this iteration heap top changes, then the current pos has a new max height
    # so we add it to res
    # if we encounter a right edge
    # we remove the height from heap so that heap top becomes the next max height
    # now if cur changes, it means we find a turning point and we add it to res
    #   if not, then there is a building higher than the right edge we are looking at.
    # if we encounter the last right edge of a continues area
    #   we remove the last height from heap so that 0 is the only item on the heap
    #   we add the bottom right point of a continuous skyline to res
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        h, res = [], []
        hp = [0]
        heapq.heapify(hp)
        pre, cur = [0] * 2
        for pos in buildings:
            h.append((pos[0], -pos[2]))
            h.append((pos[1], pos[2]))
        h.sort()
        for pos in h:
            if pos[1] < 0:
                heapq.heappush(hp, pos[1])
            else:
                hp.remove(-pos[1])
                heapq.heapify(hp)
            cur = hp[0]
            if cur != pre:
                res.append((pos[0], -cur))
                pre = cur
        return res
                