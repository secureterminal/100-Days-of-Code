## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
from helper import clearConsole
import random
print(logo)

start_game = input("Welcome, Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_card(cards):
    card = cards[random.randint(0, len(cards))-1]
    return card

def sum_user_cards(cards):
    total = 0
    for card in cards:
        total += card

    if 11 in cards and total > 21:
        total -= 10
    
    return total

house_action = ''


def sum_house_cards(cards):
    total = 0
    
    for card in cards:
        total += card
    
    # if (11 in cards) and (total < 17):
    #     total -= 10

    return total


def house_next_action(sum_of_cards, cards):
    # house > 21,  busted
    if (11 in cards) and (17 < sum_of_cards < 21):
        return 'stand'
    if sum_of_cards > 21:
        return 'bust'
    elif sum_of_cards == 21:
        return 'win'
    else:
        if sum_of_cards >= 17:
            house_action = 'stand'
        else:
            house_action = 'hit'
    
    return house_action

def compare_cards(house_card, user_card):

    user_total_var = sum_user_cards(user_card)
    house_total_var = sum_house_cards(house_card)

    if user_total_var > house_total_var:
        return 'user'
    elif house_total_var > user_total_var:
        return 'house'
    else:
        return 'draw'


def end_hand():
    start_game = 'y'
    active_hand_status = False
    continue_hitting_user = False
    house_turn = False
    user_card = []
    house_card = []
    user_card.append(get_card(cards))
    user_card.append(get_card(cards))

    print('End Hand', start_game, active_hand_status, continue_hitting_user, house_turn, user_card, house_card)

    return start_game, active_hand_status, continue_hitting_user, house_turn, user_card, house_card
    

def end_game():
    start_game = 'n'
    active_hand_status = False
    continue_hitting_user = False
    house_turn = False
    user_card = []
    house_card = []

    print('End Game', start_game, active_hand_status, continue_hitting_user, house_turn, user_card, house_card)

    return start_game, active_hand_status, continue_hitting_user, house_turn, user_card, house_card


hands_won = 0
hands_drawn = 0
hands_lost = 0
hands = 0
user_bank = 1000
# house_bank = 1000
user_card = []
house_card = []
user_card.append(get_card(cards))
house_card.append(get_card(cards))
active_hand_status = True


# MAJOR CHANGE

while (start_game == 'y'):
    # Game round per user, covers multiple hands
    if user_bank > 0:
        active_hand_status = True
        if hands == 0:
            hands += 1
            # print(all_game_stats)
            amount = input(f'\n\nWelcome to Hand {hands} Your bank is ${user_bank:,}, How much do you want to deal? >>> $')
        else: # hands > 0
            if input(f'\nHand {hands} ended, Do you want another round? Y for yes >>>').lower() == 'y':
                hands += 1
                user_card = []
                house_card = []
                user_card.append(get_card(cards))
                house_card.append(get_card(cards))

                
                amount = input(f'\n\nWelcome to Hand {hands} Your bank is ${user_bank:,}, How much do you want to deal? >>> $')
            else: # User dont want any more round
                # End the game
                # STATUS
                if user_bank > 1000:
                    print(f'''
                        Game has ended
                        Hands won = {hands_won}
                        Hands lost = {hands_lost}
                        Hands Drawn = {hands_drawn}
                        Number of Hands = {hands}
                        Amount Won = ${(user_bank - 1000):,}
                        Final Amount = ${user_bank:,}
                        ''')
                else:
                    print(f'''
                        Game has ended
                        Hands won = {hands_won}
                        Hands lost = {hands_lost}
                        Hands Drawn = {hands_drawn}
                        Number of Hands = {hands}
                        Amount Lost = ${(1000 - user_bank):,}
                        Final Amount = ${user_bank:,}
                        ''')

                start_game, active_hand_status, continue_hitting_user, house_turn, user_card, house_card = end_game()
    else: # bank < 0
        # End the game
        

        
        print('Your money don finish')
        print(f'''
                Game has ended
                Hands won = {hands_won}
                Hands lost = {hands_lost}
                Hands Drawn = {hands_drawn}
                Number of Hands = {hands}
                Amount Lost = ${(1000 - user_bank):,}
                Final Amount = ${user_bank:,}
                ''')
        start_game, active_hand_status, continue_hitting_user, house_turn, user_card, house_card = end_game()

    while (user_bank > 0) and (active_hand_status == True):
        # This handles each set of hands
        # amount input might go in here
        
        # checking if amount is valid
        try:
            amount = int(amount)
            if amount > user_bank:
                print('Insufficient funds')
                amount = input(f'\nYour bank is ${user_bank:,}, How much do you want to deal? Game will end if you put in a wrong amount >>> $')
                if int(amount) > user_bank:

                    # STATUS
                    if user_bank > 1000:
                        print(f'''
                            Game has ended
                            Hands won = {hands_won}
                            Hands lost = {hands_lost}
                            Hands Drawn = {hands_drawn}
                            Number of Hands = {hands}
                            Amount Won = ${(user_bank - 1000):,}
                            Final Amount = ${user_bank:,}
                            ''')
                    else:
                        print(f'''
                            Game has ended
                            Hands won = {hands_won}
                            Hands lost = {hands_lost}
                            Hands Drawn = {hands_drawn}
                            Number of Hands = {hands}
                            Amount Lost = ${(1000 - user_bank):,}
                            Final Amount = ${user_bank:,}
                            ''')

                    start_game, active_hand_status, continue_hitting_user, house_turn, user_card, house_card = end_game()

                    

                    # GAME_END
                    # PRINT_STATUS
                    # EXIT

            else: # valid amount entered
                user_bank = user_bank - amount
                print(f'Dealing ${amount}, you have ${user_bank:,} left in your bank')
                continue_hitting_user = True
                user_card.append(get_card(cards))

                print('User Card', user_card,  'House Card', house_card)

                print(f'Your cards: {user_card}, current score: {sum_user_cards(user_card)} ')
                print(f'Computer\'s first card: : {house_card} ')

                # Deal or stand
                if len(user_card) == 2 and sum_user_cards(user_card) == 21:
                    print(f'\nBLACKJACK!!!!!, YOUR CARDS {user_card} sums up to {sum_user_cards(user_card)}, you have won 150% of your stake equivalent to ${amount * 1.5} ')
                    # Add winnings
                    user_bank = user_bank + (amount* 2.5)
                    hands_won += 1

                    start_game, active_hand_status, continue_hitting_user, house_turn, user_card, house_card = end_hand()

                    # reset cards
                    # ask to deal, if yes active_hand_status = False, else start_game = 'n'
                    active_hand_status = False


                while continue_hitting_user == True:
                    # Keep hitting the user unless he chooses otherwise
                    if sum_user_cards(user_card) > 21:
                        print(f'Bust!!!, your score is {user_card} {sum_user_cards(user_card)}, House wins this hand with a score of {house_card} {sum_user_cards(house_card)} ')
                        # Add losses

                        hands_lost += 1

                        # HAND_END
                        
                        # PRINT_PREVIOUS_STATUS
                        # STATUS
                        if user_bank > 1000:
                            print(f'''
                                Hand has ended
                                Hands won = {hands_won}
                                Hands lost = {hands_lost}
                                Hands Drawn = {hands_drawn}
                                Number of Hands = {hands}
                                Amount Won = ${(user_bank - 1000):,}
                                Final Amount = ${user_bank:,}
                                ''')
                        else:
                            print(f'''
                                Hand has ended
                                Hands won = {hands_won}
                                Hands lost = {hands_lost}
                                Hands Drawn = {hands_drawn}
                                Number of Hands = {hands}
                                Amount Lost = ${(1000 - user_bank):,}
                                Final Amount = ${user_bank:,}
                                ''')

                        start_game, active_hand_status, continue_hitting_user, house_turn, user_card, house_card = end_hand()
                        # CONTINUE TO FIRST WHILE STATEMENT (NEXT HAND)

                        
                        active_hand_status = False # ask to start another round under first while statement
                        continue_hitting_user = False
                    elif sum_user_cards(user_card) == 21:
                        print(f'You win!!!, your score is {user_card} {sum_user_cards(user_card)}, User wins this hand.')
                        # Add winnings
                        user_bank = user_bank + (amount*2)
                        hands_won += 1

                        # HAND_END
                        # PRINT_PREVIOUS_STATUS
                        # STATUS
                        if user_bank > 1000:
                            print(f'''
                                Hand has ended
                                Hands won = {hands_won}
                                Hands lost = {hands_lost}
                                Hands Drawn = {hands_drawn}
                                Number of Hands = {hands}
                                Amount Won = ${(user_bank - 1000):,}
                                Final Amount = ${user_bank:,}
                                ''')
                        else:
                            print(f'''
                                Hand has ended
                                Hands won = {hands_won}
                                Hands lost = {hands_lost}
                                Hands Drawn = {hands_drawn}
                                Number of Hands = {hands}
                                Amount Lost = ${(1000 - user_bank):,}
                                Final Amount = ${user_bank:,}
                                ''')
                        # CONTINUE TO FIRST WHILE STATEMENT (NEXT HAND)
                        

                        start_game, active_hand_status, continue_hitting_user, house_turn, user_card, house_card = end_hand()


                    elif sum_user_cards(user_card) < 21:
                        continue_hitting_user = True # not needed
                        
                        hit_or_stand = input('Do you want to hit or stand? "H for hit and any other key for stand"  ').lower()
                        
                        if hit_or_stand == 'h':
                            print('Oya Hit Me')
                            user_card.append(get_card(cards))
                            print(user_card, house_card)

                            print(f'Your cards: {user_card}, current score: {sum_user_cards(user_card)} ')
                            print(f'Computer\'s first card: : {house_card} ')

                        else:
                            continue_hitting_user = False
                            # house plays, compare results and the set active_hand_status = False











                            print('House will start playing now')
                            house_turn = True
                            while house_turn == True:
                                # give house a card if it has just one card
                                if len(house_card) == 1:
                                    print('\n\n Hitting house its second card...\n')
                                else:
                                    print('\n\n Hitting house its NEXT card...\n')
                                house_card.append(get_card(cards))
                                print(f'House Cards: {house_card} ')

                                # Sum house cards
                                house_total = sum_house_cards(house_card)
                                print(f'House Total: {house_total} ')

                                # check for house next action
                                house_next_action_var = house_next_action(house_total, house_card)
                                print(f'house_next_action: {house_next_action_var} ')
                                
                                # if hit, give a card, else 
                                if house_next_action_var == 'hit':
                                    # house_card.append(get_card(cards))
                                    continue
                                elif house_next_action_var == 'bust':
                                    # End this hand, ask user for another round, add winings/losses
                                    print(f'Bust!!!, your score is {house_card} {sum_house_cards(house_card)}, User wins this hand with a score of {user_card} {sum_user_cards(user_card)} ')

                                    user_bank += (amount*2)
                                    hands_won += 1

                                    # STATUS
                                    if user_bank > 1000:
                                        print(f'''
                                                Hand has ended
                                                Hands won = {hands_won}
                                                Hands lost = {hands_lost}
                                                Hands Drawn = {hands_drawn}
                                                Number of Hands = {hands}
                                                Amount Won = ${(user_bank - 1000):,}
                                                Final Amount = ${user_bank:,}
                                                ''')
                                    else:
                                        print(f'''
                                                Hand has ended
                                                Hands won = {hands_won}
                                                Hands lost = {hands_lost}
                                                Hands Drawn = {hands_drawn}
                                                Number of Hands = {hands}
                                                Amount Lost = ${(1000 - user_bank):,}
                                                Final Amount = ${user_bank:,}
                                                ''')
                                        






                                    # print('Busted!!!')
                                    house_turn = False

                                    # this is supposed to end the hand
                                    start_game, active_hand_status, continue_hitting_user, house_turn, user_card, house_card = end_hand()

                                else:
                                    # House stands, compare results

                                    hand_result = compare_cards(house_card, user_card)

                                    if hand_result == 'user':
                                        hands_won += 1
                                        user_bank += (amount*2)
                                        # STATUS
                                        if user_bank > 1000:
                                            print(f'''
                                                Hand has ended
                                                Hands won = {hands_won}
                                                Hands lost = {hands_lost}
                                                Hands Drawn = {hands_drawn}
                                                Number of Hands = {hands}
                                                Amount Won = ${(user_bank - 1000):,}
                                                Final Amount = ${user_bank:,}
                                                ''')
                                        else:
                                            print(f'''
                                                Hand has ended
                                                Hands won = {hands_won}
                                                Hands lost = {hands_lost}
                                                Hands Drawn = {hands_drawn}
                                                Number of Hands = {hands}
                                                Amount Lost = ${(1000 - user_bank):,}
                                                Final Amount = ${user_bank:,}
                                                ''')
                                            
                                        
                                    elif hand_result == 'house':
                                        hands_lost += 1
                                        # STATUS
                                        if user_bank > 1000:
                                            print(f'''
                                                Hand has ended
                                                Hands won = {hands_won}
                                                Hands lost = {hands_lost}
                                                Hands Drawn = {hands_drawn}
                                                Number of Hands = {hands}
                                                Amount Won = ${(user_bank - 1000):,}
                                                Final Amount = ${user_bank:,}
                                                ''')
                                        else:
                                            print(f'''
                                                Hand has ended
                                                Hands won = {hands_won}
                                                Hands lost = {hands_lost}
                                                Hands Drawn = {hands_drawn}
                                                Number of Hands = {hands}
                                                Amount Lost = ${(1000 - user_bank):,}
                                                Final Amount = ${user_bank:,}
                                                ''')
                                            
                                    else:
                                        # draw
                                        hands_drawn += 1
                                        # refund user
                                        user_bank += amount
                                        print(f'Amount {amount} returned')
                                        # STATUS
                                        if user_bank > 1000:
                                            print(f'''
                                                Hand has ended
                                                Hands won = {hands_won}
                                                Hands lost = {hands_lost}
                                                Hands Drawn = {hands_drawn}
                                                Number of Hands = {hands}
                                                Amount Won = ${(user_bank - 1000):,}
                                                Final Amount = ${user_bank:,}
                                                ''')
                                        else:
                                            print(f'''
                                                Hand has ended
                                                Hands won = {hands_won}
                                                Hands lost = {hands_lost}
                                                Hands Drawn = {hands_drawn}
                                                Number of Hands = {hands}
                                                Amount Lost = ${(1000 - user_bank):,}
                                                Final Amount = ${user_bank:,}
                                                ''')
                                            

                                    house_turn = False
                                    active_hand_status = False
                                    start_game = 'n'
                                    # compare cards
                                    print(house_card)
                                    print(user_card)
                                    print(hand_result)
                                    print('Hand ends')

                                    start_game, active_hand_status, continue_hitting_user, house_turn, user_card, house_card = end_hand()
                                
                        
                    else:
                        # No action
                        pass
                
        except Exception as e: # amount is invalid
            print(e)
            print('Wrong amount entered, game is quitting... ')
            active_hand_status = False
            start_game = 'n'

        # check if user wants to continue playing
        # clearConsole()

    # Play again or quit

    
# all_game_stats_win = f'''
#                 Game has ended
#                 Hands won = {hands_won}
#                 Hands lost = {hands_lost}
#                 Hands Drawn = {hands_drawn}
#                 Number of Hands = {hands}
#                 Amount Won = ${(user_bank - 1000):,}
#                 Final Amount = ${user_bank:,}
#                 '''

# all_game_stats_lost = f'''
#                 Game has ended
#                 Hands won = {hands_won}
#                 Hands lost = {hands_lost}
#                 Hands Drawn = {hands_drawn}
#                 Number of Hands = {hands}
#                 Amount Lost = ${(1000 - user_bank):,}
#                 Final Amount = ${user_bank:,}
#                 '''

    

    



    