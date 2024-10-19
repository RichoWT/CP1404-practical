"""
CP1404 Practical
Word Occurences
"""

word_count = {}

text = input("text: ")
words = text.split()
for word in words:
    rate = word_count.get(word, 0)
    word_count[word] = rate + 1

word = list(word_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_count[word]}")