
# Link : https://www.hackerrank.com/challenges/two-characters

import sys

# sys.stdin = open('test1.in','r')
# sys.stdout = open('test1.out','w')



def checkCond(m,n,s):
    ts = ''
    ptr = 0
    for i in range(len(s)):
        if(s[i] == m or s[i] == n):
            ts += s[i]
            ptr = i + 1
            break
    for i in range(ptr,len(s)):
        if(s[i] == m or s[i] == n):
            ts += s[i]
            if(ts[-1] == ts[-2] ):
                return 0
    return len(ts)


def main():
    if(sys.stdin.readline() == '0'):
        sys.stdout.write('0')
        exit()
    data = sys.stdin.readline().rstrip()
    maxL = 0
    s = list(set(data))
    i = 0

    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            tmp = checkCond(s[i],s[j],data)
            if maxL < tmp :
                maxL = tmp

    sys.stdout.write(str(maxL))


main()
