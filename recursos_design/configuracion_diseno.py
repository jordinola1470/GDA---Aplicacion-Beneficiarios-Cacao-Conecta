#SIZE DEL FRAME

HEIGHT = 400
WIDTH  = 700

def width_prct(porcentaje):
    return porcentaje * WIDTH

def height_prct(porcentaje):
    return int(porcentaje * HEIGHT)

#COLORES GDA EN HEX

Cafe      = '#58151e'
Vinotinto = '#87293b'
Verde     = '#6a7950'
Amarillo  = '#de9139'

#FUENTES/SIZE DE BOTONES

font_boton = ()

#DATO GEOMETRICOS_LABEL FRAME

x_label = 25
y_label = 25

widht_label  = (width_prct(2/5)-(x_label+y_label))
height_label = height_prct(3/7)

fuente_check = ('Arial Narrow',14)

#DATOS DE PORTADOA

portada_width  = int(width_prct(0.60))
portada_height = int(portada_width/2)
fuente_portada = ('Arial Narrow',16)

#DICCIONARIO DE CAMBIO DE COLUMNA

data_frameLabels = ['MUNICIPIO', 'ZONA', 'VEREDA', 'ASOCIACIÓN', 'NOMBRES',
                    'PRIMER APELLIDO', 'SEGUNDO APELLIDO', 'N° CEDULA', 'EDAD', 'GENERO ',
                    'ETNIA', 'VICTIMA ', 'COMPONENTE', 'RANGO EDAD', 'C1_Productivo',
                    'C2_Genero', 'C2_Jovenes', 'C3_Digitales', 'C3_Institucional']

sql_frameLabels  = ['MUNICIPIO', 
                'ZONA', 
                'VEREDA', 
                'ASOCIACIÓN', 
                'NOMBRES',
                'PRIMER_APELLIDO', 
                'SEGUNDO_APELLIDO', 
                'N_CEDULA', 
                'EDAD', 
                'GENERO',
                'ETNIA', 
                'VICTIMA', 
                'COMPONENTE', 
                'RANGO_EDAD', 
                'C1_Productivo',
                'C2_Genero', 
                'C2_Jovenes', 
                'C3_Digitales', 
                'C3_Institucional']

labels_rename = dict(zip(data_frameLabels,sql_frameLabels))
