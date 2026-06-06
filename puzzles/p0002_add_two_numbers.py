"""LeetCode #2: Add Two Numbers"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """Add two numbers represented as reversed linked lists."""
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val = carry
        if l1:
            val += l1.val
            l1 = l1.next
        if l2:
            val += l2.val
            l2 = l2.next
        carry, digit = divmod(val, 10)
        current.next = ListNode(digit)
        current = current.next
    
    return dummy.next


def list_to_linked(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linked_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    l1 = list_to_linked([2, 4, 3])
    l2 = list_to_linked([5, 6, 4])
    result = add_two_numbers(l1, l2)
    assert linked_to_list(result) == [7, 0, 8]
    print("All tests passed!")
