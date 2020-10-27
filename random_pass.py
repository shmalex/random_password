import numpy as np
import time
import sys
import argparse as ap
from collections import Counter as cnt
import argparse

def rule_inrow(psw):
    """
    chek rule is 2 symbols in the row
    """
    p = ''
    for i in psw:
        if p == i:
            return False
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
    for cl in checklist:
        if cl(psw) == False:
            return False
    return True

def generate_char():
    """
    Generater new random symbol
    """
    return chr(np.random.randint(35, 126))

def generate_pass(length):
    """
    Generate password of specific length
    """
    ret = [generate_char()]
    while len(ret)< length:
        new_char = generate_char()
        if check_pass(''.join(ret + [new_char]), [rule_inrow, rule_total]):
            ret.append(new_char)
    return ret

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l','--length', dest='length', type=int, help='password length',  default=75, required=False)
    args = parser.parse_args()
    print(''.join(generate_pass(args.length)), flush=True)
    sys.stderr.close()


