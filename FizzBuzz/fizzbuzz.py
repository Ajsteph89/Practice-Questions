# Write a function called fizzBuzz that takes a single integer parameter named upTo.
# For the numbers 1 up to and including upTo, the function prints one of four things:
# Prints 'Fizz' if the number is only divisible by 3.
# Prints 'Buzz' if the number is only divisible by 5.
# Prints 'FizzBuzz' if the number is divisible by 3 and 5.
# Prints the number if the number is not divisible by either 3 or 5.


def fizzBuzz(upTo: int):
    for i in range(1, upTo +1):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 5 == 0:
            print('buzz')
        elif i % 3 == 0:
            print('fizz')
        else:
            print(i)

fizzBuzz(15)