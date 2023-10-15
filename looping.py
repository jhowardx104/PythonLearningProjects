# Looping

# for loops
primes = [1, 2, 3, 5, 7]
for prime in primes:
    print(prime)

# range to repeat x times
for x in range(5):
    print(x)

# range with start and end
for x in range(3, 6):
    print(x)

# range with start, end, skip
for x in range(3, 8, 2):
    print(x)

# while loops
# break - exits the whole loop
# continue - skips to beginning of next iteration
count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    elif count == 7:
        break
    print(count)
    count += 1

# loops allow else clauses - they run once after the loop fails
count = 0
while count < 5:
    count += 1
else:
    print('Count reached 5')

for i in range(0, 10):
    print(i)
else:
    print('For loop ended.')

# break statements don't trigger the else
for i in range(0, 3):
    if i == 1:
        break
    print(i)
else:
    print('This will never be printed.')
