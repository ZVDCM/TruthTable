from prettytable import PrettyTable
from itertools import product

pt = PrettyTable()

# string = "((P AND Q) OR (NOT(P OR Q)))"

# string = "((not(p and q)) or (not(r or s)))"

print("Truth table".center(40, "="))
print("\n- not = ¬")
print("\n- and = ^")
print("\n- or = v")

print("\nExample input: \n ((not(p and q)) or (not(z and y)))")
string = input("\nEnter string: ")

if "(" in string:
    listString = list(filter(None, [i.strip() for i in eval("'" + string.replace("(", "', '").replace(")", "', '").rstrip("'"))]))

    getOrAnd = list(filter(None, [listString[i] if "and " in listString[i].lower() or "or " in listString[i].lower() else None for i in range(len(listString))]))

    getOrAnd.sort(key=len)

    sepGetOrAnd = [i.split() for i in getOrAnd]

    getNot = list(filter(None, [listString[i] + " " + listString[i + 1] if listString[i].lower() == "not" else None for i in range(len(listString))]))

    getNot.sort(key=len)

    sepGetNot = [i.split(" ", 1) for i in getNot]

    listChars = list(set((filter(None, [i if len(i) == 1 else "" for i in " ".join(listString).split(" ")]))))
    listChars.sort()

    listConditions = list(set(getOrAnd + getNot))
    listConditions.sort(key=len)

    truth_Table_Header = listChars + list(set(listConditions + [" ".join(listString)]))
    truth_Table_Header.sort(key=len)

    boolList = [list(i) for i in product([True, False], repeat=len(listChars))]

    for i in range(len(listString)):
        if listString[i].lower() == "not":
            listString[i] = listString[i] + " " + listString[i + 1]
            listString[i + 1] = ""

    listString = list(filter(None, listString))

    for i in range(len(listConditions)):
        if "or" in listConditions[i].lower() and "not" not in listConditions[i].lower():
            orVar = getOrAnd.index(listConditions[i])

            for j in range(len(sepGetOrAnd[orVar]) - 1):
                if sepGetOrAnd[orVar][j].lower() == "or":
                    charLeft = listChars.index(sepGetOrAnd[orVar][j - 1])
                    charRight = listChars.index(sepGetOrAnd[orVar][j + 1])

                    for k in range(len(boolList)):
                        if (boolList[k][charLeft], boolList[k][charRight]).count(True) >= 1:
                            boolList[k].append(True)
                        else:
                            boolList[k].append(False)

        elif "and" in listConditions[i].lower() and "not" not in listConditions[i].lower():
            andVar = getOrAnd.index(listConditions[i])

            for j in range(len(sepGetOrAnd[andVar]) - 1):
                if sepGetOrAnd[andVar][j].lower() == "and":
                    charLeft = listChars.index(sepGetOrAnd[andVar][j - 1])
                    charRight = listChars.index(sepGetOrAnd[andVar][j + 1])

                    for k in range(len(boolList)):
                        if (boolList[k][charLeft], boolList[k][charRight]).count(True) == 2:
                            boolList[k].append(True)
                        else:
                            boolList[k].append(False)

        elif "not" in listConditions[i].lower():

            notVar = getNot.index(listConditions[i])
            rightVar = truth_Table_Header.index(sepGetNot[notVar][1])

            for k in range(len(boolList)):
                if boolList[k][rightVar]:
                    boolList[k].append(False)
                else:
                    boolList[k].append(True)

    for i in range(len(listString) - 1):
        if "or" in listString[i].lower() and len(listString[i]) <= 3:
            leftVar = truth_Table_Header.index(listString[i - 1])
            rightVar = truth_Table_Header.index(listString[i + 1])

            for j in range(len(boolList)):
                if (boolList[j][leftVar], boolList[j][rightVar]).count(True) >= 1:
                    boolList[j].append(True)
                else:
                    boolList[j].append(False)

        if "and" in listString[i].lower() and len(listString[i]) <= 3:
            leftVar = truth_Table_Header.index(listString[i - 1])
            rightVar = truth_Table_Header.index(listString[i + 1])

            for j in range(len(boolList)):
                if (boolList[j][leftVar], boolList[j][rightVar]).count(True) == 2:
                    boolList[j].append(True)
                else:
                    boolList[j].append(False)

    pt.field_names = truth_Table_Header

    for i in boolList:
        pt.add_row(i)

    print(pt)

elif "and" in string.lower() or "or" in string.lower():

    listString = list(filter(None, eval("'" + string.replace(" ", "', '") + "'")))
    listChars = list(set(filter(None, [i if len(i) == 1 else "" for i in " ".join(listString).split(" ")])))
    listChars.sort()

    truth_Table_Header = listChars + [" ".join(listString)]

    boolList = [list(i) for i in product([True, False], repeat=len(listChars))]

    for i in range(len(listString) - 1):
        if "and" in listString[i].lower():

            leftVar = listChars.index(listString[i - 1])
            rightVar = listChars.index(listString[i + 1])

            for j in range(len(boolList)):
                if (boolList[j][leftVar], boolList[j][rightVar]).count(True) == 2:
                    boolList[j].append(True)
                else:
                    boolList[j].append(False)

        elif "or" in listString[i].lower():

            leftVar = listChars.index(listString[i - 1])
            rightVar = listChars.index(listString[i + 1])

            for j in range(len(boolList)):
                if (boolList[j][leftVar], boolList[j][rightVar]).count(True) >= 1:
                    boolList[j].append(True)
                else:
                    boolList[j].append(False)

    pt.field_names = truth_Table_Header

    for i in boolList:
        pt.add_row(i)

    print(pt)

else:

    boolList = [list(i) for i in product([True, False], repeat=len(string))]

    pt.field_names = list(string)
    for i in boolList:
        pt.add_row(i)

    print(pt)
