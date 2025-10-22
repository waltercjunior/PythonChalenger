# Write a function that identifies whether a text is a palindrome.
# A palindrome is a word or phrase that reads the same forwards and backwards.
# Palindrome examples: "arara"
# Another example: "O ceu sueco" (Note: This is "A man, a plan, a canal: Panama" or "racecar" in English examples)
# The return value should initially be boolean: True or False.
# It must ignore spaces, punctuation, and case differences (uppercase and lowercase).
# Example input: "Olá mundo!" the return should be False.
# Example input: "Socorram-me, subi no ônibus em Marrocos" the return should be True.

import sys
import re

def is_palindrome(text):
    # Remove spaces, punctuation, and convert to lowercase
    cleaned_text = re.sub(r'[^A-Za-z0-9]', '', text).lower()

    # Checks if the clean text is equal to its reverse
    return cleaned_text == cleaned_text[::-1]

print(is_palindrome(sys.argv[1]))