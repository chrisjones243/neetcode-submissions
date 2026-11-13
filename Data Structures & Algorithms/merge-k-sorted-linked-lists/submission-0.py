# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node: ListNode) -> None:
        self.node: ListNode = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        res = ListNode()
        cur = res
        min_heap: List[ListNode] = []

        for lst in lists:
            if lst is not None:
                heapq.heappush(min_heap, NodeWrapper(lst))

        while len(min_heap) > 0:
            node_wrapper = heapq.heappop(min_heap)
            cur.next = node_wrapper.node
            cur = cur.next

            if node_wrapper.node.next:
                heapq.heappush(min_heap, NodeWrapper(node_wrapper.node.next))

        return res.next
        
