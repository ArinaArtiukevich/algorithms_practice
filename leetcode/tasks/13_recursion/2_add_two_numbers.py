from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class IterativeSolution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_result = l3 = ListNode()
        add_num = 0
        while l1 or l2:
            n1, n2 = 0, 0
            if l1:
                n1 = l1.val
                l1 = l1.next
            if l2:
                n2 = l2.val
                l2 = l2.next
            sum_nums = n1 + n2
            if add_num > 0:
                sum_nums += add_num
                add_num = 0
            if sum_nums >= 10:
                add_num = 1
                sum_nums %= 10
            l_result.next = ListNode(sum_nums, None)
            l_result = l_result.next

        if add_num:
            l_result.next = ListNode(add_num, None)

        return l3.next


class RecursiveSolution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0, None)
        result = []
        def helper(l1: Optional[ListNode], l2: Optional[ListNode], l3: Optional[ListNode]):
            if not l1 and not l2 and not l3:
                return
            elif not l1 and not l2:
                if l3.val > 9:
                    l3.val = l3.val % 10
                    l3.next = ListNode(1)
                return
            sum_num = 0
            if l1:
                sum_num += l1.val
                l1 = l1.next
            if l2:
                sum_num += l2.val
                l2 = l2.next
            add_num = 0
            if l3.val > 9:
                add_num = 1
                l3.val = l3.val % 10
            l3.next = ListNode(sum_num + add_num)
            helper(l1, l2, l3.next)

        helper(l1, l2, l3)
        while l3:
            print(l3.val)
            l3 = l3.next
        return l3.next


if __name__ == '__main__':
    # l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, None)))))))
    # l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, None))))

    l1 = ListNode(2, ListNode(4, ListNode(9, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, None)))
    print(RecursiveSolution().addTwoNumbers(l1, l2))
