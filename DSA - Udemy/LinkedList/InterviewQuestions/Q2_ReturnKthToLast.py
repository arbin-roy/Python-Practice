# Implement an algorithm to find nth node from last of a singly linked list
# Note: LinkedList is size is not known

from LinkedList import LinkedList


def nthToLast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    for i in range(n):
        if pointer2 is None:
            return
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(nthToLast(customLL, 4))
