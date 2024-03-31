
punctuation_counts = {'.': 0, '?': 0, '!': 0, ',': 0, '/': 0, '-': 0, '+': 0}
text = input()
for char in text:
    if char in punctuation_counts:
        punctuation_counts[char] += 1

print(punctuation_counts)
