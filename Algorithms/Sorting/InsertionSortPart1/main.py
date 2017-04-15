
# Link : https://www.hackerrank.com/challenges/insertionsort1

import sys

# sys.stdin = open('test1.in','r')
# sys.stdout = open('test1.out','w')






def main():
    if(sys.stdin.readline() == '0'):
        sys.stdout.write('0')
        exit()
    data = [ int(i) for i in sys.stdin.readline().rstrip().split(' ')]

    if data[-1] >= data[-2]:
        sys.stdout.write(str(' '.join([str(i) for i in data]))+'\n')
        exit()
    n , data[-1] = data[-1] , data[-2]
    sys.stdout.write(str(' '.join([str(i) for i in data]))+'\n')
    i = len(data) - 2
    while  i > 0 and n < data[i-1]  :
        data[i] = data[i-1]
        sys.stdout.write(str(' '.join([str(j) for j in data]))+'\n')
        i -= 1
    data[i] = n
    sys.stdout.write(str(' '.join([str(i) for i in data])))



main()
