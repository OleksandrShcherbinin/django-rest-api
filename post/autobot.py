import json
import logging
from threading import Thread
from random import choice, sample
from string import ascii_lowercase, digits, ascii_letters, punctuation
from django.conf import settings
from requests_html import HTMLSession


logger = logging.getLogger('django')

VOWELS = "aeiou"
CONSONANTS = "".join(set(ascii_lowercase) - set(VOWELS))
NAME_LENGTH_RANGE = range(3, 11)
CONTENT_SOURCE = 'https://en.wikipedia.org/wiki/Presidency_of_Donald_Trump'
PASSWORD_CHARACTERS = list(f"{ascii_letters}{digits}{punctuation}")
PASSWORD_LENGTH_RANGE = range(8, 14)
EMAIL_DOMAINS = ["@hotmail.com", "@gmail.com", "@ukr.net", "@mail.com", "@mail.kz",
                 "@yahoo.com"]

API_DOMAIN = 'http://127.0.0.1:8000/'


def get_content():
    with HTMLSession() as session:
        response = session.get(CONTENT_SOURCE)
    return [elem.text for elem in response.html.xpath('//p')]


class BotConfig:
    content_list = list(filter(lambda x: x != "", get_content()))

    def __init__(self):
        self.number_of_users = self.get_config_data()["number_of_users"]
        self.max_posts_per_user = self.get_config_data()["max_posts_per_user"]
        self.max_likes_per_user = self.get_config_data()["max_likes_per_user"]

    @staticmethod
    def get_config_data():
        with open(settings.BASE_DIR / 'config.json') as file:
            data = json.load(file)
        return data


class AutoBot(BotConfig):

    headers = {'Content-type': 'application/json',
               'Accept': 'application/json',
               'Content-Encoding': 'utf-8'}

    def __init__(self, first_name=None, last_name=None,
                 access_token=None, refresh_token=None):
        super().__init__()
        self.username = self.generate_name()
        self.password = self.generate_password()
        self.email = self.generate_email()
        self.first_name = first_name
        self.last_name = last_name
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.posts = []
        self.all_posts = []

    def user_sign_up(self):
        user = {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "password2": self.password
        }
        response = self.post_request(API_DOMAIN + 'auth/signup/',
                                     self.headers,
                                     user)
        if response.status_code == 201:
            status_code = self.user_login()
            if status_code == 200:
                status_code = self.create_posts()
                if status_code == 201 or status_code == 200:
                    self.like_self_posts()
        else:
            logger.warning(f"{response.status_code}, {response.text}")

    def user_login(self):
        response = self.post_request(API_DOMAIN + 'auth/login/',
                                     self.headers,
                                     {"username": self.username,
                                      "password": self.password})
        self.access_token = response.json().get('access')
        self.refresh_token = response.json().get('refresh')
        return response.status_code

    def create_post(self):
        self.headers["Authorization"] = f"Bearer {self.access_token}"
        content = choice(self.content_list)
        if content:
            data = {"username": self.username,
                    "title": content[:10],
                    "content": content
                    }

            response = self.post_request(API_DOMAIN + 'api/posts/',
                                         self.headers, data)
            assert response.status_code == 201 or response.status_code == 200
            self.posts.append(response.json())

    def create_posts(self):
        self.headers["Authorization"] = f"Bearer {self.access_token}"
        data = self.create_list_of_post()

        for piece in data:
            if piece:
                response = self.post_request(API_DOMAIN + 'api/posts/',
                                             self.headers, data=piece)
                assert response.status_code == 201 or response.status_code == 200
                self.posts.append(response.json())
                return response.status_code

    def like_self_posts(self):
        self.headers["Authorization"] = f"Bearer {self.access_token}"
        if self.posts:
            for post in self.posts:
                post["like"] = choice(range(1, self.max_likes_per_user))
                response = self.post_request(API_DOMAIN + f'api/posts/{post["id"]}/',
                                             self.headers, data=post, method="PUT")
                logger.info(response.json())

    def get_all_posts(self):
        self.headers["Authorization"] = f"Bearer {self.access_token}"
        response = self.post_request(API_DOMAIN + 'api/posts/',
                                     self.headers, method="GET")
        for item in response.json():
            self.all_posts.append(item)
            logger.info(item.get("title"))

    def like_a_post(self):
        pass

    @staticmethod
    def post_request(url, headers, data=None, timeout=20, method="POST"):
        with HTMLSession() as session:
            if method == "POST":
                response = session.post(url, headers=headers,
                                        json=data, timeout=timeout)
            elif method == "PUT":
                response = session.put(url, headers=headers,
                                       data=json.dumps(data), timeout=timeout)
            elif method == "GET":
                response = session.get(url, headers=headers, timeout=timeout)
        logger.info(response.status_code)
        return response

    @staticmethod
    def generate_name():
        length = choice(NAME_LENGTH_RANGE)
        word = ""
        for i in range(length):
            if i % 2 == 0:
                word += choice(CONSONANTS)
            else:
                word += choice(VOWELS)
        return word + ''.join(sample(digits, 5))

    @staticmethod
    def generate_password():
        return ''.join(sample(PASSWORD_CHARACTERS, choice(PASSWORD_LENGTH_RANGE)))

    def generate_email(self):
        return self.generate_name() + choice(EMAIL_DOMAINS)

    def create_list_of_post(self):
        content_list = []
        for _ in range(self.max_posts_per_user):
            content = choice(self.content_list)
            content_list.append({
                "username": self.username,
                "title": ' '.join(content.split()[:4]),
                "content": content
            })
        return content_list

    def __repr__(self):
        return f"({self.__class__.__name__}), users={self.number_of_users}\n" \
               f"max_posts_per_user={self.max_posts_per_user}\n" \
               f"max_likes_per_user={self.max_likes_per_user}"


def run():
    auto = AutoBot()
    bots = [auto]
    for _ in range(auto.number_of_users - 1):
        auto_bot = AutoBot()
        bots.append(auto_bot)
    logger.info(bots)

    for obj in bots:
        Thread(target=obj.user_sign_up, args=()).start()


if __name__ == '__main__':
    run()
