from random import randint

def rng_string(alphabet, length):
    """
    Generate a string of a given length
    String consists of numbers between 0 - alphabet, inclusive
    """
    bitList = []
    for _ in range(0, length):
        bitList.append(str(randint(0, alphabet)))
    return ''.join(bitList)

def generate_strings(nr_strings, alphabet, length):
    """
    Generate a number of strings
    Between 0 - alphabet
    Of random length between 0 and length
    """
    for _ in range(0, nr_strings):
        yield rng_string(alphabet, randint(0, length))

for i in generate_strings(10, 1, 10):
    print(i)
