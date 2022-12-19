# assignment: programming assignment 5: fifteen puzzle
# author: Tanvi Herwadkar
# date: December 2, 2022
# file: game.py uses TKinter to create a Fifteen Puzzle interface
#       When you click a tile adjacent to the space, the selected 
#       tile and the space switch spots
# input: n/a
# output: graphic visualization of the Fifteen Puzzle


from tkinter import *
import tkinter.font as font

from fifteen import Fifteen
from queue import Queue

SPACE = " "
game = Fifteen()
solution = Queue()

def clickButton(name):
    space_pos = game.position
    if name == game.position:
        return
    status = game.search_and_swap(name)
    if status == False:
        return
    gui.nametowidget(space_pos)['text'], gui.nametowidget(name)['text'] = gui.nametowidget(name)['text'], SPACE
    if game.is_solved():
        print("You Win!")

def moveTile(name):
    space_pos = game.position
    if name == game.position:
        return
    status = game.swap(name, space_pos, game.tiles)
    game.position = name
    if status == False:
        return
    gui.nametowidget(space_pos)['text'], gui.nametowidget(name)['text'] = gui.nametowidget(name)['text'], SPACE
    if game.is_solved():
        print("You Win!")

def clickShuffle():
    game.shuffle()
    d = game.get_items()
    for key, value in d.items():
        gui.nametowidget(key)['text'] = value.strip()

def showMoves(path):
    if path.empty():
        return
    move = path.get()
    if move == 0:
        pos, name, _ = game.up(game.position)
    elif move == 1:
        pos, name, _ = game.right(game.position)
    elif move == 2:
        pos, name, _ = game.down(game.position)
    elif move == 3:
        pos, name, _ = game.left(game.position)

    # print(f"Click: {name} at {pos}, Space: {game.position}")
    moveTile(pos)
    gui.after(1000, showMoves, path)
    return

def clickSolve():
    print("Hmm... Let's what I can do.")
    moves = game.solve()
    print("Got it! Here's what you should do...")
    # print(moves)
    for move in moves:
        solution.put(move)
    showMoves(solution)

def clickQuit():
    gui.destroy()
    
if __name__ == '__main__':    
    # make a window
    gui = Tk()
    gui.title("Fifteen")
    # make font
    font = font.Font(family='Helvetica', size='30', weight='bold')
    # make buttons
    buttons_list = []
    for key, val in game.get_items().items():
        text = val.strip()
        name = key
        button = Button(gui, text=text, name=str(name),
                      bg='white', fg='black', font=font, height=3, width=5, 
                      command= lambda name=name: clickButton(name))
        buttons_list.append(button)
    
    shuffle = Button(gui, text="shuffle", name="shuffle",
                      bg='white', fg='black', font=font, 
                      height=2, width=5, command= lambda: clickShuffle())
    solve = Button(gui, text="solve", name="solve",
                      bg='white', fg='black', font=font, 
                      height=2, width=5, command= lambda name="solve": clickSolve())
    quit = Button(gui, text="quit", name="quit",
                      bg='white', fg='black', font=font, 
                      height=2, width=5, command= lambda name="quit": clickQuit())
    
    # the key argument name is used to identify the button
    # add buttons to the window
    # use .grid() or .pack() methods
    for idx, button in enumerate(buttons_list):
        if idx in range(0, 4):
            button.grid(row=0, column=idx)
        elif idx in range(4, 8):
            button.grid(row=1, column=idx - 4)
        elif idx in range(8, 12):
            button.grid(row=2, column=idx - 8)
        elif idx in range(12, 17):
            button.grid(row=3, column=idx - 12)
    shuffle.grid(column = 0, row = 4, columnspan = 2, sticky = W+E)
    solve.grid(column = 2, row = 4, sticky = W+E)
    quit.grid(column=3, row=4)

    # update the window
    gui.mainloop()