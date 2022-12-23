# Example file for Advanced Python: Language Features by Joe Marini
# Capture pattern matching for assigning values within the match

name = input("What is your name? ")

match name:
  case "":
    print("Hello, anonymous!")
  case "Joe":
    print("Oh hi there, Joe!")
  case name:
    print (f"Hello, {name}!")
