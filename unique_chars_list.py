"""
Write a function named unique. It takes in one
parameter, a list named L. The function doesn’t mutate L
and returns a new list containing only the unique elements
in L.
"""


def uniqu(L1):
    uni=[]
    for i in range(len(L1)):
        if L1[i] in L1[i+1:]:
            pass
        elif  L1[i] in L1[:i]:
            pass
        else:
                uni.append(L1[i])


    return uni

l=[1,1,8,2,2]
print(l)
print(uniqu(l))