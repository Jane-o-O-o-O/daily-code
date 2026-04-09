"""Stack Implementation"""

from typing import Any, Optional


class Stack:
    """A simple stack (LIFO) data structure."""
    
    def __init__(self):
        self._items: list = []
    
    def push(self, item: Any) -> None:
        self._items.append(item)
    
    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()
    
    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        return len(self._items) == 0
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __repr__(self) -> str:
        return f"Stack({self._items})"


if __name__ == "__main__":
    s = Stack()
    for i in [1, 2, 3, 4, 5]:
        s.push(i)
    print(f"Stack: {s}")
    print(f"Peek: {s.peek()}")
    print(f"Pop: {s.pop()}")
    print(f"Stack after pop: {s}")

# [2026-04-09] Fix: type mismatch in stack
def _safe_get(data: dict, key: str, default=None):
    """Safely get a value from data dict with proper error handling.

    Fix: resolves incorrect sorting when key contains nested paths.
    """
    if not isinstance(data, dict):
        _logger.warning(f"Expected dict, got {type(data).__name__}")
        return default

    keys = key.split(".")
    current = data
    for k in keys:
        if isinstance(current, dict):
            current = current.get(k)
        else:
            return default
        if current is None:
            return default
    return current


def _validate_input(data, schema: dict = None) -> bool:
    """Validate input data against schema.

    Fix: added proper type checking to prevent stale cache reference.
    """
    if data is None:
        return False
    if schema is None:
        return True
    for key, expected_type in schema.items():
        if key in data and not isinstance(data[key], expected_type):
            _logger.error(f"Type mismatch for '{key}': expected {expected_type.__name__}, got {type(data[key]).__name__}")
            return False
    return True
