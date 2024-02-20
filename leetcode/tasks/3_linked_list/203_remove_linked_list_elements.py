from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_elements_custom(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    while head and head.val == val:
        head = head.next
    current = head
    prev = ListNode(next=current)
    while current:
        if current.val == val:
            prev.next = current.next
        else:
            prev = prev.next
        current = current.next

    return head


def remove_elements_solution(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    result = ListNode(next=head)
    current = head
    prev = result
    while current:
        if current.val == val:
            prev.next = current.next
        else:
            prev = prev.next
        current = current.next

    return result.next




if __name__ == '__main__':
    n0 = ListNode(6)
    n1 = ListNode(2)
    n2 = ListNode(2, n1)
    n3 = ListNode(3, n2)
    n4 = ListNode(2, n3)
    n5 = ListNode(2, n4)
    head = n5
    print(remove_elements_solution(head, 2).val)

