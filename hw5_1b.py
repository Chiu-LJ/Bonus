import random

# 定義牌的花色和點數
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# 創建並洗牌
deck = [f'{r} of {s}' for s in suits for r in ranks]
random.shuffle(deck)

# 發牌函數
def deal_cards(deck, hand):
    card = deck.pop()
    hand.append(card)

# 計算手牌點數函數
def calculate_hand_value(hand):
    value = 0
    has_ace = False

    for card in hand:
        rank = card.split()[0]
        if rank.isdigit():
            value += int(rank)
        elif rank in ['Jack', 'Queen', 'King']:
            value += 10
        elif rank == 'Ace':
            has_ace = True
            value += 11

    if has_ace and value > 21:
        value -= 10
    return value

# 初始化玩家和莊家的手牌
hands = {
    'player': [],
    'dealer': []
}

# 發初始手牌
deal_cards(deck, hands['player'])
deal_cards(deck, hands['player'])
deal_cards(deck, hands['dealer'])
deal_cards(deck, hands['dealer'])

# 玩家回合
while True:
    print(f"Player's hand: {hands['player']} (Value: {calculate_hand_value(hands['player'])})")
    print(f"Dealer's hand: [{hands['dealer'][0]}, <face down>]")

    if calculate_hand_value(hands['player']) > 21:
        print('Player busts!')
        break

    action = input('Do you want to hit or stand? ')

    if action.lower() == 'hit':
        deal_cards(deck, hands['player'])
    else:
        break

# 顯示最終手牌
print(f"Player's hand: {hands['player']} (Value: {calculate_hand_value(hands['player'])})")
print(f"Dealer's hand: {hands['dealer']} (Value: {calculate_hand_value(hands['dealer'])})")

# 遊戲結果判斷
if calculate_hand_value(hands['player']) > 21:
    print('Player busts!')
elif calculate_hand_value(hands['dealer']) > 21:
    print('Dealer busts! Player wins!')
elif calculate_hand_value(hands['player']) > calculate_hand_value(hands['dealer']):
    print('Player wins!')
elif calculate_hand_value(hands['player']) < calculate_hand_value(hands['dealer']):
    print('Dealer wins!')
else:
    print('Push!')

# 進行下一局遊戲
while True:
    wanna_play = input("Play again? (y/n): ")
    if wanna_play.lower() == "y":
        # 重置手牌和牌堆
        hands['player'].clear()
        hands['dealer'].clear()
        deck = [f'{r} of {s}' for s in suits for r in ranks]
        random.shuffle(deck)
        
        # 發新手牌
        deal_cards(deck, hands['player'])
        deal_cards(deck, hands['player'])
        deal_cards(deck, hands['dealer'])
        deal_cards(deck, hands['dealer'])

        # 玩家回合
        while True:
            print(f"Player's hand: {hands['player']} (Value: {calculate_hand_value(hands['player'])})")
            print(f"Dealer's hand: [{hands['dealer'][0]}, <face down>]")

            if calculate_hand_value(hands['player']) > 21:
                print('Player busts!')
                break

            action = input('Do you want to hit or stand? ')

            if action.lower() == 'hit':
                deal_cards(deck, hands['player'])
            else:
                break

        # 顯示最終手牌
        print(f"Player's hand: {hands['player']} (Value: {calculate_hand_value(hands['player'])})")
        print(f"Dealer's hand: {hands['dealer']} (Value: {calculate_hand_value(hands['dealer'])})")

        # 遊戲結果判斷
        if calculate_hand_value(hands['player']) > 21:
            print('Player busts!')
        elif calculate_hand_value(hands['dealer']) > 21:
            print('Dealer busts! Player wins!')
        elif calculate_hand_value(hands['player']) > calculate_hand_value(hands['dealer']):
            print('Player wins!')
        elif calculate_hand_value(hands['player']) < calculate_hand_value(hands['dealer']):
            print('Dealer wins!')
        else:
            print('Push!')
    elif wanna_play.lower() == "n":
        break
