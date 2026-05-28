"""String utils for 2026-05-28"""

def reverse(s):
    return s[::-1]

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

def vowel_count(s):
    return sum(1 for c in s.lower() if c in "aeiou")

if __name__ == "__main__":
    print(f"reverse hello: {reverse('hello')}")
    print(f"anagram: {is_anagram('listen', 'silent')}")
    print(f"vowels: {vowel_count('hello world')}")
