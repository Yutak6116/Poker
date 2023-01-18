#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame, sys, random, copy, collections, tkinter
from tkinter import *
from tkinter import messagebox
from pygame.locals import *

a = 0
player1_card1 = 0
player1_card2 = 0
player2_card1 = 0
player2_card2 = 0

p1card1 = 0
p1card2 = 0
p2card1 = 0
p2card2 = 0
bcard1 = 0
bcard2 = 0
bcard3 = 0
bcard4 = 0
bcard5 = 0

tramp_dic = {}
Marks = ['♠','♥','♦','♣']
Numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
dec = []
dec2 = []
def ini():
    global dec
    dec = []
    for i in range(4):
        for j in range(13):
            dec.append((Marks[i],Numbers[j]))

def ini2():
    global dec2
    dec2 = []
    for i in range(4):
        for j in range(13):
            dec2.append((Marks[i],Numbers[j]))   
            
ini()
for i in range(52):
    tramp_dic[dec[i]] = "image" + str(i) + ".png"

def if_flush(hand):
    if hand[0][0] ==  hand[1][0] ==  hand[2][0] ==  hand[3][0] == hand[4][0]:
        return True
    else:
        return False

def if_straight(hand):
    hand_num = []
    for i in range(5):
        hand_num.append(hand[i][1])
    hand_num.sort()  
    
    if hand_num[0]+4 == hand_num[1]+3 == hand_num[2]+2 == hand_num[3]+1 == hand_num[4]:
        return True
    elif hand_num[0] == 1 and hand_num[1] == 10 and hand_num[1]+3 == hand_num[2]+2 == hand_num[3]+1 == hand_num[4]:
        return True
    else:
        return False

def if_pairs(hand):
    c = 0 
    #c counts pairs.
    #If hand is one pair,if_pairs(hand) returns 1 (2C1)
    #If hand is two pairs,if_pairs(hand) returns 2 (2C1 * 2)
    #If hand is three of a kind,if_pairs(hand) returns 3 (3C2)
    #If hand is full house,if_pairs(hand) returns 4 (2C1 + 3C2)
    #If hand is four of a kind,if_pairs(hand) returns 6 (4C2)
    for i in range(4):
        for j in range(i+1,5):
            if hand[i][1] == hand[j][1]:
                c += 1
    return(c)
    
def strength(hand):
    f = if_flush(hand)
    s = if_straight(hand)
    p = if_pairs(hand)
    if f and s:
        return 8
    #8 means straight flush
    elif p == 6:
        return 7
    #7 means four of a kind
    elif p == 4:
        return 6
    #6 means full house
    elif f:
        return 5
    #5 means flush
    elif s:
        return 4
    #4 means straight
    elif p == 3:
        return 3
    #3 means three of a kind
    elif p == 2:
        return 2
    #2 means two pairs
    elif p == 1:
        return 1
    #1 means one pairs
    else:
        return 0
    #0 means high card
    
#In the next function,
#2 means player1 wins
#1 means draw
#0 means player2 wins

def det_winner(p1_hand,p2_hand):
    if strength(p1_hand) > strength(p2_hand):
        return 2
    elif strength(p1_hand) < strength(p2_hand):
        return 0
    else:
            p1_numbers = []
            p2_numbers = []
            for i in range(5):
                p1_numbers.append(p1_hand[i][1])
                p2_numbers.append(p2_hand[i][1])
            p1_numbers.sort()
            p2_numbers.sort()
            
            if strength(p1_hand) == 0 or strength(p1_hand) == 4 or strength(p1_hand) == 5 or strength(p1_hand) == 8:    
                if p1_numbers[0] == 1 and p2_numbers[0] != 1:
                    return 2
                elif p1_numbers[0] != 1 and p2_numbers[0] == 1: 
                    return 0
                else:
                    for i in range(1,6):
                        if p1_numbers[-i] > p2_numbers[-i] :
                            return 2
                        elif p1_numbers[-i] < p2_numbers[-i] :
                            return 0
                    if p1_numbers == p2_numbers:
                        return 1

            elif strength(p1_hand) == 1:
                    a1 = collections.Counter(p1_numbers)
                    a2 = collections.Counter(p2_numbers)
                    b1 = [i for i in a1 if a1[i] == 2]
                    b2 = [i for i in a2 if a2[i] == 2]
                    if b1[0] == 1 and b2[0] != 1:
                        return 2
                    elif b2[0] == 1 and b1[0] != 1:
                        return 0
                    else:
                        if b1[0] > b2[0]:
                                return 2
                        elif b1[0] < b2[0]:
                                return 0
                        else:
                            p1_numbers.remove(b1[0])
                            p2_numbers.remove(b2[0])
                            if p1_numbers[0] == 1 and p2_numbers[0] != 1:
                                    return 2
                            elif p1_numbers[0] != 1 and p2_numbers[0] == 1:
                                    return 0
                            else:        
                                for i in range(1,4):
                                    if p1_numbers[-i] > p2_numbers[-i] :
                                        return 2
                                    elif p1_numbers[-i] < p2_numbers[-i] :
                                        return 0
                                if p1_numbers == p2_numbers:
                                    return 1

            elif strength(p1_hand) == 2:
                    a1 = collections.Counter(p1_numbers)
                    a2 = collections.Counter(p2_numbers)
                    b1 = [i for i in a1 if a1[i] == 2]
                    b2 = [i for i in a2 if a2[i] == 2]
                    c1 = [i for i in a1 if a1[i] == 1]
                    c2 = [i for i in a2 if a2[i] == 1]
                    b1.sort()
                    b2.sort()
                    if b1[0] == 1 and b2[0] != 1:
                        return 2
                    elif b2[0] == 1 and b1[0] != 1:
                        return 0
                    else:
                        for i in range(1,3):
                                if b1[-i] > b2[-i] :
                                    return 2
                                elif b1[-i] < b2[-i] :
                                    return 0
                                    
                        if c1[0] == 1 and c2[0] != 1:
                                  return 2
                        elif c1[0] != 1 and c2[0] == 1:
                                  return 0
                        else:
                            if c1[0] > c2[0]:
                                return 2
                            elif c1[0] < c2[0]:
                                return 0
                            else:
                                return 1

            elif strength(p1_hand) == 3:
                    a1 = collections.Counter(p1_numbers)
                    a2 = collections.Counter(p2_numbers)
                    b1 = [i for i in a1 if a1[i] == 3]
                    b2 = [i for i in a2 if a2[i] == 3]
                    if b1[0] == 1 and b2[0] != 1:
                        return 2
                    elif b2[0] == 1 and b1[0] != 1:
                        return 0
                    else:
                        if b1[0] > b2[0]:
                                return 2
                        elif b1[0] < b2[0]:
                                return 0
                        else:
                            p1_numbers.remove(b1[0])
                            p2_numbers.remove(b2[0])
                            if p1_numbers[0] == 1 and p2_numbers[0] != 1:
                                    return 2
                            elif p1_numbers[0] != 1 and p2_numbers[0] == 1:
                                    return 0
                            else:
                                for i in range(1,3):
                                    if p1_numbers[-i] > p2_numbers[-i] :
                                        return 2
                                    elif p1_numbers[-i] < p2_numbers[-i] :
                                        return 0
                                if p1_numbers == p2_numbers:
                                        return 1
                                        

            elif strength(p1_hand) == 6:
                    a1 = collections.Counter(p1_numbers)
                    a2 = collections.Counter(p2_numbers)
                    b1 = [i for i in a1 if a1[i] == 3]
                    b2 = [i for i in a2 if a2[i] == 3]
                    c1 = [i for i in a1 if a1[i] == 2]
                    c2 = [i for i in a2 if a2[i] == 2]
                    if b1[0] == 1 and b2[0] != 1:
                        return 2
                    elif b1[0] != 1 and b2[0] == 1:
                        return 0
                    else:
                        if b1[0] > b2[0]:
                                return 2
                        elif b1[0] < b2[0]:
                                return 0
                        else:
                            if c1[0] == 1 and c2[0] != 1:
                                    return 2
                            elif c1[0] != 1 and c2[0] == 1:
                                    return 0
                            else:
                                if c1[0] > c2[0]:
                                    return 2
                                elif c1[0] < c2[0]:
                                    return 0
                                else:
                                    return 1

            elif strength(p1_hand) == 7:
                    a1 = collections.Counter(p1_numbers)
                    a2 = collections.Counter(p2_numbers)
                    b1 = [i for i in a1 if a1[i] == 4]
                    b2 = [i for i in a2 if a2[i] == 4]
                    c1 = [i for i in a1 if a1[i] == 1]
                    c2 = [i for i in a2 if a2[i] == 1]
                    if b1[0] == 1 and b2[0] != 1:
                        return 2
                    elif b2[0] == 1 and b1[0] != 1:
                        return 0
                    else:
                        if b1[0] > b2[0]:
                                return 2
                        elif b1[0] < b2[0]:
                                return 0
                        else:
                            if c1[0] == 1 and c2[0] != 1:
                                    return 2
                            elif c1[0] != 1 and c2[0] == 1:
                                    return 0
                            else:
                                if c1[0] > c2[0]:
                                    return 2
                                elif c1[0] < c2[0]:
                                    return 0
                                else:
                                    return 1
                                        
#Choose the most stronghest hand function
def cms(hand_list):
    if len(hand_list) == 1:
        return hand_list[0]
    else:
        hand_list2 = copy.deepcopy(hand_list)
        if det_winner(hand_list[0],hand_list[1]):
            hand_list2.remove(hand_list[1])
            return cms(hand_list2)
        else: 
            hand_list2.remove(hand_list[0])
            return cms(hand_list2)

#Choose the most stronghest hand from 7 cards function        
def det_hand(hands):
    hand_list = []
    for i in range(6):
        for j in range(i,6):
            copyhands = copy.deepcopy(hands)
            copyhands.pop(i)
            copyhands.pop(j)
            hand_list.append(copyhands)
    return cms(hand_list)

#Choose the most strongest hand from 6 cards function
def det_hand_from6(hands):
    hand_list = []
    for i in range(6):
        copyhands = copy.deepcopy(hands)
        copyhands.pop(i)
        hand_list.append(copyhands)
    return cms(hand_list)    

def det_winner2(p1_hand,p2_hand,board):
    p1_hands = p1_hand + board 
    p2_hands = p2_hand + board
    p1_cards = det_hand(p1_hands)
    p2_cards = det_hand(p2_hands)
    if det_winner(p1_cards,p2_cards) == 2:
        winner = 0 
        tips[winner] = tips[winner] + sum(f_tips)
        f_tips = [i * 0 for i in f_tips]
    if det_winner(p1_cards,p2_cards) == 1:
        for i in range(2):
            tips[i] = tips[i] + sum(f_tips) / 2
            f_tips = [j * 0 for j in f_tips]
    if det_winner(p1_cards,p2_cards) == 0:
        winner = 1 
        tips[winner] = tips[winner] + sum(f_tips)
        f_tips = [i * 0 for i in f_tips]
        
def draw():
    drawcard = dec.pop(random.randrange(len(dec)))
    return drawcard

def draw2():
    drawcard = dec2.pop(random.randrange(len(dec)))
    return drawcard

#賭け額の移動、ゲームの進行
#SB:1$, BB:2$, Everyone has 100$ at first.
SB,BB = 1,2
buy_in = 100
pot = 0
tips = []
f_tips = []
if_actioned = []
if_noplay = []
if_all_in = []
for i in range(2):
    tips.append(buy_in)
    f_tips.append(0)
    if_actioned.append(0)
    if_noplay.append(0)
    if_all_in.append(0)
#f_tips means tips in front of the player

whoBB = random.randrange(2)
def pay_SB_BB():
    global tips,f_tips,whoBB,if_actioned
    
    whoBB = (whoBB + 1) % 2
    whoSB = (whoBB - 1) % 2
    x = 0
    y = 0
    if tips[whoBB] < BB:
        f_tips[whoBB] = tips[whoBB]
        tips[whoBB] = 0
        if_actioned[whoBB] = 1
        x = 1
    if tips[whoSB] < SB:
        f_tips[whoSB] = tips[whoSB]
        tips[whoSB] = 0
        if_actioned[whoSB] = 1
        y = 1
        
    if x == 0:
        tips[whoBB] -= BB
        f_tips[whoBB] += BB
    if y == 0:
        tips[whoSB] -= SB
        f_tips[whoSB] += SB    

def bet(n,money):
    global tips,f_tips,if_actioned
    
    if f_tips[n] != 0:
        print("You cannot bet.")
        return False
    elif tips[n] < money or money < BB:
        print("You cannot bet",money)
        return False
    else:
        tips[n] -= money
        f_tips[n] += money
        if_actioned[n] = 1
        return True

def rai_se(n,money):
    global tips,f_tips,if_actioned
    f_tips2 = f_tips
    f_tips2.sort()
    
    if tips[n] + f_tips[n] < money or money <= max(f_tips) or max(f_tips) == 0:
        print("You cannot raise",money)
        return False
        
    elif money < 2*max(f_tips) - f_tips2[-2] or money < 2*BB:
        if money == tips[n] + f_tips[n]:
            tips[n] += f_tips[n] - money
            f_tips[n] = money
            if_actioned[n] = 1
            return True
        else:
            print("You cannot raise.")
            return False
    
    else:
        tips[n] += f_tips[n] - money
        f_tips[n] = money
        if_actioned[n] = 1
        return True

def call(n):
    global tips,f_tips,if_actioned
    
    if sum(f_tips) == 0:
        print("You cannot call.")
        return False
    elif max(f_tips) > tips[n] + f_tips[n]:
        f_tips[n] += tips[n]
        tips[n] = 0
        if_actioned[n] = 1
        return True
    else:
        tips[n] -= max(f_tips) - f_tips[n]
        f_tips[n] = max(f_tips)
        if_actioned[n] = 1
        return True

def fold(n):
    global f_tips,pot,if_actioned,if_noplay
    
    if f_tips[n] == max(f_tips) or tips[n] == 0:
        print("You cannot fold.")
        return False
    else:
        pot += f_tips[n]
        f_tips[n] = 0
        if_actioned[n] = 1
        if_noplay[n] = 1   
        return True

def check(n):
    global if_actioned
    
    if f_tips[n] == max(f_tips):
        if_actioned[n] = 1
        return True
    else:
        print("You cannot check.")
        return False

def if_next():
    if 0 in if_actioned:
        return False
    else:
        if 0 in tips:
            b = []
            c = []
            for i in range(2):
                if not tips[i]:
                    b.append(i)
                    c.append(f_tips[i])
                    f_tips[i] = 0
            a = collections.Counter(f_tips)
            if len(a) == 1:
                return True
            elif len(a) == 2:
                if max(c) <= max(f_tips):
                    return True
                else:
                    return False
            else:
                return False    
            
        else:
            a = collections.Counter(f_tips)
            if 0 in f_tips:
                if len(a) == 2:
                    return True
                else:
                    return False
            else:
                if len(a) == 1:
                    return True
                else:
                    return False

def make_pot():
    global pot,f_tips,if_actioned
    
    if_actioned = []
    for i in range(2):
        pot += f_tips[i]
        f_tips[i] = 0
        if_actioned.append(0)

def if_gamefinish():
    global winner
    if tips.count(0) == 1:
        winner = tips.index(2 * buy_in) 
        return True
    else:
        return False

def if_dealfinish():
    #if if_dealfinish() returns 2,someone all-ined and a pot winner is ditermined.
    #if if_dealfinish() returns 1,everyone except one player folded and the player wins pot.
    #if if_dealfinish() returns 0,dealing will continue.
    global if_all_in,if_noplay
    if_fold = if_noplay
    for i in range(2):
        if tips[i] == 0:
            if_all_in[i] = 1
            if_noplay[i] = 1
            
    z = collections.Counter(if_noplay)
    y = collections.Counter(if_all_in)
    if z[0] == 1 and z[1] == 1:
        if len(y) == 2:
            return 2
        elif len(y) == 1:
            if y[1] > 0:
                return 2
            else:
                return 1
    elif z[1] == 2:
        if y[1] == 1:
            return 1
        else:
            return 2
    else:
        return 0

#<要入力> 数字入力 
def input_number():
    pass

#<要入力> playerの動作 ボタンが触られるまで動作を停止
def player_action():
    pass

#<輸入力>　player、CPUのアクションを受け付け、カードオープン、商社の決定を行う
def dealer(n, now_board, screen):
    pass

#AI
powercard = [1,13,12,11]
hand = [draw(),draw()]
def count_win(hand,now_board):
    steps = 0
    count = 0
    while steps <= 10:
        ini2()
        dec2.remove(hand[0])    
        dec2.remove(hand[1])
        if len(hand + now_board) == 5:
            for i in range(3):
                dec2.remove(now_board[i])
            enemy_hand = [draw2(),draw2()]
            if det_winner((hand + now_board),(enemy_hand + now_board)) == 2:
                  count += 1
        elif len(hand + now_board) == 6:
            for i in range(4):
                dec2.remove(now_board[i])
            enemy_hand = [draw2(),draw2()]
            if det_winner(det_hand_from6(hand + now_board),det_hand_from6(enemy_hand + now_board)) == 2:
                  count += 1
        elif len(hand + now_board) == 7:
            for i in range(5):
                dec2.remove(now_board[i])
            enemy_hand = [draw2(),draw2()]
            if det_winner(det_hand(hand + now_board),det_hand(enemy_hand + now_board)) == 2:
                  count += 1
        steps += 1
    return count

def poker_AI(n,hand,now_board):
    global pot,tips,f_tips,if_actioned
    #poker AI movement at the preflop
    if now_board == []:
        random_a = random.randrange(100)
        if hand[0][1] in powercard or hand[1][1] in powercard or hand[0][0] == hand[1][0] or hand[0][1] == hand[1][1]:
            if max(f_tips) == BB:
                if rai_se(n,3*BB):
                    rai_se(n,3*BB)
                elif rai_se(n,tips[n]):
                    rai_se(n,tips[n])
                elif call(n):
                    call(n)
                elif fold(n):
                    fold(n)
                        
                        
            else:
                if 0 <= random_a < 20:
                    fold(n)
                elif 20 <= random_a < 80:
                    call(n)
                else:
                    rai_se(n,3*max(f_tips))
        else:
            if check(n):
                check(n)
            else:
                fold(n)
                
    #poker AI movement at the flop    
    elif len(now_board) == 3:
        random_a = random.randrange(100)
        if check(n) == True:
            if count_win(hand,now_board) <= 5:
                if 0 <= random_a < 50:
                    if bet(n,pot//3):
                        bet(n,pot//3)
                    elif rai_se(n,tips[n]):
                        rai_se(n,tips[n])
                    elif call(n):
                        call(n)
                    elif fold(n):
                        fold(n)    
                else:
                    check(n)
            else:
                if bet(n,pot//3):
                    bet(n,pot//3)
                elif rai_se(n,tips[n]):
                    rai_se(n,tips[n])
                elif call(n):
                    call(n)
                elif fold(n):
                    fold(n)
        else:
            if count_win(hand,now_board) <= 5:
                fold(n)
            else:
                if 0 <= random_a < 70:
                    call(n)
                else: fold(n)    
    elif len(now_board) == 4: 
        random_a = random.randrange(100)
        if check(n) == True:
            if count_win(hand,now_board) <= 5:
                if 0 <= random_a < 50:
                    if bet(n,pot//3):
                        bet(n,pot//3)
                    elif rai_se(n,tips[n]):
                        rai_se(n,tips[n])
                    elif call(n):
                        call(n)
                    elif fold(n):
                        fold(n)    
                    else:
                        check(n)
            else:
                if bet(n,pot//3):
                    bet(n,pot//3)
                elif rai_se(n,tips[n]):
                    rai_se(n,tips[n])
                elif call(n):
                    call(n)
                elif fold(n):
                    fold(n)
        else:
            if count_win(hand,now_board) <= 5:
                fold(n)
            else:
                if 0 <= random_a < 70:
                    call(n)
                else:
                    if rai_se(3*max(f_tips)):
                        rai_se(3*max(f_tips))
                    elif rai_se(n,tips[n]):
                        rai_se(n,tips[n])
                    elif call(n):
                        call(n)
                    elif fold(n):
                        fold(n)    
                        
    else:                    
        random_a = random.randrange(100)
        if check(n) == True:
            if count_win(hand,now_board) <= 5:
                if 0 <= random_a < 50:
                    check(n)
                elif 50 < random_a  <= 80:
                    if bet(n,pot//3):
                        bet(n,pot//3)
                    elif rai_se(n,tips[n]):
                        rai_se(n,tips[n])
                    elif call(n):
                        call(n)
                    elif fold(n):
                        fold(n)    
                    else:
                        if bet(n,pot):
                            bet(n,pot)
                        elif rai_se(n,tips[n]):
                            rai_se(n,tips[n])
                        elif call(n):
                            call(n)
                        elif fold(n):
                            fold(n)    
            else:
                if 0 <= random_a <= 10:
                    check(n)
                elif 10 < random_a <= 40:
                    if bet(n,pot//3):
                        bet(n,pot//3)
                    elif rai_se(n,tips[n]):
                        rai_se(n,tips[n])
                    elif call(n):
                        call(n)
                    elif fold(n):
                        fold(n)    
                    else:
                        bet(n,pot)
        else:
            if count_win(hand,now_board) <= 5:
                fold(n)
            else:
                if 0 <= random_a < 70:
                    call(n)
                else: 
                    if rai_se(3*max(f_tips)):
                        rai_se(3*max(f_tips))
                    elif rai_se(n,tips[n]):
                        rai_se(n,tips[n])
                    elif call(n):
                        call(n)
                    elif fold(n):
                        fold(n)

#表示
black = (0, 0, 0)
red = (255, 0, 0)
white = (255,255,255)
brown = (115, 66, 41)
orange = (233,168, 38)
green = (0,100,0)

def drawing_newcard():
    ini()
    p1card1 = draw()
    p1card2 = draw()
    p1_hand = [p1card1, p1card2]
    p2card1 = draw()
    p2card2 = draw()
    p2_hand = [p2card1, p2card2]
    bcard1 = draw()
    bcard2 = draw()
    bcard3 = draw()
    bcard4 = draw()
    bcard5 = draw()
    board = [bcard1, bcard2, bcard3, bcard4, bcard5]

def painting_newcard(screen):
    player1_card1 = pygame.image.load(tramp_dic[p1card1])
    player1_card1 = pygame.transform.scale(player1_card1,(80,120))
    player1_card2 = pygame.image.load(tramp_dic[p1card2])
    player1_card2 = pygame.transform.scale(player1_card2,(80,120))
    player2_card1_hide = pygame.image.load("image52.png")
    player2_card1_hide = pygame.transform.scale(player2_card1_hide,(80,120))
    player2_card2_hide = pygame.image.load("image52.png")
    player2_card2_hide = pygame.transform.scale(player2_card2_hide,(80,120))
    player2_card1_open = pygame.image.load(tramp_dic[p2card1])
    player2_card1_open = pygame.transform.scale(player2_card1_open,(80,120))
    player2_card2_open = pygame.image.load(tramp_dic[p2card2])
    player2_card2_open = pygame.transform.scale(player2_card2_open,(80,120))

    board_card1 = pygame.image.load("image52.png")
    board_card1 = pygame.transform.scale(board_card1,(80,120))
    board_card2 = pygame.image.load("image52.png")
    board_card2 = pygame.transform.scale(board_card2,(80,120))                                         
    board_card3 = pygame.image.load("image52.png")
    board_card3 = pygame.transform.scale(board_card3,(80,120))
    board_card4 = pygame.image.load("image52.png")
    board_card4 = pygame.transform.scale(board_card4,(80,120))                                         
    board_card5 = pygame.image.load("image52.png")
    board_card5 = pygame.transform.scale(board_card5,(80,120))

    screen.blit(player1_card1,(300,560))
    screen.blit(player1_card2,(360,560))
    screen.blit(player2_card1_hide,(640,140))
    screen.blit(player2_card2_hide,(580,140))
    screen.blit(board_card1,(330,355))                                     
    screen.blit(board_card2,(400,355))  
    screen.blit(board_card3,(470,355))                                       
    screen.blit(board_card4,(540,355))                                       
    screen.blit(board_card5,(610,355))

    pygame.display.flip()

def tips_update(screen):
    pygame.draw.rect(screen, white , Rect(360, 520, 80, 20))
    pygame.draw.rect(screen, white , Rect(640, 290, 80, 20))
    pygame.draw.rect(screen, white , Rect(480, 700, 80, 20))
    pygame.draw.rect(screen, white , Rect(610, 90, 80, 20))
    pygame.draw.rect(screen, white , Rect(360, 320, 80, 20))
    font1 = pygame.font.SysFont(None, 20)
    text_f_tips1 = font1.render(str(f_tips[0]), True, (0,0,0))
    text_f_tips2 = font1.render(str(f_tips[1]), True, (0,0,0))
    text_tips1 = font1.render(str(tips[0]), True, (0,0,0))
    text_tips2 = font1.render(str(tips[1]), True, (0,0,0))
    text_pot = font1.render(str(pot), True, (0,0,0))
    screen.blit(text_f_tips1, text_f_tips1.get_rect(center=(400,530)))
    screen.blit(text_f_tips2, text_f_tips2.get_rect(center=(680,300)))
    screen.blit(text_tips1, text_tips1.get_rect(center=(520,710)))
    screen.blit(text_tips2, text_tips2.get_rect(center=(650,100))) 
    screen.blit(text_pot, text_pot.get_rect(center=(400,330)))

    font2 = pygame.font.SysFont(None, 25)
    button1 = pygame.Rect(80, 700, 70, 50)  
    button2 = pygame.Rect(160, 700, 70, 50)
    button3 = pygame.Rect(240, 700, 70, 50)  
    button4 = pygame.Rect(320, 700, 70, 50)
    button5 = pygame.Rect(400, 700, 70, 50) 
    text1 = font2.render("CHECK", True, (0,0,0))
    text2 = font2.render("FOLD", True, (0,0,0))
    text3 = font2.render("CALL", True, (0,0,0))
    text4 = font2.render("BET", True, (0,0,0))
    text5 = font2.render("RAISE", True, (0,0,0))

    if f_tips[0] == max(f_tips):
        pygame.draw.rect(screen, orange, button1)
        screen.blit(text1, text1.get_rect(center=(115,725)))
    else:
        pygame.draw.rect(screen, green, button1)
    if f_tips[0] != max(f_tips) and tips[0] != 0:
        pygame.draw.rect(screen, orange, button2)
        screen.blit(text2, text2.get_rect(center=(195,725)))
    else:
        pygame.draw.rect(screen, green, button2)
    if sum(f_tips) != 0:
        pygame.draw.rect(screen, orange, button3)
        screen.blit(text3, text3.get_rect(center=(275,725)))
    else:
        pygame.draw.rect(screen, green, button3)
    if f_tips[0] == 0:
        pygame.draw.rect(screen, orange, button4)
        screen.blit(text4, text4.get_rect(center=(355,725)))
    else:
        pygame.draw.rect(screen, green, button4)
    if len([i for i in f_tips if i > f_tips[0]]) != 0 and tips[0] > max(f_tips)-f_tips[0]:
        pygame.draw.rect(screen, orange, button5)
        screen.blit(text5, text5.get_rect(center=(435,725)))
    else:
        pygame.draw.rect(screen, green, button5) 

def flop(screen):
    pygame.time.delay(1000)
    board_card1 = pygame.image.load(tramp_dic[bcard1])
    board_card1 = pygame.transform.scale(board_card1,(80,120))
    board_card2 = pygame.image.load(tramp_dic[bcard2])
    board_card2 = pygame.transform.scale(board_card2,(80,120))
    board_card3 = pygame.image.load(tramp_dic[bcard3])
    board_card3 = pygame.transform.scale(board_card3,(80,120))
    screen.blit(board_card1,(330,355))                                     
    screen.blit(board_card2,(400,355))  
    screen.blit(board_card3,(470,355))
    now_board = [bcard1, bcard2, bcard3]
    if_actioned = [i * 0 for i in if_actioned]
    pygame.display.flip()

def turn(screen):
    pygame.time.delay(1000)
    board_card4 = pygame.image.load(tramp_dic[bcard4])
    board_card4 = pygame.transform.scale(board_card4,(80,120))
    screen.blit(board_card4,(540,355))
    now_board = [bcard1, bcard2, bcard3, bcard4]
    if_actioned = [i * 0 for i in if_actioned]
    pygame.display.flip()

def river(screen):
    pygame.time.delay(1000)
    board_card5 = pygame.image.load(tramp_dic[bcard5])
    board_card5 = pygame.transform.scale(board_card5,(80,120))
    screen.blit(board_card5,(610,355))
    now_board = [bcard1, bcard2, bcard3, bcard4, bcard5]
    if_actioned = [i * 0 for i in if_actioned]
    pygame.display.flip()

def main():
    global tips, f_tips
    global player1_card1,player1_card2,player2_card1_open,player2_card2_open,p1_hand,p2_hand,board
    global event

    # ゲームの初期化処理
    gamescene = 0
    pygame.init()
    pygame.display.set_caption("Poker")
    screen = pygame.display.set_mode((1000,800))
    FPS = 60
    clock = pygame.time.Clock()

    #gamescene0における描画準備
    startbuttonrect = Rect(300, 500, 400, 100) 
    startbutton = [pygame.transform.scale(pygame.image.load("pushstart.png"),(400,100))]
    startscreenrect = Rect(0, 0, 1000, 800)
    startscreen = [pygame.transform.scale(pygame.image.load("Startscreen.jpg"),(1000,800))]

    #gamescene1における描画準備











# In[ ]: