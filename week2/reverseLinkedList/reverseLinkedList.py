# https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        my_ptr = head
        prev = None

        while my_ptr:
            temp_next = my_ptr.next
            my_ptr.next = prev
            prev = my_ptr
            my_ptr = temp_next
            
        return prev