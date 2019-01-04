import sys

def get_args(argv):
    pattern, text = None, None

    if ('-t' not in argv or '-p' not in argv) and '-h' not in argv:
        argv = ['-h']

    try:
        if '-t' in argv:
            text = argv[argv.index('-t') + 1]
        elif '--text' in argv:
            text = argv[argv.index('--text') + 1]
    except: 
        text = " ".join(sys.stdin.readlines())

    
    try:
        if '-p' in argv:
            pattern = argv[argv.index('-p') + 1]
        elif '--pattern' in argv:
            pattern = argv[argv.index('--pattern') + 1]
    except: print('"-p" has been passed incorrectly do "-h" for HELP')

    try:
        if ('-h' in argv or '--help' in argv):
            print ('Returns indexes where a pattern exists in a certain text\npython3 main.py -p my_pattern -t my_text\n')
            print ('  -p, --pattern [string]        the pattern you\'re looking for')
            print ('  -t, --text [string]           the text you want to search in')
            print ('  -h, --help                  Show help\n')

    except: pass

    if '-t' not in argv and '-p' not in argv:
        exit()
    return text, pattern