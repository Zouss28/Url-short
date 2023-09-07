from string import ascii_lowercase, digits
from random import choice

def shortcode_generator():
    return ''.join(choice(ascii_lowercase+digits) for _ in range(6))
