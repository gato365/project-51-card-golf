# Golf Card Game Project


## **Golf Card Game Procedure**

1. **Setup**:
   - Use a standard 52-card deck.
   - Shuffle the deck thoroughly.

2. **Dealing**:
   - Each player is dealt six cards, face down.
   - Players may not look at their cards during the deal.

3. **Initial Reveal**:
   - Each player selects two of their six cards at random and reveals them to all players, including themselves. The other four cards remain face down and unknown.

4. **Creating the Discard Pile**:
   - The dealer flips the top card from the remaining deck to start the discard pile, making this card visible to all players.

5. **Gameplay**:
   - The player to the right of the dealer (designated as 'North') begins.
   - Players take turns in a clockwise direction.

6. **Player's Turn**:
   - Each player has two options for their draw:
     - **Option 1**: Draw the visible top card from the discard pile.
     - **Option 2**: Draw a hidden card from the top of the deck.

7. **Card Replacement**:
   - After drawing a card, the player replaces one of their six cards with the drawn card.
     - If the card was drawn from the discard pile, it can replace any one of the six cards (known or unknown).
     - If the card was drawn from the deck, it typically replaces one of the known cards.
   - The replaced card is then revealed to all players (if it was unknown) and placed face up on the discard pile.

8. **Continuing Play**:
   - Play continues with each player taking turns, drawing and replacing cards.

9. **End of the Round**:
   - The round can end based on predetermined conditions, such as when the deck is depleted or after a set number of turns.

10. **Scoring**:
   - At the end of a round, players reveal all their cards.
   - Scores are calculated based on the values of the cards (numerical value for number cards, 10 for face cards, 1 for Aces).
   - The goal is to have the lowest score.

11. **Winning the Game**:
   - After a set number of rounds (like nine or eighteen, akin to golf), the player with the lowest cumulative score wins.




## 1. Basic Game Setup (Deck, Cards, and Dealing)

### Implementation
- [ ] **Card Class**: Implement a class to represent each card, with attributes for suit and value.

- [ ] **Deck Class**: Implement a class to represent the deck. This should include methods to generate a full set of cards, shuffle, and deal them.
    - count: Returns the number of cards remaining in the deck. Useful for checking if the deck is empty
    - replenish: If your game rules require, you can add a method to replenish the deck with cards from the discard pile.
    
- [ ] **Player Class**: Implement a class to represent each player, holding their hand of cards.
    - show_hand: Display the player's current hand. This could be more elaborate than just printing the hand; for example, it could show which cards are known and which are hidden.
    - swap_card: Method to swap a card from the player's hand with one from the deck or the discard pile.
    - reveal_card: If a player's turn results in revealing a card, this method could handle that.
    - score: Calculate and return the player's current score, based on the cards in hand.

- [ ] **Initial Setup**: Code to initialize the game with a deck and players.

### Testing and Debugging
- [ ] Test card creation and representation.
- [ ] Test deck shuffling and dealing functionalities.
- [ ] Ensure each player receives the correct number of cards.

## 2. Game Logic (Turns, Drawing, and Replacing Cards)

### Implementation
- [ ] **Turn Management**: Implement turn-taking logic for each player.
- [ ] **Drawing Logic**: Code for players to draw cards from the deck or discard pile.
- [ ] **Replacing Cards**: Allow players to swap out cards from their hand.

### Testing and Debugging
- [ ] Test turn-taking sequence among players.
- [ ] Validate drawing and card replacement logic.
- [ ] Check for any logical errors or edge cases in turn mechanics.

## 3. Gameplay Mechanics (Player Actions, Discard Pile Management)

### Implementation
- [ ] **Player Actions**: Implement actions that players can take during their turn.
- [ ] **Discard Pile Management**: Code to handle the discard pile and its interaction with the game.

### Testing and Debugging
- [ ] Test various player actions for correctness.
- [ ] Ensure discard pile is managed correctly with each player's actions.

## 4. Scoring and End Game Conditions

### Implementation
- [ ] **Scoring System**: Implement the scoring mechanism based on the rules of Golf.
- [ ] **End Game Logic**: Code to determine the end of the game and declare a winner.

### Testing and Debugging
- [ ] Test the scoring system for accuracy.
- [ ] Validate the end game conditions and winner declaration.

## 5. User Interface

### Implementation
- [ ] **Text-based Interface**: If applicable, create a basic text-based interface for the game.
- [ ] **Graphical Interface**: For a more advanced approach, develop a graphical user interface (optional and more complex).

### Testing and Debugging
- [ ] Test the interface for usability and clarity.
- [ ] Debug any issues with user inputs or interface displays.


GolfGame
|
|-- players: List[Player]
|-- deck: Deck
|-- discard_pile: List[Card]
|
|-- start_game()
|-- play_round()
|-- take_turn()
|-- display_all_hands()
|-- reveal_card_and_check_game_over()  # proposed method

Player
|
|-- hand: List[Card]
|
|-- draw(deck: Deck)
|-- discard(card: Card, discard_pile: List[Card])
|-- swap_card(card: Card, deck: Deck)
|-- reveal_card(index: int)
|-- calculate_score()

Deck
|
|-- cards: List[Card]
|
|-- shuffle()
|-- draw_card()

Card
|
|-- reveal()
