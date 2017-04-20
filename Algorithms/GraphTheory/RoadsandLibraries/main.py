
# Link : https://www.hackerrank.com/challenges/torque-and-development


##########

import sys

# sys.stdin = open('test1.in','r')
# sys.stdout = open('test1.out','w')


########    Only 2 Test case passed .  Most are Time Out . 1 is incorrect


def main():
    test = int(sys.stdin.readline().rstrip())
    for t in range(test):
        keys = [ int(i) for i in sys.stdin.readline().rstrip().split()]
        edges = [[] for i in range(keys[0])]
        for k in range(keys[1]):
            temp = [int(i) for i in sys.stdin.readline().rstrip().split()]
            edges[temp[0]-1].append(temp[1]-1)
        st = []
        cost = keys[2]
        if(keys[2] > keys[3]):
            cost -= keys[3]
        else:
            cost -= keys[2]
        for i in range(len(edges)):
            if (len(st) == keys[0]):
                break
            if( i not in st):
                st.append(i)
                if(keys[2] > keys[3]):
                    cost += keys[3]
                else:
                    cost += keys[2]
            for j in range(len(edges[i])):
                if edges[i][j] not in st:
                    st.append(edges[i][j])
                    if(keys[2] > keys[3]):
                        cost += keys[3]
                    else:
                        cost += keys[2]
        sys.stdout.write(str(cost))
        if(t < test-1):
            sys.stdout.write('\n')





main()
