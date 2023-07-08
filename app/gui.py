
import sys
sys.path.append('/Users/josealonsoordinolaaucca/Documents/Documentos/Programacion/app_beneficiariosGDA/app')
sys.path.append('/Users/josealonsoordinolaaucca/Documents/Documentos/Programacion/app_beneficiariosGDA/modelo')
sys.path.append('/Users/josealonsoordinolaaucca/Documents/Documentos/Programacion/app_beneficiariosGDA/recursos_design')
sys.path.append('/Users/josealonsoordinolaaucca/Documents/Documentos/Programacion/app_beneficiariosGDA/recursos_design/logo/Cacao Conecta (Color).png')
sys.path.append('/Users/josealonsoordinolaaucca/Documents/Documentos/Programacion/app_beneficiariosGDA/base_datos/conexion_db.py')
sys.path.append('/Users/josealonsoordinolaaucca/Documents/Documentos/Programacion/app_beneficiariosGDA/base_datos')


import tkinter as tk
import tkmacosx as tkm
import tkinter.messagebox as messagebox


from tkmacosx import Button
from PIL import ImageTk, Image
from boton_sql import actualizar_estado_boton_base
from recursos_design.configuracion_diseno import *
from modelo.modelo_beneficiarios import ModeloDatos
from check_button import CheckButtons
from tree_view import TablaData


class Marco(tk.Frame):
    def __init__(self,root = None ,bg=None,width=None,height=None):
        super().__init__(root, bg=bg,width=width,height=height)
        self.bg = None
        self.pack()

    '''BOTONES'''
    def menu_botones(self):
        #clase funciones del modelo, para importar las funciones desde el modelo

        modelo_datos = ModeloDatos()
        
        
        #boton actualizar
        self.boton_base_estado = False #el boton se encuentra desactivado al iniciar la app
    
        self.boton_base = tkm.Button(self, 
                                     text='MODELAR',
                                     disabledbackground =Cafe,
                                     disabledforeground=Cafe,
                                     state='disabled',
                                     width=120,
                                     borderless = True,
                                     command = lambda : [modelo_datos.data_wragling(),                                                        
                                                         messagebox.showinfo('Info', 'Operacion Realizada \n\n Boton SUBIR SQL Creado'),
                                                         actualizar_estado_boton_base(self,True)])
        self.boton_base.place(x=15,y=215)

        #boton subir sql
        self.boton_subir = tkm.Button(self, 
                                text='SUBIR DATA',
                                width=120,
                                borderless = True,
                                command = lambda: [modelo_datos.crear_tabla()])

    '''TABLA VISTA - FRAME'''
    def marco_tabla(self,width,height):
        tabla_beneficiarios = TablaData(self)
        tabla_beneficiarios.tabla(width,height)

        #BOTON ACTUALZIAR DATOS DEL DASHBOARD E INDICADORES CLAVES
        boton_actualizar = tkm.Button(
            self,
            text='DASHBOARD',
            width=120,
            borderless=True,
            command=lambda: [tabla_beneficiarios.tabla(width, height),
                             tabla_beneficiarios.render_datos()])
        boton_actualizar.place(x=500, y=2)


    '''INDICADORES CLAVES Y DASHBOARD'''

    
        #FUNCIONES SQL
        #LABELS A RENDERIZAR 

    '''CHECK_BUTTON - MARCO INTERNO'''
    def marco_interno(self):
        self.marco_checkbutton = tk.LabelFrame(self,
                                               text='Instrumentos - Check List',
                                               fg='white',
                                               font=fuente_portada,
                                               bg=Cafe,
                                               bd=1,
                                               relief='sunken')
        
        self.marco_checkbutton.place(x=x_label,y=y_label,width=widht_label,height=height_label)

        lista_check_botones = CheckButtons(self.marco_checkbutton,self.boton_base)
        lista_check_botones.create_checkbuttons()

    '''PORTADA'''
    #PORTADA DE LA APLICACION: SIN FUNCIONALIDAD ES SOLO IMAGEN
    def portada(self):
        # Ruta de la imagen
        self.ruta_imagen = "recursos_design/logo/Cacao Conecta (Color).png"

        # Cargar la imagen
        self.imagen = Image.open(self.ruta_imagen)
        self.imagen = self.imagen.resize((portada_width, portada_height))  # Ajustar el tamaño de la imagen si es necesario

        # Convertir la imagen a un objeto compatible con Tkinter
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)

        # Crear una etiqueta para mostrar la imagen
        self.etiqueta_imagen = tk.Label(self, image=self.imagen_tk)
        self.etiqueta_imagen.image = self.imagen_tk  # Guardar una referencia a la imagen para evitar que se elimine por el recolector de basura
        self.etiqueta_imagen.place(x=0,y=height_prct(0.05))
