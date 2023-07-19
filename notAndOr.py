from prettytable import PrettyTable

pt = PrettyTable()

'''

not = negation
    - T = F
    - F = T

and = ^
    - T T = T
    - T F = F
    - F T = F
    - F F = F

or = v
   - T F = T
   - F T = T
   - T T = T
   - F F = F

'''

boolList = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

'''

0 - True
1 - False

'''

# AND

# for i in range(len(boolList)):
#     if boolList[i].count(0) == 2:
#         boolList[i].append(0)
#     else:
#         boolList[i].append(1)
#
#
# for i in boolList:
#     print(i)

# OR

# for i in range(len(boolList)):
#     if boolList[i].count(0) >= 1:
#         boolList[i].append(0)
#     else:
#         boolList[i].append(1)
#
# for i in boolList:
#     print(i)

listvar = ["p", "q", "p and q", "p or q", "not p or q", "p and q or not p or q"]

# p and q
for i in range(len(boolList)):
    if boolList[i].count(0) == 2:
        boolList[i].append(0)
    else:
        boolList[i].append(1)

# p or q
for i in range(len(boolList)):
    if boolList[i][:2].count(0) >= 1:
        boolList[i].append(0)
    else:
        boolList[i].append(1)

# not p or q
for i in range(len(boolList)):
    if boolList[i][-1] == 0:
        boolList[i].append(1)
    else:
        boolList[i].append(0)

# p and q or not p and q
for i in range(len(boolList)):
    if boolList[i][2:].count(0) <= 2:
        boolList[i].append(0)
    else:
        boolList[i].append(1)

pt.field_names = listvar

for i in range(len(boolList)):
    for j in range(len(boolList[i])):
        if boolList[i][j] == 0:
            boolList[i][j] = True
        else:
            boolList[i][j] = False

for i in boolList:
    pt.add_row(i)

print("((P AND Q) OR (NOT(P OR Q)))".center(73, "="))
print(pt)
