# 2 players, player 1 always starts first and they are both trying to reduce m to 1 the most efficient way. find which player wins based on n the number of towers and m the height of the towers. players lose if they have no move


n = 3
m = 6

def towerBreakers(n, m):
    if m == 1:
        print(2)
    elif n % 2 == 0:
        print(2)
    else:
        print(1)

towerBreakers(n,m)

# player 1 always wins if there is an odd number of towers player 2 would always win if there is an even number of towers.  If the game starts with towers height of 1, player 1 loses becuase he has no move