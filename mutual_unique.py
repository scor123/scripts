"""
Write a function named common. It takes in two
parameters, lists named L1 and L2. The function doesn’t
mutate L1 or L2. It returns True if every unique element
in L1 is in L2 and if every unique element in L2 is in L1.
It returns False otherwise. Hint: try to reuse your
function from Q25.2. For example,
common([1,2,3], [3,1,2]) returns True
common([1,1,1], [1]) returns True
common([1], [1, 2]) returns False
"""

def uniqu(L1):
    uni=[]
    if len(L1) == 1:
        uni.append(L1[0])
        return uni
    for i in range(len(L1)):
        if L1[i] in L1[i+1:]:
            pass
        elif  L1[i] in L1[:i]:
            uni.append(L1[i])
            pass
        else:
                uni.append(L1[i])


    return uni

l1=[1,2,3]
L1=uniqu(l1)
l2=[3,1,2]
L2=uniqu(l2)
print(L1)
print(L2)


def comm(L1,L2):
    trues=[]
    if len(L1)!=len(L2):
        return False
    else:
        for i in L1:
            if i not in L2:
                return False
            else:
                for j in L2:
                    if j not in L1:
                        return False

                    else:
                        trues.append(True)
    for i in range(len(trues)):
        if trues[i] == False:
            return False
        else:
            return True


print(comm(L1,L2))
