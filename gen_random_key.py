import string
import random


def gen_random_key (key_length):
    return = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(key_length)])


#gen_random_key(128)
