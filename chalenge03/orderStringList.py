# Write a function that takes a list of strings and returns a new list with the strings sorted in alphabetical order.
# Example: "Olá mundo" should return "mundo", "Olá"
# For sorting, uppercase, lowercase, accents, and special characters should be ignored.
# However, for the output, the strings must retain their original form.
# Example: "Maçã" "LARANJA" "banana" should return "banana", "LARANJA", "Maçã"
# You can try using words in english or portuguese.

import sys

# Function to auxiliar for normalize the strings before order
def normalize(s):
    # import unicodedata module to help with accent removal
    import unicodedata
    # Convert to lowercase and remove accents
    s = s.lower()
    # Remove accents
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
    return ''.join(c for c in s if c.isalnum())

# Function to order the list of strings
def order_string_list(string_list):
    return sorted(string_list, key=normalize)  

print(order_string_list(sys.argv[1:]))