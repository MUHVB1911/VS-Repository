print("hello whats your name")
name = input("enter your name: ")
print("hello " + name)
print("what is your age (the game is +5)")
age = int(input("enter your age: "))
if age < 5:
    print("you are too young to play")
elif age > 100:
    print("you are too old to play")
else:
    print("you can play the game")
print("______________________________________________________________________________")
print("what is the capital of egypt?")
answer = input("enter your answer: ")
if answer.lower() == "cairo":
    print("correct +1")
else:
    print("wrong -1")
print("______________________________________________________________________________")
print("what is the capital of saudi arabia?")
answer = input("enter your answer: ")
if answer.lower() == "riyadh":
    print("correct +1")
else:
    print("wrong -1")
print("______________________________________________________________________________")
print("what is age of ZAMALEK?")
answer = input("enter your answer: ")
if answer == "115":
    print("correct +1")
else:
    print("wrong -1")
print("______________________________________________________________________________")
print("what is the capital of france?")
answer = input("enter your answer: ")
if answer.lower() == "paris":
    print("correct +1")
else:
    print("wrong -1")
print("______________________________________________________________________________")
print("what is the capital of spain?")
answer = input("enter your answer: ")
if answer.lower() == "madrid":
    print("correct +1")
else:
    print("wrong -1")
print("______________________________________________________________________________")
