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