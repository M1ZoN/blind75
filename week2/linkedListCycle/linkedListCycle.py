# https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        myHash = {}

        pointer = head

        while pointer:
            if pointer in myHash:
                return True
            else:
                myHash[pointer] = 1
            pointer = pointer.next
        return False

root = ListNode(3)
node2 = ListNode(2)
node0 = ListNode(0)
node4 = ListNode(4)

root.next = node2
node2.next = node0
node0.next = node4
node4.next = node2

print(Solution().hasCycle(root))