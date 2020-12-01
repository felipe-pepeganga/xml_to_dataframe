from tkinter import *
from tkinter import messagebox
import active_products as ap
import os

def call_export():
    ap.exportar_csv()
    messagebox.showinfo("Informacion", "archivo exportado.")
def call_plu():
    ap.plu()
    messagebox.showinfo("Informacion", "archivo modificado.")
    
raiz = Tk()
raiz.title("Conversion de xml a dataframe")
raiz.resizable(1,1)
raiz.geometry("225x225")

"""path = str(os.path.dirname(__file__))
print(path)
img = PhotoImage(file=path+'/descarga.png')
background_label = Label(raiz, image=img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
raiz.tk.call('wm', 'iconphoto', raiz._w, img)"""
exportar = Button(raiz, text='Exportar', command=call_export).grid(row=4, column=1)
plu = Button(raiz, text='0 PLUS', command=call_plu).grid(row=4, column=2)
"""frame = Frame()
frame.pack()
frame.config(bg="red")
frame.config(width="650", height="350")"""
raiz.mainloop()