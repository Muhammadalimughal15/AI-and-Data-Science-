n = int(input())
words = []
word_count = {}

for _ in range(n):
    word = input()
    words.append(word)
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(len(set(words)))
for word in words:
    if word not in words[:words.index(word)]:
        print(word_count[word], end=" ")