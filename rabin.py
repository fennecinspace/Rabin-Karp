utf_length = 1112064

def simple_hasher(pattern):
    return sum( bytearray(pattern, 'utf-8') )
    
def rabin_hasher(pattern):
    return sum ([ bytearray(pattern, 'utf-8')[i] * ( utf_length ** i) for i in range(0, len(pattern)) ])

def rabin_karp(pattern, text):
    # pattern length
    m = len(pattern)
    # test length
    n = len(text)
    # pattern hashed
    pattern_hash = simple_hasher(pattern)

    for i in range(0, n - m + 1):
        # checking if hashes match
        sub_text_hash = simple_hasher(text[i: i + m])
        if pattern_hash == sub_text_hash:
            # checking if strings match
            if pattern == text[i: i + m]:
                print('Pattern "{}" matched at {}'.format(pattern, i))