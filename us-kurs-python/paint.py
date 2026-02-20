from tkinter import *
from tkinter.messagebox import showinfo

def info(zdarzenie=None):
    showinfo("Instrukcja", """Rysujemy linie poruszajac mysza z przytrzymanym lewym przyciskiem, kasujemy rysunek prawym przyciskiem myszy, wcisniecie któregokolwiek klawisza konczy dzialanie programu""")

def czysc(zdarzenie=None):
    tlo.delete('all')

def zamknij(zdarzenie=None):
    czysc()
    okno.quit()
    okno.destroy()

# poczatek linii
def poczatek(zdarzenie):
    global x,y
    x=zdarzenie.x
    y=zdarzenie.y

# koniec linii
def rysuj(zdarzenie):
    global x,y
    if x is not None:
        tlo.create_line(x,y,zdarzenie.x,zdarzenie.y,fill="black")
        x=zdarzenie.x
        y=zdarzenie.y

def koncz(zdarzenie):
    global x,y
    rysuj(zdarzenie)
    x = None

x = None
okno = Tk()

menu = Menu(okno)
menuplik = Menu(menu)
menuplik.add_command(label="Instrukcja", command=info)
menuplik.add_separator()
menuplik.add_command(label="Koniec", command=zamknij)
menu.add_cascade(label="Plik", menu=menuplik)

okno.config(menu=menu)

tlo = Canvas(okno,width=400, height=400, bg="yellow")
tlo.pack(fill=BOTH,expand=YES)

tlo.bind("<Button-1>", poczatek)
tlo.bind("<Button-3>", czysc)
tlo.bind("<ButtonRelease-1>", koncz)
tlo.bind("<Motion>", rysuj)

okno.bind("<Any-KeyPress>", zamknij)

okno.mainloop()
