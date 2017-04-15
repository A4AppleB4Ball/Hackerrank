
# Problem Link : https://www.hackerrank.com/contests/hourrank-19/challenges/what-are-the-odds


import sys

sys.stdin = open('test1.in','r')
sys.stdout = open('test1.out','w')




def main():
    data = [int(i) for i in sys.stdin.readlines()[1].rstrip().split(' ')]
    i=0
    count = 0
    while i<len(data):
        i += data[i] + 1
        count += 1
    sys.stdout.write(str(count))

main()
