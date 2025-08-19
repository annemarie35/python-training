def square_int():
    x = 3
    ans = 0
    for num_iteration in range(abs(x)):
        ans = ans + abs(x)
    print(f'{x}*{x} = {ans}')

square_int()

def modify_index_within_loop():
    for i in range(2):
        print(i)
        i=0
        print(f'After: {i}')

modify_index_within_loop()

def nested_loops():
    x = 3
    for j in range(x):
        print(f'-- {j} -- outer loop -----')
        for i in range(x):
            print('++++ inner loop ++++')
            x=2

nested_loops()