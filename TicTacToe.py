import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Tic Tac Toe 2.0")
turnsX=[]
turnsO=[]
current_turn="X"
buttons={}
Win_combinations=[[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)],[(2,0),(2,1),(2,2)],
                  [(0,0),(1,0),(2,0)],[(0,1),(1,1),(2,1)],[(0,2),(1,2),(2,2)],
                  [(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
def Grid():
    for row in range(3):
        for col in range(3):
            button=tk.Button(root,text='',width=10,height=5,bg='lightblue',command=lambda r=row, c=col: on_button_click(r, c))
            button.grid(row=row,column=col)
            buttons[(row, col)] = button

def game_over_window(winner):
    global GameOverWindow
    GameOverWindow= tk.Toplevel(root)
    GameOverWindow.title("Game Over")
    GameOverWindow.geometry("300x100")
    GameOverWindow.configure(bg='lightblue')
    tk.Label(GameOverWindow,text=f"{winner} Has Won!",bg='lightblue').pack(pady=5)
    restart_button=tk.Button(GameOverWindow,text="Restart",bg='lightblue',command=Restart_Game)
    restart_button.pack(pady=10)



def Restart_Game():
    global current_turn, turnsX, turnsO
    current_turn="X"
    turnsX.clear()
    turnsO.clear()
    for button in buttons.values():
        button.config(text='',bg='lightblue')
    GameOverWindow.destroy()

def on_button_click(row, col):
    global current_turn, turnsX, turnsO
    if buttons[(row, col)].cget('text') == '':
        buttons[(row, col)].config(text=current_turn,font=('Arial',11,'bold'))
        if current_turn=="X": 
            current_turn="O"
            turnsX.append((row, col))
            if len(turnsX)>3:
                buttons[turnsX[0]].config(text='',bg='lightblue')
                buttons[turnsO[0]].config(text='O',font=('Arial',11),bg='blue') 
                turnsX.pop(0)
            if len(turnsX)==3:
                if turnsX in Win_combinations:
                    print("X wins!")
                    game_over_window("X")


        elif current_turn=="O":
            current_turn="X"
            turnsO.append((row, col))
            if len(turnsO)>3:
                buttons[turnsO[0]].config(text='',bg='lightblue')
                buttons[turnsX[0]].config(text='X',font=('Arial',11),bg='blue')
                turnsO.pop(0)
            if len(turnsO)==3:
                buttons[turnsX[0]].config(text='X',font=('Arial',11),bg='blue')
                if turnsO in Win_combinations:
                    print("O wins!")
                    game_over_window("O")



Grid()
root.mainloop()