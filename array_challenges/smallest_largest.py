# Find the largest and the smallest number in a given array

def find_me(array):

    min_num = min(array)
    max_num = max(array)

    return f'The maximum number is: {max_num} and the smallest number is: {min_num}'


print(find_me([1,2,2000,3,4,5,6,-10,6,7,8,9,1100,-5]))