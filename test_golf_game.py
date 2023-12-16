import unittest
import multiprocessing
from golf_card_game import GolfGame, Deck, Player

class TestGolfGame(unittest.TestCase):
    def setUp(self):
        self.game = GolfGame(['Alice', 'Bob'])

    def test_init(self):
        self.assertIsInstance(self.game.deck, Deck)
        self.assertEqual(len(self.game.players), 2)
        self.assertEqual(self.game.current_player_index, 0)

    def test_start_game(self):
        self.game.start_game()
        for player in self.game.players:
            self.assertEqual(len(player.hand), 6)

    def test_take_turn(self):
        self.game.start_game()
        self.game.take_turn()
        self.assertEqual(self.game.current_player_index, 1)

    def test_play_round(self):
        self.game.start_game()
        self.game.play_round()
        self.assertEqual(self.game.current_player_index, 0)

    def test_replenish_deck_from_discard(self):
        self.game.discard_pile = self.game.deck.cards
        self.game.deck.cards = []
        self.game.replenish_deck_from_discard()
        self.assertEqual(len(self.game.deck.cards), 52)
        self.assertEqual(len(self.game.discard_pile), 0)

    def test_calculate_scores(self):
        self.game.start_game()
        scores = self.game.calculate_scores()
        self.assertEqual(len(scores), 2)


    def test_play_game(self):
        self.game.play_game()
        self.assertEqual(len(self.game.deck.cards), 0)

if __name__ == '__main__':
    unittest.main()