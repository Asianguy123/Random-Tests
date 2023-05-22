# Stacks and Queues

'''
1 - Write a program to create a queue and display all the members and size of the queue. The data in the queue is the numbers 0 to 6. The expected Output is 0 1 2 3 4 5 6 with the size of the queue being 7

2 - Write a program to find whether a queue is empty or not. The output is Boolean values of True or False.

3 - Write a program to create a FIFO queue showing data being enqueued and dequeued. The data in the queue is the numbers 0 to 6.

4 - Write a program to push three items into the stack and print the items from the stack.

5 - Write a program that peeks the stack and returns the size of the stack

6 - Write a program that checks the stack is empty, then pushes elements onto the stack until the stack is full. Confirm the by a boolean statement confirming the stack is full.
'''

# ---------------------------------------------------------------------------------------------------------------------
# Tests

def test1(data_struct, length, max_length):
    for i in range(length):
        enqueue(data_struct, i, max_length)
    print(data_struct)
    print(get_length(f'Queue length: {data_struct}'))

def test2(data_struct):
    print(check_empty(data_struct))

def test3(data_struct, length, max_length):
    for i in range(length):
        enqueue(data_struct, i, max_length)
        print(queue)
    for x in range(length):
        print(dequeue(data_struct))
        print(queue)

def test4(data_struct, max_length):
    val1 = input('Enter something:  ')
    val2 = input('Enter something:  ')
    val3 = input('Enter something:  ')
    values = [val1, val2, val3]
    for i in values:
        stack_push(stack, i, max_length)
    print(data_struct)

def test5(data_struct):
    stack_peek(data_struct)
    print(get_length(data_struct))

def test6(data_struct, max_length):
    if check_empty(data_struct):
        for i in range(max_length + 1):
            if (get_length(data_struct) + 1) >= max_length:
                print('Stack overflow')
                break
            else:
                stack_push(i)
        
# ---------------------------------------------------------------------------------------------------------------------
# Queue Functions

def enqueue(data_struct, val, max_length):
    if (get_length(queue) + 1) < max_length:
        data_struct.append(val)
    else:
        print('Queue overflow')

def dequeue(data_struct):
    val = data_struct.pop(0)
    return val

# ---------------------------------------------------------------------------------------------------------------------
# Stack Functions

def stack_pop(data_struct):
    val = data_struct.pop(-1)
    return val

def stack_push(data_struct, val, max_length):
    if (get_length(stack) + 1) < max_length:
        data_struct.append(val)
        print(val)
    else:
        print('Stack overflow')

def stack_peek(data_struct, length):
    val = data_struct[0]
    print(val)

# ---------------------------------------------------------------------------------------------------------------------
# General Functions

def check_empty(data_struct):
    if data_struct:
        return True
    return False

def get_length(data_struct):
    return len(data_struct)

def main():
    stack_max_length = 9
    queue_max_length = 10

    # call tests here as required
    
    
queue = []
stack = []    

if __name__ == '__main__':
    main()
