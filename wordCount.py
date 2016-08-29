
number_of_words = {}
maxlen = 0
text = input("Enter text: ")
words = text.split()
words.sort()

word = 0
for word in words:
    if word in number_of_words:
        number_of_words[word] += 1
    else:
        number_of_words[word] = 1
maxlen = max(len(word) for word in number_of_words)
for word in sorted(number_of_words):
    print("{:<{}} : {}".format(word, maxlen, number_of_words[word]))
