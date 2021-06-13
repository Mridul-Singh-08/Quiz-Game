print("Welcome to The Quiz")

playing = input("do you want to play, Yes/No? ")

if playing.lower() != "yes":
    quit()

print("Let's Start the Game!")
score = 0



answer = input("QUE[1] What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1
else:
    print("Incorrect!")

answer = input("QUE[2] What does BFT stand for? ")
if answer.lower() == "breadth first traversal":
    print("correct")
    score += 1
else:
    print("Incorrect!")

answer = input("QUE[3] Which is a programming language for creating special programs like applets? ")
if answer.lower() == "java":
    print("correct")
    score += 1
else:
    print("Incorrect!")

answer = input("QUE[4] The set of instructions which tell a computer what to do is called? ")
if answer.lower() == "program":
    print("correct")
    score += 1
else:
    print("Incorrect!")

answer = input("QUE[5] LAN stands for? ")
if answer.lower() == "local area network":
    print("correct")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct.")
print("You got " + str(( (score / 5 ) * 100 )) + " %")