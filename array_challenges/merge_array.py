# Merge two sorted arrays into one single sorted array

def merge_me(x, y):

    x.sort()
    y.sort()

    z = x + y

    z.sort()

    return z

print(merge_me([1,3,5,7,9,2,4,6,8], [1, 5, 7, 2, 6, 9, 3, 4, 8]))