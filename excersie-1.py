# Python quiz game

questions=("which country is the biggest in earth?: ",
           "what is the most using coding language?: ",
           "how many bones are in the human budy?: ",
           "which planet is the biggest in our solor system?: ",
           "What is the easy coding language?: ")
options=(('A. Canada', 'B. Australia', 'C. USA', 'D. Russia'),
         ('A. Python', 'B. C/C++', 'C. Javascript', "D. Java"),
         ('A. 207', 'B. 204', 'C. 206', 'D. 209'),
         ('A. Mars', 'B. Venera', 'C. saturan', 'D. Earth'),
         ('A. C/C++', 'B. Python', 'C. Java', 'D. javascript'))

answers=('D','A','C','C','B')
guesses=[]
scores=0
question_num=0

for question in questions:
    print('-'*30)
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess=input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        scores+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num+=1
    
print("Answers: ",end='')
for asnwer in answers:
    print(asnwer, end=" ")
print()

print("guess: ",end='')
for guess in guesses:
    print(guess, end=" ")
print()

score=int(scores/len(questions)*100)
print(f"Your score is the {score}%")