


"""
This is simple mashing game
"""


nam1_first = input("Enter the name1_first")
nam1_last = input("Enter the name1_last")
end=len(nam1_first)//2

nam2_first = input("Enter the name2_first")
nam2_last = input("Enter the name2_last")
if len(nam1_first)%2 == 0:
     end=len(nam1_first)//2
     nam1_first_half = nam1_first[0:end]
else:
     end= int(len(nam1_first)/2)
     nam1_first_half = nam1_first[0:end]

if len(nam1_last) % 2 == 0:
     nam1_last_half = nam1_last[0:len(nam1_last) // 2]
else:
     nam1_last_half = nam1_last[0:len(nam1_last) // 2]


if len(nam2_first)%2 == 0:
     end=len(nam2_first)//2
     nam2_first_half = nam2_first[end:]
else:
     end= int(len(nam2_first)//2)
     nam2_first_half = nam2_first[end:]

if len(nam2_last) % 2 == 0:
     nam2_last_half = nam2_last[len(nam2_last) // 2:]
else:
     nam2_last_half = nam2_last[len(nam2_last) // 2:]
mash1 = nam1_first_half +nam2_first_half
mash2= nam1_last_half + nam2_last_half
print(mash1)
print(mash2)
