
from base_datos.conexion_db import ConexionDB


#actualizacion del boton en funcion al click
''' El boton estado subir se renderiza una vez que el estado del boton_sql cambia a True, todo esto gracias a la ejecucion de lafuncion
    actualizar estado del boton, la cual contiene una condicion que permite el place del boton en la pantalla, al cumplirse el booleano'''

def actualizar_estado_boton_base(self,estado):
    
    self.boton_base_estado = estado    

    if self.boton_base_estado:
        self.boton_subir.place(x=147,y=215)
    else:
        self.boton_subir.pack_forget()

def retrieve_datos():
    conexion     = ConexionDB('beneficiarios_gda')
 
    sql_retrieve = '''SELECT MUNICIPIO,
                             NOMBRES,
                             PRIMER_APELLIDO,
                             SEGUNDO_APELLIDO,
                             C1_Productivo,
                             C2_Genero,
                             C2_Jovenes,
                             C3_Digitales,
                             C3_Institucional 
                      FROM 'Beneficiarios Y3' ;''' 

    conexion.cursor.execute(sql_retrieve)

    lista_beneficiarios = conexion.cursor.fetchall()

    conexion.cerrar_conexion()

    return lista_beneficiarios

