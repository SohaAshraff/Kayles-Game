lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
empty_list  = ['-' for i in range(20)]
for i in range (0,len(lst)):
    print("player 1 enter numbers : ")
    player1 = list(map(int,input().split()))
    #check if the player entered 1 number or 2 numbers
    if len(player1) > 1 :
        if player1[0] >= 10 and player1[1] >= 10 :
            lst.reverse()
            player1[0] -= 10
            player1[1] -= 10
            lst[lst.index(player1[0])] = '-'
            lst[lst.index(player1[1])] = '-'
            lst.reverse()
        elif player1[0] >= 10 and player1[1] <= 10:
            lst.reverse()
            player1[0] -= 10
            lst[lst.index(player1[0])] = '-'
            lst.reverse()
            lst[lst.index(player1[1])] = '-'
        elif player1[1] >= 10 and player1[0] <= 10 :
            lst.reverse()
            player1[1] -= 10
            lst[lst.index(player1[1])] = '-'
            lst.reverse()
            lst[lst.index(player1[0])] = '-'
        else:
            lst[lst.index(player1[0])] = '-'
            lst[lst.index(player1[1])] = '-'
        print(*lst)
    #this case for 1 number
    else:
        if player1[0] >= 10 :
            lst.reverse()
            player1[0] -= 10
            lst[lst.index(player1[0])] = '-'
            lst.reverse()
        else:
            lst[lst.index(player1[0])] = '-'
        print(*lst)
    if lst == empty_list:
        print("player 1 won")
        exit()
    print("player 2 enter numbers : ")
    player2 = list(map(int,input().split()))
    if len(player2) > 1 :
        if player2[0] >= 10 and player2[1] >= 10:
            lst.reverse()
            player2[0] -= 10
            player2[1] -= 10
            lst[lst.index(player2[0])] = '-'
            lst[lst.index(player2[1])] = '-'
            lst.reverse()
        elif player2[0] >= 10 and player2[1] <= 10:
            lst.reverse()
            player2[0] -= 10
            lst[lst.index(player2[0])] = '-'
            lst.reverse()
            lst[lst.index(player2[1])] = '-'
        elif player2[1] >= 10 and player2[0] <= 10:
            lst.reverse()
            player2[1] -= 10
            lst[lst.index(player2[1])] = '-'
            lst.reverse()
            lst[lst.index(player2[0])] = '-'
        else:
            lst[lst.index(player2[0])] = '-'
            lst[lst.index(player2[1])] = '-'
        print(*lst)

    else:
        if player2[0] >= 10:
            lst.reverse()
            player2[0] -= 10
            lst[lst.index(player2[0])] = '-'
            lst.reverse()
        else:
            lst[lst.index(player2[0])] = '-'
        print(*lst)
    if lst == empty_list:
        print("player 2 won")
        exit()