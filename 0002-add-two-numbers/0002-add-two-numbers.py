# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root=ListNode()
        curr=root
        carry=0
        while l1 or l2 or carry:
            if l1:
                v1=l1.val
            else:
                v1=0
            if l2:
                v2=l2.val
            else:
                v2=0
            val=v1+v2+carry
            carry=val//10
            val=val%10
            curr.next=ListNode(val)
            curr=curr.next
            if l1:
                l1=l1.next 
            else:None
            if l2:
                l2=l2.next
            else:None
        return root.next        
        