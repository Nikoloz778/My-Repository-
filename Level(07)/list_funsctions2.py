foods=["hamburger","pizza","coca cola"]
prices=[]
total=0
hamburger=5.99
pizza=6.90
coca_cola= 2

while True:
    food=input("What you want to buy?(enter q to exit if you want to remove ane product just write product name and minus.) ")
    if food.lower()=="q":
        break
    elif food == "hamburger":
        total+=hamburger
        print(f"price: {total}%")
    elif food == "pizza":
        total+=pizza
        print(f"price: {total}$")
    elif food == "coca cola":
        total+=coca_cola
        print(f"price: {total}$")
    elif food == "hamburger-":
        total-=hamburger
        print(f"price: {total}$")
        print(f"food was removed ")
    elif food == "pizza-":
        total-=pizza
        print(f"price: {total}$")
        print(f"{food} was removed.")
    elif food == "coca cola-":
        total-=coca_cola
        print(f"price: {total}")
        print(f"{food} was removed.")
    elif food == foods + "-" and total==0:
        print("you havnt orgered yet")
print("Thanks for using our platform. Have a good day!")
print("you will get your food in minutes")
