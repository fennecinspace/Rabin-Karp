utf_length = 1112064

def simple_hasher(pattern):
    return sum( bytearray(pattern, 'utf-8') )
    
def rabin_hasher(pattern):
    return sum ([ bytearray(pattern, 'utf-8')[i] * ( utf_length ** i) for i in range(0, len(pattern)) ])