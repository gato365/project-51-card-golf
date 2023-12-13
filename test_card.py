# Import the Card class from golf_game.py
from golf_card_game import Card


def test_valid_card_creation():
    # Test creation of cards with valid suits and values
    for suit in Card.VALID_SUITS:
        for value in Card.VALID_VALUES:
            try:
                card = Card(suit, value)
                assert card.suit == suit and card.value == value, f"Failed to create {value} of {suit}"
            except ValueError:
                assert False, f"Valid card {value} of {suit} raised ValueError"

def test_card_representation():
    # Create a card instance and test its string representation
    card = Card("Spades", "A")
    assert str(card) == "A of Spades", "String representation should be 'A of Spades'"



def test_invalid_card_creation():
    # Test creation of cards with invalid suits and values
    invalid_suit = "Rocks"
    invalid_value = "11"
    try:
        Card(invalid_suit, Card.VALID_VALUES[0])
        assert False, "Invalid suit should raise ValueError"
    except ValueError:
        pass  # This is expected

    try:
        Card(Card.VALID_SUITS[0], invalid_value)
        assert False, "Invalid value should raise ValueError"
    except ValueError:
        pass  # This is expected


# Run the tests
if __name__ == "__main__":
    test_valid_card_creation()
    test_card_representation()
    test_invalid_card_creation()
    print("All card tests passed!")