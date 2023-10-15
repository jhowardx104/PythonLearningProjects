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
