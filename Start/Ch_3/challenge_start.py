# Example file for Advanced Python: Language Features by Joe Marini
# Programming challenge for comprehensions

import string
import pprint


test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"

# YOUR CODE HERE

# print the data
str_data = {
    "Length": len(test_str),
    "Digits": sum([c.isdigit() for c in test_str]),
    "Punctuation": sum([not (c.isalnum() or c.isspace()) for c in test_str]),
    "Unique Letters": (ul := ''.join({c for c in test_str if c.isalpha()})),
    "Unique Count": len(ul)
}

pprint.pp(str_data)
