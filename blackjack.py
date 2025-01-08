import random
import time
import math
done = False
deck = []
chips = 1000

art = ''' 
 -------    -------
|A♠     |  |K♥     |
|       |  |       |
|       |  |       |
|       |  |       |
|     ♠A|  |     ♥K|
 -------    ------- 
'''

def shuffle(deck):
    deck = ["A♠", "2♠", "3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠","A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣","A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥","A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦"]
    return deck

def value(card):
    if card[0] == "1" or card[0] == "J" or card[0] == "Q" or card[0] == "K":
        return 10
    elif card[0] == "A":
        return 1
    else:
        return int(card[0])



def deckDraw(receiver):
    new_card = random.choice(deck)
    deck.remove(new_card)
    receiver.append(new_card)
    val = 0
    for x in receiver:
        val = val + value(x)
    if val > 11:
        return val
    else:
        aces = 0
        for i in receiver:
            if (i[0] == "A"):
                aces = 1
        if aces == 1:
            val = val + 10
        return val
            



while chips > 0:
    deck = shuffle(deck)
    dealer = []
    player = []
    player_value = 0
    dealer_value = 0
    move = "null"
    moved = False
    dealer_black = False
    player_black = False
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print(art + '\n\nBlackjack! Dealer must hit to 16 and stand on 17\n\n\n')
    print(f'Chips: {chips}')
    bet = 0
    while bet == 0:
        try:
            betTry = int(input('Place bet: '))
            if betTry > chips:
                print("\nBet too high\n")
            else:
                bet = betTry
        except:
            print("\nNot a valid bet\n")

    print()

    player_value = deckDraw(player)
    player_value = deckDraw(player)
    dealer_value = deckDraw(dealer)
    dealer_value = deckDraw(dealer)
    
    if dealer_value == 21:
        print(f'Dealer: |{dealer[0]}| |{dealer[1]}|')
        print('Blackjack!')
        move = "over"
        dealer_black = True
    else:
        print(f'Dealer: |{dealer[0]}| |?|')

    print(f'\n\nPlayer: |{player[0]}| |{player[1]}| -> {player_value}')
    if player_value == 21:
        print('Blackjack!')
        player_black = True
        move = "over"
    print('\n\n\n\n')



    while move != "over":
        if move == "null" and (bet * 2) <= chips:
            move = str(input("Hit/Stand/Double Down: "))
        elif player_value == 21:
            move = "s"
        else:
            move = str(input("Hit/Stand: "))

        if move.lower() == "hit" or move.lower() == "h":
            player_value = deckDraw(player)
            print('\nPlayer:',end=" ")
            for y in range(len(player)):
                    print(f'|{player[y]}|', end=" ")
            print(f'-> {player_value}')
            print('\n')
            if player_value > 21:
                print('Bust!')
                move = "over"
            moved = True
        elif move.lower() == "double down" or move.lower() == "double" or move.lower() == "d" or move.lower() == "dd":
            if bet * 2 > chips:
                print("\nNot enough chips\n")                
            elif moved == False:
                bet = bet * 2
                player_value = deckDraw(player)
                print('\nPlayer:',end=" ")
                for y in range(len(player)):
                        print(f'|{player[y]}|', end=" ")
                print(f'-> {player_value}')
                print('\n')
                if player_value > 21:
                    print('Bust!')
                move = "over"
            else:
                print("\nCannot Double Down after first turn\n")
        elif move.lower() == "s" or move.lower() == "stand":
            move = "over"
        else:
            print("\nNot a valid move\n")
    print('\n\n\n')
    
    if player_value < 22 and (dealer_black + player_black) == False:
        game = True
        print('Dealer:\n')
    else:
        game = False
    while game == True:
        for y in range(len(dealer)):
            print(f'|{dealer[y]}|', end=" ")
        print(f'-> {dealer_value}')
        if dealer_value > 21:
            print('\nBust!')
        print('\n')        
        if dealer_value > 16:
            game = False
        else:
            dealer_value = deckDraw(dealer)
        time.sleep(1)

    print('\n\n')
    if player_value < dealer_value and dealer_value < 22:
        print('House wins')
        chips = chips - bet
    elif player_value > dealer_value and player_value < 22:
        print('You win!')
        chips = chips + bet
        if player_black == True:
            chips = chips + math.ceil(bet/2)
    elif dealer_value > 21:
        print('You win!')
        chips = chips + bet
        if player_black == True:
            chips = chips + math.ceil(bet/2)        
    elif player_value > 21:
        print('House wins')
        chips = chips - bet
    elif player_value == dealer_value:
        print('Draw')
    print(f'\nChips: {chips}')

    
    time.sleep(5)

print("\n\n\n\n\n\nYou Lost :(\n\nTry again next time!")

time.sleep(5)
