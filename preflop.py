import random


def raise_first_in(position, hand):
    # utg and utg+1 have same rfi ranges
    utg = {"AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "AKs", "AQs", "AJs", "ATs", "A5s",
           "KQs", "KJs", "KTs", "QJs", "QTs", "JTs", "J9s", "T9s", "98s",
           "AKo", "AQo"}
    utg2 = {"AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "AKs", "AQs", "AJs", "ATs", "A9s", "A8s", "A5s", "A4s",
            "KQs", "KJs", "KTs", "K9s", "QJs", "QTs", "Q9s", "JTs", "J9s", "T9s", "98s",
            "AKo", "AQo", "AJo"}
    lj = {"AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "55",
          "AKs", "AQs", "AJs", "ATs", "A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s",
          "KQs", "KJs", "KTs", "K9s", "QJs", "QTs", "Q9s", "JTs", "J9s", "T9s", "98s", "87s", "76s",
          "AKo", "AQo", "AJo", "KQo"}
    hj = {"AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "55", "44",
          "AKs", "AQs", "AJs", "ATs", "A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s",
          "KQs", "KJs", "KTs", "K9s", "QJs", "QTs", "Q9s", "JTs", "J9s", "T9s", "T8s", "98s", "97s", "87s", "76s", "65s",
          "AKo", "AQo", "AJo", "ATo", "KQo", "KJo", "QJo"}
    co = {"AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "55", "44", "33", "22",
          "AKs", "AQs", "AJs", "ATs", "A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s",
          "KQs", "KJs", "KTs", "K9s", "K8s", "QJs", "QTs", "Q9s", "Q8s", "JTs", "J9s", "J8s", "T9s", "T8s",
          "98s", "97s", "87s", "86s", "76s", "65s", "54s",
          "AKo", "AQo", "AJo", "ATo", "KQo", "KJo", "KTo", "QJo", "QTo", "JTo"}
    btn = {"AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "55", "44", "33", "22",
           "AKs", "AQs", "AJs", "ATs", "A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s",
           "KQs", "KJs", "KTs", "K9s", "K8s", "K7s", "K6s", "K5s", "K4s", "K3s",
           "QJs", "QTs", "Q9s", "Q8s", "Q7s", "Q6s", "Q5s",
           "JTs", "J9s", "J8s", "J7s", "J6s", "T9s", "T8s", "T7s", "T6s",
           "98s", "97s",  "96s", "87s", "86s", "85s", "76s", "75s", "65s", "64s", "54s", "43s",
           "AKo", "AQo", "AJo", "ATo", "A9o", "A8o", "A7o", "A6o", "A5o", "A4o", "A3o", "A2o",
           "KQo", "KJo", "KTo", "K9o", "QJo", "QTo", "Q9o", "JTo", "J9o", "T9o"}
    sb = {"AA", "KK", "QQ", "JJ", "TT", "99", "88", "77", "66", "55", "44", "33", "22",
          "AKs", "AQs", "AJs", "ATs", "A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s",
          "KQs", "KJs", "KTs", "K9s", "K8s", "K7s", "K6s", "K5s", "K4s", "K3s", "K2s",
          "QJs", "QTs", "Q9s", "Q8s", "Q7s", "Q6s", "Q5s", "Q4s",
          "JTs", "J9s", "J8s", "J7s", "J6s", "T9s", "T8s", "T7s", "T6s",
          "98s", "97s", "96s", "95s", "87s", "86s", "85s", "84s", "76s", "75s", "74s",
          "65s", "64s", "63s", "54s", "53s", "43s", "32s",
          "AKo", "AQo", "AJo", "ATo", "A9o", "A8o", "A7o", "A6o", "A5o", "A4o", "A3o", "A2o",
          "KQo", "KJo", "KTo", "K9o", "K8o", "QJo", "QTo", "Q9o", "Q8o", "JTo", "J9o", "J8o", "T9o", "T8o", "98o"}

    # it is not possible to be in RFI situation on BB
    ranges = {"utg": utg, "utg1": utg, "utg2": utg2, "lj": lj, "hj": hj, "co": co, "btn": btn, "sb": sb, "bb": {}}
    return hand in ranges[position]


def preflop_3bet_defense(position, hand):
    # for speed purposes, eliminating any hands with < 50% chance of calling or raising, combined
    if position == "sb":
        hands = {"AA": (0, 100), "AKs": (0, 100), "AQs": (50, 50), "AJs": (75, 25), "ATs": (100, 0), "A9s": (100, 0),
                 "A8s": (100, 0), "A7s": (100, 0), "A6s": (78, 0), "A4s": (67, 33), "A3s": (100, 0),
                 "AKo": (0, 100), "KK": (0, 100), "KQs": (55, 45), "KJs": (33, 33), "KTs": (40, 60), "K9s": (0, 100),
                 "K8s": (67, 0), "K7s": (17, 50), "K5s": (100, 0),
                 "AQo": (20, 80), "KQo": (33, 33), "QQ": (0, 100), "QJs": (20, 80), "QTs": (0, 100), "Q9s": (62, 0),
                 "AJo": (50, 50), "KJo": (40, 20), "JJ": (0, 100), "JTs": (71, 29), "J9s": (100, 0),
                 "ATo": (71, 0), "TT": (67, 33), "T9s": (14, 57), "T8s": (71, 0),
                 "99": (50, 50), "88": (75, 25), "77": (100, 0), "66": (75, 25), "55": (88, 12), "44": (100, 0),
                 "33": (78, 0), "22": (75, 0),
                 "98s": (100, 0), "76s": (0, 100), "65s": (0, 100), "54s": (50, 50)}
    elif position == "bb":
        hands = {"AA": (0, 100), "AKs": (0, 100), "AQs": (25, 75), "AJs": (100, 0), "ATs": (100, 0), "A9s": (100, 0),
                 "A8s": (100, 0), "A7s": (100, 0), "A6s": (100, 0), "A5s": (100, 0), "A4s": (100, 0), "A3s": (100, 0),
                 "A2s": (100, 0),
                 "AKo": (8, 83), "KK": (0, 100), "KQs": (0, 67), "KJs": (60, 0), "KTs": (33, 17), "K9s": (100, 0),
                 "K8s": (100, 0), "K7s": (71, 14), "K6s": (100, 0), "K5s": (67, 0), "K4s": (80, 0), "K3s": (88, 0),
                 "K2s": (100, 0),
                 "AQo": (10, 90), "KQo": (50, 40), "QQ": (0, 100), "QJs": (33, 33), "QTs": (33, 33), "Q9s": (100, 0),
                 "Q8s": (80, 0), "Q7s": (88, 0), "Q6s": (75, 0), "Q5s": (60, 0), "Q4s": (100, 0), "Q3s": (71, 0),
                 "Q2s": (100, 0),
                 "AJo": (75, 25), "KJo": (95, 0), "QJ": (54, 15), "JJ": (40, 60), "JTs": (50, 33), "J9s": (50, 50),
                 "J8s": (67, 0), "J7s": (80, 0), "J4s": (100, 0), "J3s": (57, 0),
                 "ATo": (100, 0), "KTo": (33, 17), "QTo": (73, 0), "JTo": (78, 0), "TT": (50, 50), "T9s": (50, 50),
                 "T8s": (50, 0), "T7s": (57, 0), "T6s": (100, 0), "T5s": (100, 0), "T4s": (75, 0),
                 "99": (67, 0), "88": (50, 0), "77": (100, 0), "66": (50, 50), "55": (100, 0), "44": (80, 0),
                 "33": (83, 0), "22": (100, 0),
                 "A9o": (76, 0), "Q9o": (50, 0), "J9o": (54, 15), "T9o": (62, 12), "98s": (100, 0), "96s": (100, 0),
                 "95s": (57, 0), "93s": (50, 0),
                 "A8o": (67, 0), "K8o": (67, 0), "T8o": (53, 0), "87s": (20, 40), "85s": (100, 0), "84s": (50, 0),
                 "82s": (50, 0),
                 "A7o": (54, 0), "76s": (25, 75), "75s": (100, 0), "74s": (100, 0),
                 "A6o": (54, 8), "76o": (73, 0), "65s": (0, 86), "64s": (80, 0), "63s": (67, 0),
                 "A5o": (30, 20), "K5o": (40, 10), "65o": (64, 0), "54s": (50, 40), "53s": (50, 0), "52s": (50, 0),
                 "A4o": (55, 9), "54o": (75, 0), "43s": (62, 12), "42s": (78, 0), "32s": (100, 0)}
    else:
        hands = {"AA": (0, 100), "AKs": (0, 100), "AQs": (80, 20), "AJs": (100, 0), "ATs": (25, 75), "A9s": (44, 22),
                 "A8s": (67, 33), "A7s": (56, 22), "A5s": (25, 50), "A4s": (75, 25), "A3s": (33, 33), "A2s": (25, 25),
                 "AKo": (17, 83), "KK": (0, 100), "KQs": (75, 25), "KJs": (50, 50), "KTs": (62, 38), "K9s": (0, 56),
                 "AQo": (42, 47), "KQo": (11, 39), "QQ": (60, 40), "QJs": (60, 40), "QTs": (40, 20),
                 "JJ": (43, 57), "JTs": (75, 25), "TT": (25, 50), "T9s": (50, 0), "T8s": (50, 0),
                 "99": (44, 44), "88": (70, 20), "77": (90, 10), "66": (38, 25), "55": (50, 33), "44": (50, 0),
                 "76s": (11, 56)}

    t = (0, 0)
    if hand in hands:
        t = hands[hand]
    num = random.randint(0, 100)
    if num < t[0]:
        return "Call"
    elif num < t[0]+t[1]:
        return "Raise"
    return "Fold"


def preflop_4or5bet_defense(hand):
    hands = {"AA": (0, 100), "AKs": (0, 100), "KK": (0, 100), "QQ": (40, 60), "AKo": (50, 50), "JJ": (50, 0)}
    t = (0, 0)
    if hand in hands:
        t = hands[hand]
    num = random.randint(0, 100)
    if num < t[0]:
        return "Call"
    elif num < t[0]+t[1]:
        return "Raise"
    return "Fold"
