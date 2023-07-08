import pandas as pd
import warnings
warnings.filterwarnings('ignore')

'''-------------------------------------------------------------------------------------------------------------------'''
'''PRIMERA FUNCION'''

def funcionBeneficiarios_C1(beneficiaries_C1):
    #Filtro Beneficiarios = Activos 
    beneficiaries_C1 = beneficiaries_C1[beneficiaries_C1['ESTADO BENEFICIARIO/A'] == 'ACTIVO']

    #Seleccion de columnas para la BD
    beneficiaries_C1 = beneficiaries_C1[['MUNICIPIO', 'ZONA', 'VEREDA','ASOCIACIÓN', 'NOMBRES', 
                                        'PRIMER APELLIDO','SEGUNDO APELLIDO', 'N° CEDULA', 'EDAD',
                                        'GENERO', 'ETNIA', 'VICTIMA']]

    #Limpieza de las cadenas de texto en formato title
    beneficiaries_C1[['ZONA','VEREDA','NOMBRES','PRIMER APELLIDO','SEGUNDO APELLIDO']] = \
        beneficiaries_C1[['ZONA','VEREDA','NOMBRES','PRIMER APELLIDO','SEGUNDO APELLIDO']]\
            .apply(lambda x:x.str.lower().str.title())

    #Se incluiyen los 0 a la izquierda a los valores de la cedula
    beneficiaries_C1['N° CEDULA'] = [str(x).zfill(10) for x in beneficiaries_C1['N° CEDULA']]

    #Se redondea la fecha de nacimiento al mayor numero entero
    beneficiaries_C1['EDAD'] = [round(x) for x in beneficiaries_C1['EDAD']]

    #Se incluye columna de componente para poder identificar tratamiento del beneficiario en funcion del componente
    beneficiaries_C1['COMPONENTE'] = 'C1_Productivo'

    #Ajuste labels de columna genero y victima para la concatenacion con los demas instrumentos
    beneficiaries_C1.rename(columns={'GENERO':'GENERO ','VICTIMA':'VICTIMA '},inplace=True)

    return beneficiaries_C1


'''-------------------------------------------------------------------------------------------------------------------'''
'''SEGUNDA FUNCION'''

def funcionBeneficiarios_C2_C3(data):
    data = data.drop_duplicates(subset='N° CEDULA')
    data = data[['MUNICIPIO', 'ZONA', 'VEREDA', 'NOMBRES',
                 'PRIMER APELLIDO', 'SEGUNDO APELLIDO', 'N° CEDULA',
                 'EDAD', 'GENERO ', 'ETNIA', 'VICTIMA ','COMPONENTE']]
    
    #Se incluiyen los 0 a la izquierda a los valores de la cedula
    data['N° CEDULA'] = [str(x).zfill(10) for x in data['N° CEDULA']]

    return data


'''-------------------------------------------------------------------------------------------------------------------'''
'''TERCERA FUNCION'''

def funcionBeneficiarios(data):

    #creacion columna rango de edad
    data['RANGO EDAD'] = ['18 - 28' if x>17 and x<29 else '-' for x in data['EDAD']]

    '''Base de Datos'''
    data_pivote = data.pivot_table(
                            index='N° CEDULA',
                            columns='COMPONENTE',
                            values='MUNICIPIO',
                            aggfunc = 'count'                        
                            ).fillna('-')
    
    data = pd.merge(
                        left     = data,
                        right    = data_pivote,
                        left_on  = 'N° CEDULA',        
                        right_on = 'N° CEDULA',
                        how      = 'left'
                    )

    data = data.drop_duplicates(subset='N° CEDULA')

    return data
