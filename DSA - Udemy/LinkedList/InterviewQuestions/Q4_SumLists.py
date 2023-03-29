# Question 4 - Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit.
#              The digits are stored in reverse order, such that the 1's digit is at the head of the list.
#              Write a function that adds the two numbers and return the sum as a linked list

from LinkedList import LinkedList


def sumLists(l1, l2):
    n1 = l1.head
    n2 = l2.head
    carry = 0
    ll = LinkedList()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next

        ll.add(int(result % 10))
        carry = result // 10
    if carry > 0:
        ll.add(carry)
    return ll


list1 = LinkedList().generate(3, 1, 9)
list2 = LinkedList().generate(3, 1, 9)
print(list1)
print(list2)
print(sumLists(list1, list2))
