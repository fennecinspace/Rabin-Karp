from rabin import Rabin

## sample file
import os
SAMPLE_FILE = os.path.join((os.path.abspath(os.path.dirname(__file__))), '..', 'sample.txt')

if __name__ == '__main__':
    # text = 'Hello World How Are You Doing How  HowToday ?'
    with open(SAMPLE_FILE, 'r') as f:
        text = f.read()
        
    to_find = 'how'

    r = Rabin(to_find, text)
    r.search(use_rabin_fingerprint = True)

    print("Pattern found at positions {}".format(r.result))
