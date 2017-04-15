
# Link : https://www.hackerrank.com/contests/w31/challenges/spanning-tree-fraction

import sys

# sys.stdin = open('test1.in','r')
# sys.stdout = open('test1.out','w')






def main():
    data = sys.stdin.readline().rstrip()
    sample = [ord('a'),ord('e'),ord('i'),ord('o'),ord('u'),ord('y')]
    for i in range(len(data)-1):
        if( data[i] == data[i+1] or (ord(data[i]) in sample  and ord(data[i+1]) in sample)):
            sys.stdout.write('No')
            exit()
    sys.stdout.write('Yes')



main()
