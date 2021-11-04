import logging

# print(dir(logging))

logging.basicConfig(filename='test.log', format='%(asctime)s : %(levelname)s : 	%(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')

def add(x, y):
    '''Add Function'''
    return x + y

def subtract(x, y):
    '''Subtract Function'''
    return x - y

def multiply(x, y):
    '''Multiply Function'''
    return x * y

def divide(x, y):
    '''Divide Function'''
    return x // y

num_1 = 100
num_2 = 20

add_result = add(num_1, num_2)
logging.info(f'Add {num_1} + {num_2} = {add_result}')

sub_result = subtract(num_1, num_2)
logging.info(f'Subtract {num_1} - {num_2} = {sub_result}')

multiply_result = multiply(num_1, num_2)
logging.info(f'Multiply {num_1} * {num_2} = {multiply_result}')

divide_result = divide(num_1, num_2)
logging.info(f'Divide {num_1} / {num_2} = {divide_result}')