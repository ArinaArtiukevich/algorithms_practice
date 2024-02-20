class Node:
    def __init__(self, prev=None, next=None, value=0):
        self.prev = prev
        self.next = next
        self.value = value


class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def get_representation(self) -> str:
        output = ''
        current_node = self.head
        if current_node is None:
            output = "empty"
        else:
            while current_node is not None:
                output += str(current_node.value) + " -> "
                current_node = current_node.next
        return output

    def get_reversed_representation(self) -> str:
        output = ''
        current_node = self.head
        if current_node is None:
            output = "empty"
        else:
            while current_node.next is not None:
                current_node = current_node.next
            while current_node is not None:
                output += str(current_node.value) + " -> "
                current_node = current_node.prev
        return output

    def add_head(self, value):
        new_node = Node(value=value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_tail(self, value):
        new_node = Node(value=value)
        current_node = self.head
        if current_node is None:
            self.head = new_node
        else:
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    def add_at(self, value, position):
        if position == 0:
            self.add_head(value)
            return
        new_node = Node(value=value)
        current_node = self.head
        current_position = 0

        if current_node is None:
            raise IndexError("No elements")
        while (current_node.next is not None) and (current_position != position - 1):
            current_position += 1
            current_node = current_node.next
        if current_position != position - 1:
            raise IndexError("No elements")

        if current_node.next is not None:
            new_node.next = current_node.next
            current_node.next.prev = new_node
        new_node.prev = current_node
        current_node.next = new_node

    def delete_head(self):
        if self.head is None:
            raise IndexError("No elements")
        if self.head.next is not None:
            self.head.next.prev = None
        self.head = self.head.next

    def delete_tail(self):
        current_node = self.head
        if current_node is None:
            raise IndexError("No elements")
        while current_node.next is not None:
            current_node = current_node.next
        if current_node.prev is None:
            self.head = None
        else:
            current_node.prev.next = None
            current_node.prev = None

    def delete_at(self, position):
        current_node = self.head
        current_position = 0

        if current_node is None:
            raise IndexError("No elements")
        if position == 0:
            self.delete_head()
            return
        while (current_node.next is not None) and (current_position != position):
            current_position += 1
            current_node = current_node.next
        if current_position != position:
            raise IndexError("No elements")

        if current_node.next is not None:
            current_node.next.prev = current_node.prev
            current_node.next = None

        current_node.prev.next = current_node.next
        current_node.prev = None


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.add_head(3)
    dll.delete_tail()
    # dll.add_head(2)
    # dll.add_head(1)
    #
    # dll.add_at(4, 3)
    # dll.add_at(0, 1)
    #
    # dll.add_tail(4)
    # dll.add_tail(5)
    # dll.add_tail(6)
    #
    # dll.delete_at(7)

    print(dll.get_representation())
    print(dll.get_reversed_representation())
