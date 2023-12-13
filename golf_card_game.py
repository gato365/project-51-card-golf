import random

# Constants for the suits and values
SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']



# Card class
class Card:
    VALID_SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    VALID_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, value):
        if suit not in self.VALID_SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        if value not in self.VALID_VALUES:
            raise ValueError(f"Invalid value: {value}")

        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


# Deck class
class Deck:
    def __init__(self):
        SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, value) for suit in SUITS for value in VALUES]

    def shuffle(self):
        random.shuffle(self.cards)
        
    def count(self):
        return len(self.cards)
    
    def deal(self):
        if self.count() == 0:
            raise ValueError("Cannot deal from an empty deck")
        return self.cards.pop(0)

    def replenish(self, discard_pile):
        self.cards.extend(discard_pile)
        discard_pile.clear()
        self.shuffle()
    
    

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

    def show_cards(self):
        return self.hand

    def discard(self, card, deck):
        if card in self.hand:
            self.hand.remove(card)
            deck.replenish([card])

    def swap_card(self, card, deck):
        if card in self.hand:
            self.hand.remove(card)
            new_card = deck.deal()
            self.hand.append(new_card)
            deck.replenish([card])
            return new_card
        return None

    def score(self):
        score = 0
        for card in self.hand:
            if card.value == '2':  # For '2', the score is -2
                score -= 2
            elif card.value == 'A':  # For 'A', the score is 1
                score += 1
            elif card.value.isdigit():  # For other numerical cards, the score is the card's value
                score += int(card.value)
            elif card.value in ['J', 'Q', 'K']:  # For face cards, the score is 10
                score += 10
        return score

# Game class
class GolfGame:
    def __init__(self, players):
        self.deck = Deck()
        self.deck.shuffle()
        self.discard_pile = []  # Initialize the discard pile
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


    def replenish_deck_from_discard(self):
        self.deck.replenish(self.discard_pile)
    # Additional methods for game logic, scoring, etc., can be added here
