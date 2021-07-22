
filename = input("Enter a file name: ")
file = open(filename)

word_dict = dict()

for line in file:
    words = line.split()
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1

for key, value in word_dict.items() :
    print(key, value)

