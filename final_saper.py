


from colorama import Fore, Back, Style # trzeba ściągnąć colorama
import getch # trzeba sciagnac getch
import os
import random


def add_bombs(bomb_num):
    global hidemap
    for bomb in range(bomb_num):
        dim1 = random.randint(0,len_edge - 1)
        dim2 = random.randint(0,len_edge - 1)
        if hidemap[dim1][dim2] != "*": 
            hidemap[dim1][dim2] = "*"
            addpoints(dim1,dim2)

def addpoints(dim1,dim2): 
    global hidemap
    newdim1 = dim1 - 1
    newdim2 = dim2 - 1
    for square_a in range(3):
        newdim1 = dim1 - 1
        for square_b in range(3):
            try:
                if newdim1 > -1 and newdim2 > -1:
                    hidemap[newdim1][newdim2] += 1
            except:
                pass
            newdim1 += 1
        newdim2 += 1

def input_map_size():
    global len_edge
    global bomb_num
    global hidemap
    global x
    global y
    global move_count
    global visiblemap
    len_edge = 0
    bomb_num = 0
    while len_edge not in range(1,16):
        try:
            len_edge = int(input("Enter size of map (max:15): \n"))
        except:
            pass
    max_bomb_num = len_edge ** 2 // 2
    while bomb_num not in range(1, max_bomb_num):
        try:
            bomb_num = int(input("Enter number of bombs (max: 50%\ of squares): \n"))
        except:
            pass
    for line in range(len_edge):
        hidemap.append([0]*len_edge)
    for line in range(len_edge):
        visiblemap.append(["[ ]"]*len_edge) 
    x = len_edge // 2
    y = len_edge // 2 
    move_count = 0 

def screen(hidemap):    
    count = 0
    for row in hidemap:
        final_screen = ""
        joined_row = final_screen.join(str(hidemap[count]))
        print(abs(count - len_edge), joined_row) 
        count += 1
    bottom_line_of_numbers = [" "]
    for i in range(1,len_edge + 1):
        bottom_line_of_numbers.append(f"  {i}")
    print("".join(bottom_line_of_numbers))

def hidemap_generator():
    global hidemap
    global visiblemap
    os.system('clear')
    hidemap = []
    visiblemap = []
    input_map_size()
    dim1 = len_edge
    dim2 = len_edge
    add_bombs(bomb_num)
    addpoints(dim1,dim2)

def placeflag(y,x):
    if visiblemap[y][x] == "< >":
        visiblemap[y][x] = "<F>"
    elif visiblemap[y][x] == "<F>":
        visiblemap[y][x] = "< >"

def menu():
    print("\n")
    print(Fore.CYAN + "< S * A * P * E * R >" .center(60, " "))
    print(Style.RESET_ALL)

    print(Back.GREEN + "Play - press 'p'" .center(60, " "))
    print(Style.RESET_ALL)

    print(Back.YELLOW + "Instructions - press 'i'" .center(60, " "))
    print(Style.RESET_ALL)

    print(Back.RED + "Exit - press 'e'" .center(60, " "))
    print(Style.RESET_ALL)

    user_input = 0
    while user_input not in ["p", "i", "e"]:
        user_input = getch.getch()
        if user_input == "p":
            hidemap_generator()
            play_saper()
        elif user_input == "i":
            show_instructions()
        elif user_input == "e":
            exit()

def play_saper():  
    global move_count
    max_move_count = len_edge**2 - bomb_num 
    current_square_mark(y,x)
    screen()
    while 1:
        choosing_square()
        cycle(y,x)
        screen()
        if move_count == max_move_count:
            break   
    win_game()

def choosing_square():
    global y, x
    while 1: 
        key = getch.getch()
        if key in ["a","w","s","d","c","f"]:
            if key == "c":
                if visiblemap[y][x] in ["< >", "<F>"]:
                    break
            elif key == "f":
                placeflag(y,x)
            current_square_unmark(y,x)
            if key == "a":
                move_square("left")
            elif key == "w":
                move_square("up")
            elif key == "s":
                move_square("down")
            elif key == "d":
                move_square("right")
            current_square_mark(y,x)
            screen()
        continue

def current_square_unmark(y,x):
    visiblemap[y][x] = "[" + visiblemap[y][x][1] + "]"

def current_square_mark(y,x):
    visiblemap[y][x] =  "<" + visiblemap[y][x][1] + ">"

def move_square(direction):
    global y, x
    if direction == "right":
        if x < len_edge - 1 :
            x += 1
    if direction == "left":
        if x > 0:
            x -= 1
    if direction == "up":
        if y > 0:
            y -= 1
    if direction == "down":
        if y < len_edge - 1:
            y += 1

def cycle(y,x):
    global visiblemap
    global move_count
    visiblemap[y][x] =f"<{str(hidemap[y][x])}>"
    if visiblemap[y][x] == "<*>":
        game_over()
    move_count += 1
    if visiblemap[y][x] == "<0>":
        unveil_zeros(y,x)

def unveil_zeros(y,x):
    global move_count
    new_y = y - 1
    new_x = x - 1
    for i in range(3):
        new_x = x - 1 
        for z in range(3):
            if new_y in range(len_edge) and new_x in range(len_edge) and visiblemap[new_y][new_x] == "[ ]":
                visiblemap[new_y][new_x] =f"[{str(hidemap[new_y][new_x])}]"
                move_count  += 1
                if visiblemap[new_y][new_x] in ["[0]"]:
                    unveil_zeros(new_y,new_x)
            new_x += 1
        new_y += 1

def screen():
    os.system('clear')
    count = 0
    for row in visiblemap:
        final_screen = ""
        joined_row = final_screen.join(visiblemap[count])
        print(joined_row) 
        count += 1

def win_game():
    screen()
    print("  you won, congrats!")
    print("  press 'm' to return to menu")
    while 1:
        key = getch.getch()
        if key == "m":
            menu()

def game_over():
    global visiblemap
    global listofmoves
    screen()
    print("    GAME OVER")
    print("  press 'm' to return to menu")
    while 1:
        key = getch.getch()
        if key == "m":
            menu()

def show_instructions():
    print(">move around with 'W','A','S','D' keys, check the chosen square with 'C' key")
    print(">you can mark or unmark the current square with 'F'")
    print(">the uncovered number indicates how many bombs are hidden in neighbouring areas")
    print(">you lose when you uncover a bomb, win when you uncover everything except bombs")
    print(">good luck!")
    print("                 press 'm' to return to menu")
    while 1:
        key = getch.getch()
        if key == "m":
            menu()

menu()

