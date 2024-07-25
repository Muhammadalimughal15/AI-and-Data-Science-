words = input("Enter a sequence of whitespace separated words: ").split()

unique_words = set(words)
sorted_words = sorted(unique_words)

print(' '.join(sorted_words))