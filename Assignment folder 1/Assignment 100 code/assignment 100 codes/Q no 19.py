from operator import itemgetter

def sort_tuples():
    tuples = []
    while True:
        user_input = input("Enter a tuple (name, age, score) or 'quit' to finish: ")
        if user_input.lower() == 'quit':
            break
        name, age, score = user_input.split(',')
        tuples.append((name, int(age), int(score)))
    sorted_tuples = sorted(tuples, key=itemgetter(0, 1, 2))
    for t in sorted_tuples:
        print("({0}, {1}, {2})".format(t[0], t[1], t[2]))

sort_tuples()