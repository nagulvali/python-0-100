
# 01. Reverse a string
def reverse_string(s: str) -> str:
    return s[::-1]

# 02. Check if a string is a palindrome
def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# 03. Count the number of vowels in a string
def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# 04. Find the first non-repeating character in a string
def first_non_repeating_char(s: str) -> str:
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

# 05. Check if two strings are anagrams
def are_anagrams(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

# 06. Find the longest word in a string
def longest_word(s: str) -> str:
    words = s.split()
    return max(words, key=len) if words else ""

# 07. Replace all spaces in a string with a specified character
def replace_spaces(s: str, char: str) -> str:
    return s.replace(" ", char)

# 08. Count the number of occurrences of a substring in a string
def count_substring(s: str, substring: str) -> int:
    return s.count(substring)

# 09. Convert a string to title case
def to_title_case(s: str) -> str:
    return ' '.join(word.capitalize() for word in s.split())

# 10. Check if a string contains only digits
def is_digit_string(s: str) -> bool:
    return s.isdigit()

# 11. Remove all punctuation from a string
import string
def remove_punctuation(s: str) -> str:
    return s.translate(str.maketrans('', '', string.punctuation))

# 12. Find the number of words in a string
def count_words(s: str) -> int:
    return len(s.split())

# 13. Check if a string is a valid email address
import re
