# 141. Linked List Cycle

Date Created: July 6, 2022 5:35 PM
Difficulty: Easy
Due Date: July 9, 2022
Status: Next Up
Week #: Week 2

# Description

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true` *if there is a cycle in the linked list*. Otherwise, return `false`.

**Example 1:**

![Untitled](141%20Linked%20List%20Cycle%201d1401cd20584fcd891df95cd0543619/Untitled.png)

```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

```

# Solution

```python
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
```