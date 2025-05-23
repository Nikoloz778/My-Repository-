rows=int(input("enter number of rows: "))
columns=int(input("enter number of columns: "))
symbol=input("Enter a symbol: ")


for i in range(rows):
    for x in range(columns):
        print(symbol, end=" ")
    print()
  