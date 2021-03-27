import random

tossListA = ['odd','even']
tossListB = ['batting','balling']

player = False

while player == False:
    tossA = int(input('odd or even? (enter 0 for odd and 1 for even) '))
    
    if tossA == 0 or tossA == 1:
        tossA1 = tossListA[tossA]
        print('you chose' , tossA1)
        player = True
    else:
        print('please give a valid input')
        player = False
    
tossB = int(input('enter number for toss '))

tossC = random.randint(1,10)

tossD = tossB + tossC

tossE = random.randint(0,1)

print('the coputer chose' , tossC)

turnA = None
turnB = None

if tossA1 == 'odd':
    if tossD%2 != 0:
            print('you win the toss!')
            playerSelect1 = int(input('do you want to bat or ball? (enter 0 for batting and 1 for balling) '))
            turnA = tossListB[playerSelect1]
            print('okay! the player will now do' , turnA)
    elif tossD%2 == 0:
            print('the computer won the toss')
            turnB = tossListB[tossE]
            print('the computer will now do' , turnB)

elif tossA1 == 'even':
        if tossD%2 != 0:
            print('the computer won the toss')
            turnB = tossListB[tossE]
            print('the computer will now do' , turnB)
        elif tossD%2 == 0:
            print('you win the toss!')
            playerSelect1 = int(input('do you want to bat or ball? (enter 0 for batting and 1 for balling) '))
            turnA = tossListB[playerSelect1]
            print('okay! the player will now do' , turnA)

if turnA == "batting" or turnB == "balling":
    playerTurn  = False
    run = []
    total  = 0
    while playerTurn == False:
        computerBall = random.randint(0,10)
        playerBat = int(input('enter your number for batting '))
        if playerBat > 10:
            print('please enter a number between 0 and 10')
            continue
        print('the computer chose' , computerBall)
        if playerBat == computerBall:
            playerTurn = True
            print('you are out!')
            print('the computer will now bat')
            continue
        else:
            run.append(playerBat)
            continue
    for ele in range(0, len(run)): 
        total = total + run[ele] 
    print('your total runs are' , total)
    
    playerTurn2 = False
    run2 = []
    total2 = 0
    while playerTurn2 == False:
        computerBat = random.randint(0,10)
        playerBall = int(input("please enter a number for balling "))
        if playerBall > 10:
            print('please enter a number between 0 and 10')
            continue
        print('the computer chose' , computerBat)
        if computerBat == playerBall:
            playerTurn2 = True
            print('the computer is out!')
            continue
        else:
            run2.append(computerBat)
            continue
      
    for ele2 in range(0,len(run2)):
        total2 = total2 + run2[ele2]
        print('the total runs of computer is' , total2)

    if total >> total2:
        print('the player won')
    elif total2 >> total:
        print('the computer won')
    

if turnA == "balling" or turnB == "batting":
    playerTurn = False
    run = []
    total = 0
    while playerTurn == False:
        computerBat = random.randint(0,10)
        playerBall = int(input("please enter a number for balling "))
        if playerBall > 10:
            print('please enter a number between 0 and 10')
            continue
        print('the computer chose' , computerBat)
        if computerBat == playerBall:
            playerTurn = True
            print('the computer is out!')
            continue
        else:
            run.append(computerBat)
            continue
    for ele in range(0,len(run)):
        total = total + run[ele]
    print('the total runs of computer is' , total)

    playerTurn2  = False
    run2 = []
    total2  = 0
    while playerTurn2 == False:
        computerBall = random.randint(0,10)
        playerBat = int(input('enter your number for batting '))
        if playerBat > 10:
            print('please enter a number between 0 and 10')
            continue
        print('the computer chose' , computerBall)
        if playerBat == computerBall:
            playerTurn2 = True
            print('you are out!')
            print('the computer will now bat')
            continue
        else:
            run.append(playerBat)
            player = False
            continue
    for ele2 in range(0, len(run2)): 
        total2 = total2 + run[ele2] 
    print('your total runs are' , total2)


    if total >> total2:
        print('the player won')
    elif total2 >> total:
        print('the computer won')