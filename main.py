import tkinter as tk
import config

from recursos_design.configuracion_diseno import *
from app.gui import Marco

def main():
    root = tk.Tk()
    root.title('GDA Cacao Conecta - MEL Beneficiaries App')
    root.resizable(width=True,height=True)
    root.geometry(f'{int(1.3*WIDTH)}x{(2*HEIGHT)}')
    root.config(bg='white') 

    #IMAGEN GDA PORTADA
    portada = Marco(root,'white', width_prct(0.6), height_prct(0.67))
    portada.portada()
    portada.place(x=0,y=0)
    
    #MENU BOTONES
    marco = Marco(root,Cafe, width_prct(0.4),height_prct(0.67))
    marco.menu_botones()
    marco.marco_interno()
    marco.place(x=width_prct(0.6),y=0)

    #MENU TREEVIEW
    
    treeview = Marco(root,bg=Cafe,width = 700,height = (1.30*HEIGHT))  
    treeview.marco_tabla(WIDTH,(1.23*HEIGHT))    
    treeview.place(x=0,y=height_prct(0.62))
  
    root.mainloop()

if __name__ == '__main__':
    main()




