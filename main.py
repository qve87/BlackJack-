############### Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def hit_or_stand(player_list, cards):
    global game_on
    while True:
        h_or_s = input("Would like to Hit or Stand? Press 'h' or 's': ").lower()

        if h_or_s == "h":
            player_list.append(random.choice(cards))

            if sum(player_list) > 21 and 11 in player:
                ace_index = player.index(11)
                player[ace_index] = 1
            elif sum(player_list) > 21:
                print(f"Your new hand: {player_list}")
                print(f"Sum of your new hand: {sum(player_list)}")
                print("You BUST!\n")
                game_on = False
                break
            print(f"Your new hand: {player_list}")
            print(f"Sum of your new hand: {sum(player_list)}\n")
        elif h_or_s == "s":
            break
        else:
            print("Sorry, I didn't understand! Please type 'h' or 's'.\n")

    return sum(player_list)


def dealer_turn(dealer_cards, cards_list):
    global game_on
    dealer_cards.pop()
    dealer_cards.append(random.choice(cards_list))
    while True:

        if 17 <= sum(dealer_cards) <= 21:
            print(f"Dealer's new hand: {dealer_cards}\n"
                  f"Sum of Dealer's new hand: {sum(dealer_cards)}")
            break
        elif sum(dealer_cards) < 17:
            dealer_cards.append(random.choice(cards_list))
            print(f"Dealer's new hand: {dealer_cards}\n"
                  f"Sum of Dealer's new hand: {sum(dealer_cards)}")
            if sum(dealer_cards) > 21:
                print("Dealer BUST!\n")
                game_on = False
                break

    return sum(dealer_cards)


game_on = True

while game_on:

    print(logo)
    player = [random.choice(cards) for card in range(0, 2)]
    dealer = [random.choice(cards), "Hidden card"]

    print(f"Dealer's hand: {dealer} \n")
    print(f"Player's hand: {player} \n"
          f"Total sum of Player's card: {sum(player)}\n")

    player_sum = hit_or_stand(player, cards)
    if player_sum > 21:
        pass
    else:
        dealer_sum = dealer_turn(dealer, cards)


    while game_on:
        if player_sum > dealer_sum:
            print("Player WINS!\n")
            game_on = False
            break
        elif dealer_sum > player_sum:
            print("Player LOSE!\n")
            break
        else:
            print("DRAW!\n")
            break

    while True:

        g = input("Do you want to try again. y/n: ").lower()

        if g == "y":
            game_on = True
            break
        elif g == "n":
            print("Thanks for playing!")
            game_on = False
            break
        else:
            print("I don't understand. Please type 'y' or 'n'.")
            continue
