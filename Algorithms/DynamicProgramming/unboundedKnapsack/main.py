from copy import deepcopy
# Link : https://www.hackerrank.com/challenges/unbounded-knapsack


##########    Time Out   O(2^n) Algo   Not Optimal   Not Correct

import sys

# sys.stdin = open('test1.in','r')
# sys.stdout = open('test1.out','w')


def MaxSumRec(data , s ):
    # print(data , s)
    if data == []:
        return 0
    elif s == 0:
        return 0
    else:
        if s % data[0] == 0:
            return s
        else:
            i = s // data[0]
            k = s - (data[0] * i)
            del data[0]
            return max( (s-k + MaxSumRec(deepcopy(data), k )), MaxSumRec(deepcopy(data), s ) )



def main():
    t = int(sys.stdin.readline().rstrip())
    for k in range(t):
        s = [int(i) for i in sys.stdin.readline().rstrip().split(' ')]
        data = [int(i) for i in sys.stdin.readline().rstrip().split(' ')]
        a = list(set(data))
        a.sort()
        a.reverse()
        # sys.stdout.write(str(a))
        maxSum = MaxSumRec(a,s[1])
        sys.stdout.write(str(int(maxSum)))
        if k < t-1:
            sys.stdout.write("\n")



main()
