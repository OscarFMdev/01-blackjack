import os

def clear_console():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')


print("Welcome to blackjack!")
player_name = input("What's your name player? \n")
print("Ok {name}, here are the instructions:".format(name=player_name))
input("Press Enter to continue...")
clear_console()
print("You will have 100 chips and the house will have 500 chips.")
input("Press Enter to continue...")
clear_console()
print("I will give you 2 cards, and you will be able to see one of my cards.")
input("Press Enter to continue...")
clear_console()
print("Cards 2 to 10 has the same value as the number in the card.")
input("Press Enter to continue...")
clear_console()
print("J, Q and K cards have a value of ten, and A has a value of 1 or 11 (depending of your convenience).")
input("Press Enter to continue...")
clear_console()
print("If you have both of your cards with the same value (for example K and K)")
input("Press Enter to continue...")
clear_console()
print("You will be able to split your hand, so you can play with both hands,")
input("Press Enter to continue...")
clear_console()
print("however, you will have to pay double for double chances of winning.")
input("Press Enter to continue...")
clear_console()
print("Your goal is to get closer to 21, you can ask for more cards")
print("but if you have more than 21, you loose!")

response = ""

while response != "stop":
  response = input("Say something... ")