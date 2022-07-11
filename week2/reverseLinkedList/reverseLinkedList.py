# https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        my_ptr = head
        my_stack = []

        while (my_ptr):
            my_stack.append(my_ptr.val)
            my_ptr = my_ptr.next

        new_head = ListNode()

        my_ptr = new_head
        while my_stack:
            temp = ListNode(my_stack.pop())
            my_ptr.next = temp
            my_ptr = my_ptr.next

        return new_head.next