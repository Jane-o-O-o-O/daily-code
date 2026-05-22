
"""String Manipulation Utilities"""


def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (case-insensitive, alphanumeric only)."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def count_words(s: str) -> int:
    """Count the number of words in a string."""
    return len(s.split())


def title_case(s: str) -> str:
    """Convert string to title case."""
    return ' '.join(word.capitalize() for word in s.split())


def truncate(s: str, max_length: int, suffix: str = '...') -> str:
    """Truncate string to max_length, adding suffix if truncated."""
    if len(s) <= max_length:
        return s
    return s[:max_length - len(suffix)] + suffix


def anagram_check(s1: str, s2: str) -> bool:
    """Check if two strings are anagrams."""
    clean = lambda s: sorted(c.lower() for c in s if c.isalnum())
    return clean(s1) == clean(s2)


def char_frequency(s: str) -> dict:
    """Count frequency of each character in a string."""
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq


def longest_common_prefix(strs: list) -> str:
    """Find the longest common prefix among a list of strings."""
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def compress_string(s: str) -> str:
    """Basic run-length encoding compression."""
    if not s:
        return ""
    
    result = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + (str(count) if count > 1 else ''))
            count = 1
    
    result.append(s[-1] + (str(count) if count > 1 else ''))
    return ''.join(result)


def decompress_string(s: str) -> str:
    """Decompress run-length encoded string."""
    result = []
    i = 0
    
    while i < len(s):
        char = s[i]
        i += 1
        num_str = ''
        
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
        
        count = int(num_str) if num_str else 1
        result.append(char * count)
    
    return ''.join(result)


if __name__ == "__main__":
    print(f"Reverse: {reverse_string('hello')}")
    print(f"Palindrome 'racecar': {is_palindrome('racecar')}")
    print(f"Anagram check 'listen'/'silent': {anagram_check('listen', 'silent')}")
    print(f"Compress 'aaabbc': {compress_string('aaabbc')}")
    print(f"Decompress 'a3b2c1': {decompress_string('a3b2c1')}")
