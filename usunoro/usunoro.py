
import random

def deckMake(people):
    [deck.append(x+1) for i in range(people + 1) for x in [i] * 4]
    #print(deck)
    random.shuffle(deck)
    random.shuffle(deck)
    handMake(people)

def peopleNum():
    while True:
        comNum = input("Computerの人数を入力してください。(2 ~ 12): " )
        if comNum.isdigit():
            if 2 <= int(comNum) <= 12:
                print(str(int(comNum) + 1) + '人でプレイします。')
                return int(comNum)    
        print('有効な数字を入力してください。')

def playerChange(number):
    if hand[0][0] == hand[0][1] == hand[0][2] == hand[0][3]:
        gameSet(1)
        return
    while True:
        hand[0].sort()
        print(hand[0])
        playerNum = input("捨てる数字を入力してください:" )
        if playerNum.isdigit():
            try:
                if 1 <= int(playerNum) <= number + 1:
                    hand[0].remove(int(playerNum))
                    return int(playerNum)
            except ValueError:
                pass
        print('有効な数字を入力してください。')

def handMake(number):
    hand.append([deck[(x * 4):((x+1) * 4)] for x in range(number + 1)])
    #print(hand)

def gameSet(number):
    #引数は誰がクリアしたか(自分は1)(番号若い人のみ処理される可能性があるため要チェック)
    count.append(number)

def comAI(number):
    #引数はnumber人目のcomputerかを表す。
    hand[number].sort()
    check = 0
    for n in range(3):
        if hand[number][n] == hand[number][n + 1]:
            check += (2 ** n)
    if check == 7:
        x = 0
        gameSet(number + 1)
    elif check == 6:
        x = hand[number].pop(0)
    elif check == 5:
        random.shuffle(hand[number])
        x = hand[number].pop()
    elif check == 4:
        x = hand[number].pop(random.randrange(2))
    elif check == 3:
        x = hand[number].pop()
    elif check == 2:
        x = hand[number].pop(random.randrange(2) * 3)
    elif check == 1:
        x = hand[number].pop(random.randrange(2) + 2)
    else:
        x = hand[number].pop(random.randrange(4))
    return x

count = []
deck = []
hand = []
change = []
people = peopleNum()
deckMake(people) 
#print(deck)
hand = hand[0]
while True:
    #print(hand)
    #初期配牌
    for n in range(people):
        change.append(comAI(n + 1))
    if count:
        if hand[0][0] == hand[0][1] == hand[0][2] == hand[0][3]:
            gameSet(1)
        for n in range(people):
            hand[n + 1].append(change[n])
            for n in range(people):
                try:
                    hand[n + 1].remove(0)
                except ValueError:
                    pass
        break
    change.append(playerChange(people))
    print(str(change[0]) + "を受け取りました")
    for n in range(people + 1):
        hand[n].append(change[n])
    change = []
print(hand)
count.sort()
#順番が2,3,4,...10,11,12,13,1となっているため
print(str(count) + "人目がクリア")
