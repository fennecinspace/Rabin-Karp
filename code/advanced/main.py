from rabin import Rabin
from common import get_args, sys

## sample file
import os
SAMPLE_FILE = os.path.join((os.path.abspath(os.path.dirname(__file__))), '..', 'sample.txt')

if __name__ == '__main__':
    text, to_find = get_args(sys.argv[1:])

    r = Rabin(to_find, text)
    r.search(use_rabin_fingerprint = True)

    if r.result:
        print("Pattern '{}' found at positions {}".format(to_find, r.result))
    else:
        print("No match found for pattern '{}'".format(to_find)) 