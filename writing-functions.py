# Functions
def print_hello_world():
    print('Hello, World!')


def print_user(username, age):
    print("Hello, %s, age %d" % (username, age))


def power(value, exponent):
    return value ** exponent


print_hello_world()
print_user("jhoward", 32)
result = power(3, 4)
print(result)


# functions with variable number of parameters
def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("Rest: %s" % list(therest))


foo(1, 2, 3, 4, 5, 6)
