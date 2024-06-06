class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append a node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """Prepend a node with the given data to the start of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        """Delete the first node containing the given data."""
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next
        
        if current_node.next:
            current_node.next = current_node.next.next

    def print_list(self):
        """Print all elements in the linked list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def insert_after_node(self, prev_node, data):
        """Insert a new node after the given node."""
        if not prev_node:
            print("The given previous node must in LinkedList.")
            return
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_at_position(self, position):
        """Delete the node at a specific position."""
        if not self.head:
            return
        
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
        
        if temp is None or temp.next is None:
            return
        
        next = temp.next.next
        temp.next = None
        temp.next = next

    def length(self):
        """Return the length of the linked list."""
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
