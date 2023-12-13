import golf_card_game as gcg
import random

# Initialize the game
game = gcg.GolfGame(['Player 1', 'Player 2'])

# Start the game and display initial hands
game.start_game()
print("Initial hands:")
game.display_all_hands()


# Play rounds until the deck is empty or a player has revealed all their cards
while len(game.deck) > 0:
    game.play_round()
    print("\nHands after this round:")
    game.display_all_hands()

    # Reveal a card for each player and check if the game is over
    for player in game.players:
        score = player.calculate_score()
        print(f"{player.name}'s score: {score}")
        unrevealed_cards = [card for card in player.hand if not card.revealed]
        if unrevealed_cards:  # Check if there are any unrevealed cards left
            card = random.choice(unrevealed_cards)
            card.reveal()  # Reveal the card
            print(f"{player.name} revealed: {card}")
        else:
            print(f"{player.name} has revealed all their cards. Game over!")
            break
    else:
        continue  # executed if the loop ended normally (no break)
    break  # executed if 'continue' was not hit (break)
