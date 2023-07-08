import tkinter as tk

from tkinter import ttk
from boton_sql import retrieve_datos


class TablaData():
    def __init__(self,parent_widget):

        self.columnas = ('MUN',
                         'Nombre',
                         '1° Apellido',
                         '2° Apellido',
                         'Productivo',
                         'Genero',
                         'Jovenes',
                         'Digital',
                         'Institucional')

        self.parent_widget = parent_widget 
        self.tabla_datos = None

    def tabla(self,width,height):
        '''Config de estilo del widget'''
        #Clase de estilos para los encabezados, valores de la tabla y las interacciones con ella
        self.style = ttk.Style()
        self.style.configure('Treeview.Heading',
                             background = 'red',#no se ejecuta
                             foreground='black',
                             font=('Arial Narrow',13,'bold'))

        self.style.configure("Treeview",
                             foreground='black',
                             font=('Arial Narrow',12))
        
        self.style.layout('Treeview.Heading', [('Treeheading.cell', {'sticky': 'nswe'}), ('Treeheading.image', {'side': 'right', 'sticky': ''}), ('Treeheading.text', {'side': 'top', 'sticky': 'w'})])

        # print(self.style.layout('Treeview.Heading'))
        
        '''Creacion del Widget'''
        self.tabla_datos = ttk.Treeview(self.parent_widget,
                                        columns = self.columnas,
                                        style='Treeview')
        
        #Creacion de los valores de tamaño proporcionales para que las columnas se renderizen en el marce de forma simetrica
        numero_columnas = len(self.columnas)
        size_columnas   = int((width-35)/(numero_columnas))

        self.tabla_datos.heading('#0', text='ID')
        self.tabla_datos.column('#0', width=35, stretch=False,anchor='w')

        for col in self.columnas:
            self.tabla_datos.column(col, width=size_columnas,anchor='w',stretch=False)
            self.tabla_datos.heading(col, text=col)    
            
        self.tabla_datos.place(x=0,y=35,width=width,height=height)

    def render_datos(self): 
        lista_beneficiarios = retrieve_datos()

        # print(len((lista_beneficiarios[0])))
        # print(len((lista_beneficiarios)))
        # # print(self.tabla_datos)
        
        for i,p in enumerate(lista_beneficiarios):
            self.tabla_datos.insert('','end',text=(i+1),values=(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8]))
            
        
        