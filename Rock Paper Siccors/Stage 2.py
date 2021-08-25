import random
my_choose = input()
lists = ['rock', 'paper', 'scissors']
bot_choose = random.choice(lists)

if my_choose == 'paper' and  bot_choose == 'scissors':
    print("Sorry, but the computer chose scissors")
if my_choose == 'scissors' and bot_choose == 'rock':
    print("Sorry, but the computer chose rock")
if my_choose == 'rock' and bot_choose == 'paper':
    print("Sorry, but the computer chose paper")

if my_choose == 'paper' and bot_choose == 'rock':
    print("Well done. The computer chose rock and failed")
if my_choose == 'scissors' and bot_choose == 'paper':
    print("Well done. The computer chose paper and failed")
if my_choose == 'rock' and bot_choose == 'scissors':
    print("Well done. The computer chose scissors and failed")

if my_choose == bot_choose:
    print(f"There is a draw ({my_choose})")
