name=input("What is your name: ")
score=int(input("enter your score: "))
time=int(input("enter time(in minutes!): "))

if time > 120 and score < 20:
    print(f"{name}you faild the test.")
elif time < 120 and score > 20:
    print(f"{name}, you passed the test!") 