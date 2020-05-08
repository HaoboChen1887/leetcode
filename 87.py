class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(len(s1)):
            print(i)
            print(s1[:i], s2[:i])
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])):
                return True
            if (self.isScramble(s1[:i], s2[:len(s2) - i]) and self.isScramble(s1[i:], s2[len(s2) - i:])):
                return True
        return False

def stringToString(input):
    import json

    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s1 = stringToString(line);
            line = next(lines)
            s2 = stringToString(line);
            
            ret = Solution().isScramble(s1, s2)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()