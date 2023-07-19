from prettytable import PrettyTable

x = PrettyTable()

def getChars(str):
    listChars = list(str)

    return listChars


def createCharsBoolList(lst):
    n = 2 ** len(lst)

    half = int(len(lst) / 2)

    boolList = [[True if (x // (2 ** (len(lst) - 1 - y))) % 2 != 1 else False for x in range(n)] for y in
                range(len(lst))]

    return boolList

while True:

    string = input("Enter string: ")

    try:

        x.field_names = getChars(string)

        newList = [
            [createCharsBoolList(getChars(string))[j][i] for j in range(len(createCharsBoolList(getChars(string))))] for
            i in range(len(createCharsBoolList(getChars(string))[0]))]

        for i in newList:
            x.add_row(i)

        print(x)
        break

    except Exception:

        print("\n!Field names must be unique!\n")




