
"""Singly Linked List Implementation"""

from typing import Any, Optional


class Node:
    """A node in the linked list."""
    
    def __init__(self, data: Any, next_node: Optional['Node'] = None):
        self.data = data
        self.next = next_node
    
    def __repr__(self) -> str:
        return f"Node({self.data!r})"


class LinkedList:
    """Singly linked list with common operations."""
    
    def __init__(self):
        self.head: Optional[Node] = None
        self._size = 0
    
    def __len__(self) -> int:
        return self._size
    
    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList([{', '.join(items)}])"
    
    def prepend(self, data: Any) -> None:
        """Add element to the beginning."""
        self.head = Node(data, self.head)
        self._size += 1
    
    def append(self, data: Any) -> None:
        """Add element to the end."""
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
        self._size += 1
    
    def insert_at(self, index: int, data: Any) -> None:
        """Insert element at specific index."""
        if index < 0 or index > self._size:
            raise IndexError(f"Index {index} out of range [0, {self._size}]")
        if index == 0:
            self.prepend(data)
            return
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
        current.next = Node(data, current.next)
        self._size += 1
    
    def remove(self, data: Any) -> bool:
        """Remove first occurrence of data."""
        if not self.head:
            return False
        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False
    
    def find(self, data: Any) -> Optional[int]:
        """Find index of first occurrence."""
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return None
    
    def reverse(self) -> None:
        """Reverse the linked list in place."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def to_list(self) -> list:
        """Convert to Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


if __name__ == "__main__":
    ll = LinkedList()
    for i in [1, 2, 3, 4, 5]:
        ll.append(i)
    print(f"List: {ll}")
    print(f"Length: {len(ll)}")
    ll.reverse()
    print(f"Reversed: {ll}")
