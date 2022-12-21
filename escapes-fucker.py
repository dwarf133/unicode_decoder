#!/usr/bin/python3
import urllib.parse
import sys

def decode(path: str) -> bool:
    decoded = ''
    with open(path, 'r') as file:
        input = file.read()
        decoded = input.encode('ascii').decode('unicode-escape')
    with open(f'decoded_{path}', 'x') as file:
        file.write(decoded)
    return True

if __name__ == '__main__':
    sys.argv.append('t.json') #just for debug
    if len(sys.argv) < 2:
        raise ValueError('Please write path to file')
    else:
        status = decode(sys.argv[1])
    print(f'{"Succesed" if status else "Error"}')