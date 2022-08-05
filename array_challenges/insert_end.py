# Insert an element at the end of an array

a = [1,2,3,4]

def insert_me(a, num):

    a.insert(len(a), num)

    print(a)

insert_me(a, 5)

