import numpy as np
import time
import sys
import argparse as ap
from collections import Counter as cnt
import argparse

start_char, end_char = 35, 126
char_range = end_char - start_char


def rule_inrow(psw):
    """
    checks the rule whether 2 symbols are in the sequence
    """
    previous = ''
    for c in psw:
        if previous == c:
            return False
        previous = c
    return True


def rule_total(psw, maxx=5):
    """
    checks if password contains one symbol more the maxx times
    """
    if max(cnt(psw).values()) > maxx:
        return False
    return True


def check_pass(psw, checklist):
    """
    Iterates through list of rules
    """
    for func in checklist:
        if len(func) > 1:
            cl = func[0]
            args = [func[1]]
        else:
            cl = func[0]
            args = []
        if cl(psw, *args) == False:
            return False
    return True


def generate_char():
    """
    Generater new random symbol
    """
    return chr(np.random.randint(35, 126))


def generate_pass(length, maxx):
    """
    Generate password of specific length
    """
    ret = [generate_char()]
    while len(ret) < length:
        new_char = generate_char()
        if check_pass(''.join(ret + [new_char]), [(rule_inrow,), (rule_total, maxx)]):
            ret.append(new_char)
    return ret


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length', dest='length', type=int,
                        help='password length',  default=75, required=False)
    args = parser.parse_args()
    maxx = max(1, args.length // char_range)+1

    print(''.join(generate_pass(args.length, maxx)), flush=True)
    sys.stderr.close()