# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy: ListNode = ListNode(0, head)
        group_prev = dummy

        while True:
            # Walk k steps to get the kth group
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            group_next = kth.next
            kth.next = None # Detach this group

            group_head = group_prev.next
            new_head, new_tail = self._reverseLinkedList(group_head)

            #  Stitch the group back in
            group_prev.next = new_head
            new_tail.next = group_next
            group_prev = new_tail

        return None

    def _reverseLinkedList(self, head: ListNode) -> (ListNode, ListNode):
        """Returns (head, tail) of the reversed list."""
        prev: ListNode | None = None
        cur: ListNode | None = head

        while cur is not None:
            next_node: ListNode | None = cur.next
            cur.next = prev

            prev = cur
            cur = next_node

        return (prev, head)



        



