#weight converter program 

weight=int(input("enter your weight(just numbers): "))
unit=input("kilograms or pounds(K/L): ")

if unit == "K":
    weight=weight*2.205
    print(f"you are {round(weight, 3)}Lbs! ")
elif unit == "L":
    weight=weight/2.205
    print(f"you are {round(weight, 3)}kgs! ")
else:
    print(" one of values are not valid!")