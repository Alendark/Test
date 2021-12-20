f1 = open('file_1.txt', 'r')
l1 = f1.read()
n = int(l1)

f2 = open('file_2.txt', 'r')
l2 = f2.read()
m = int(l2)

import itertools

start_str=''.join(map(str,[it for it in range(1,n+1)]))

allresult=itertools.permutations(start_str, m)


def checking(seq):
    for it in range(0,len(seq)-1):
        if int(seq[it])+1!=int(seq[it+1]) :
            if seq[it+1]=='1' and seq[it]==str(n):
                continue
            return False
    return True


total_result=list(filter(checking,allresult))

print(total_result)
