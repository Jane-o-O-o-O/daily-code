
"""Binary Search Tree Implementation"""

from typing import Any, Optional, List


class TreeNode:
    """A node in the binary search tree."""
    
    def __init__(self, val: Any):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
    
    def __repr__(self) -> str:
        return f"TreeNode({self.val!r})"


class BinarySearchTree:
    """Binary Search Tree with insertion, search, and traversal."""
    
    def __init__(self):
        self.root: Optional[TreeNode] = None
        self._size = 0
    
    def __len__(self) -> int:
        return self._size
    
    def insert(self, val: Any) -> None:
        """Insert a value into the BST."""
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)
        self._size += 1
    
    def _insert_recursive(self, node: TreeNode, val: Any) -> None:
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)
    
    def search(self, val: Any) -> bool:
        """Search for a value in the BST."""
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node: Optional[TreeNode], val: Any) -> bool:
        if node is None:
            return False
        if val == node.val:
            return True
        elif val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)
    
    def inorder(self) -> List[Any]:
        """In-order traversal (sorted order)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node: Optional[TreeNode], result: List) -> None:
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)
    
    def preorder(self) -> List[Any]:
        """Pre-order traversal."""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node: Optional[TreeNode], result: List) -> None:
        if node:
            result.append(node.val)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder(self) -> List[Any]:
        """Post-order traversal."""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node: Optional[TreeNode], result: List) -> None:
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.val)
    
    def find_min(self) -> Optional[Any]:
        """Find the minimum value."""
        if not self.root:
            return None
        node = self.root
        while node.left:
            node = node.left
        return node.val
    
    def find_max(self) -> Optional[Any]:
        """Find the maximum value."""
        if not self.root:
            return None
        node = self.root
        while node.right:
            node = node.right
        return node.val
    
    def height(self) -> int:
        """Calculate the height of the tree."""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)


if __name__ == "__main__":
    bst = BinarySearchTree()
    for val in [5, 3, 7, 1, 4, 6, 8]:
        bst.insert(val)
    print(f"In-order: {bst.inorder()}")
    print(f"Height: {bst.height()}")
    print(f"Min: {bst.find_min()}, Max: {bst.find_max()}")
    print(f"Search 4: {bst.search(4)}")
    print(f"Search 9: {bst.search(9)}")

# [2026-04-07] sorting algorithms
class SortingAlgorithmsHandler:
    """Handler for sorting algorithms operations."""

    def __init__(self, config: dict = None):
        self._config = config or {}
        self._initialized = False
        self._cache = {}

    def initialize(self) -> bool:
        """Initialize the handler with current configuration."""
        if self._initialized:
            return True
        try:
            self._validate_config()
            self._initialized = True
            return True
        except Exception as e:
            logger.warning(f"Initialization failed: {e}")
            return False

    def _validate_config(self):
        """Validate configuration parameters."""
        required = self._required_keys()
        missing = [k for k in required if k not in self._config]
        if missing:
            raise ValueError(f"Missing config keys: {missing}")

    def _required_keys(self) -> list:
        return ["enabled"]

    def process(self, data: dict) -> dict:
        """Process data through the handler."""
        if not self._initialized:
            self.initialize()
        result = self._transform(data)
        self._cache[data.get("id", "default")] = result
        return result

    def _transform(self, data: dict) -> dict:
        """Apply transformation to input data."""
        return {"status": "processed", "data": data, "handler": self.__class__.__name__}

    def clear_cache(self):
        """Clear the internal cache."""
        self._cache.clear()
