import re

with open("hello.txt", 'r', encoding="utf8") as f:
    data = f.read()


def get_words(filename):
    file = re.sub("[^А-Яа-я]", " ", filename.lower())
    words = file.split()
    return words

def get_words_dict(words):
    words_dict = {}
    for i in words:
        if i in words_dict:
            words_dict[i] += 1
        else:
            words_dict[i] = 1
    return words_dict

data_one = get_words(data)
print(get_words_dict(data_one))