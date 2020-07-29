class Solution:
    # bfs: res counts the depth of bfs
    # because when bfs find the goal, the path is always optimal
    # so we only need to return res + 1
    # this problem is equivalent to bfs because for every letter there are 25 possible replacements
    # which is equivalent to having 25 directions to go on a map
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        s = set(wordList)
        if endWord not in s:
            return 0
        q = deque([beginWord])
        res = 0
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res + 1
                for i in range(len(word)):
                    newWord = word
                    for c in string.ascii_lowercase:
                        newWord = word[:i] + c + word[i + 1:]
                        if newWord in s and newWord != word:
                            q.append(newWord)
                            s.remove(newWord)
            res += 1
        return 0
