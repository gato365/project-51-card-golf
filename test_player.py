import unittest
from golf_card_game import Player, Deck, Card

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Test Player")
        self.deck = Deck()

    def test_draw(self):
        self.player.draw(self.deck)
        self.assertEqual(len(self.player.hand), 1)
        self.assertIsInstance(self.player.hand[0], Card)

    def test_show_cards(self):
        self.player.draw(self.deck)
        self.assertEqual(len(self.player.show_cards()), 1)
        self.assertIsInstance(self.player.show_cards()[0], Card)

    def test_discard(self):
        card = self.player.draw(self.deck)
        self.player.discard(card, self.deck)
        self.assertEqual(len(self.player.hand), 0)

    def test_swap_card(self):
        card = self.player.draw(self.deck)
        new_card = self.player.swap_card(card, self.deck)
        self.assertNotEqual(card, new_card)
        self.assertEqual(len(self.player.hand), 1)

    def test_score(self):
        self.player.hand = [Card('Hearts', '2'), Card('Diamonds', 'A')]
        self.assertEqual(self.player.score(), -1)

if __name__ == '__main__':
    unittest.main()