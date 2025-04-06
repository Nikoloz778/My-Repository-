a=50
b=60
print(pow(a-b,2) if a>b else pow(b-a,2))

age=int(input("how old are you? "))
print("you can get in" if age > 18 else "you are too young to get in")