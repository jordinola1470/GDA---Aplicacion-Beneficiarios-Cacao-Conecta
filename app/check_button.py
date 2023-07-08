import tkinter as tk
from recursos_design.configuracion_diseno import *

class CheckButtons():
    def __init__(self, marco_checkbutton,boton_base):
        self.marco_checkbutton = marco_checkbutton
        self.boton_base = boton_base

        self.valores = ['CC01-Productividad',
                   'CC21-Genero',
                   'CC22-Jovenes',
                   'CC23-Gobernanza',
                   'CC31-Habilidades Digitales',
                   'CC32-Institucional']
        
        self.variables = []

    def create_checkbuttons(self):
        '''Funcion que crea el widget, los renderiza y condiciona el boton base
            
            - Revisa si todos han sido marcados por medio de la funcion all(), 
              y cambia el estado del boton_base 

            - Cambia el estado del boton_base en funcion a el valor de todos los botones

            - Renderiza los checkbuttons en pantalla, tomando como referencia, las lista
              self.valores'''


        '''01'''
        def obtener_estados():
            todos_marcados_true = all(var.get() for var in self.variables)#variables caputa si todos los valores son TRUE
            #condicional que cambia el estado del boton
            
            if todos_marcados_true:
                self.boton_base.config(
                                    fg='black',
                                    state='normal')
            else:
                self.boton_base.config(disabledbackground = Cafe,
                                    disabledforeground = Cafe,
                                    relief = 'flat',
                                    state='disabled')
                
        '''02'''
        def deshabilitar_boton_base():
            self.boton_base.config(state='disabled')


        '''03'''
        for i, valor in enumerate(self.valores):
            var = tk.BooleanVar()
            var.trace('w',lambda *args: obtener_estados())
            var.trace('w', lambda *args: deshabilitar_boton_base())
            
            self.variables.append(var)

            checkbutton = tk.Checkbutton(self.marco_checkbutton, 
                                         text=valor, 
                                         variable=var,
                                         background=Cafe,
                                         selectcolor='black',
                                         font=fuente_check,
                                         fg='white')

            checkbutton.place(x=20 , y=23 * i)

