n = int(input())
scores = list(set(map(int, input().split())))
scores.sort(reverse=True)
print(scores[1])