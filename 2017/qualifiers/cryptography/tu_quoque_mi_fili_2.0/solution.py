from itertools import count
from base64 import b64decode
import sys

def add(l):
    return (l[0] - l[1]) % 256

def process(text, start):
    return bytes(map(add, zip(text, count(start=start, step=1))))

def main(text, start):
    res = process(text, start)
    print(res.decode('ascii'))

if __name__ == "__main__":
    start = 42
    text = b64decode(open("cipher.txt").read())
    main(text, start)
