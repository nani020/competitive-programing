# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        l = ListNode(-1)
        l.next = head
        prev=l
        curr =  l.next
        while curr:
            if curr.next and curr.val == curr.next.val:
                value = curr.val
                
                while curr and curr.val == value:
                    curr = curr.next
                    
                prev.next = curr
                
            else:
                prev=curr 
                curr=curr.next
                
        return l.next