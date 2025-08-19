def sum_prime_numbers():
    primes_sum = 0
    for number in range(3, 999):
        prime = True
        for i in range(2, number):
            if (number % i == 0):
                prime = False
        if prime:
            primes_sum = primes_sum + number
    print('The sum of the prime numbers greater than 2 and less than 1000 is: ', primes_sum)


sum_prime_numbers()

