# 这个解法是基于出现频率多的字幕始终最先被放置，必须保证出现频率最多的字母满足条件
# 首先用一个map记录每个字母的出现频率
# 由于heapq只能构建min heap我们取频率的负值以构建max heap
# 迭代直到max heap为空，每次拿出堆顶元素（出现频率最多的字母）
# 将他附加到答案中并放入冷却字典中，该字母在满足距离k之前不能再出现
# 满足距离后再将cd中的字母放回堆中，如此往复直到堆为空最后得到满足条件的排列
# 如果该排列长度和原字符串一样说明所有字母都被重排过，条件满足。否则说明有字母未被处理，不存在满足条件的排列。

import heapq
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1: 
            return s
        m = collections.defaultdict(int) 
        for c in s:
            m[c] += 1
        cd = {}
        ans = []
        freqs = [[-m[c],  c] for c in m]
        heapq.heapify(freqs)
        while freqs:
            freq, c = heapq.heappop(freqs)
            ans.append(c)
            freq += 1
            if freq < 0:
                cd[c] = [freq, c]
                print
            if len(ans) >= k and ans[-k] in cd:
                [prev_freq, prev_c] = cd.pop(ans[-k])
                heapq.heappush(freqs, [prev_freq, prev_c])
        return ''.join(ans) if len(ans) == len(s) else ""
