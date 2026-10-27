import random

def evaluate_hand():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f"{r}{s}" for r in ranks for s in suits]
    
    # Draw 5 random cards
    hand = random.sample(deck, 5)
    hand_ranks = [card[:-1] for card in hand]
    
    print(f"Your Hand: {', '.join(hand)}")
    
    # Check for matches
    unique_ranks = set(hand_ranks)
    if len(unique_ranks) < 5:
        print("Result: You have a Pair or better! 🎉")
    else:
        print("Result: High Card. 🃏")

if __name__ == "__main__":
    evaluate_hand()
