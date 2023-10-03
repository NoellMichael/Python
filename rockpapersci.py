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

import random

images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors!"))
print(images[user_choice])
computer_choice = random.randint(0, 2)
print(f"computer chose: {computer_choice}")
print(images[computer_choice])
if computer_choice > user_choice:
    print("you lose!")
elif computer_choice == user_choice:
    print("its a tie!")
else:
    print("you win")