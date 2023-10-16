sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
    if word != 'the':
        word_lengths.append(len(word))
print(words)
print(word_lengths)

word_lengths_with_comprehension = [len(word) for word in words if word != "the"]
print(word_lengths_with_comprehension)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_numbers = [number for number in numbers if number >= 0]
negative_numbers = [number for number in numbers if number < 0]
print(positive_numbers)
print(negative_numbers)
