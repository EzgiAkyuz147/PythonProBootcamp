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
list=[rock, paper, scissors]
selection =random.choice(list)

humanchoise =input("What do you choose? Type '1' rock, Type '2' paper, Type '3' scissors\n")
if humanchoise == "1":
    print(humanchoise)
    print(rock)
    print(f"Computer chose:\n{selection}")
    if selection == rock:
        print("Draw")
    elif selection == paper:
        print("You lose")
    elif selection == scissors:
        print("You win")
elif humanchoise == "2":
    print(humanchoise)
    print(paper)
    print(f"Computer chose:\n{selection}")
    if selection == rock:
        print("You win")
    elif selection == paper:
        print("Draw")
    elif selection == scissors:
        print("You lose")
elif humanchoise == "3":
    print(humanchoise)
    print(scissors)
    print(f"Computer chose:\n{selection}")
    if selection == rock:
        print("You lose")
    elif selection == paper:
        print("You win")
    elif selection == scissors:
        print("Draw")