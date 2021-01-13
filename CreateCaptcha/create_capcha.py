#! /bin/python3

import random
import string
from captcha.image import ImageCaptcha

def get_random_password_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str

def main():

    image = ImageCaptcha()
    key_list = []
    token = 0
    variable = get_random_password_string(16)

    for i in range(0,5):
        key_list.append(variable[:6])
        variable = (variable[2:])
    print(key_list)

    for e in key_list:
        filename = ("out" + str(token) + ".png")
        image.write(e, filename)
        token += 1

if __name__ == "__main__":
    main()