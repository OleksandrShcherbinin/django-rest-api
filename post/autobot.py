import json
from string import ascii_lowercase, digits
from random import choice, sample
from django.conf import settings
import requests

VOWELS = "aeiou"
CONSONANTS = "".join(set(ascii_lowercase) - set(VOWELS))
NAME_LENGTH_RANGE = [3, 4, 5, 6, 7, 8, 9, 10]


class AutoBot:

    def __init__(self):
        self.number_of_users = self.get_config_data()["number_of_users"]
        self.max_posts_per_user = self.get_config_data()["max_posts_per_user"]
        self.max_likes_per_user = self.get_config_data()["max_likes_per_user"]

    def get_config_data(self):
        with open('config.json') as file:
            data = json.load(file)
        return data

    @staticmethod
    def generate_word():
        length = choice(NAME_LENGTH_RANGE)
        word = ""
        for i in range(length):
            if i % 2 == 0:
                word += choice(CONSONANTS)
            else:
                word += choice(VOWELS)
        return word + ''.join(sample(digits, 5))

    @staticmethod
    def get_content(self):
        requests.get('https://en.wikipedia.org/wiki/Presidency_of_Donald_Trump')

    def user_list(self):
        return [{"username": self.generate_word()} for _ in range(1, self.number_of_users + 1)]

    def __repr__(self):
        return f"({self.__class__.__name__}), users={self.number_of_users}\n" \
               f"max_posts_per_user={self.max_posts_per_user}\n" \
               f"max_likes_per_user={self.max_likes_per_user}"


if __name__ == '__main__':
    auto = AutoBot()
    print(auto.generate_word())
    print(auto, auto.user_list())
