import os
import random

def clear_console():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to blackjack!")
player_name = input("What's your name player? \n")
print("Ok {name}, here are the instructions:".format(name=player_name))
print("You will have 100 chips and the house will have 500 chips.")
input("Press Enter to continue...")
clear_console()
print("I will give you 2 cards, and you will be able to see one of my cards.")
print("Cards 2 to 10 has the same value as the number in the card.")
print("J, Q and K cards have a value of ten, and A has a value of 1 or 11 (depending of your convenience).")
input("Press Enter to continue...")
clear_console()
print("If you have both of your cards with the same value (for example K and K)")
print("You will be able to split your hand, so you can play with both hands,")
print("however, you will have to pay double for double chances of winning.")
input("Press Enter to continue...")
clear_console()
print("Your goal is to get closer to 21, you can ask for more cards")
print("but if you have more than 21, you loose!")
clear_console()

response = ""

playing_cards = {
  "A" : [1, 11],
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "10": 10,
  "J": 10,
  "Q": 10,
  "K": 10,
}

playing_cards_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class Game:
  house_hand = []
  house_balance = 500
  total = 0

  def start_game(self):
    card_1 = random.choice(playing_cards_list)
    card_2 = random.choice(playing_cards_list)
    self.house_hand = [card_1, card_2]
    print("The house is showing a " + self.house_hand[0] + "card")

  def describe_game(self):
    self.start_game()
    print("Current house hand is: ")
    for card in self.house_hand:
      print(card + " card.")
      self.total += playing_cards[card]
    print("Total is: " + str(self.total))

  def pick_card(self):
    if self.total == 21:
      print("The house got 21! You loose")
    if self.total >= 17:
      self.end_game()


  def stay(self):
    self.describe_game()

  def end_game(self, player):
    if player.total <= self.total:
      print("You loose!")
      print("House total: {total}".format(total=self.total))
      print("Your total: {total}".format(total=player.total))
    else:
      print("You win!")
      print("House total: {total}".format(total=self.total))
      print("Your total: {total}".format(total=player.total))

    self.total = 0


class Player:
  name = player_name
  balance = 100
  current_bet = 0
  current_hand = []
  current_round = 0
  splitted_hand = False
  total = 0

  def bet(self):
    while True:
      try:
        amount = int(input("How much would you like to bet? \n"))
        if amount > self.balance:
            print("Sorry, you don't have enough balance. Your balance is", self.balance)
        else:
            break  # If input is successfully converted to an integer and does not exceed the balance, exit the loop
      except ValueError:
        print("Please enter a valid integer.")
    self.current_bet = amount
    self.balance -= amount
    print("If you loose this game your balance will be: {balance}".format(balance = self.balance))
    

  def play_a_game(self):
    card_1 = random.choice(playing_cards_list)
    card_2 = random.choice(playing_cards_list)
    self.current_hand = [card_1, card_2]

  def prompt_player(self, game):
    choice = ""
    while self.total < 21 and choice != "0":
      print("TOTAL:::::::::::::::::::::::::::::::::::::::::: " + str(self.total))
      print("What would you like to do next?")
      if self.current_round == 0 and (self.current_hand[0] == self.current_hand[1]):
        choice = input("""
        1. Ask another card
        2. Stay with this hand
        3. Split hand
        0. Exit
        """)
      else:
        choice = input("""
        1. Ask another card
        2. Stay with this hand
        0. Exit
        """)

        if choice == "1":
          card = random.choice(playing_cards_list)
          self.current_hand.append(card)
          self.describe_game()

        elif choice == "2":
          game.stay()
      
        elif choice == "3":
          pass
        
        elif choice == "0":
          print("Your balance was: " + str(self.balance))
          print("Goodbye!")
      
    

  def describe_game(self):
    clear_console()
    self.total = 0
    for card in self.current_hand:
      if card == "A":
        if self.total + 11 > 21:
          self.total += 1
        else:
          self.total += 11
      else:
        self.total += playing_cards[card]
      
      print("You have a " + card + " card")
    
    print("Total of your hand is: " + str(self.total))
    return self.total
  
  def stay(self, game):
    self.describe_game()

  
  def round_check(self, game):
    total = self.describe_game()
    if total > 21:
      print("You loose this round!")
    else:
      self.prompt_player(game)

  def win_a_game(self):
    self.balance += self.current_bet * 2
    print("You win, your new balance is: " + str(self.balance) + " chips")

  def loose_a_game(self):
    print("You loose, your balance is: " + str(self.balance) + " chips")

game_1 = Game()
player_1 = Player()
player_1.bet()
player_1.play_a_game()
player_1.round_check(game_1)