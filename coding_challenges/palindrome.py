# For a given string S, write a function to check if it is a palindrome. 
# Taking a string as its paramter, your function should return True if the given string is a Pailindrome.
# -- A string is said to be a palindrome if it is the same when read backwards --

def palindrome_me(x):
    
    if x == x[::-1]:
        return True
    else:
        return False


print(palindrome_me('hannah'))
print(palindrome_me('hello'))