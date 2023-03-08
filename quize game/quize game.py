print ("welcome to my game")
playing = input("do you want to play the game? ").lower()
if playing != "yes":
    quit()

print ("lets play the game :)")
score = 0

answer = input("what is CPU stand for? ")
if answer.lower() == "central processing unit":
    print ("correct")
    score += 1
else:
    print ("incrrect")

answer = input("what is RAM stand for? ")
if answer.lower() == "random access memory":
    print ("correct")
    score += 1
else:
    print ("incrrect")

answer = input("what is ROM stand for? ")
if answer.lower() == "read only memory":
    print ("correct")
    score += 1
else:
    print ("incrrect")

print("you got correct " + str(score) + " out of three question")
print("you got " + str((score/4) * 100) + "%")
    