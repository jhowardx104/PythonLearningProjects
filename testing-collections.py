# List
myList = []
myList.append(1)
myList.append(2)
myList.append(3)

print(myList[1])
print(myList)

# iterate list
for x in myList:
    print(x)


# Dictionaries
class DirectoryEntry:
    def __init__(self, age, state):
        self._age = age
        self._state = state

    def __str__(self):
        return "Age: %d\nState:%s" % (self._age, self._state)

# initialize a phonebook
phonebook = {
    "Jake": DirectoryEntry(32, 'PA'),
    "Eric": DirectoryEntry(27, 'TX'),
    "Steve": DirectoryEntry(32, 'PA')
}

# iterate a dictionary
for key, value in phonebook.items():
    print("Name %s\n%s\n" % (key, value.__str__()))


print("Count before deletion: %d" % len(phonebook))
del phonebook["Jake"]
print("Jake was removed?: %s" % ("Jake" not in phonebook))
phonebook.pop("Eric")
print("Eric was removed?: %s" % ("Eric" not in phonebook))
