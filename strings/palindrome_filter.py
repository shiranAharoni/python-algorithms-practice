"""
Check Palindrome by Filtering Non-Letters
Given a string containing letters, digits, and symbols, determine if it reads the same forwards and backwards when considering only alphabetic characters (case-insensitive).

Example

Input
code = A1b2B!a

Output
1

Explanation
- Step 1: Extract only letters → ['A','b','B','a'] 
- Step 2: Convert to lowercase → ['a','b','b','a'] 
- Step 3: Compare sequence forward and backw
"""

def isAlphabeticPalindrome(code):
    code = code.lower()
    i, j = 0, len(code) - 1
    while i < j:
        if not code[i].isalpha():
            i += 1
            continue
        if not code[j].isalpha():
            j -= 1
            continue
        if code[i] != code[j]:
            return False
        i += 1
        j -= 1
    return True

