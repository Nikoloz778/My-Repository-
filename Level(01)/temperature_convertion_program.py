#Temperature convertion program

unit=input("Is this temperature in Celcius or Farenheit(F/C): ")
temperature=int(input("enter temperature: "))

if unit == "F":
    temperature=round((temperature*9)/5+32,1)
    print(f"this temperature in Celciuses is {temperature}")
elif unit == "C":
    temperature=round((temperature-32)*5/9)
    print(f"this temperature in Farenheits is {temperature}")
else:
    print("one of values are not correct.")