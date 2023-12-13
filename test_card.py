import unittest
from golf_card_game import Card

class TestCard(unittest.TestCase):
    def test_valid_card_creation(self):
        for suit in Card.VALID_SUITS:
            for value in Card.VALID_VALUES:
                card = Card(suit, value)
                self.assertEqual(card.suit, suit)
                self.assertEqual(card.value, value)

    def test_card_representation(self):
        card = Card("Spades", "A")
        self.assertEqual(str(card), "A of Spades")

    def test_invalid_card_creation(self):
        invalid_suit = "Rocks"
        invalid_value = "11"
        with self.assertRaises(ValueError):
            Card(invalid_suit, Card.VALID_VALUES[0])
        with self.assertRaises(ValueError):
            Card(Card.VALID_SUITS[0], invalid_value)

if __name__ == '__main__':
    unittest.main()