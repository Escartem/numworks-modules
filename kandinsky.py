# TODO : la fonction get_pixel ne marche pas
# TODO : la fonction draw_string n'a pas la bonne taille
# TODO : il faut ajouter un background blanc à la fonction draw_string pour être + proche de ce que fait la Numworks 

from tkinter import Tk, Canvas, TOP, mainloop, DISABLED, Button, LEFT

class Color:
    def __init__(self, r, g, b):
        self.rgb = (r, g, b)
        self.hex = f'#{r:02x}{g:02x}{b:02x}'
    
    def __repr__(self):
        return str(self.rgb)

fen = Tk()
can = Canvas(fen, width=310, height=222, bg='white')
can.pack(side=TOP, padx=0, pady=0)

#window = [[Color(255, 255, 255) for i in range(310)] for j in range(222)]

def color(r, g, b):
    return Color(r, g, b)

def fill_rect(x, y, width, height, color:Color):
    #for i in range(y, yy):
    #    for j in range(x, xx):
    #        window[i][j] = color
    can.create_rectangle(x, y, x+width, y+height, fill=color.hex, outline='', dash='')
    can.update()

def draw_string(text, x, y):
    can.create_text(x, y, text=text, anchor="nw")
    can.update()

def set_pixel(x, y, color:Color):
    #window[y][x] = color
    can.create_rectangle(x, y, x+1, y+1, fill=color.hex)

def get_pixel(x, y):
    #return window[y][x]
    pass

def start(program):
    b1 = Button(fen, text='Lancer', command=lambda : program(), bg='black' , fg='green')
    b1.pack(side=LEFT, padx=5, pady=5)
    fen.mainloop()