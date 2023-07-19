from prettytable import PrettyTable

characters = input("Enter Strings: ")

listBool = [[True if j == "0" else False for j in bin(i)[2:].zfill(len(bin(2 ** len(characters))[2:]) - 1)] for i in
            range(2 ** len(characters))]

pTable = PrettyTable()

pTable.field_names = list(characters)

while True:

    try:

        for i in range(len(listBool)):
            pTable.add_row(listBool[i])

        print(pTable)

        break

    except Exception:

        print("!Field header must be unique!")
