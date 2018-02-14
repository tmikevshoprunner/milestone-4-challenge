import random


def list_generator_1d(min, max, length):
    """
    Generates a list of length `length`, with int values between `min` and `max`
    :param min: int
    :param max: int
    :param length: int
    :return:
    """

    return [random.randint(min, max) for _ in range(length)]


def list_generator_2d(min, max, side):
    """
    Generates a square list of length `side` with integer values between `min` and `max`
    :param min: int
    :param max: int
    :param side: int
    :return:
    """
    multi_list = []

    for i in range(0, side-1):
        multi_list.append(list_generator_1d(min, max, side))

    return multi_list


def find_1d():
    # Play with length to see how your algorithm performs
    length = 10
    max = length
    min = 0
    needle = random.randint(min, max)
    haystack_1d = list_generator_1d(min, max, length)

    was_found = False

    # Write an algorithm here that finds `needle` in `haystack_1d`

    if was_found:
        print "We found the needle in the haystack!"
    else:
        print "We didn't find anything :-("


def find_2d():

    # Play with length to see how your algorithm performs
    length = 100
    max = length
    min = 0
    needle = random.randint(min, max)
    haystack_2d = list_generator_2d(min, max, length)

    was_found = False

    # Write an algorithm here that finds `needle` in `haystack_2d`

    if was_found:
        print "We found the needle in the haystack!"
    else:
        print "We didn't find anything :-("
