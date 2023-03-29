# Question 5 - Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
#              Note that the intersection is defined based on reference, not value.
#              That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node
#              of the second linked list, then they are intersecting.

from LinkedList import LinkedList, Node


def intersection(l1, l2):
    if l1.tail is not l2.tail:
        return False
    len1 = len(l1)
    len2 = len(l2)

    shorter = l1 if len1 < len2 else l2
    longer = l2 if len1 < len2 else l1

    diff = len(longer) - len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    return longerNode


# Helper addition method
def addSameNode(l1, l2, v):
    tempNode = Node(v)

    l1.tail.next = tempNode
    l1.tail = tempNode

    l2.tail.next = tempNode
    l2.tail = tempNode


list1 = LinkedList().generate(3, 1, 9)
list2 = LinkedList().generate(4, 1, 9)

# addSameNode(list1, list2, 7)
addSameNode(list1, list2, 11)
addSameNode(list1, list2, 14)

print(list1)
print(list2)
print(intersection(list1, list2))
