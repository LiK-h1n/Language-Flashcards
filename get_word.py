from nltk.corpus import words
from random import randint

english_words = words.words()


def get_random_word():
    index = randint(1, len(english_words))
    return english_words[index]


if __name__ == "__main__":
    print(get_random_word())
