# string formatting

# Formatting arguments
# %s - string
# %d - Integer
# %f - Float
# %.<num_digits>f - Float to fixed precision (rounds)
# %x/%X - Integers in hex representation (lowercase/uppercase)

name = "Jake"
age = 32
print('Hello, %s!' % name)
print('Hello, %s - age %d' % (name, age))

aList = [1, 2, 3]
print('My list: %s' % aList)

aFloat = 3.793857923084
print('My float: %f' % aFloat)
print('To 3 Decimals: %.3f' % aFloat)

anInt = 134345245345
print('Hex (lowercase): %x' % anInt)
print('Hex (uppercase): %X' % anInt)

# string operations
aString = "Hello World!"

# length
print('Length: %d' % len(aString))

# index of
print("Index of 'o': %d" % aString.index('o'))

# count
print("Count of 'l': %d" % aString.count('l'))

# substring
# start:stop
# start:stop:step - start at index, stop at index, take every n-th
# ::-1 - reverse string
print("Substring by range: %s" % aString[3:9])
print("Substring with step: %s" % aString[3:9:2])
print("Reversed: %s" % aString[::-1])

# to upper/lower
print("To Upper Case: %s" % aString.upper())
print("To Lower Case: %s" % aString.lower())

# Starts With/Ends With
print("Starts with 'Hello': %s" % aString.startswith('Hello'))
print("Ends with 'asdf': %s" % aString.endswith("asdf"))
print("Ends with '!': %s" % aString.endswith("!"))

# split strings
print("Split words count: %d" % len(aString.split(" ")))
