import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images =[rock, paper, scissors]
userChoice = input("What do you choose? Type 0 for rock, 1 for paper, and 2 for sicssors")
computerChoice = random.randint(0, len(images)-1)
print(computerChoice,userChoice)
print(images[userChoice])
print("computer chose: ")
print()
if userChoice == 0:
    if computerChoice == 0:
        print("Draw")
    elif computerChoice == 1:
        print("Loose")
    elif computerChoice == 2:
        print("Win")
if userChoice == 1:
    if computerChoice == 0:
        print("Win")
    elif computerChoice == 1:
        print("Draw")
