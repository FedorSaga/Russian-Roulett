import random
countplayers = int(input('ENTER AMMOUNT OF PLAYERS(THERE CAN NOT BE MORE THAN 3 PLAYERS!):'))
players = []
player = 0
shots = 0
bullets = [0,0,0,0,0,1]
print('''RULES: This game emitate revolver that has only 1/6 bullet. Players will take turns\n
shooting. When someone will shoot a bullet, he/she will loose!''')
for i in range(countplayers):
    players.append(input('ENTER NAME/NICKNAME:'))
while shots < 6:
    if player > countplayers-1:
        player = 0
    print(players[0],'is shooting!\nPress ENTER to shoot')
    input()
    delete = random.choice(bullets)
    bullets.remove(delete)
    if delete == 1:
        print('BOOOOM!!! You died! GG')
        break
    else:
        print('CKLIC! Wow! you are lucky')
    player+=1
    shots+=1
