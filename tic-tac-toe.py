"""
Tic-tac-toe game
"""
import tkinter
from tkinter import *

window = Tk()

window.geometry("556x432")

player = None

roundWho = True

playerSelect = []

player2Select = []


def res():
    global btn, player, player2Select, playerSelect, roundWho
    for i in range(9):
        btn[i].config(text="", state="disabled", bg="#aaafff")
    player = None
    roundWho = True
    playerSelect = []
    player2Select = []
    btnchoiceo.config(state="normal", bg="#ffffff")
    btnchoicex.config(state="normal", bg="#ffffff")
    btnres.config(text="Select X or Y", state="disabled")


def endgame(w, i, i2, i3):
    global btn, player
    if w == None:
        btnres.config(text="Draw.\nRestart?", state="normal")
        for i in range(9):
            btn[i].config(state="disabled")
        return
    btn[i].config(bg="#ff00ff")
    btn[i2].config(bg="#ff00ff")
    btn[i3].config(bg="#ff00ff")
    for i in range(9):
        btn[i].config(state="disabled")
    if roundWho:
        btnres.config(text=f"Winner is {player}.\nRestart?", state="normal")
    else:
        if player == "X":
            btnres.config(text="Winner is O.\nRestart?", state="normal")
        else:
            btnres.config(text="Winner is X.\nRestart?", state="normal")


def enablebtn():
    global btn, playerSelect, player2Select
    for i in range(9):
        if i not in playerSelect and i not in player2Select:
            btn[i].config(state="normal", bg="#aaafff")
        else:
            btn[i].config(state="disabled", bg="#0fffff")
    return


def check_end():
    global btn, playerSelect, player2Select
    for i in range(9):
        if playerSelect.count(i) and i <= 2 and playerSelect.count(i + 3) and playerSelect.count(i + 6):
            endgame(True, i, i+3, i+6)
        if playerSelect.count(i) and i == 0 and playerSelect.count(4) and playerSelect.count(8):
            endgame(True, 0, 4, 8)
        elif playerSelect.count(i) and not i % 3:
            if playerSelect.count(i + 1):
                if playerSelect.count(i + 2):
                    endgame(True, i, i+1, i+2)
        elif playerSelect.count(i) and i == 2 and playerSelect.count(4) and playerSelect.count(6):
            endgame(True, 2, 4, 6)
    for i in range(9):
        if player2Select.count(i) and i <= 2 and player2Select.count(i + 3) and player2Select.count(i + 6):
            endgame(False, i, i+3, i+6)
        if player2Select.count(i) and i == 0 and player2Select.count(4) and player2Select.count(8):
            endgame(False, 0, 4, 8)
        elif player2Select.count(i) and not i % 3:
            if player2Select.count(i + 1):
                if player2Select.count(i + 2):
                    endgame(False, i, i+1, i+2)
        elif player2Select.count(i) and i == 2 and player2Select.count(4) and player2Select.count(6):
            endgame(False, 2, 4, 6)
    if len(playerSelect) + len(player2Select) == 9:
        endgame(None, 1, 2, 3)
    return


def game(x):
    global player, btn, playerSelect, player2Select, roundWho
    if roundWho:
        playerSelect.append(btn.index(x))
        x.config(text=player)
        for i in btn:
            i.config(state="disabled", bg="#0fffff")
        enablebtn()
        check_end()
        roundWho = False
        if player == "X":
            btnchoicex.config(bg="#ffffff")
            btnchoiceo.config(bg="coral")
        else:
            btnchoiceo.config(bg="#ffffff")
            btnchoicex.config(bg="coral")
    else:
        player2Select.append(btn.index(x))
        if player == "X":
            x.config(text="O")
            btnchoiceo.config(bg="#ffffff")
            btnchoicex.config(bg="coral")
        else:
            x.config(text="X")
            btnchoiceo.config(bg="coral")
            btnchoicex.config(bg="#ffffff")
        for i in btn:
            i.config(state="disabled", bg="#0fffff")
        enablebtn()
        check_end()
        roundWho = True

    return


def choice(x_or_y):
    global btn, player
    if x_or_y:
        player = "X"
        for i in btn:
            i.config(state="normal", bg="#aaafff")
        btnchoiceo.config(state="disabled")
        btnchoicex.config(state="disabled", bg="coral")
    else:
        player = "O"
        for i in btn:
            i.config(state="normal", bg="#aaafff")
        btnchoicex.config(state="disabled")
        btnchoiceo.config(state="disabled", bg="coral")


btn = [i for i in range(9)]

btn[0] = Button(
    text="",
    width=3,
    height=1,
    font=("Comicsans 55"),
    command=lambda: game(btn[0])
)
btn[0].grid(column=0, row=0)


btn[1] = Button(
    text="",
    width=3,
    height=1,
    font=("Comicsans 55"),
    command=lambda: game(btn[1])
)
btn[1].grid(column=1, row=0)

btn[2] = Button(
    text="",
    width=3,
    height=1,
    font=("Comicsans 55"),
    command=lambda: game(btn[2])
)
btn[2].grid(column=2, row=0)

btn[3] = Button(
    text="",
    width=3,
    height=1,
    font=("Comicsans 55"),
    command=lambda: game(btn[3])
)
btn[3].grid(column=0, row=1)

btn[4] = Button(
    text="",
    width=3,
    height=1,
    font=("Comicsans 55"),
    command=lambda: game(btn[4])
)
btn[4].grid(column=1, row=1)

btn[5] = Button(
    text="",
    width=3,
    height=1,
    font=("Comicsans 55"),
    command=lambda: game(btn[5])
)
btn[5].grid(column=2, row=1)


btn[6] = Button(
    text="",
    width=3,
    height=1,
    font=("Comicsans 55"),
    command=lambda: game(btn[6])
)
btn[6].grid(column=0, row=2)

btn[7] = Button(
    text="",
    width=3,
    height=1,
    font=("Comicsans 55"),
    command=lambda: game(btn[7])
)
btn[7].grid(column=1, row=2)

btn[8] = Button(
    text="",
    width=3,
    height=1,
    font=("Comicsans 55"),
    command=lambda: game(btn[8])
)
btn[8].grid(column=2, row=2)

for i in btn:
    i.config(text="", state="disabled", bg="#0fffff")


btnchoicex = Button(
    text="X",
    width=3,
    font=("Comicsans 55"),
    command=lambda: choice(True)
)
btnchoicex.grid(row=0, column=3)

btnchoiceo = Button(
    text="O",
    width=3,
    font=("Comicsans 55"),
    command=lambda: choice(False)
)
btnchoiceo.grid(row=1, column=3)

btnres = Button(
    text="Select X or Y",
    width=10,
    height=5,
    font=("Comicsans 15"),
    command=res,
    state="disabled"
)
btnres.grid(row=2, column=3)

window.mainloop()
