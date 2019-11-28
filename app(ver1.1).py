import random
import sys
import time


def welcome_message():
    print("\n|------------------------|")
    print("| Welcome to Black Jack! |")
    print("|------------------------|\n")


def replay():
    while True:
        answer = input("Would you like to play again? Y/N ")
        if answer == "y" or answer == "Y":
            game_start()
        elif answer == "n" or answer == "N":
            print("Good Game!")
            sys.exit(0)
        else:
            print("I don't understand...")


def game_start():
    welcome_message()
    # construct and shuffle the deck
    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    suite = ["♥", "♣", "♦", "♣"]
    deck = []
    for i in numbers:
        for k in suite:
            deck.append(str(i) + k)
    random.shuffle(deck)

    # Deal the cards
    first_player_card = random.choice(deck)
    deck.remove(first_player_card)
    first_dealer_card = random.choice(deck)
    deck.remove(first_dealer_card)
    second_player_card = random.choice(deck)
    deck.remove(second_player_card)
    second_dealer_card = random.choice(deck)
    deck.remove(second_dealer_card)

    player_hand = [first_player_card, second_player_card]
    print("Here is your hand: ")
    print(player_hand)
    print("-----------------")
    print("Here is the dealer's hand: ")
    dealer_hand = ["[ ]", second_dealer_card]
    print(dealer_hand)
    print("-----------------")

    # get the sum of the starting player hand
    player_sum = 0
    for i in player_hand:
        if i[0] == "J" or i[0] == "Q" or i[0] == "K" or (i[0] == "1" and i[1] == "0"):
            player_sum += 10
        elif i[0] == "A":
            player_sum += 11
        else:
            player_sum += int(i[0])
    # get the sum of the dealer's hand
    dealer_sum = 0
    for i in dealer_hand:
        if i =="[ ]":
            dealer_hand[0] = first_dealer_card
            if first_dealer_card[0] == "J" or first_dealer_card[0] == "Q" or first_dealer_card[0] == "K" or (first_dealer_card[0] == "1" and first_dealer_card[1] == "0"):
                dealer_sum += 10
            elif first_dealer_card[0] == "A":
                dealer_sum += 11
            else:
                dealer_sum += int(first_dealer_card[0])
        elif i[0] == "J" or i[0] == "Q" or i[0] == "K" or (i[0] == "1" and i[1] == "0"):
            dealer_sum += 10
        elif i[0] == "A":
            dealer_sum += 11
        else:
            dealer_sum += int(i[0])
    # checks to see if anybody gets 21 on first hand
    if player_sum == 21 and dealer_sum == 21:
        print(dealer_hand)
        print("It's a push!")
        time.sleep(1)
    elif player_sum == 21 and dealer_sum != 21:
        print("You got 21! Great Job!")
        time.sleep(1)
    elif player_sum != 21 and dealer_sum == 21:
        print(dealer_hand)
        print("Dealer gets 21! Try again...")
        time.sleep(1)
    else:
        a_count_1 = True
        a_count_2 = True
        a_count_3 = True
        a_count_4 = True
        if player_sum == 22:
            player_sum -= 10
            a_count_1 = False

        # player turn
        while player_sum <= 21:
            a_count = 0
            print(player_hand)
            print("You have:", player_sum)
            choice = input("Would you like to hit or stand: H/S   ")
            if choice == "h" or choice == "H":
                next_card = random.choice(deck)
                deck.remove(next_card)
                player_hand.append(next_card)
                if next_card[0] == "J" or next_card[0] == "Q" or next_card[0] == "K" or (next_card[0] == "1" and next_card[1] == "0"):
                    player_sum += 10
                    if player_sum > 21:
                        for i in player_hand:
                            if i[0] == "A":
                                a_count += 1
                                if a_count == 1 and a_count_1 == True:
                                    player_sum -= 10
                                    a_count_1 = False
                                elif a_count == 2 and a_count_2 == True:
                                    player_sum -= 10
                                    a_count_2 = False
                                elif a_count == 3 and a_count_3 == True:
                                    player_sum -= 10
                                    a_count_3 = False
                                elif a_count == 4 and a_count_4 == True:
                                    player_sum -= 10
                                    a_count_4 = False
                elif next_card[0] == "A":
                    player_sum += 11
                    if player_sum > 21:
                        for i in player_hand:
                            if i[0] == "A":
                                a_count += 1
                                if a_count == 1 and a_count_1 == True:
                                    player_sum -= 10
                                    a_count_1 = False
                                    break
                                elif a_count == 2 and a_count_2 == True:
                                    player_sum -= 10
                                    a_count_2 = False
                                    break
                                elif a_count == 3 and a_count_3 == True:
                                    player_sum -= 10
                                    a_count_3 = False
                                    break
                                elif a_count == 4 and a_count_4 == True:
                                    player_sum -= 10
                                    a_count_4 = False
                                    break
                            else:
                                continue
                else:
                    player_sum += int(next_card[0])
                    if player_sum > 21:
                        for i in player_hand:
                            if i[0] == "A":
                                a_count += 1
                                if a_count == 1 and a_count_1 == True:
                                    player_sum -= 10
                                    a_count_1 = False
                                elif a_count == 2 and a_count_2 == True:
                                    player_sum -= 10
                                    a_count_2 = False
                                elif a_count == 3 and a_count_3 == True:
                                    player_sum -= 10
                                    a_count_3 = False
                                elif a_count == 4 and a_count_4 == True:
                                    player_sum -= 10
                                    a_count_4 = False
                            else:
                                continue
                    else:
                        continue

            elif choice == "s" or choice == "S":
                # dealer turn
                print("Dealer turn:")
                input("Press 'Enter' to continue.")
                while dealer_sum <= 21:
                    print(dealer_hand, dealer_sum)
                    if dealer_sum >= 17:
                        if dealer_sum < player_sum:
                            time.sleep(1)
                            print("You win!")
                            time.sleep(1)
                            replay()
                        elif dealer_sum > player_sum:
                            time.sleep(1)
                            print("Dealer wins!")
                            time.sleep(1)
                            replay()
                        elif dealer_sum == player_sum:
                            time.sleep(1)
                            print("It's a push!")
                            time.sleep(1)
                            replay()
                    else:
                        next_card = random.choice(deck)
                        deck.remove(next_card)
                        dealer_hand.append(next_card)
                        if next_card[0] == "J" or next_card[0] == "Q" or next_card[0] == "K" or (next_card[0] == "1" and next_card[1] == "0"):
                            dealer_sum += 10
                            time.sleep(1)
                        elif next_card[0] == "A":
                            dealer_sum += 11
                            time.sleep(1)
                        else:
                            dealer_sum += int(next_card[0])
                            time.sleep(1)
                print(dealer_hand, dealer_sum)
                time.sleep(1)
                print("Dealer Busted! You Win!")
                time.sleep(1)
                replay()
        print(player_hand, player_sum)
        print("You busted...")
        time.sleep(1)
        replay()
    replay()


game_start()
