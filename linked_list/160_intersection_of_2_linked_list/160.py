# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 本思路类似找到链表中的环，方式是通过变换遍历的链表达到使两个指针遍历相同长度的目的
    # 利用这个方法可以补齐不同长度链表的差值并且保证第二次遇到交叉点的时候位于同一位置
    # 画图好理解
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        a, b = headA, headB
        while a != b:
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a
            
        
    # iterate through 2 linked list respectively, maintain a hashset to record nodes in the first list,
    # while iterating through the second list, check against the set and find the intersection
#    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#        m = set()
#        if not headA or not headB:
#            return None
#        
#        while headA:
#            m.add(headA)
#            headA = headA.next
#        
#        while headB:
#            if headB in m:
#                return headB
#            headB = headB.next
#            
#        return None