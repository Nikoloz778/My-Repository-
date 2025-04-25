name=input("Enter you name here: ")
length=len(name)
digits_spaces=name.isalpha()

if length < 12 and digits_spaces == True:
    print("correct")
else:
    print("it have to contain only alphabets and it must not have spaces.")

