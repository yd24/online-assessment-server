#https://stackoverflow.com/questions/33588668/how-to-set-a-random-integer-as-the-default-value-for-a-django-charfield
import random

def random_img_int():
    return random.randint(1,5)

def random_view_int():
    return random.randint(1, 20)