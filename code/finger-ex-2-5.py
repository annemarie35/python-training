def while_loop():
    print_nb = input('How many times should i print the letter X?')
    to_print = 'x' * int(print_nb)
    print(to_print)


while_loop()

def find_divisible():
    x = 1
    while True:
        if x % 11 == 0 and x % 12 == 0:
            break
        x = x + 1
    print(x, 'is divisible by 11 and 12')

find_divisible()

def find_largest_odd_number():
    nb_1, nb_2, nb_3, nb_4, nb_5, nb_6, nb_7, nb_8, nb_9, nb_10= input('Write 10 numbers separated by a space: ').split()
    largest_odd_number = -1
    if int(nb_1) % 2 != 0:
        largest_odd_number = int(nb_1)
    if int(nb_2) % 2 != 0 and int(nb_2) > largest_odd_number:
        largest_odd_number = int(nb_2)
    if int(nb_3) % 2 != 0 and int(nb_3) > largest_odd_number:
        largest_odd_number = int(nb_3)
    if int(nb_4) % 2 != 0 and int(nb_4) > largest_odd_number:
        largest_odd_number = int(nb_4)
    if int(nb_5) % 2 != 0 and int(nb_5) > largest_odd_number:
        largest_odd_number = int(nb_5)
    if int(nb_6) % 2 != 0 and int(nb_6) > largest_odd_number:
        largest_odd_number = int(nb_6)
    if int(nb_7) % 2 != 0 and int(nb_7) > largest_odd_number:
        largest_odd_number = int(nb_7)
    if int(nb_8) % 2 != 0 and int(nb_8) > largest_odd_number:
        largest_odd_number = int(nb_8)
    if int(nb_9) % 2 != 0 and int(nb_9) > largest_odd_number:
        largest_odd_number = int(nb_9)
    if int(nb_10) % 2 != 0 and int(nb_10) > largest_odd_number:
        largest_odd_number = int(nb_10)
    print(f'The largest odd number is {largest_odd_number}')
    if largest_odd_number < 0:
        print('No odd number was found')

find_largest_odd_number()

def find_largest_odd_number_refacto_while():
    # test with 56 4 234 7 89 65 0 45 3 90
    numbers_list = input('Write 10 numbers separated by a space: ')
    largest_odd_number = -1
    for number in numbers_list.split():
        if int(number) % 2 != 0 and int(number)  > largest_odd_number:
            largest_odd_number = int(number)

    print(f'The largest odd number is {largest_odd_number}')
    if largest_odd_number < 0:
        print('No odd number was found')

find_largest_odd_number_refacto_while()