from pandas import read_csv
from random import randint


def get_random_word():
    df = read_csv("words.csv")
    return df["word"][randint(0, 999)]


if __name__ == "__main__":
    print(get_random_word())
