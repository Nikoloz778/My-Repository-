user_age= int(input("Enter your age: "))

while user_age <1 or user_age >10:
    print(f"{user_age} is not valid.")
    user_age=int(input("here is your second chance:"))
print("very good this is better.")
