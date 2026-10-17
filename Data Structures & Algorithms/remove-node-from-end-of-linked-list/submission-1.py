# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        nodes = [dummy]
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next 
        target = len(nodes)-n

        nodes[target - 1].next = nodes[target].next
        return dummy.next



