import re

# findall, search, split, sub

# The findall() function returns a list containing all matches.
print('findall() func:')
TEXT = "The rain in Spain"
w = re.findall("ai", TEXT)

if (w):
  print(f"Yes, It appeared {len(w)} times")
else:
  print("No match")

print('------------------------------------------------')

# The search() function searches the string for a match, and returns a Match object if there is a match.
# Returns a match where the string contains a white space character
print('search() func:')
x = re.search("\s", TEXT)
print("The first white-space character is located in position:", x.start())

print('------------------------------------------------')

# A Match Object is an object containing information about the search and the result.
print('search() func:')
i = re.search("ai", TEXT)
print(i) #this will print an object

print('------------------------------------------------')

# The split() function returns a list where the string has been split at each match:
print('split() func:')
y = re.split("\s", TEXT)
print(y)

print('------------------------------------------------')

# The sub() function replaces the matches with the text of your choice:
print('sub() func:')
z  = re.sub("\s", "9", TEXT)
print(z)
