class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        from collections import deque
        res = []
        s = set(wordList)
        p = [beginWord]
        paths = deque([p])
        level, min_level = 1, sys.maxsize
        words = set()
        # use a queue to keep track of all possible paths
        # words stores all words visted by so far
        # if len(t) > level(i.e. length of a path is longer than levels that are visited)
        #   there are two cases:
        #       1. this path t is not the optimal path
        #       2. we are visiting a new level
        #           in either case we delete all visited words from dictionary
        #           and clear the words set. 
        #   if level > min_level: it means this path t is not the optimal path and we discard it
        #   NOTE: min_level is updated only when we find an optimal solution by the property of bfs
        #       so we won't discard anything before we find at least one optimal path
        # otherwise we take the last word from the path and 
        # check if there are valid transformations in the dictionary
        # if the word we found happens to be the endword, we add it to res and update minLevel
        #   because bfs always find the optimal solution first
        # otherwise if we found a valid word, we generate a new path and enqueue it
        while paths:
            t = paths.popleft()
            if len(t) > level:
                for w in words:
                    s.remove(w)
                words.clear()
                level = len(t)
                if level > min_level:
                    break
            last = t[-1]
            for i in range(len(last)):
                newLast = last
                for c in string.ascii_lowercase:
                    newLast = last[:i] + c + last[i + 1:]
                    if newLast not in s:
                        continue
                    words.add(newLast)
                    nextPath = t + [newLast]
                    if newLast == endWord:
                        res.append(nextPath)
                        minLevel = level
                    else:
                        paths.append(nextPath)
        return res
                   