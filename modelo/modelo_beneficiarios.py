#Librerias
import sys
sys.path.append('/Users/josealonsoordinolaaucca/Documents/Documentos/Programacion/app_beneficiariosGDA/app')
sys.path.append('/Users/josealonsoordinolaaucca/Documents/Documentos/Programacion/app_beneficiariosGDA/modelo')
sys.path.append('/Users/josealonsoordinolaaucca/Documents/Documentos/Programacion/app_beneficiariosGDA/recursos_design')
sys.path.append('/Users/josealonsoordinolaaucca/Documents/Documentos/Programacion/app_beneficiariosGDA/base_datos')


import pandas as pd
import warnings
warnings.filterwarnings('ignore')
#Built-In Jose Ordinola Functions

from subfunciones_beneficiarios import funcionBeneficiarios_C1,funcionBeneficiarios_C2_C3,funcionBeneficiarios
from base_datos.conexion_db import ConexionDB
from recursos_design.configuracion_diseno import *



class ModeloDatos():
    def __init__(self):

        self.data_wrangling_frame = None

    def data_wragling(self):

        '''
        --------------
        COMPONENTE 01:
        --------------
        Se cargan los beneficiarios "activos" al cierre del ultimo reporte Trimestral
        ------------------------------------------------------------------------------
        '''

        '''Instrumento CC01'''
        instrumentoCC01 = '/Users/josealonsoordinolaaucca/Library/CloudStorage/OneDrive-Bibliotecascompartidas:FundaciónIdeasparalaPaz/Gobernanza y Seguridad - GDA/M&E/GDA Y3/MyE_GDA_Componente 1/CC01 Reporte de Productividad Y3.xlsx'
        beneficiaries_C1 = pd.read_excel(instrumentoCC01,header=4)

        '''Beneficiarios Componente C1''' 
        beneficiaries_C1 = funcionBeneficiarios_C1(beneficiaries_C1)


        '''
        --------------
        COMPONENTE 02:
        --------------
        Se cargan los beneficiarios "activos" al cierre del ultimo reporte Trimestral 

        Se toman en consideracion tres bases del C2 :

            1.- Genero
            2.- Jovenes
            3.- Gobernanza
        ------------------------------------------------------------------------------
        '''

        '''Instrumentos C2'''
        instrumentoCC21 = '/Users/josealonsoordinolaaucca/Library/CloudStorage/OneDrive-Bibliotecascompartidas:FundaciónIdeasparalaPaz/Gobernanza y Seguridad - GDA/M&E/GDA Y3/MyE_GDA_Componente 2/CC21_Lista_Asistencia_Genero.xlsx'
        instrumentoCC22 = '/Users/josealonsoordinolaaucca/Library/CloudStorage/OneDrive-Bibliotecascompartidas:FundaciónIdeasparalaPaz/Gobernanza y Seguridad - GDA/M&E/GDA Y3/MyE_GDA_Componente 2/CC22_Lista_Asistencia_Jovenes.xlsx'
        instrumentoCC23 = '/Users/josealonsoordinolaaucca/Library/CloudStorage/OneDrive-Bibliotecascompartidas:FundaciónIdeasparalaPaz/Gobernanza y Seguridad - GDA/M&E/GDA Y3/MyE_GDA_Componente 2/CC23_Lista_Asistencia_Gobernanza.xlsx'

        beneficiaries_CC21 = pd.read_excel(instrumentoCC21,sheet_name='resumen_mel')
        beneficiaries_CC22 = pd.read_excel(instrumentoCC22,sheet_name='resumen_mel')
        beneficiaries_CC23 = pd.read_excel(instrumentoCC23,sheet_name='resumen_mel')

        '''Beneficiarios Componente C2'''
        beneficiaries_CC21,beneficiaries_CC22,beneficiaries_CC23 = funcionBeneficiarios_C2_C3(beneficiaries_CC21),\
                                                                funcionBeneficiarios_C2_C3(beneficiaries_CC22),\
                                                                funcionBeneficiarios_C2_C3(beneficiaries_CC23)

        beneficiaries_C2 = pd.concat([beneficiaries_CC21,beneficiaries_CC22,beneficiaries_CC23])

        '''
        --------------
        COMPONENTE 03:
        --------------
        Se cargan los beneficiarios "activos" al cierre del ultimo reporte Trimestral 

        Se toman en consideracion dos bases del C3 :

            1.- Habilidades Digitales
            2.- Institucional 
        ------------------------------------------------------------------------------
        '''

        '''Instrumentos C3'''
        instrumentoCC31 = '/Users/josealonsoordinolaaucca/Library/CloudStorage/OneDrive-Bibliotecascompartidas:FundaciónIdeasparalaPaz/Gobernanza y Seguridad - GDA/M&E/GDA Y3/MyE_GDA_Componente 3/CC31_Lista_Asistencia_Institucional.xlsx'
        instrumentoCC32 = '/Users/josealonsoordinolaaucca/Library/CloudStorage/OneDrive-Bibliotecascompartidas:FundaciónIdeasparalaPaz/Gobernanza y Seguridad - GDA/M&E/GDA Y3/MyE_GDA_Componente 3/CC32_Lista_Asistencia_Habilidades Digitales.xlsx'

        beneficiaries_CC31 = pd.read_excel(instrumentoCC31,sheet_name='resumen_mel')
        beneficiaries_CC32 = pd.read_excel(instrumentoCC32,sheet_name='resumen_mel')

        '''Beneficiarios Componente C3'''
        beneficiaries_CC31,beneficiaries_CC32 = funcionBeneficiarios_C2_C3(beneficiaries_CC31),\
                                                funcionBeneficiarios_C2_C3(beneficiaries_CC32),\
                                                
        beneficiaries_C3 = pd.concat([beneficiaries_CC31,beneficiaries_CC32])


        '''
        ------------------------------------------------------------------------------
        BENEFICIARIOS Y3
        ------------------------------------------------------------------------------
            Se concatenan la base de beneficiarios registrados en los intrumentos de 
            las actividades realizadas por componente
                
                C1 -> Productividad
                C2 -> Jovenes, Genero, Gobernanza
                C3 -> Institucional, Habilidades Blandas
            
            * El codigo genera un conteo por COMPONENTE
            * Despues crea una base de datos unificada de los beneficiarios que
            incluye las actividades en las cuales participa el beneficiario.    
                
        ------------------------------------------------------------------------------ '''

        '''* BASE PARA FILTRAR DATOS POR COMPONENTE'''
        beneficiaries_draft = pd.concat([beneficiaries_C1,
                                        beneficiaries_C2,
                                        beneficiaries_C3]) 

        '''* BASE UNIFICADA DE BENEFICIARIOS Y3'''
        self.data_wrangling_frame = funcionBeneficiarios(beneficiaries_draft)

        print(self.data_wrangling_frame.shape)


    def crear_tabla(self):
        conexion = ConexionDB('beneficiarios_gda')

        sql_crear = ''' 
            CREATE TABLE 'Beneficiarios Y3' (
                'MUNICIPIO' VARCHAR(50), 
                'ZONA' VARCHAR(50), 
                'VEREDA' VARCHAR(50), 
                'ASOCIACIÓN' VARCHAR(50), 
                'NOMBRES' VARCHAR(50),
                'PRIMER_APELLIDO' VARCHAR(50), 
                'SEGUNDO_APELLIDO' VARCHAR(50), 
                'N_CEDULA' VARCHAR(50) NOT NULL, 
                'EDAD'VARCHAR(50), 
                'GENERO' VARCHAR(50),
                'ETNIA' VARCHAR(50), 
                'VICTIMA' VARCHAR(50), 
                'COMPONENTE' VARCHAR(50), 
                'RANGO_EDAD' VARCHAR(50), 
                'C1_Productivo' VARCHAR(50),
                'C2_Genero' VARCHAR(50), 
                'C2_Jovenes' VARCHAR(50), 
                'C3_Digitales' VARCHAR(50), 
                'C3_Institucional VARCHAR(50)',
                PRIMARY KEY("N_CEDULA")
        );'''

        sql_drop = ''' 
            DROP TABLE IF EXISTS 'Beneficiarios Y3' 
        ;'''

        conexion.cursor.execute(sql_drop)
        conexion.cursor.execute(sql_crear)
        
        #########

        self.data_wrangling_frame = self.data_wrangling_frame.rename(columns=labels_rename)

        # self.sql_valores = ''
        # for index,row in self.data_wrangling_frame.iterrows():
        #     valores = ', '.join([f'{str(valor)}' for valor in row]) #une los valores de las columnas como un csv
        #     self.sql_valores += f"({valores}), " #las convierte en sets

        # # Elimina la coma final
        # self.sql_valores = self.sql_valores.rstrip(', ')

        # # Construye el statement completo
    
        # sql_insert = f"INSERT INTO 'Benediciarios Y3' VALUES {self.sql_valores};"

        # print(sql_insert)

        # conexion.cursor.execute(sql_insert)


        self.data_wrangling_frame.to_sql(name = 'Beneficiarios Y3',
                                         con = conexion.conn, 
                                         if_exists = 'replace',
                                         index = False)    



        conexion.cerrar_conexion()