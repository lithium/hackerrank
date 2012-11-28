#!/bin/python

def calculate(dist,my_moves,their_moves,draw=1):
    i_have = 100.0
    they_have = 100.0

    for i in range(0,len(my_moves)):
        if my_moves[i] > their_moves[i]:
            who_won = 'me'
        elif my_moves[i] < their_moves[i]:
            who_won = 'them'
        else:
            who_won = 'me' if draw else 'them'
            draw = 0 if draw else 1

        if who_won == 'me':
            i_have -= my_moves[i]
        elif who_won == 'them':
            they_have -= their_moves[i]

    if dist < 2:
        return int(i_have)

    q = i_have/dist + dist/they_have + 1

    return max(1,min(int(round(q)),i_have))








def calculate_bid(player,pos,first_moves,second_moves):
    """your logic here"""
    if player == 1:
        return calculate(pos,first_moves,second_moves,1)
    return calculate(11 - pos,second_moves,first_moves,0)


#gets the id of the player
player = input()

scotch_pos = input()         #current position of the scotch

first_moves = [int(i) for i in raw_input().split()]
second_moves = [int(i) for i in raw_input().split()]
bid = calculate_bid(player,scotch_pos,first_moves,second_moves)
print bid
