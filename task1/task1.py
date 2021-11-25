n= int(input("Чисто массива: "))
m= int(input("Задайте длинну массива: "))
import itertools

#start to string
start_str=''.join(map(str,[it for it in range(1,n+1)]))
#get all perm
allresult=itertools.permutations(start_str, m)


def checking(sequence):
    for it in range(0,len(sequence)-1):
        if int(sequence[it])+1!=int(sequence[it+1]) :
            if sequence[it+1]=='1' and sequence[it]==str(n):
                continue
            return False
    return True

#drop wrong result
total_result=list(filter(checking,allresult))

print(total_result)
