import unittest
import random
from golf_card_game import Deck, Card  # assuming the Deck and Card classes are in golf_card_game.py

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_initial_deck_size(self):
        self.assertEqual(self.deck.count(), 52)  # a new deck should have 52 cards

    def test_shuffle(self):
        cards_before_shuffle = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(self.deck.cards, cards_before_shuffle)  # shuffling should change the order of the cards

    def test_deal(self):
        card_dealt = self.deck.deal()
        self.assertIsInstance(card_dealt, Card)  # the dealt card should be an instance of the Card class
        self.assertEqual(self.deck.count(), 51)  # after dealing one card, the deck should have 51 cards

    def test_replenish(self):
        discard_pile = [self.deck.deal() for _ in range(5)]  # deal 5 cards to the discard pile
        self.deck.replenish(discard_pile)
        self.assertEqual(self.deck.count(), 52)  # after replenishing, the deck should have 52 cards again
        self.assertEqual(len(discard_pile), 0)  # the discard pile should be empty after replenishing

    def test_deal_from_empty_deck(self):
        for _ in range(52):  # deal all cards
            self.deck.deal()
        with self.assertRaises(ValueError):  # dealing from an empty deck should raise a ValueError
            self.deck.deal()

if __name__ == '__main__':
    unittest.main()