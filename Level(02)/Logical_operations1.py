name=input("What is your name? ")
temp=int(input("what temperature is outside? "))
sunny_or_not=input("Is sunny outside?(yes/no) ")

if 30 > temp > 20 and sunny_or_not == "yes":
    print(f"{name}, there is warm outside!")
elif 10 <temp < 20 and sunny_or_not == "no":
    print(f"{name}, there is cold outside!")
elif 30 < temp and sunny_or_not == "yes":
    print(f"{name}! there is burning everything outside!!")
elif temp < 10 and sunny_or_not == "no":
    print(f"{name}! there is freezing everything outside!!")


