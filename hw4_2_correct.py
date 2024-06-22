import random


def calculate_value(cards):
    value = 0
    for card in cards:
        if card == "ACE" and value + 11 <= 21:
            value += 11
        elif card[0] == "JACK" or card[0] == "QUEEN" or card[0] == "KING":
            value += 10
        elif card[0] == "ACE":
            value += 1
        else:
            value += int(card[0])
    return value


def display_cards(cards):
    results = "with the hand:"
    for card in cards:
        results += f" {card[0]}-{card[1]}"
    print(results)
    print()


play_again = True

while play_again:
    deck = ["ACE", "2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK", "QUEEN", "KING"]
    suits = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]

    cards = []

    # generate the deck of cards: 52 cards (13 cards * 4 suits)
    for suit in suits:
        for card in deck:
            cards.append((card, suit))

    random.shuffle(cards)

    # print("The first 5 cards are:")
    # for card in cards[:5]:
    #     print(card[0], "of", card[1])

    player = []
    player_value = 0
    player_busted = False
    dealer = []
    dealer_value = 0
    dealer_busted = False

    # deal 2 cards to the player and 2 cards to the dealer
    while len(player) < 2:
        player.append(cards.pop(0))
        dealer.append(cards.pop(0))
        # calculate the value of the player's cards
        # player_value = calculate_value(player)
        # dealer_value = calculate_value(dealer)

    while True:
        player_value = calculate_value(player)
        print(f"\nYour current value is: {player_value}")
        display_cards(player)
        choice = input(f"Hit or stay? (Hit = 1, Stay = 0): ")
        if choice == "1":
            card = cards.pop(0)
            print(f"You draw {card[0]}-{card[1]}")
            player.append(card)
            player_value = calculate_value(player)
            if player_value > 21:
                print(f"\nYour current value is Bust! (>21)")
                display_cards(player)
                player_busted = True
                break
        elif choice == "0":
            break

    while True and player_busted == False:
        dealer_value = calculate_value(dealer)
        print(f"\nDealer's current value is: {dealer_value}")
        display_cards(dealer)
        if dealer_value < 17:
            card = cards.pop(0)
            print(f"Dealer draws {card[0]}-{card[1]}")
            dealer.append(card)
            dealer_value = calculate_value(dealer)
            if dealer_value > 21:
                print(f"Dealer's current value is Bust! (>21)")
                display_cards(dealer)
                dealer_busted = True
                break
        else:
            break

    if player_busted:
        print("*** Dealer wins! ***")
    elif dealer_busted:
        print("*** You beat the dealer! ***")
    elif player_value == dealer_value:
        print("*** You tied the dealer, nobody wins. ***")
    elif player_value > dealer_value:
        print("*** You beat the dealer! ***")
    elif player_value < dealer_value:
        print("*** Dealer wins! ***")

    play_again = input("Want to play again? (y/n): ")
    if play_again == "n":
        break
    else:
        play_again = True
