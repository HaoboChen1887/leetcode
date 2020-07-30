class Solution:
    # use a monotonous decreasing stack to track possible traps
    # if the stack is empty or new height is less than top height
    #    push the new height onto stack and move to next height
    # otherwise, pop from stack, now the stack should have at least one item or a trap can't be formed
    #   the item poped is the relative bottom for the current iteration
    #   now the stack top is the other edge of the trap
    #   pick the smaller height between two edges and calculate the height of trap
    #   the width of trap is calculated by idx difference
    def trap(self, height: List[int]) -> int:
        i = 0
        st = []
        res = 0
        while i < len(height):
            if not st or height[st[-1]] >= height[i]:
                st.append(i)
                i += 1
            else:
                bottom = st.pop()
                if not st:
                    continue
                res += (min(height[i], height[st[-1]]) - height[bottom]) * (i - 1 - st[-1])
        return res