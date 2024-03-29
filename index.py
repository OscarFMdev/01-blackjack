import os
import random

def clear_console():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

def enter_continue():
    input("Press Enter to continue...")
    clear_console()

print("Welcome to blackjack!")
player_name = input("What's your name player? \n")
if player_name == "":
    player_name = "Stranger"
print("Ok {name}, here are the instructions:".format(name=player_name))
print("You will have 100 chips and the house will have 500 chips.")
enter_continue()
print("I will give you 2 cards, and you will be able to see one of my cards.")
print("Cards 2 to 10 have the same value as the number in the card.")
print("J, Q, and K cards have a value of ten, and A has a value of 1 or 11 (depending on your convenience).")
enter_continue()
print("If you have both of your cards with the same value (for example K and K),")
print("You will be able to split your hand, so you can play with both hands,")
print("however, you will have to pay double for double chances of winning.")
enter_continue()
print("Your goal is to get closer to 21; you can ask for more cards,")
print("but if you have more than 21, you lose!")
clear_console()

response = ""

playing_cards = {
    "A": [1, 11],
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

cards_array = []

def restart_deck():
    global cards_array
    playing_cards_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cards_array = playing_cards_list * 4

def pick_a_card():
    global cards_array
    card = random.choice(cards_array)
    cards_array.remove(card)
    print("Picked card:", card)
    return card

class Game:
    house_hand = []
    house_balance = 500
    total = 0

    def start_game(self):
        restart_deck()
        card_1 = pick_a_card()
        card_2 = pick_a_card()
        self.house_hand = [card_1, card_2]
        self.show_card()

    def describe_game(self):
        clear_console()
        self.total = 0
        self.start_game()
        print("Current house hand is: ")
        for card in self.house_hand:
            print(card + " card.")
            if "A" in self.house_hand:
                if self.total + 11 > 21:
                    self.total += 1
                else:
                    self.total += 11
            else:
                self.total += playing_cards[card]
        print("Total is: " + str(self.total))

    def pick_card(self, player):
        random_card = pick_a_card()
        self.house_hand.append(random_card)
        self.describe_game()
        if self.total == 21:
            print("The house got 21! You lose")
        if self.total >= 17:
            self.end_round(player)

    def stay(self, player):
        self.describe_game()
        while self.total < 17:
            self.pick_card(player)

    def end_round(self, player):
        if player.total <= self.total:
            print("You lose!")
            print("House total: {total}".format(total=self.total))
            print("Your total: {total}".format(total=player.total))
            player.loose_a_round(self)
        else:
            print("You win!")
            print("House total: {total}".format(total=self.total))
            print("Your total: {total}".format(total=player.total))
            player.win_a_round(self)

        self.total = 0

    def show_card(self):
        print("The house is showing a " + self.house_hand[0] + " card")

class Player:
    def __init__(self):
        self.name = player_name
        self.balance = 100
        self.current_bet = 0
        self.current_hand = []
        self.current_round = 0
        self.splitted_hand = False
        self.total = 0

    def bet(self):
        while True:
            try:
                amount = int(input("How much would you like to bet? \n"))
                if amount > self.balance:
                    print("Sorry, you don't have enough balance. Your balance is", self.balance)
                else:
                    break
            except ValueError:
                print("Please enter a valid integer.")
        self.current_bet = amount
        self.balance -= amount
        print("If you lose this game your balance will be: {balance}".format(balance=self.balance))

    def play_a_game(self, game):
        game.start_game()
        card_1 = pick_a_card()
        card_2 = pick_a_card()
        self.current_hand = [card_1, card_2]
        if self.blackjack(game):
            self.win_a_round(game)

    def blackjack(self, game):
        face_cards = {"K", "Q", "J", "10"}
        if "A" in self.current_hand and face_cards.intersection(set(self.current_hand)):
            return True

    def prompt_player(self, game):
        choice = ""
        while self.total < 21 and choice != "0":
            game.show_card()
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
                card = pick_a_card()
                self.current_hand.append(card)
                self.describe_game()

            elif choice == "2":
                game.stay(self)

            elif choice == "3":
                self.split_hand_game()
                self.splitted_hand = True

            elif choice == "0":
                print("Your balance was: " + str(self.balance))
                print("Goodbye!")

            if self.total > 21:
                print("You lose this round")
                self.loose_a_round(game)

            if self.total == 21:
                print("You win this round")
                self.win_a_round(game)

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

    def stay(self, player):
      self.describe_game()
      while self.total < 17:
          self.pick_card(player)
      
      # Check if the house total is less than the player total
      if self.total <= player.total:
          self.end_round(player)
      else:
          print("The house stays with a total of", self.total)
          if self.total == player.total:
              print("It's a tie!")
          else:
              print("You win!")
              player.win_a_round(self)

    def round_check(self, game):
        total = self.describe_game()
        if total > 21:
            print("You lose this round!")
        else:
            self.prompt_player(game)

    def win_a_round(self, game):
        enter_continue()
        self.balance += self.current_bet * 2
        game.house_balance -= self.current_bet
        if self.blackjack(game):
            print("{card1} and {card2} YOU HAVE BLACKJACK!!!".format(card1=self.current_hand[0], card2=self.current_hand[1]))
        print("You win, your new balance is: " + str(self.balance) + " chips.")
        print("House balance is: " + str(game.house_balance) + " chips.")
        if game.house_balance > 0:
            self.bet()
            self.play_a_game(game)
            self.round_check(game)
        else:
            self.victory()

    def loose_a_round(self, game):
        enter_continue()
        game.house_balance += self.current_bet
        print("You lose, your balance is: " + str(self.balance) + " chips.")
        print("House balance is: " + str(game.house_balance) + " chips.")
        if self.balance > 0:
            self.bet()
            self.play_a_game(game)
            self.round_check(game)
        else:
            self.defeat()

    def victory(self):
        print("Very well played!")
        print("You have defeated the house (even when the House always wins...)")
        print("Your balance is: {balance}".format(balance=self.balance))
        print("Goodbye!")
        exit()

    def defeat(self):
        print("You have been defeated by the house!")
        print("Try again!")
        exit()

    def can_split_hand_check(self):
        return (self.balance - self.current_bet) >= 0

    def split_hand_game(self):
        if not self.can_split_hand_check():
            print("You can't split your hand, not enough chips")
        else:
            print("You decided to split your hand")
            print("You will get 2 hands")
            print("Let's start your first game:")
            print("Your first card is {card}".format(card=self.current_hand[0]))
            print("You receive a {card}".format(card=pick_a_card()))
            print("Your second card is {card}".format(card=self.current_hand[1]))
            print("You receive a {card}".format(card=pick_a_card()))


game_1 = Game()
player_1 = Player()

player_1.bet()
player_1.play_a_game(game_1)
player_1.round_check(game_1)
