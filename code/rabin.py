def get_char_value(char):
    '''
    return an int value of a character ( utf-8 representation of a character )
    Input:
    - (character)
    Output:
    - utf8 encoded value
    '''

    return bytearray(char, 'utf-8')[0]


def rolling_hash(pattern, old_char = None, old_hash = None):
    '''
    applies the rolling hash algorithm\n
    Input:
    - first iteration (pattern to hash)
    - other iterations (pattern to hash, last charachter in old hash, old hash)
    Output:
    - hash value
    '''
    prime = 101
 
    if old_char and old_hash:
        new_char_index = len(pattern) - 1

        old_char_val = get_char_value(old_char)
        new_char_val = get_char_value(pattern[new_char_index])

        tmp1 = (old_hash - old_char_val) // 101 
        tmp2 = new_char_val * ( prime ** new_char_index )

        hashed_chars = tmp1 + tmp2

    else:
        tmp = [ get_char_value(char) * ( prime ** i ) for i, char in enumerate(pattern) ]
        hashed_chars = sum(tmp)
    
    return hashed_chars


def rabin_karp(pattern, text):
    '''
    rabin karp algorithm\n
    Input: 
    - (pattern to search for, text to search in)
    Output:
    - list of all indexes where the pattern was found
    '''
    pattern_positions = []
    # pattern length
    m = len(pattern)
    # test length
    n = len(text)
    # pattern hashed
    pattern_hash = rolling_hash(pattern)

    for i in range(0, n - m + 1):
        if i == 0:
            # first iteration
            sub_text_hash = rolling_hash(text[i: i + m])
        else:
            # other iterations
            sub_text_hash = rolling_hash(text[i: i + m], text[i-1], sub_text_hash)
        
        # checking if hashes match
        if pattern_hash == sub_text_hash:
            # checking if strings match
            if pattern == text[i: i + m]:
                print('Pattern "{}" matched at {}'.format(pattern, i))
                pattern_positions += [i]
    
    return pattern_positions