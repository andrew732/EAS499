Poker Bot
=================

This is the code for the poker bot for my EAS 499 thesis.


Installation
-----

1) Users must first clone and install pyeval7 from https://github.com/julianandrews/pyeval7, as parts of the code uses some 
functions in the eval7 folder of the library (1).
2) Simply run the poker bot programs in the same project that has the eval7 folder 
(i.e. set eval7 as a source root in PyCharm)


Files Contained
-----

1) performance_test.py - list of all the timing tests to run, presented in section 5.3.3
2) poker_bot.py - the poker bot itself, with all functions listed in section 5.3.2
3) preflop.py - converted preflop charts in dictionary/python form (2)(3)


API Calls for poker_bot.py
-----

1) preflop_action(hand, position, last_bet, no_limpers, three_bet=False, stack=500, bb=5)
2) betting_round_1(cards, board_cards, opponents, bet, pot, preflop_agg=False, position=False, stack=500, raised=False, pot_type=2)
3) betting_round_2(cards, board_cards, opponents, bet, pot, preflop_agg=False, position=False, stack=500, raised=False, pot_type=2)
4) river_action(cards, board_cards, opponents, bet, pot, raised=False, first_bet=False, pot_type=2)

Sources
-----
(1) Julianandrews. (2015, November 29). pyeval7. Retrieved from https://github.com/julianandrews/pyeval7
(2) Upswing Poker. (n.d.). Preflop Guide: Raising First In. Preflop Guide: Raising First In. Retrieved from https://upswingpoker.com/wp-content/uploads/2018/02/Preflop-Guide-for-RFI-v21-1.pdf
(3) Pierre. (2019, July 30). Pluribus Poker Preflop Defense Detailed part 1 of 2. Retrieved from https://pluribus-poker-ai.com/2019/08/05/pluribus-poker-preflop-defense-detailed/
