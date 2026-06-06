"""String utility functions"""


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def count_words(s: str) -> int:
    """Count the number of words in a string."""
    return len(s.split())


def reverse_words(s: str) -> str:
    """Reverse the order of words in a string."""
    return " ".join(s.split()[::-1])


def capitalize_first(s: str) -> str:
    """Capitalize the first letter of each word."""
    return " ".join(word.capitalize() for word in s.split())


def caesar_cipher(text: str, shift: int) -> str:
    """Apply Caesar cipher with given shift."""
    result = []
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return "".join(result)


if __name__ == "__main__":
    print(f"Palindrome: {is_palindrome('A man a plan a canal Panama')}")
    print(f"Word count: {count_words('Hello world foo bar')}")
    print(f"Reverse: {reverse_words('Hello world foo bar')}")
    print(f"Caesar: {caesar_cipher('Hello World', 3)}")
