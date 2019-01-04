class Rabin:
    def __init__(self, pattern, text, alpha_len = 2097152, prime = 101):
        self._pattern = pattern
        self.text = text
        self.alpha_len = alpha_len
        self.prime = prime
        self.result = []
        self.h = pow(self.alpha_len, self.pattern_len - 1)
    

    @property
    def pattern_len(self):
        return len(self._pattern)


    @property
    def text_len(self):
        return len(self.text)


    @property
    def pattern(self):
        return self._pattern


    @pattern.setter
    def pattern(self, value):
        self._pattern = value
        self.h = pow(self.alpha_len, self.pattern_len - 1)


    def simple_rolling_hash(self, pattern, old_char = None, old_hash = None):
        '''
        applies a simple rolling hash algorithm\n
        Input:
        - first iteration (pattern to hash)
        - other iterations (pattern to hash, last charachter in old hash, old hash)
        Output:
        - hash value
        '''

        if old_char and old_hash:
            new_char_index = self.pattern_len - 1

            old_char_val = ord(old_char)
            new_char_val = ord(pattern[new_char_index])

            tmp1 = (old_hash - old_char_val) // 101 
            tmp2 = new_char_val * ( self.prime ** new_char_index )

            hashed_chars = tmp1 + tmp2

        else:
            tmp = [ ord(char) * ( self.prime ** i ) for i, char in enumerate(pattern) ]
            hashed_chars = sum(tmp)
        
        return hashed_chars
        

    def rabin_rolling_hash(self, pattern, old_char = None, old_hash = None):
        '''
        applies the rabin fingerprint hashing algorithm\n
        Input:
        - first iteration (pattern to hash)
        - other iterations (pattern to hash, last charachter in old hash, old hash)
        Output:
        - hash value
        '''
        if old_hash and old_char:
            new_char_index = self.pattern_len - 1
            new_hash = old_hash - ( ord(old_char) * self.h )
            new_hash = (new_hash  * self.alpha_len ) + ord(pattern[new_char_index])
            new_hash = new_hash % self.prime
            if new_hash < 0:
                new_hash = new_hash + self.prime
            hashed_chars = new_hash
        
        else:
            hash_val = 0
            for char in pattern:
                hash_val = ( self.alpha_len * hash_val + ord(char) ) % self.prime
            hashed_chars = hash_val

        return hashed_chars


    def search(self, use_rabin_fingerprint = False):
        '''
        rabin karp algorithm\n
        Input: 
        - (pattern to search for, text to search in)
        Output:
        - list of all indexes where the pattern was found
        '''
        self.result = []
        # pattern hashed
        if use_rabin_fingerprint:
            pattern_hash = self.rabin_rolling_hash(self.pattern)
        else:
            pattern_hash = self.simple_rolling_hash(self.pattern)

        for i in range(0, self.text_len - self.pattern_len + 1):
            if i == 0:
                # first iteration
                if use_rabin_fingerprint:
                    sub_text_hash = self.rabin_rolling_hash(self.text[i: i + self.pattern_len])
                else:
                    sub_text_hash = self.simple_rolling_hash(self.text[i: i + self.pattern_len])
            else:
                # other iterations
                if use_rabin_fingerprint:
                    sub_text_hash = self.rabin_rolling_hash(self.text[i: i + self.pattern_len], self.text[i-1], sub_text_hash)
                else:
                    sub_text_hash = self.simple_rolling_hash(self.text[i: i + self.pattern_len], self.text[i-1], sub_text_hash)
            
            # checking if hashes match
            if pattern_hash == sub_text_hash:
                # checking if strings match
                if self.pattern == self.text[i: i + self.pattern_len]:
                    # print('Pattern "{}" matched at {}'.format(self.pattern, i))
                    self.result += [i]
        
