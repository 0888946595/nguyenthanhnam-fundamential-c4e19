map = {
    "size_x": 5,
    "size_y": 5,
}

player = {
    'x': 3, 
    'y': 4,
}

boxes = [
    {'x': 1, 'y': 1},
    {'x': 2, 'y': 2},
    {'x': 3, 'y': 3},
]

playing = True
while playing:
    destination = [
        {'x': 3, 'y': 2},
        {'x': 4, 'y': 3},
        {'x': 4, 'y': 4}
    ]
    for y in range (map['size_y']):
        for x in range (map['size_x']):
            player_is_here = False
            if x == player['x'] and y == player['y']:
                player_is_here = True
            box_is_here = False
            for box in boxes:
                if box['x'] == x and box ['y'] == y:
                    box_is_here = True
            des_is_here = False
            for des in destination:
                if des['x'] == x and des['y'] == y:
                    des_is_here = True
                    
            if player_is_here == True:
                print ("P ", end="")
            elif box_is_here == True:
                print ("B ", end="")
            elif des_is_here == True:
                print ("D ", end="")
            else:
                print ("- ", end="")
        print ()

    move  = input("Your move: ").upper()
    dx = 0
    dy = 0
    if move =="W":
        # player['y'] -= 1
        dy = -1
    elif move == "A":
        # player['x'] -= 1
        dx = -1
    elif move == "S":
        # player['y'] +=1
        dy = 1
    elif move == "D":
        # player['x'] +=1 
        dx = 1
    else:
        print("Buzzz")
        playing = False
        # break
    
    if 0 <=  player['x'] + dx < map['size_x'] and 0 <= player['y'] + dy < map['size_y']:
        player['x'] += dx
        player['y'] += dy

    for box in boxes:
        if box ['x']== player['x'] and box['y'] == player['y']:
            box['x'] += dx
            box ['y'] += dy

    # note:
    # 
