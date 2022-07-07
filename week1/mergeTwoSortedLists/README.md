# Merge Two Sorted Lists

Date Created: July 1, 2022 5:21 PM
Difficulty: Easy
Due Date: July 2, 2022
Status: Completed
Week #: Week 1

# Description:

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return *the head of the merged linked list*.

Example 1:

![Untitled](Merge%20Two%20Sorted%20Lists%20b898b4c3a64f41fe8058945e3948cbe4/Untitled.png)

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

```

**Example 2:**

```
Input: list1 = [], list2 = []
Output: []

```

**Example 3:**

```
Input: list1 = [], list2 = [0]
Output: [0]
```

# Solution:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    resList = ListNode()
    it = resList

    while list1 and list2:
        if (list1.val < list2.val):
            resList.next = list1
            resList = resList.next
            list1 = list1.next
        else:
            resList.next = list2
            resList = resList.next
            list2 = list2.next
    
    if list1 or list2:
        resList.next = (list1) if list1 else list2
    return it.next

list1 = ListNode(1)
list2 = ListNode(1)

node1 = ListNode(2)
list1.next = node1
node2 = ListNode(4)
node1.next = node2

node3 = ListNode(3)
list2.next = node3
node4 = ListNode(4)
node3.next = node4

myList = mergeTwoLists(list1, list2)

while myList:
    print(myList.val)
    myList = myList.next
```