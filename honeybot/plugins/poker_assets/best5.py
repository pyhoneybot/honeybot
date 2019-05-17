''' poker hand evaluator '''

# pylint: disable=W0612

import itertools

def best_hand(hand):
    ''' from a 7-card hand, return the best 5 card hand '''

    return max(itertools.combinations(hand, 5), key=hand_rank)

def hand_rank(hand):
    ''' return a value indicating the ranking of a hand '''

    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return 8, max(ranks)

    elif kind(4, ranks):
        # four of a kind
        return 7, kind(4, ranks), kind(1, ranks)

    elif kind(3, ranks) and kind(2, ranks):
        # full house
        return 6, kind(3, ranks), kind(2, ranks)

    elif flush(hand):
        # all cards of same suit
        return 5, ranks

    elif straight(ranks):
        # cards in sequence
        return 4, max(ranks)

    elif kind(3, ranks):
        # 3 cards of same rank
        return 3, kind(3, ranks), ranks

    elif two_pair(ranks):
        # 2 pairs of same rank
        return 2, two_pair(ranks), ranks

    elif kind(2, ranks):
        # 1 pair of same rank
        return 1, kind(2, ranks), ranks

    else:
        # Nothing (High Card)
        return 0, ranks

def card_ranks(hand):
    ''' return a list of the ranks, sorted with higher first '''

    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    # to handle the (A-5) straight case
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def flush(hand):
    ''' return True if all the cards have the same suit '''

    suits = [s for r, s in hand]
    return len(set(suits)) == 1

def straight(ranks):
    ''' return True if the ordered ranks form a 5-card straight '''

    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

def kind(n, ranks):
    ''' return the first rank that this hand has exactly n-of-a-kind of. Return None if there is no
    n-of-a-kind in the hand '''

    for r in ranks:

        if ranks.count(r) == n:
            return r

    return None

def two_pair(ranks):
    ''' if there are two pair here, return the two ranks of the two pairs, else None '''

    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return pair, lowpair

    else:
        return None

def test_best_hand(playerhand):
    # S = Spade
    # D = Diamond
    # C = Club
    # H = Heart
    # assert (sorted(best_hand('6C 7C 8C 9C TC 5C JS'.split())) == ['6C', '7C', '8C', '9C', 'TC'])
    # assert (sorted(best_hand('TD TC TH 7C 7D 8C 8S'.split())) == ['8C', '8S', 'TC', 'TD', 'TH'])
    # assert (sorted(best_hand('JD TC TH 7C 7D 7S 7H'.split())) == ['7C', '7D', '7H', '7S', 'JD'])
    # return 'test_best_hand passes'
    # return sorted(best_hand('2D 2C 2H 7C 7D KC KS'.split()))
    return sorted(best_hand(playerhand.split()))
