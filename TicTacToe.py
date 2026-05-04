import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe 2.0")
turnsX=[]
turnsO=[]
current_turn="X"
buttons={}
def Grid():
    for row in range(3):
        for col in range(3):
            button=tk.Button(root,text='',width=10,height=5,bg='lightblue',command=lambda r=row, c=col: on_button_click(r, c))
            button.grid(row=row,column=col)
            buttons[(row, col)] = button

def on_button_click(row, col):
    global current_turn, turnsX, turnsO
    if buttons[(row, col)].cget('text') == '':
        buttons[(row, col)].config(text=current_turn,font=('Arial',11,'bold'))
        if current_turn=="X": 
            current_turn="O"
            turnsX.append((row, col))
            if len(turnsX)>3:
                buttons[turnsX[0]].config(text='',bg='lightblue')
                turnsX.pop(0)
            if len(turnsX)==3:
                buttons[turnsX[0]].config(text='X',font=('Arial',11),bg='blue')

        elif current_turn=="O":
            current_turn="X"
            turnsO.append((row, col))
            if len(turnsO)>3:
                buttons[turnsO[0]].config(text='',bg='lightblue')
                turnsO.pop(0)
            if len(turnsO)==3:
                buttons[turnsO[0]].config(text='O',font=('Arial',11),bg='blue')




Grid()
root.mainloop()