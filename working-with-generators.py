# working with generators
import random


# generates 6 random lottery numbers and a modifier number
def lottery():
    for i in range(6):
        yield random.randint(1, 40)
    yield random.randint(1, 15)


# infinitely generates fibonacci numbers
def infinite_fib():
    a = 0
    b = 1

    while True:
        a, b = b, (a+b)
        yield b


# generates the first n fibonacci numbers
def fibonacci(n):
    a = 0
    b = 1

    count = 0
    while count < n:
        a, b = b, (a+b)
        count += 1
        yield b


for random_number in lottery():
    print("Next random number: %d" % random_number)

for next_fib in fibonacci(5):
    print("Next fib: %d" % next_fib)

counter = 0
for next_fib in infinite_fib():
    print("Infinite fib: %d" % next_fib)
    counter += 1
    if counter == 10:
        break
