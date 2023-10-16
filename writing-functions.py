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


# specify argument by name (unnamed also possible)
def bar(first, second, third, **options):
    if options.get('action') == 'sum':
        print("The sum is: %d" % (first + second + third))

    if options.get('number') == 'first':
        return first


result = bar(1, 2, 3)
print(result)
