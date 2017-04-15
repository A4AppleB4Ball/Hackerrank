
# Link : https://www.hackerrank.com/contests/w31/challenges/accurate-sorting

import sys

# sys.stdin = open('test1.in','r')
# sys.stdout = open('test1.out','w')



def main():
    k = int(sys.stdin.readline().rstrip())
    for i in range(k):
        n = int(sys.stdin.readline().rstrip())
        arr = [int(m) for m in sys.stdin.readline().rstrip().split(' ')]
        j=0
        for j in range(n):
            if(abs(arr[j] - j) > 1):
                sys.stdout.write('No\n')
                break
        if j == n-1 :
            sys.stdout.write('Yes\n')







main()
