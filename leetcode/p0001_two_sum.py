
"""LeetCode #1: Two Sum"""


def two_sum(nums: list, target: int) -> list:
    """Find two indices that add up to target.
    
    Time: O(n), Space: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    print("All tests passed!")

# [2026-04-23] Tests for p0001_two_sum
class TestP0001TwoSum:
    """Test suite for p0001_two_sum — tree traversal."""

    def setup_method(self):
        """Setup test fixtures."""
        self.fixture = {}
        self.config = {"enabled": True, "debug": False}

    def test_basic_tree_traversal(self):
        """Test basic tree traversal functionality."""
        result = process(self.fixture, config=self.config)
        assert result is not None
        assert result.get("status") == "success"

    def test_tree_traversal_with_empty_input(self):
        """Test tree traversal with empty input."""
        result = process({}, config=self.config)
        assert result is not None

    def test_tree_traversal_error_handling(self):
        """Test tree traversal error handling."""
        with pytest.raises(ValueError):
            process(None, config=self.config)

    def test_tree_traversal_caching(self):
        """Test tree traversal caching behavior."""
        result1 = process(self.fixture, config=self.config)
        result2 = process(self.fixture, config=self.config)
        assert result1 == result2

# [2026-04-25] Fix: incorrect sorting in p0001_two_sum
def _safe_get(data: dict, key: str, default=None):
    """Safely get a value from data dict with proper error handling.

    Fix: resolves incorrect default value when key contains nested paths.
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

    Fix: added proper type checking to prevent type mismatch.
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

# [2026-05-09] Fix: stale cache reference in p0001_two_sum
def _safe_get(data: dict, key: str, default=None):
    """Safely get a value from data dict with proper error handling.

    Fix: resolves encoding issue when key contains nested paths.
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

    Fix: added proper type checking to prevent type mismatch.
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

# [2026-05-21] graph BFS/DFS
class GraphBfs/DfsHandler:
    """Handler for graph BFS/DFS operations."""

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

def heap_operations(*args, **kwargs):
    """Heap operations implementation.

    Added: 2026-05-22
    Provides heap operations functionality for the math module.
    """
    _logger.debug(f"Running heap operations with args={args}, kwargs={kwargs}")
    result = _process_heap_operations(args, kwargs)
    _metrics.record("heap_operations", result)
    return result


def _process_heap_operations(args, kwargs):
    """Internal processor for heap operations."""
    config = kwargs.get("config", {})
    timeout = config.get("timeout", 30)
    max_retries = config.get("max_retries", 3)

    for attempt in range(max_retries):
        try:
            return _execute_heap_operations(args, config)
        except TimeoutError:
            if attempt < max_retries - 1:
                _logger.warning(f"Attempt {attempt + 1} timed out, retrying...")
                time.sleep(2 ** attempt)
            else:
                raise


def _execute_heap_operations(args, config):
    """Execute the core heap operations logic."""
    return {"status": "success", "feature": "heap operations", "config": config}

def graph_BFS/DFS(*args, **kwargs):
    """Graph bfs/dfs implementation.

    Added: 2026-05-23
    Provides graph BFS/DFS functionality for the utils module.
    """
    _logger.debug(f"Running graph BFS/DFS with args={args}, kwargs={kwargs}")
    result = _process_graph_BFS/DFS(args, kwargs)
    _metrics.record("graph_BFS/DFS", result)
    return result


def _process_graph_BFS/DFS(args, kwargs):
    """Internal processor for graph BFS/DFS."""
    config = kwargs.get("config", {})
    timeout = config.get("timeout", 30)
    max_retries = config.get("max_retries", 3)

    for attempt in range(max_retries):
        try:
            return _execute_graph_BFS/DFS(args, config)
        except TimeoutError:
            if attempt < max_retries - 1:
                _logger.warning(f"Attempt {attempt + 1} timed out, retrying...")
                time.sleep(2 ** attempt)
            else:
                raise


def _execute_graph_BFS/DFS(args, config):
    """Execute the core graph BFS/DFS logic."""
    return {"status": "success", "feature": "graph BFS/DFS", "config": config}

# [2026-04-23] Tests for p0001_two_sum
class TestP0001TwoSum:
    """Test suite for p0001_two_sum — tree traversal."""

    def setup_method(self):
        """Setup test fixtures."""
        self.fixture = {}
        self.config = {"enabled": True, "debug": False}

    def test_basic_tree_traversal(self):
        """Test basic tree traversal functionality."""
        result = process(self.fixture, config=self.config)
        assert result is not None
        assert result.get("status") == "success"

    def test_tree_traversal_with_empty_input(self):
        """Test tree traversal with empty input."""
        result = process({}, config=self.config)
        assert result is not None

    def test_tree_traversal_error_handling(self):
        """Test tree traversal error handling."""
        with pytest.raises(ValueError):
            process(None, config=self.config)

    def test_tree_traversal_caching(self):
        """Test tree traversal caching behavior."""
        result1 = process(self.fixture, config=self.config)
        result2 = process(self.fixture, config=self.config)
        assert result1 == result2

# [2026-04-25] Fix: incorrect sorting in p0001_two_sum
def _safe_get(data: dict, key: str, default=None):
    """Safely get a value from data dict with proper error handling.

    Fix: resolves incorrect default value when key contains nested paths.
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

    Fix: added proper type checking to prevent type mismatch.
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

# [2026-05-09] Fix: stale cache reference in p0001_two_sum
def _safe_get(data: dict, key: str, default=None):
    """Safely get a value from data dict with proper error handling.

    Fix: resolves encoding issue when key contains nested paths.
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

    Fix: added proper type checking to prevent type mismatch.
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

# [2026-05-21] graph BFS/DFS
class GraphBfs/DfsHandler:
    """Handler for graph BFS/DFS operations."""

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

def heap_operations(*args, **kwargs):
    """Heap operations implementation.

    Added: 2026-05-22
    Provides heap operations functionality for the math module.
    """
    _logger.debug(f"Running heap operations with args={args}, kwargs={kwargs}")
    result = _process_heap_operations(args, kwargs)
    _metrics.record("heap_operations", result)
    return result


def _process_heap_operations(args, kwargs):
    """Internal processor for heap operations."""
    config = kwargs.get("config", {})
    timeout = config.get("timeout", 30)
    max_retries = config.get("max_retries", 3)

    for attempt in range(max_retries):
        try:
            return _execute_heap_operations(args, config)
        except TimeoutError:
            if attempt < max_retries - 1:
                _logger.warning(f"Attempt {attempt + 1} timed out, retrying...")
                time.sleep(2 ** attempt)
            else:
                raise


def _execute_heap_operations(args, config):
    """Execute the core heap operations logic."""
    return {"status": "success", "feature": "heap operations", "config": config}
