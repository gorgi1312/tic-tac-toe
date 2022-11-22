from tkinter import *
import random


def next_turn(row, column):
    global player
    global result1
    global result2
    if buttons[row][column]['text'] == '' and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=players[1]+" Turn")
            elif check_winner() is True:
                result1 += 1
                label.config(text=(player+' Winner'))
                label_points1.config(text=players[0]+" points:"+str(result1))
            elif check_winner() =="Tie":
                label.config(text=("Tie"))
        else:
            buttons[row][column]["text"] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=players[0]+" Turn")
            elif check_winner() is True:
                result2 += 1
                label.config(text=(players[1] + 'Winner'))
                label_points2.config(text=players[1] + " points:" + str(result2))
            elif check_winner() == "Tie":
                label.config(text=("Tie"))


def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons [row][1]['text'] == buttons [row][2]['text'] != '':
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]['text'] == buttons[2][column]['text'] != '':
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    if buttons[0][0]["text"] == buttons [1][1]['text'] == buttons [2][2]['text'] != '':
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]["text"] == buttons [1][1]['text'] == buttons [2][0]['text'] != '':
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif empty() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="gold")
        return "Tie"
    else:
        return False


def empty():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != '':
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player+'Turn')
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text='', bg="#F0F0F0")




window = Tk()
window.title("Tic tac toe")
players = ['X', "O"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
result1 = 0
result2 = 0
game_frame = Frame(window)
game_frame.config(bg="grey")
game_frame.pack()
label = Label(game_frame, text=player+" Turn", font=("Arial",40))
label.grid(column=3, row=0)
label_points1 = Label(game_frame,text=players[0]+"Points:", font=("Arial",20))
label_points1.grid(column=2, row=0)
label_points2 = Label(game_frame,text=players[1]+"Points:", font=("Arial",20))
label_points2.grid(column=4, row=0)
reset_button = Button(game_frame, text="RESET", font=("Arial", 28), command=new_game)
reset_button.grid(column=3, row=1)
frame = Frame(game_frame)
frame.grid(column=3, row=2)
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text='', font=("Arial",40), width=5,
                         height=2, command=lambda row=row, column=column:
                        next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)
window.mainloop()