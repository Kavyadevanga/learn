playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okay! Let's Play: ")

score = 0

answer = input("CPU stands for: ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("GPU stands for: ")
if answer.lower() == "Graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("RAM stands for: ")
if answer.lower() == "Random Access Memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 3) * 100) + "%")