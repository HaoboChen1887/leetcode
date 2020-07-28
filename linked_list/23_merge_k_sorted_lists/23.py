# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # use a min heap to maintain the order, add one item at a time
    # NOTE: python heapq maintains a minheap. if we want to specify a priority, form tuples with the priority as the first key
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        if not lists:
            return None
        lists = [(head.val, idx, head) if head else None for idx, head in enumerate(lists)]
        hp = []
        for head in lists:
            if head:
                hp.append(head)
        heapq.heapify(hp)
        dummy = ListNode(-1, None)
        cur = dummy
        while hp:
            _, idx, cur.next = heapq.heappop(hp)
            cur = cur.next
            if cur.next:
                heapq.heappush(hp, (cur.next.val, idx, cur.next))
        return dummy.next
        
            
    # divide the list of lists into halves until indivisible
    # merge two list at a time until all lists are merged
#    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#        if not lists:
#            return None
#        if len(lists) < 2:
#            return lists[0]
#        mid = len(lists) // 2
#        left = self.mergeKLists(lists[:mid])
#        right = self.mergeKLists(lists[mid:])
#        
#        dummy = ListNode(-1, None)
#        cur = dummy
#        while left and right:
#            if left.val <= right.val:
#                cur.next = left
#                left = left.next
#            else:
#                cur.next = right
#                right = right.next
#            cur = cur.next
#        if left:
#            cur.next = left
#        if right:
#            cur.next = right
#            
#        return dummy.next