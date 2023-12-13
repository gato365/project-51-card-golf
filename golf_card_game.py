import random

# Constants for the suits and values
SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']



# Card class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

# Deck class
class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in SUITS for value in VALUES]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        card = deck.deal()
        if card:
            self.hand.append(card)
            return card
        return None

    # Add more methods for player actions, such as show_cards, swap_card, etc.

# Game class
class GolfGame:
    def __init__(self, players):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = [Player(name) for name in players]
        self.current_player_index = 0

    def start_game(self):
        # Deal 6 cards to each player
        for player in self.players:
            player.draw_hand(self.deck, 6)

    def take_turn(self):
        # Current player takes their turn
        current_player = self.players[self.current_player_index]
        print(f"It's {current_player.name}'s turn.")

        # Example turn logic (can be expanded with game rules)
        drawn_card = current_player.draw(self.deck)
        print(f"{current_player.name} drew {drawn_card}")

        # Example of moving to the next player
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_round(self):
        # Each player takes a turn
        for _ in range(len(self.players)):
            self.take_turn()

    # Additional methods for game logic, scoring, etc., can be added here
