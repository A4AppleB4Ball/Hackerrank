
# Link : https://www.hackerrank.com/contests/w31/challenges/accurate-sorting

import sys

sys.stdin = open('test1.in','r')
sys.stdout = open('test1.out','w')



def main():
    k = int(sys.stdin.readline().rstrip())
    for i in range(k):
        n = int(sys.stdin.readline().rstrip())
        arr = [int(m) for m in sys.stdin.readline().rstrip().split(' ')]
        flag = 1
        while flag:
            flag = 0
            for j in range(n-1):
                if(arr[j]>arr[j+1]):
                    flag = 1
            if(flag == 0):
                sys.stdout.write('Yes')
                if(i < k-1):
                    sys.stdout.write('\n')
                break
            flag = 0
            for j in range(n-1):
                if((abs(arr[j]-arr[j+1]) == 1) and (arr[j] > arr[j+1])):
                    arr[j] , arr[j+1] = arr[j+1] , arr[j]
                    flag = 1
            if(flag == 0):
                sys.stdout.write('No')
                if(i < k-1):
                    sys.stdout.write('\n')
                tFlag = 0
                break







main()
