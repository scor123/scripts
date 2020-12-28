"""


Write a function named invert_dict that takes as input
a dictionary. The function returns a new dictionary; the
values are now the original keys, and the keys are now the
original values. Assume that the values of the input
dictionary are immutable and unique.
"""


def invert_dict(d):
    dic1={}
    for i in d.keys():
         dic1[d[i]] =i
    return dic1




dic={"first":1,"second":2,"third":3,"fource":4}
print(invert_dict(dic))