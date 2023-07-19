string = "((P AND Q) OR (NOT(P OR Q)))"

if "(" in string:
    listString = list(filter(None, [i.strip() for i in eval("'" + string.replace("(", "', '").replace(")", "', '").rstrip("'"))]))
    getOrAnd = list(filter(None, [listString[i] if "and " in listString[i].lower() or "or " in listString[i].lower() else None for i in range(len(listString))]))
    sepGetOrAnd = [i.split() for i in getOrAnd]
    getNot = list(filter(None, [listString[i]+ " " + listString[i + 1] if listString[i].lower() == "not" else None for i in range(len(listString))]))
    sepGetNot = getNot[0].split(" ", 1)
    listChars = list(set((filter(None, [i if len(i) == 1 else "" for i in " ".join(listString).split(" ")]))))
    listChars.sort()
    listConditions = list(set(getOrAnd + getNot))
    listConditions.sort(key=len)
    truth_Table_Header = listChars + getOrAnd + getNot + [" ".join(listString)]

    for i in range(len(listString)-1):
        if listString[i].lower() == "not":
            listString[i] = listString[i]+ " " +listString[i + 1]
            listString.remove(listString[i+1])

    print(listString)
    print(listChars)
    print(getOrAnd)
    print(sepGetOrAnd)
    print(getNot)
    print(sepGetNot)
    print(listConditions)
    print([" ".join(listString)])
    print(truth_Table_Header)

else:
    listString = list(filter(None, eval("'" + string.replace(" ", "', '") + "'")))
    listChars = list(set(filter(None, [i if len(i) == 1 else "" for i in " ".join(listString).split(" ")])))
    listChars.sort()

    print(listChars)
    print(listString)
