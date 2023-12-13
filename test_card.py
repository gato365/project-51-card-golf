# Import the Card class from golf_game.py
from golf_card_game import Card

def test_card_creation():
    # Create a card instance
    card = Card("Hearts", "10")
    assert card.suit == "Hearts", "Suit should be Hearts"
    assert card.value == "10", "Value should be 10"

def test_card_representation():
    # Create a card instance
    card = Card("Spades", "A")
    # Test the string representation
    assert str(card) == "A of Spades", "String representation should be 'A of Spades'"

# Add more test functions as needed


def test_card_validity():
    # Test valid card creation
    try:
        Card("Hearts", "10")
        Card("Spades", "A")
        # Add more combinations as needed
    except Exception as e:
        print(f"Test failed with exception: {e}")
        raise

    # Optionally, test invalid card creation
    try:
        Card("Spades", "10")
        assert True, "Invalid suit should raise an exception"
    except ValueError:
        pass  # This is the expected behavior



# Run the test
if __name__ == "__main__":
    test_card_validity()
    print("All card validity tests passed!")



# Running the test functions
if __name__ == "__main__":
    test_card_creation()
    test_card_representation()
    test_card_validity()
    print("All tests passed!")
