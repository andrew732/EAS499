import preflop
import eval7


def preflop_action(hand, position, last_bet, no_limpers, three_bet=False, stack=500, bb=5):
    # rewrite hand to preflop format
    if len(hand) == 4:
        if hand[0] == hand[2]:
            hand = hand[0]+hand[2]
        elif hand[1] == hand[3]:
            hand = hand[0]+hand[2]+"s"
        else:
            hand = hand[0]+hand[2]+"o"

    # if not a 3 or 4 bet possibility
    if last_bet == bb:
        # if told to raise first in, raise
        # has limpers, play tighter
        if preflop.raise_first_in(position, hand):
            action = ("Raise", (3+no_limpers)*bb)
        else:
            # don't fold if check is possible
            if position == "bb":
                if preflop.preflop_3bet_defense(position, hand) == "Raise":
                    action = ("Raise", (3+no_limpers)*bb)
                else:
                    action = ("Check", )
            else:
                action = ("Fold", )

        if no_limpers > 0:
            if hand not in {'AA', 'AKs', 'AQs', 'AJs', 'AKo', 'KK', 'KQs', 'KJs', 'AQo', 'KQo', 'QQ', 'JJ', 'TT'} and \
                    action[0] == "Raise":
                action = ("Call", )
    else:
        if three_bet:
            action = (preflop.preflop_4or5bet_defense(hand), )
        else:
            action = (preflop.preflop_3bet_defense(position, hand), )

        if action[0] == "Raise":
            action = ("Raise", 3*last_bet+no_limpers*bb)

    # short stacked, should jam
    if action[0] == "Raise":
        if stack <= 10*bb:
            return "Raise "+str(stack)
        else:
            return "Raise "+str(action[1])
    return action[0]


def good_flush_draw(cards, board):
    suits = cards[1::2] + board[1::2]
    counts = [suits.count(i) for i in ['h', 'd', 'c', 's']]
    if max(counts) <= 3:
        return False
    # if suited
    elif cards[1] == cards[3] and max(counts) == 4:
        return True
    else:
        if max(counts) >= 4:
            if cards[1] == counts.index(max(counts)):
                return cards[0] in ['A', 'K', 'Q']
            else:
                return cards[2] in ['A', 'K', 'Q']


def four_to_flush(board):
    suits = board[1::2]
    return max([suits.count(i) for i in ['h', 'd', 'c', 's']]) >= 4


def oesd(cards, board):
    nums = list(set(cards[::2] + board[::2]))
    casted_nums = []
    for num in nums:
        if num == 'A':
            casted_nums.append(1)
            casted_nums.append(14)
        elif num == 'K':
            casted_nums.append(13)
        elif num == 'Q':
            casted_nums.append(12)
        elif num == 'J':
            casted_nums.append(11)
        elif num == 'T':
            casted_nums.append(10)
        else:
            casted_nums.append(int(num))
    consec = 0
    max_consec = 0
    casted_nums.sort()
    for first, second in zip(casted_nums, casted_nums[1:]):
        if first == second - 1:
            consec += 1
        else:
            # if you don't have A234
            if first != 4:
                max_consec = max(max_consec, consec)
            consec = 0
    # if you don't have JQKA
    if not (casted_nums[-1] == 14 and consec == 3):
        max_consec = max(max_consec, consec)
    return max_consec >= 3


def four_to_straight(board):
    nums = list(set(board[::2]))
    casted_nums = []
    for num in nums:
        if num == 'A':
            casted_nums.append(1)
            casted_nums.append(14)
        elif num == 'K':
            casted_nums.append(13)
        elif num == 'Q':
            casted_nums.append(12)
        elif num == 'J':
            casted_nums.append(11)
        elif num == 'T':
            casted_nums.append(10)
        else:
            casted_nums.append(int(num))
    consec = 0
    max_consec = 0
    casted_nums.sort()
    for first, second in zip(casted_nums, casted_nums[1:]):
        if first == second - 1:
            consec += 1
        else:
            max_consec = max(max_consec, consec)
            consec = 0
    max_consec = max(max_consec, consec)
    return max_consec == 3


def tpttk(cards, board):
    board = list(board[::2])
    casted_board = []
    for num in board:
        if num == 'A':
            casted_board.append(14)
        elif num == 'K':
            casted_board.append(13)
        elif num == 'Q':
            casted_board.append(12)
        elif num == 'J':
            casted_board.append(11)
        elif num == 'T':
            casted_board.append(10)
        else:
            casted_board.append(int(num))
    cards = list(cards[::2])
    casted_cards = []
    for num in cards:
        if num == 'A':
            casted_cards.append(14)
        elif num == 'K':
            casted_cards.append(13)
        elif num == 'Q':
            casted_cards.append(12)
        elif num == 'J':
            casted_cards.append(11)
        elif num == 'T':
            casted_cards.append(10)
        else:
            casted_cards.append(int(num))
    if max(casted_cards) == max(casted_board):
        casted_cards.remove(max(casted_cards))
        # next highest card is Q or better
        if max(casted_cards) >= 12:
            return True
    return False


def play_the_board(cards, board_cards):
    hand = [eval7.Card(s) for s in (cards[:2], cards[2:])]
    board = [eval7.Card(s) for s in [board_cards[i:i+2] for i in range(0, len(board_cards), 2)]]
    hand_type = eval7.hand_type(eval7.evaluate(hand + board))
    board_type = eval7.hand_type(eval7.evaluate(board))

    if hand_type != board_type:
        return False
    # cannot have a higher pair/trips
    elif hand_type in ['High Card', 'Pair', 'Trips']:
        return True
    # can have a higher two pair, if evaluation is highly different
    elif hand_type in ['Two Pair']:
        # do something
        numbers = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        return [2 if (cards+board_cards)[::2].count(i) == 2 else 0 for i in numbers] == \
               [2 if board_cards[::2].count(i) == 2 else 0 for i in numbers]
    # five card hands will evaluate to the same
    else:
        return eval7.evaluate(hand+board) == eval7.evaluate(board)


def paired_card(board_cards):
    board = list(board_cards[::2])
    casted_board = []
    for num in board:
        if num == 'A':
            casted_board.append(14)
        elif num == 'K':
            casted_board.append(13)
        elif num == 'Q':
            casted_board.append(12)
        elif num == 'J':
            casted_board.append(11)
        elif num == 'T':
            casted_board.append(10)
        else:
            casted_board.append(int(num))
    casted_board.sort(reverse=True)
    for (i, j) in zip(casted_board, casted_board[1:]):
        if i == j:
            return i
    return None


def highest_two_pair(cards, board_cards):
    board = list(board_cards[::2])+list(cards[::2])
    casted_board = []
    for num in board:
        if num == 'A':
            casted_board.append(14)
        elif num == 'K':
            casted_board.append(13)
        elif num == 'Q':
            casted_board.append(12)
        elif num == 'J':
            casted_board.append(11)
        elif num == 'T':
            casted_board.append(10)
        else:
            casted_board.append(int(num))
    casted_board.sort(reverse=True)
    for (i, j) in zip(casted_board, casted_board[1:]):
        if i == j:
            return i
    return None


def betting_round_1(cards, board_cards, opponents, bet, pot, preflop_agg=False, position=False, stack=500, raised=False, pot_type=2):
    action = betting_round_1_wrapped(cards, board_cards, opponents, bet, pot, position=position,
                                     preflop_agg=preflop_agg, raised=raised, pot_type=pot_type)
    if action in ["Fold", "Check"]:
        return action
    elif action == "Call":
        if stack <= bet or stack-bet < 0.1 * (pot+bet):
            return "All In"
        else:
            return action
    else:
        action_bet = action.split(" ")
        amount = float(action_bet[1])
        if stack <= amount or stack-amount < 0.1 * (pot+amount):
            return "All In"
        else:
            return action


def betting_round_1_wrapped(cards, board_cards, opponents, bet, pot, preflop_agg=False, position=False, raised=False, pot_type=2):
    hand = [eval7.Card(s) for s in (cards[:2], cards[2:])]
    board = [eval7.Card(s) for s in [board_cards[i:i+2] for i in range(0, len(board_cards), 2)]]
    current_hand = eval7.hand_type(eval7.evaluate(hand + board))

    if raised:
        if current_hand in ['High Card', 'Pair'] or play_the_board(cards, board_cards):
            return "Fold"
        elif current_hand == 'Two Pair':
            if paired_card(board_cards) and paired_card(board_cards) >= highest_two_pair(cards, board_cards):
                return "Fold"
            return "Call"
        else:
            return "Call"

    # multi-way pot, bluff less
    if opponents > 1:
        # someone bet, only call if have pair, oesd, fd
        if bet > 0:
            if play_the_board(cards, board_cards):
                return "Fold"
            if current_hand == 'High Card':
                # want a good flush draw, or an oesd w/ hole cards
                if bet < pot and (good_flush_draw(cards, board_cards) or
                                  (oesd(cards, board_cards) and not oesd("", board_cards))):
                    return "Call"
                return "Fold"
            elif current_hand == 'Pair' and bet > 0.5 * pot:
                return "Fold"
            else:
                return "Call"

        # no one bet, bet if you are pre-flop aggressor IP
        if (preflop_agg or position) and current_hand != 'High Card' and not play_the_board(cards, board_cards):
            return "Bet "+str(pot/3)
        else:
            return "Check"

    # heads up
    else:
        # since not playing limp pot, pots are either RFI, 3-bet, 4-bet+
        RFI = "22+, 32s, 53s+, 63s+, 74s+, 84s+, 95s+, T6s+, J6s+, " \
              "Q4s+, K2s+, A2s+, A2o+, K8o+, Q8o+, J8o+, T8o+, 98o+"
        TBet = "ATo+, KJo+, QJo+, 44+, 65s, 76s, 87s, 97s+, T8s+, J9s+, Q9s+, K9s+, A2s+"
        FBet = "TT+, AJs+, KQs, AQo+"
        villain_ranges = {2: RFI, 3: TBet, 4: FBet}
        villain = eval7.HandRange(villain_ranges[pot_type])
        equity = eval7.py_hand_vs_range_monte_carlo(hand, villain, board, 1000)

        # someone bet, only call if enough equity
        if bet > 0:
            if equity > bet/(bet+pot):
                return "Call"
            else:
                return "Fold"

        # no one bet, bet if you are pre-flop aggressor and have > 50% equity against range
        if (preflop_agg or position) and equity > 0.5:
            return "Bet "+str(pot/3)
        else:
            return "Check"


def betting_round_2(cards, board_cards, opponents, bet, pot, preflop_agg=False, position=False, stack=500, raised=False, pot_type=2):
    action = betting_round_2_wrapped(cards, board_cards, opponents, bet, pot, position=position,
                                     preflop_agg=preflop_agg, raised=raised, pot_type=pot_type)
    if action in ["Fold", "Check"]:
        return action
    elif action == "Call":
        if stack <= bet or stack-bet < 0.1 * (pot+bet):
            return "All In"
        else:
            return action
    else:
        action_bet = action.split(" ")
        amount = float(action_bet[1])
        if stack <= amount or stack-amount < 0.1 * (pot+amount):
            return "All In"
        else:
            return action


# defined to be the second round of betting (i.e. the turn, if the flop contained betting)
def betting_round_2_wrapped(cards, board_cards, opponents, bet, pot, preflop_agg=False, position=False, raised=False, pot_type=2):
    hand = [eval7.Card(s) for s in (cards[:2], cards[2:])]
    board = [eval7.Card(s) for s in [board_cards[i:i+2] for i in range(0, len(board_cards), 2)]]
    current_hand = eval7.hand_type(eval7.evaluate(hand + board))

    if raised:
        if current_hand in ['High Card', 'Pair', 'Two Pair'] or play_the_board(cards, board_cards):
            return "Fold"
        else:
            return "Call"

    # multi-way pot, bluff less
    if opponents > 1:
        # someone bet again, only call if have top pair (if bet < pot) or better
        if bet > 0:
            if play_the_board(cards, board_cards):
                return "Fold"
            if current_hand == 'High Card':
                return "Fold"
            elif current_hand == 'Pair':
                if not tpttk(cards, board_cards):
                    return "Fold"
                else:
                    return "Call"
            elif current_hand == 'Two Pair':
                if paired_card(board_cards):
                    return "Fold"
                return "Call"
            else:
                return "Call"

        # no one bet, bet if you are pre-flop aggressor IP
        if (preflop_agg or position) and current_hand not in ['High Card', 'Pair'] and \
                not play_the_board(cards, board_cards):
            return "Bet " + str(pot * 0.70)
        else:
            return "Check"

    # heads up
    else:
        # since not playing limp pot, pots are either RFI, 3-bet, 4-bet+
        RFI = "22+, 32s, 53s+, 63s+, 74s+, 84s+, 95s+, T6s+, J6s+, " \
              "Q4s+, K2s+, A2s+, A2o+, K8o+, Q8o+, J8o+, T8o+, 98o+"
        TBet = "ATo+, KJo+, QJo+, 44+, 65s, 76s, 87s, 97s+, T8s+, J9s+, Q9s+, K9s+, A2s+"
        FBet = "TT+, AJs+, KQs, AQo+"
        villain_ranges = {2: RFI, 3: TBet, 4: FBet}
        villain = eval7.HandRange(villain_ranges[pot_type])
        equity = eval7.py_hand_vs_range_monte_carlo(hand, villain, board, 1000)

        # someone bet, only call if above 75% equity, since second bullet
        if bet > 0:
            if equity > 0.75:
                return "Call"
            else:
                return "Fold"

        # no one bet, bet if you are pre-flop aggressor and have > 50% equity against range
        if (preflop_agg or position) and equity > 0.5:
            return "Bet " + str(pot * 0.7)
        else:
            return "Check"


def river_action(cards, board_cards, opponents, bet, pot, stack=500, first_bet=False,
                 raised=False, pot_type=2):
    action = river_action_wrapped(cards, board_cards, opponents, bet, pot, first_bet=first_bet,
                                     raised=raised, pot_type=pot_type)
    if action in ["Fold", "Check"]:
        return action
    elif action == "Call":
        if stack <= bet or stack-bet < 0.1 * (pot+bet):
            return "All In"
        else:
            return action
    else:
        action_bet = action.split(" ")
        amount = float(action_bet[1])
        if stack <= amount or stack-amount < 0.1 * (pot+amount):
            return "All In"
        else:
            return action


def river_action_wrapped(cards, board_cards, opponents, bet, pot, raised=False, first_bet=False, pot_type=2):
    hand = [eval7.Card(s) for s in (cards[:2], cards[2:])]
    board = [eval7.Card(s) for s in [board_cards[i:i + 2] for i in range(0, len(board_cards), 2)]]
    current_hand = eval7.hand_type(eval7.evaluate(hand + board))

    # if you have nuts, raise or jam
    RFI = "22+, 32s, 53s+, 63s+, 74s+, 84s+, 95s+, T6s+, J6s+, " \
          "Q4s+, K2s+, A2s+, A2o+, K8o+, Q8o+, J8o+, T8o+, 98o+"
    TBet = "ATo+, KJo+, QJo+, 44+, 65s, 76s, 87s, 97s+, T8s+, J9s+, Q9s+, K9s+, A2s+"
    FBet = "TT+, AJs+, KQs, AQo+"
    villain_ranges = {2: RFI, 3: TBet, 4: FBet}
    villain = eval7.HandRange(villain_ranges[pot_type])
    equity = eval7.py_hand_vs_range_monte_carlo(hand, villain, board, 1000)

    if raised:
        if equity > 0.99:
            return "Raise "+str(2.5*bet)
        elif equity > 0.95:
            return "Call"
        else:
            return "Fold"

    if equity > 0.97:
        if bet > 0:
            return "Raise "+str(2.5*bet)
        else:
            return "Bet "+str(0.8*pot)

    # else, look into non-raising methods
    # multi-way pot
    if opponents > 1:
        # someone bet, only call if top pair or better (< 2 rounds of bets)
        if bet > 0:
            if first_bet:
                if current_hand != 'High Card' and not play_the_board(cards, board_cards):
                    if current_hand == 'Pair':
                        if not tpttk(cards, board_cards):
                            return "Fold"
                    return "Call"
            if play_the_board(cards, board_cards):
                return "Fold"
            if current_hand == 'High Card' or current_hand == 'Pair':
                return "Fold"
            elif current_hand == 'Two Pair':
                if paired_card(board_cards) and max(list(board_cards[::2])) >= highest_two_pair(cards, board_cards):
                    return "Fold"
                return "Call"
            else:
                return "Call"

        # no one bet, bet if you have trips or better
        if current_hand not in ['High Card', 'Pair', 'Two Pair'] and not play_the_board(cards, board_cards):
            return "Bet " + str(pot*0.8)
        else:
            return "Check"

    # heads up
    else:
        # someone bet, only call if enough equity, above 80%
        if bet > 0:
            if first_bet:
                if equity > bet / (bet + pot):
                    return "Call"
                else:
                    return "Fold"
            elif equity > 0.80:
                return "Call"
            else:
                return "Fold"
        else:
            if equity > 0.80:
                return "Bet " + str(pot*0.8)
            else:
                return "Check"
