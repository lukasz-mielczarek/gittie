visiblemap = [["[ ]","[ ]","[ ]","[ ]","[ ]"],
["[ ]","[ ]","[ ]","[ ]","[ ]"],
["[ ]","[ ]","[ ]","[ ]","[ ]"],
["[ ]","[ ]","[ ]","[ ]","[ ]"],
["[ ]","[ ]","[ ]","[ ]","[ ]"]]

hidemap = [['*',1,1,1,1],
[1,2,2,'*',1],
[0,1,'*',3,2],
[0,2,2,3,'*'],
[0,1,'*',2,1]]

listofmoves = [] #czy w tym miejscu?

def placeflag(x,y):
    flag = "[@]"
    if visiblemap[5-y][x-1] == "[ ]":
        visiblemap[5-y][x-1] = flag
    else: 
        print ("you cant place a flag on a position you already uncovered")

def menu():
    print("\n")
    print("< S * A * P * E * R >")
    print("\n")
    print("Play - press 'p'")
    print("Instructions - press 'i'")
    print("Exit - press 'e'")
    menu_input = input(": ")
    if menu_input == "p":
        play_saper()
    elif menu_input == "i":
        show_instructions()
    elif menu_input == "e":
        exit()
    else:
        print("value error")

def play_saper():
    screen()
    for i in range(20):
        user_input()
        cycle(x,y)
        screen()
    win_game()     

def user_input():
    global x
    global y
    global listofmoves
    while True:
        try:
            x, y = input("... ").split()  # x i y muszą być wprzedziale 1-5
            x = int(x)
            y = int(y)
            break
        except:
            print("type in x and y coordinates separated with a space bar...")
    check_newmove(x,y)

def check_value(x,y):
    pass

def check_newmove(x,y):
    global listofmoves
    newmove = False
    if not [x,y] in listofmoves :
        newmove = True 
    while [x,y] in listofmoves:
        x, y = input("U did the same move before... ").split()  # x i y muszą być wprzedziale 1-5
    listofmoves.append([x,y])

# ch_place to nie zmienna globalna                
def cycle(x, y):
    ch_place = "[" + str(hidemap[5-y][x-1]) + "]"
    if ch_place == "[*]":           #sprawdzamy czy bomba
        visiblemap[5-y][x-1] = ch_place
        game_over()
    else:
        visiblemap[5-y][x-1] = ch_place   #zamiast 5 moze byc n, wymiar planszy 
    
def screen():
    count = 0
    for i in visiblemap:
        final_screen = ""
        a = final_screen.join(visiblemap[count])
        print(abs(count - 5),a)
        count += 1
    print("   1  2  3  4  5 ")

def win_game():
    print("    you won, congrats!")
    
    menu()

def game_over():
    global visiblemap
    global listofmoves
    screen()
    print("\n")
    print("    GAME OVER")
    visiblemap = [["[ ]","[ ]","[ ]","[ ]","[ ]"],
    ["[ ]","[ ]","[ ]","[ ]","[ ]"],
    ["[ ]","[ ]","[ ]","[ ]","[ ]"],
    ["[ ]","[ ]","[ ]","[ ]","[ ]"],
    ["[ ]","[ ]","[ ]","[ ]","[ ]"]]
    listofmoves = []
    menu()

def show_instructions():
    print(">uncover areas on the board by typing in coordinates")
    print(">type in x and y coordinated separated with a space bar")
    print(">the uncovered number indicates how many bombs are hidden in neighbouring areas")
    print(">you lose when you uncover a bomb, win when you uncover everything except bombs")
    print(">good luck!")
    menu()

menu()