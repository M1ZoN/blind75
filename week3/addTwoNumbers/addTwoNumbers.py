# https://leetcode.com/problems/add-two-numbers/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ov = 0

        ptr = l1
        ptr2 = l2
        
        newList = ListNode()
        ptr3 = newList

        while ptr and ptr2:
            val = (ov + ptr.val + ptr2.val) % 10
            ov = (ov + ptr.val + ptr2.val) // 10
            tempPtr = ListNode(val)
            ptr3.next = tempPtr
            ptr3 = ptr3.next
            ptr = ptr.next
            ptr2 = ptr2.next

        while ptr:
            val = (ov + ptr.val) % 10
            ov = (ptr.val + ov) // 10
            tempPtr = ListNode(val)
            ptr3.next = tempPtr
            ptr3 = ptr3.next
            ptr = ptr.next

        while ptr2:
            val = (ov + ptr2.val) % 10
            ov = (ptr2.val + ov) // 10
            tempPtr = ListNode(val)
            ptr3.next = tempPtr
            ptr3 = ptr3.next
            ptr2 = ptr2.next
            
        if ov:
            Ov_node = ListNode(ov)
            ptr3.next = Ov_node
            
        return newList.next
            


a = Solution()
l3 = ListNode(3)
l4 = ListNode(4, l3)
l2 = ListNode(2, l4)

ll4 = ListNode(4)
l6 = ListNode(6, ll4)
l5 = ListNode(5, l6)

a.addTwoNumbers(l2, l5)