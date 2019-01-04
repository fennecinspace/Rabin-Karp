# Rabin Karp String Matching Algorithm

this is a project for the module TPA

the `code/simple` folder is the one used in the presentation, while the `code/advanced` folder is the one containing all the work required by the professor.

## install requirements

```bash
sudo apt-get install python3
```

## Use

```bash
cd code/advanced
```

then do the following for information

```bash
python3 main.py -h
```

### Examples

#### normal use

```bash
python3 main.py -p "word" -t "this is a word, and word sure word"
```

#### piping a text file

```bash
cat text.txt | python3 main.py -p "word" -t
```

#### using multiple patterns

use a text file that contains each pattern in a new line

```bash
cat patterns.txt | xargs -i -n1 python main.py -p {} -t "this is my text oki"
```

#### using multiple patterns with a text file

use a text file that contains each pattern in a new line, and another text file that contains the text you want to search in

```bash
xargs -a patterns.txt -I {} python3 main.py -p {} -t "$(< text.txt)"
```