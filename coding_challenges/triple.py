# Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.

def triple_and(x, y, z):
    
    result = x + y + z

    return result == 3

# print(triple_and(True, True, False))


def triple_me(i, j, k):

    my_list = [i, j, k]
    # all() returns True if all items in an iterable are true, otherwise false
    t = all(my_list)

    return t

# print(triple_me(True, True, True))




# define a function named all_equal that takes a list and checks whether all elements in the list are the same.
# For example, calling all_equal([1, 1, 1]) should return True

def all_equal(list_me):
    
    if len(list_me) == len(set(list_me)):
        return False
    else:
        return True

print(all_equal([1, 2, 3, 4, 5]))
print(all_equal([2, 2, 2]))
print(all_equal([6, 6, 6, 6, 6]))



from itertools import groupby

def all_equal_me(my_list):
    g = groupby(my_list)

    return next(g, True) and not next(g, False)


print()
print(all_equal_me([1, 2, 3, 4, 5]))
print(all_equal_me([2, 2, 2]))
print(all_equal_me([6, 6, 6, 6, 6]))