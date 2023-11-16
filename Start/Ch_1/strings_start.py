# Example file for Advanced Python: Language Features by Joe Marini
# strings and bytes are not directly interchangeable
# strings contain unicode, bytes are raw 8-bit values

# define some starting values
from encodings import utf_8


b = bytes([0x41, 0x42, 0x43, 0x44])
print(b)

s = "This is a string"
print(s)

# TODO: Try combining them.

# TODO: Bytes and strings need to be properly encoded and decoded
# before you can work on them together
s2 = b.decode("utf_8")
print(s+s2)
b2 = s.encode("utf_8")
print(b+b2)
# TODO: encode the string as UTF-32
b3 = s.encode("utf_32")
print(b+b3)
