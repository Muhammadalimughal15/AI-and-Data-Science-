from collections import Counter

def word_frequency():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    word_freq = Counter(words)
    for key in sorted(word_freq.keys()):
        print(f"{key}:{word_freq[key]}")

word_frequency()