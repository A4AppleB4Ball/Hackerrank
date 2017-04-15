
# Link : https://www.hackerrank.com/challenges/camelcase

import sys

# sys.stdin = open('test1.in','r')
# sys.stdout = open('test1.out','w')


def main():
    data = sys.stdin.readline().rstrip()
    count = 0
    i = 0
    while i < len(data) :
        if ord(data[i]) < 97:
            count += 1
        i += 1
    if(len(data) > 0):
        count += 1
    sys.stdout.write(str(count))


main()
