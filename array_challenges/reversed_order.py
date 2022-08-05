# Print array in reverse order

array = [1,2,3,4,5,6,7]

def reverse_me(array):

    rev = list(reversed(array))
    return rev

def reverse_another(array):

    top = [i for i in reversed(array)]

    return top

# print(reverse_me(array))

print(reverse_another(array))