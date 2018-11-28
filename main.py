from rabin import rabin_karp

## sample file
import os
SAMPLE_FILE = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'sample.txt')

if __name__ == '__main__':
    # text = 'Hello World How Are You Doing How  HowToday ?'
    text = open(SAMPLE_FILE, 'r').read()
    to_find = 'how' 
    rabin_karp(to_find, text)
