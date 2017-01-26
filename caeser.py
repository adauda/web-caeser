import string

def alphabet_position(char):

    pos = string.printable.index(char)

    if char.islower():
        pos = string.ascii_lowercase.index(char)
        return pos

    elif char.isupper():
        pos = string.ascii_uppercase.index(char)
        return pos

    return pos

def rotate_character(char, rot):

    new_pos = (alphabet_position(char) + rot) % 26

    if char.islower():
        char = string.ascii_lowercase[new_pos]
        return char

    elif char.isupper():
        char = string.ascii_uppercase[new_pos]
        return char

    return char


def encrypt(text, rot):

    new_text = ""

    i = 0
    new = ""
    for l in text:
        new += l + "MySpace"

    new = new.split("MySpace")
    length = len(new)-1

    while length > 0:
        new_text += rotate_character(new[i], rot)
        i += 1
        length -= 1

    return new_text
