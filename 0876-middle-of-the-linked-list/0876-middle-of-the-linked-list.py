# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        end = middle = head
        while end and end.next:
            middle,end = middle.next,end.next.next
        return middle
    def middle(head):
        end=middle=head
        while end and end.next:
            middle=middle.next
            end=end.next.next
            