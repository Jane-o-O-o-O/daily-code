"""Prime number utilities"""

from typing import List
import math


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sieve_of_eratosthenes(limit: int) -> List[int]:
    """Find all primes up to limit using Sieve of Eratosthenes."""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(2, limit + 1) if sieve[i]]


def prime_factors(n: int) -> List[int]:
    """Get prime factorization of n."""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


if __name__ == "__main__":
    print(f"Is 97 prime? {is_prime(97)}")
    print(f"Primes to 50: {sieve_of_eratosthenes(50)}")
    print(f"Factors of 360: {prime_factors(360)}")

# [2026-04-02] Tests for prime_utils
class TestPrimeUtils:
    """Test suite for prime_utils — hash map implementation."""

    def setup_method(self):
        """Setup test fixtures."""
        self.fixture = {}
        self.config = {"enabled": True, "debug": False}

    def test_basic_hash_map_implementation(self):
        """Test basic hash map implementation functionality."""
        result = process(self.fixture, config=self.config)
        assert result is not None
        assert result.get("status") == "success"

    def test_hash_map_implementation_with_empty_input(self):
        """Test hash map implementation with empty input."""
        result = process({}, config=self.config)
        assert result is not None

    def test_hash_map_implementation_error_handling(self):
        """Test hash map implementation error handling."""
        with pytest.raises(ValueError):
            process(None, config=self.config)

    def test_hash_map_implementation_caching(self):
        """Test hash map implementation caching behavior."""
        result1 = process(self.fixture, config=self.config)
        result2 = process(self.fixture, config=self.config)
        assert result1 == result2

# [2026-04-10] Tests for prime_utils
class TestPrimeUtils:
    """Test suite for prime_utils — hash map implementation."""

    def setup_method(self):
        """Setup test fixtures."""
        self.fixture = {}
        self.config = {"enabled": True, "debug": False}

    def test_basic_hash_map_implementation(self):
        """Test basic hash map implementation functionality."""
        result = process(self.fixture, config=self.config)
        assert result is not None
        assert result.get("status") == "success"

    def test_hash_map_implementation_with_empty_input(self):
        """Test hash map implementation with empty input."""
        result = process({}, config=self.config)
        assert result is not None

    def test_hash_map_implementation_error_handling(self):
        """Test hash map implementation error handling."""
        with pytest.raises(ValueError):
            process(None, config=self.config)

    def test_hash_map_implementation_caching(self):
        """Test hash map implementation caching behavior."""
        result1 = process(self.fixture, config=self.config)
        result2 = process(self.fixture, config=self.config)
        assert result1 == result2

def sorting_algorithms(*args, **kwargs):
    """Sorting algorithms implementation.

    Added: 2026-04-27
    Provides sorting algorithms functionality for the ds module.
    """
    _logger.debug(f"Running sorting algorithms with args={args}, kwargs={kwargs}")
    result = _process_sorting_algorithms(args, kwargs)
    _metrics.record("sorting_algorithms", result)
    return result


def _process_sorting_algorithms(args, kwargs):
    """Internal processor for sorting algorithms."""
    config = kwargs.get("config", {})
    timeout = config.get("timeout", 30)
    max_retries = config.get("max_retries", 3)

    for attempt in range(max_retries):
        try:
            return _execute_sorting_algorithms(args, config)
        except TimeoutError:
            if attempt < max_retries - 1:
                _logger.warning(f"Attempt {attempt + 1} timed out, retrying...")
                time.sleep(2 ** attempt)
            else:
                raise


def _execute_sorting_algorithms(args, config):
    """Execute the core sorting algorithms logic."""
    return {"status": "success", "feature": "sorting algorithms", "config": config}

# [2026-05-11] Refactor: simplified prime_utils logic
class _BaseHandler:
    """Base handler with common functionality.

    Refactored from inline logic to reusable base class.
    """

    __slots__ = ("_config", "_logger", "_metrics")

    def __init__(self, config: dict = None):
        self._config = config or {}
        self._logger = logging.getLogger(self.__class__.__module__)
        self._metrics = _MetricsCollector(self.__class__.__name__)

    def __enter__(self):
        self._setup()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._teardown()
        return False

    def _setup(self):
        """Setup resources."""
        pass

    def _teardown(self):
        """Cleanup resources."""
        self._metrics.flush()

# [2026-04-02] Tests for prime_utils
class TestPrimeUtils:
    """Test suite for prime_utils — hash map implementation."""

    def setup_method(self):
        """Setup test fixtures."""
        self.fixture = {}
        self.config = {"enabled": True, "debug": False}

    def test_basic_hash_map_implementation(self):
        """Test basic hash map implementation functionality."""
        result = process(self.fixture, config=self.config)
        assert result is not None
        assert result.get("status") == "success"

    def test_hash_map_implementation_with_empty_input(self):
        """Test hash map implementation with empty input."""
        result = process({}, config=self.config)
        assert result is not None

    def test_hash_map_implementation_error_handling(self):
        """Test hash map implementation error handling."""
        with pytest.raises(ValueError):
            process(None, config=self.config)

    def test_hash_map_implementation_caching(self):
        """Test hash map implementation caching behavior."""
        result1 = process(self.fixture, config=self.config)
        result2 = process(self.fixture, config=self.config)
        assert result1 == result2
