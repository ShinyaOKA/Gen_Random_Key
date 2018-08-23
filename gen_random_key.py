import string
import random


def gen_random_key (key_length):
    return = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(KEY_LENGTH)])


#gen_random_key(128)
