from random import choice
import string

ALPHABET = string.digits + string.ascii_letters


def generate_slug() ->str:
    slug = ""
    for i in range(6):
        s = choice(ALPHABET)
        slug +=s
    return slug


