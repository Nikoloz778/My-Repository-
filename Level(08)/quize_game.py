questions=("Who was a ruler in Georgia at that time?(Didostatis Kosntantines Marjvena)",
           "Who loved Shorena? (Didostatis Konstantiens Marjvena)",
           "From where was konstantine?(Didostati Konstantines Marjvena)")

options=(("A. Vakhtang Gorgasali","B. David IV", "C. George I", "D. Bagrat Kurapalat"),
         ("A. king Giorgi ","B. Konstantine arsakidze", "C, Farsman sparsi", "D. Amrosi"),
         ("A. lazeti","B. Fxovi", "C. Mtskheta", "D. Javaxeti"))
answers=("C","B","A")
guesses=[]
score = 0
question_num = 0

for question in questions:
    print("----------------------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess=input("Enter your answer(A B C D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is a correct answer.")
    question_num+=1


print("answers: ",end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score= int(score/len(questions)*100)
print(f"you gussed {score}% !")