from random import randint
s=input("Hello! What is your name?\n")
print("Well, " +s+ ", I am thinking of a number between 1 and 20.")
answer=randint(1,20)
cnt=0
while(True):
    a=int(input("Take a guess.\n"))
    if answer == a:
        print(f"Good job, KBTU! You guessed my number in {cnt} guesses!")
        break
    elif answer>a:
        cnt=cnt+1
        print("Your guess is too low.")
    elif answer < a:
        cnt=cnt+1
        print("Your guess is too big.")