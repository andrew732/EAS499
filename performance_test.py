import poker_bot
import time
import numpy as np
import random
import itertools

# runtime of preflop_action
def test_preflop():
    positions = ["bb", "sb", "btn", "co", "hj", "lj", "utg2", "utg1", "utg"]
    numbers = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    bets = [2, 6, 20]
    no_limpers = 2
    times = []

    for last_bet in bets:
        three_bet = last_bet == 20
        for position in positions:
            for i in range(len(numbers)):
                for j in range(i, len(numbers)):
                    cards = numbers[i]+numbers[j]
                    if i == j:
                        hand = cards
                        start = time.time()
                        poker_bot.preflop_action(hand, position, last_bet, no_limpers, three_bet=three_bet)
                        length = time.time()-start
                        times.append(length)
                    else:
                        hand = cards+'o'
                        start = time.time()
                        poker_bot.preflop_action(hand, position, last_bet, no_limpers, three_bet=three_bet)
                        length = time.time() - start
                        times.append(length)
                        hand = cards+'s'
                        start = time.time()
                        poker_bot.preflop_action(hand, position, last_bet, no_limpers, three_bet=three_bet)
                        length = time.time() - start
                        times.append(length)

    print("Number of iterations: "+str(len(times)))
    print("Average runtime: "+str(np.mean(times)))
    print("Standard Deviation runtime: "+str(np.std(times)))


# runtime of preflop_action
def test_betting_round_1(opponents):
    numbers = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    suits = ['h', 'c', 's', 'd']
    times = []
    pot = 50
    bets = [0, 30]
    types = [2, 3, 4]

    for bet in bets:
        for pot_type in types:
            for i in range(len(numbers)):
                for j in range(i, len(numbers)):
                    if i == j:
                        for suit1, suit2 in itertools.combinations(suits, 2):
                            cards = numbers[i]+suit1+numbers[j]+suit2
                            used = {numbers[i]+suit1, numbers[j]+suit2}
                            for i in range(10):
                                board_cards = ""
                                while len(board_cards) < 6:
                                    candidate_number = random.randint(0, 12)
                                    candidate_suit = random.randint(0, 3)
                                    card = numbers[candidate_number]+suits[candidate_suit]
                                    if card not in used:
                                        used.add(card)
                                        board_cards += card
                                # if len(times) % 1000 == 0:
                                #     print(len(times))
                                start = time.time()
                                poker_bot.betting_round_1(cards, board_cards, opponents, bet, pot, pot_type=pot_type)
                                length = time.time()-start
                                times.append(length)
                    else:
                        for suit1, suit2 in zip(suits, suits):
                            cards = numbers[i]+suit1+numbers[j]+suit2
                            used = {numbers[i]+suit1, numbers[j]+suit2}
                            for i in range(10):
                                board_cards = ""
                                while len(board_cards) < 6:
                                    candidate_number = random.randint(0, 12)
                                    candidate_suit = random.randint(0, 3)
                                    card = numbers[candidate_number]+suits[candidate_suit]
                                    if card not in used:
                                        used.add(card)
                                        board_cards += card
                                # if len(times) % 1000 == 0:
                                #     print(len(times))
                                start = time.time()
                                poker_bot.betting_round_1(cards, board_cards, opponents, bet, pot, pot_type=pot_type)
                                length = time.time()-start
                                times.append(length)

    print("Number of iterations: "+str(len(times)))
    print("Average runtime: "+str(np.mean(times)))
    print("Standard Deviation runtime: "+str(np.std(times)))


# runtime of preflop_action
def test_betting_round_2(opponents):
    numbers = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    suits = ['h', 'c', 's', 'd']
    times = []
    pot = 50
    bets = [0, 30]
    types = [2, 3, 4]

    for bet in bets:
        for pot_type in types:
            for i in range(len(numbers)):
                for j in range(i, len(numbers)):
                    if i == j:
                        for suit1, suit2 in itertools.combinations(suits, 2):
                            cards = numbers[i]+suit1+numbers[j]+suit2
                            used = {numbers[i]+suit1, numbers[j]+suit2}
                            for i in range(10):
                                board_cards = ""
                                while len(board_cards) < 8:
                                    candidate_number = random.randint(0, 12)
                                    candidate_suit = random.randint(0, 3)
                                    card = numbers[candidate_number]+suits[candidate_suit]
                                    if card not in used:
                                        used.add(card)
                                        board_cards += card
                                # if len(times) % 1000 == 0:
                                #     print(len(times))
                                start = time.time()
                                poker_bot.betting_round_2(cards, board_cards, opponents, bet, pot, pot_type=pot_type)
                                length = time.time()-start
                                times.append(length)
                    else:
                        for suit1, suit2 in zip(suits, suits):
                            cards = numbers[i]+suit1+numbers[j]+suit2
                            used = {numbers[i]+suit1, numbers[j]+suit2}
                            for i in range(10):
                                board_cards = ""
                                while len(board_cards) < 8:
                                    candidate_number = random.randint(0, 12)
                                    candidate_suit = random.randint(0, 3)
                                    card = numbers[candidate_number]+suits[candidate_suit]
                                    if card not in used:
                                        used.add(card)
                                        board_cards += card
                                # if len(times) % 1000 == 0:
                                #     print(len(times))
                                start = time.time()
                                poker_bot.betting_round_2(cards, board_cards, opponents, bet, pot, pot_type=pot_type)
                                length = time.time()-start
                                times.append(length)

    print("Number of iterations: "+str(len(times)))
    print("Average runtime: "+str(np.mean(times)))
    print("Standard Deviation runtime: "+str(np.std(times)))


# runtime of preflop_action
def test_river(opponents):
    numbers = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    suits = ['h', 'c', 's', 'd']
    times = []
    pot = 50
    bets = [0, 30]
    types = [2, 3, 4]

    for bet in bets:
        for pot_type in types:
            for i in range(len(numbers)):
                for j in range(i, len(numbers)):
                    if i == j:
                        for suit1, suit2 in itertools.combinations(suits, 2):
                            cards = numbers[i]+suit1+numbers[j]+suit2
                            used = {numbers[i]+suit1, numbers[j]+suit2}
                            for i in range(10):
                                board_cards = ""
                                while len(board_cards) < 10:
                                    candidate_number = random.randint(0, 12)
                                    candidate_suit = random.randint(0, 3)
                                    card = numbers[candidate_number]+suits[candidate_suit]
                                    if card not in used:
                                        used.add(card)
                                        board_cards += card
                                # if len(times) % 1000 == 0:
                                #     print(len(times))
                                start = time.time()
                                poker_bot.river_action(cards, board_cards, opponents, bet, pot, pot_type=pot_type)
                                length = time.time()-start
                                times.append(length)
                    else:
                        for suit1, suit2 in zip(suits, suits):
                            cards = numbers[i]+suit1+numbers[j]+suit2
                            used = {numbers[i]+suit1, numbers[j]+suit2}
                            for i in range(10):
                                board_cards = ""
                                while len(board_cards) < 10:
                                    candidate_number = random.randint(0, 12)
                                    candidate_suit = random.randint(0, 3)
                                    card = numbers[candidate_number]+suits[candidate_suit]
                                    if card not in used:
                                        used.add(card)
                                        board_cards += card
                                # if len(times) % 1000 == 0:
                                #     print(len(times))
                                start = time.time()
                                poker_bot.river_action(cards, board_cards, opponents, bet, pot, pot_type=pot_type)
                                length = time.time()-start
                                times.append(length)

    print("Number of iterations: "+str(len(times)))
    print("Average runtime: "+str(np.mean(times)))
    print("Standard Deviation runtime: "+str(np.std(times)))


test_preflop()
test_betting_round_1(1)
test_betting_round_1(2)
test_betting_round_2(1)
test_betting_round_2(2)
test_river(1)
test_river(2)