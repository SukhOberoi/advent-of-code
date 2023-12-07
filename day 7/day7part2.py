def card_type(hand):
    if "J" in hand and hand != "JJJJJ":
        lens = {}
        for char in hand:
            if char != "J":
                if lens.get(char):
                    lens[char]+=1
                else:
                    lens[char]=1
        vals= list(lens.values())
        hand = hand.replace("J", list(lens.keys())[vals.index(max(vals))])
    hand = list(hand)
    uniqueCards = len(set(hand))
    match uniqueCards:
        case 5:
            return 7 #high card
        case 4:
            return 6 #one pair
        case 3:
            for i in range(3):
                if hand.count(hand[i])==3:
                    return 4 #three of a kid
            return 5  #2 pairs
        case 2:
            for i in range(2):
                if hand.count(hand[i])==4:
                    return 2 #4 of a kind
            return 3 #full house
        case 1:
            return 1 #5 of a kind
        
        
order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
def compare(hand1, hand2):
    if hand1[-1]<hand2[-1]:
        return -1
    elif hand1[-1]>hand2[-1]:
        return 1
    else:
        i=0
        while hand1[0][i]==hand2[0][i]:
            i+=1
        if order.index(hand1[0][i])<order.index(hand2[0][i]):
            return -1
        else:
            return 1
        
        
from functools import cmp_to_key
with open("day 7\\input.txt", "r") as file:
    data = file.read()
    data = data.split()
    typelist = list(zip(data[::2], [int(x) for x in data[1::2]], [card_type(x) for x in data[::2]]))
    typelist = sorted(typelist, key= cmp_to_key(compare), reverse=True)
    winnings=0
    for index, handtuple in enumerate(typelist):
        winnings+=handtuple[1]*(index+1)
    print(winnings)