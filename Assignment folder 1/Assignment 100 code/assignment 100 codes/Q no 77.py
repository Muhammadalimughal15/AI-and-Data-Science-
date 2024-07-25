subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

sentences = [f"{subject} {verb} {object}." for subject in subjects for verb in verbs for object in objects]
print(sentences)