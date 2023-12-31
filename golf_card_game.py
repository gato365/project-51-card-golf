import random

# Constants for the suits and values
SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']



# Card class
class Card:
    VALID_SUITS = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    VALID_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, value, revealed=False):
        if suit not in self.VALID_SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        if value not in self.VALID_VALUES:
            raise ValueError(f"Invalid value: {value}")

        self.suit = suit
        self.value = value
        self.revealed = revealed  # Add the revealed attribute

    def reveal(self):
        self.revealed = True  # Add a method to reveal the card

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
    
    def draw_card(self):
        return self.cards.pop()
    
# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        card = deck.draw_card()
        if card is not None:
            if len(self.hand) < 2:  # The first two cards are always revealed
                card.reveal()
            self.hand.append(card)
        return card

    def reveal_card(self, index):
        # Check if the card is in the hand and hasn't been revealed yet
        if index < len(self.hand) and not self.hand[index].revealed:
            card = self.hand[index]
            card.reveal()  # Reveal the card
            print(f"{self.name} revealed: {card}")
            return card
        else:
            print("Invalid card index or card already revealed")
            return None

    def display_hand(self):
        # Display the revealed cards and hide the rest
        displayed_hand = [str(card) if card.revealed else 'Unknown' for card in self.hand]
        return ', '.join(displayed_hand)

    def show_cards(self):
        return self.hand

    def discard(self, card, discard_pile):
        if card in self.hand:
            self.hand.remove(card)
            discard_pile.append(card)

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
    
    def calculate_score(self):
        score = 0
        
        for card in self.hand:
            if card.revealed:
                if card.value == '2':  # For '2', the score is -2
                    score -= 2
                elif card.value == 'A':  # For 'A', the score is 1
                    score += 1
                elif card.value.isdigit():  # For other numerical cards, the score is the card's value
                    score += int(card.value)
                elif card.value in ['J', 'Q', 'K']:  # For face cards, the score is 10
                    score += 10
        return score

# Golf Game class
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
            for _ in range(6):
                player.draw(self.deck)

    def take_turn(self):
        # Current player takes their turn
        current_player = self.players[self.current_player_index]
        print(f"It's {current_player.name}'s turn.")

        # Player can only draw from deck if it's not empty
        if len(self.deck) > 0:
            drawn_card = current_player.draw(self.deck)
            print(f"{current_player.name} drew {drawn_card}")

            # Player discards a card
            discarded_card = current_player.discard(drawn_card, self.discard_pile)

        # Move to the next player
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_round(self):
        # Each player takes a turn
        for _ in range(len(self.players)):
            self.take_turn()

        # At the end of the round, replenish the deck from the discard pile
        self.replenish_deck_from_discard()

    def replenish_deck_from_discard(self):
        self.deck.replenish(self.discard_pile)
        self.discard_pile = []

    def calculate_scores(self):
        # Calculate and return scores for all players
        scores = {}
        for player in self.players:
            score = player.score()
            scores[player.name] = score
        return scores

    def play_game(self):
        # Play rounds until the deck is empty
        while len(self.deck) > 0:
            self.play_round()

        # Calculate final scores
        self.calculate_scores()
    
    def display_all_hands(self):
        for player in self.players:
            print(f"{player.name}'s hand: {player.display_hand()}")