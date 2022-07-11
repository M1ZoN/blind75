# 206. Reverse Linked List

Date Created: July 6, 2022 5:49 PM
Difficulty: Easy
Due Date: July 13, 2022
Status: Next Up
Week #: Week 2

# Description

Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

**Example 1:**

![Untitled](206%20Reverse%20Linked%20List%20f881e290f3ed4ec582d8069372a19fcb/Untitled.png)

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

```

**Example 2:**

![Untitled](206%20Reverse%20Linked%20List%20f881e290f3ed4ec582d8069372a19fcb/Untitled%201.png)

```
Input: head = [1,2]
Output: [2,1]

```

**Example 3:**

```
Input: head = []
Output: []
```

# Solution

**Using Queue:**

```python
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
```

**Using inplace changing pointers**

```python
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
```