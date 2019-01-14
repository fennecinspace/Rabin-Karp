import os
SAMPLE_FILE = os.path.join((os.path.abspath(os.path.dirname(__file__))), 'sample.txt')

alpha_len = 2097152 # nb of representable characters in utf-8


def calc_hash(pattern, prime):
    hash_val = 0
    
    for char in pattern:
        hash_val = ( alpha_len * hash_val + ord(char) ) % prime
    
    return hash_val


def recalc_hash(old_hash, old_char, new_char, h, prime):
    new_hash = old_hash - ( ord(old_char) * h )
    new_hash = (new_hash  * alpha_len ) + ord(new_char)
    new_hash = new_hash % prime

    if new_hash < 0:
        new_hash = new_hash + prime

    return new_hash



def search(pattern, text, prime = 101): 
    res = []
    pl = len(pattern) 
    tl = len(text)
    h = pow(alpha_len, pl - 1)

    # hash value of pattern
    pattern_hash = calc_hash(pattern, prime)
    # first window hash
    win_hash = calc_hash(text[:pl], prime)
    
    # windows sliding
    for i in range(0, tl - pl - 1): 
        if pattern_hash == win_hash:
            if pattern == text[i: i + pl]:
                res += [i]
                print('Pattern "{}" matched at {}'.format(pattern, i))
  
        ## next window hash val
        win_hash = recalc_hash(
            old_char = text[i], 
            old_hash = win_hash, 
            new_char = text[i + pl], 
            h = h, 
            prime = prime
        )

    return res


if __name__ == '__main__':
    # text = 'Hello World How Are You Doing How  HowToday ?'
    text = open(SAMPLE_FILE, 'r').read()
    to_find = 'how'

    res = search(to_find, text)

    print("Pattern found at positions {}".format(res))
