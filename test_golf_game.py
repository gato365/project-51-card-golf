import unittest
from golf_card_game import GolfGame, Card

class TestGolfGame(unittest.TestCase):
    def setUp(self):
        self.game = GolfGame(["Player 1", "Player 2"])

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
        self.game.discard_pile = [Card('Hearts', str(i)) for i in range(2, 7)]
        
        self.game.replenish_deck_from_discard()
        self.assertEqual(len(self.game.discard_pile), 0)

    def test_calculate_scores(self):
        self.game.start_game()
        self.game.players[0].hand = [Card('Hearts', '2'), Card('Diamonds', 'A')]
        self.game.players[1].hand = [Card('Hearts', '3'), Card('Diamonds', '4')]
        scores = self.game.calculate_scores()
        self.assertEqual(scores, {"Player 1": -1, "Player 2": 7})

if __name__ == '__main__':
    unittest.main()