# Boolean conditions

x = 2
print(x == 2)
print(x == 3)
print(x < 3)

name = "Jake"
age = 32

# use and/or to combine conditions in decisions
if name == "Jake" and age > 20:
    print('Your name is Jake, and you are also older than 20')
if name == "Jake" or name == "Mariah":
    print('Your name is either Jake or Mariah')

# use in to check if value is contained in list
if name in ['Jake', 'Mariah']:
    print('Your name is in the list.')

# if/elif/else
if name == "Jake":
    print('Husband')
elif name == "Mariah":
    print('Wife')
else:
    print('Neither')

# is operator - makes sure that instances match, not values
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

x = y
print(x is y)

# not operator - inverts the boolean expression
if not name == "Jake":
    print('You are not Jake.')
