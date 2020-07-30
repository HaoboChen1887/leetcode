class Solution:
    # use a monotonous increasing stack to track the status
    # we append a 0 to the end of the original list for calculating the last entry
    # if the stack is empty or heights[st[-1]] < new height, push the new height on the stack
    #   to maintain the increasing trend
    # otherwise, if we encounter a new height that is lower than heights[st[-1]],
    # it triggers calculations for previous heights
    # the calculation loop until the new height is greater than heights[st[-1]]
    #   when calculating, we first pop the stack top and calculate the largest area its height can cover
    #   Note: the largest possible width is maintained by the second to the top item on the stack
    #       and because the stack is monotonous increasing, we decrease the height every time we pop
    #       but since height poped before the current height can cover its height, the width doesn't change
    #       that's also why we use the second to the top item to maintain the width
    #       if the stack is empty then the width is simply i because array starts from 0
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        st = []
        res = 0
        for i in range(len(heights)):
            while st and heights[st[-1]] >= heights[i]:
                cur = st.pop()
                res = max(res, (i if not st else (i - st[-1] - 1)) * heights[cur])
            st.append(i)
        return res