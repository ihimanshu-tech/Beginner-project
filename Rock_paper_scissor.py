echo "# Beginner-project" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ihimanshu-tech/Beginner-project.git
git push -u origin main

'''-1 for stone 
0 for paper
1 for scissor
'''
import random

c = random.choice([-1, 0, 1])
youstr = input("Enter your Choice (s for Stone, p for Paper, k for Scissor): ")
youdict = {"s": -1, "p": 0, "k": 1}
revdict = {-1: "Stone", 0: "Paper", 1: "Scissor"}

if youstr in youdict:
    you = youdict[youstr]
    print(f"You Chose: {revdict[you]} \nComputer Chose: {revdict[c]}")
    
    if c == you:
        print("Draw")
    elif (you == -1 and c == 1) or (you == 0 and c == -1) or (you == 1 and c == 0):
        print("You Win")
    else:
        print("You Lose")
else:
    print("Invalid input! Please enter 's' for Stone, 'p' for Paper, or 'k' for Scissor.")
