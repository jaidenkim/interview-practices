# https://leetcode.com/problems/design-linked-list/?envType=problem-list-v2&envId=linked-list
from typing import Optional, Any


class Node:
    def __init__(self, val: Optional[Any] = None, next: Optional[Any] = None):
        self.val = val
        self.next = next


class MyLinkedList:
    """
    Input
    ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
    [[], [1], [3], [1, 2], [1], [1], [1]]
    Output
    [null, null, null, null, 2, null, 3]

    Explanation
    MyLinkedList myLinkedList = new MyLinkedList();
    myLinkedList.addAtHead(1);
    myLinkedList.addAtTail(3);
    myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
    myLinkedList.get(1);              // return 2
    myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
    myLinkedList.get(1);              // return 3
    """

    def __init__(self):
        """Assume all nodes in the linked list are 0-indexed."""
        self.nodes = []

    def get(self, index: int) -> int:
        if index < len(self.nodes):
            return self.nodes[index].val
        return -1

    def addAtHead(self, val: int) -> None:
        # After the insertion, the new node will be the first node of the linked list.
        self.nodes.insert(0, Node(val=val))
        if len(self.nodes) > 1:
            # connect to next node
            self.nodes[0].next = self.nodes[1]

    def addAtTail(self, val: int) -> None:
        self.nodes.append(Node(val=val))
        if len(self.nodes) > 1:
            # connect to prev node
            self.nodes[-2].next = self.nodes[-1]

    def addAtIndex(self, index: int, val: int) -> None:
        if index > len(self.nodes):
            return
        if index == 0:  # append at the start
            self.addAtHead(val)
        elif index == len(self.nodes) or index == -1:  # append at the end
            self.addAtTail(val)
        else:  # always has prev or next node
            self.nodes.insert(index, Node(val=val))
            # connect to both direction
            self.nodes[index - 1].next = self.nodes[index]
            self.nodes[index].next = self.nodes[index + 1]

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.nodes):
            self.nodes.pop(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
