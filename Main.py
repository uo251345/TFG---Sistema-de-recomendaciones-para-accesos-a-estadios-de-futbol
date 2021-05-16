try:
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import ion

    
    

except:
    raise
 
import networkx as nx

import numpy

import uuid

import Funciones 

import Clases

import threading
import time

import sys

import os

import colorama
from colorama import Fore, Style, Back


#Para ignorar algunos warning de libreia deprecated
import warnings
warnings.filterwarnings("ignore")
    
    
    
DEBUG=False


#Ubicacion del fichero Main.py
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


#Variables para la ejecuccion del programa
rutaMasCorta = False
rutaMasRapida = False
rutaSegunAtributos = False
simularRutaConControlDeOcupaciones = False


#VARIABLES GLOBALES
FACTOR_SUBIDA_ESCALERAS = 0.79
FACTOR_BAJADA_ESCALERAS = 0.57 
FACTOR_PLANOS = 1.56




#Habilita el modo interactivo en pyplot para poder mostrar y continuar
ion()

#Inicializar Grafo
G=nx.MultiDiGraph()

# Añadimos los nodos con su posicion 

#Nodo puerta
G.add_node('P1', pos=(3, -0.5))

#Nodo del Nivel 0
G.add_node('01', pos=(2, 1))
G.add_node('02', pos=(4, 1))

#Nodo del Nivel 1
G.add_node('11', pos=(1, 2))
G.add_node('12', pos=(2, 2))
G.add_node('13', pos=(3, 2))
G.add_node('14', pos=(4, 2))
G.add_node('15', pos=(5, 2))

#Nodo del Nivel 2
G.add_node('21', pos=(1, 3.5))
G.add_node('22', pos=(2, 3.5))
G.add_node('23', pos=(3, 3.5))
G.add_node('24', pos=(4, 3.5))
G.add_node('25', pos=(5, 3.5))

#Nodo del Nivel 3
G.add_node('31', pos=(1, 5.5))
G.add_node('32', pos=(3, 5.5))
G.add_node('33', pos=(5, 5.5))







# Añadimos los enlaces con los pesos de cada uno y la etiqueta    (Esta parte se leera de un JSON y se rellenara sola)

#Los de la puerta
G.add_edge('P1','12',weight=9.0 ,  label='', tipoEnlace = 'escalera', longitud = '9.0' , inclinacion = '+', barandilla = 'True', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'False', pasilloSeco = 'True', pasilloIluminado = 'False' , ocupacion = '0.0' )
G.add_edge('P1','14',weight=9.0 , label='', tipoEnlace = 'escalera', longitud = '9.0' , inclinacion = '+', barandilla = 'True', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'False', pasilloSeco = 'True', pasilloIluminado = 'False' , ocupacion = '0.0' )
G.add_edge('P1','22',weight=30.0 , label='', tipoEnlace = 'escalera', longitud = '30.0' , inclinacion = '+', barandilla = 'True', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'False', pasilloSeco = 'True', pasilloIluminado = 'False' , ocupacion = '0.0' )
G.add_edge('P1','24',weight=30.0 , label='', tipoEnlace = 'escalera', longitud = '30.0' , inclinacion = '+', barandilla = 'True', pasilloBuenEstado = 'False',  pasilloAmplio = 'True', pasilloVentildo = 'False', pasilloSeco = 'True', pasilloIluminado = 'False' , ocupacion = '0.0' )

#Los del Nivel 0
G.add_edge('01','12',weight=9.0 , label='', tipoEnlace = 'escalera', longitud = '10.0' , inclinacion = '+', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'False', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('01','02',weight=20.0 , label='', tipoEnlace = 'plano', longitud = '20.0' , inclinacion = '', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'False', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('02','01',weight=20.0 , label='', tipoEnlace = 'plano', longitud = '20.0' , inclinacion = '', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'False', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('02','14',weight=9.0 , label='', tipoEnlace = 'escalera', longitud = '10.0' , inclinacion = '+', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'False', pasilloIluminado = 'True' , ocupacion = '0.0' )


#Los del Nivel 1
G.add_edge('11','12',weight=10.0 , label='', tipoEnlace = 'plano', longitud = '10.0' , inclinacion = '', barandilla = 'True', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'True', pasilloSeco = 'False', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('11','21',weight=20.0 , label='', tipoEnlace = 'escalera', longitud = '20.0' , inclinacion = '+', barandilla = 'True', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'False', pasilloIluminado = 'True' , ocupacion = '0.0' )

G.add_edge('12','01',weight=9.0 , label='', tipoEnlace = 'escalera', longitud = '10.0' , inclinacion = '-', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'False', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('12','11',weight=10.0 , label='', tipoEnlace = 'plano', longitud = '10.0' , inclinacion = '', barandilla = 'True', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'True', pasilloSeco = 'False', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('12','13',weight=10.0 , label='', tipoEnlace = 'plano', longitud = '10.0' , inclinacion = '', barandilla = 'True', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'True', pasilloSeco = 'False', pasilloIluminado = 'True' , ocupacion = '0.0' )

G.add_edge('13','12',weight=10.0 , label='', tipoEnlace = 'plano', longitud = '10.0' , inclinacion = '', barandilla = 'True', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'True', pasilloSeco = 'False', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('13','14',weight=10.0 , label='', tipoEnlace = 'plano', longitud = '10.0' , inclinacion = '', barandilla = 'True', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'True', pasilloSeco = 'False', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('13','23',weight=20.0 , label='', tipoEnlace = 'escalera', longitud = '20.0' , inclinacion = '+', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'False', pasilloIluminado = 'True' , ocupacion = '0.0' )

G.add_edge('14','02',weight=9.0 , label='', tipoEnlace = 'escalera', longitud = '10.0' , inclinacion = '-', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'False', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('14','13',weight=10.0 , label='', tipoEnlace = 'plano', longitud = '10.0' , inclinacion = '', barandilla = 'True', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'True', pasilloSeco = 'False', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('14','15',weight=10.0 , label='', tipoEnlace = 'plano', longitud = '10.0' , inclinacion = '', barandilla = 'True', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'True', pasilloSeco = 'False', pasilloIluminado = 'True' , ocupacion = '0.0' )

G.add_edge('15','14',weight=10.0 , label='', tipoEnlace = 'plano', longitud = '10.0' , inclinacion = '', barandilla = 'True', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'True', pasilloSeco = 'False', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('15','25',weight=20.0 , label='', tipoEnlace = 'escalera', longitud = '20.0' , inclinacion = '+', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'False', pasilloIluminado = 'True' , ocupacion = '0.0' )



#Los del Nivel 2
G.add_edge('21','11',weight=20.0 , label='', tipoEnlace = 'escalera', longitud = '20.0' , inclinacion = '-', barandilla = 'True', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('21','22',weight=10.0 , label='', tipoEnlace = 'plano', longitud = '10.0' , inclinacion = '', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'True', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('21','31',weight=25.0 , label='', tipoEnlace = 'escalera', longitud = '25.0' , inclinacion = '+', barandilla = 'True', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )

G.add_edge('22','21',weight=10.0 , label='', tipoEnlace = 'plano', longitud = '10.0' , inclinacion = '', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'True', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('22','23',weight=10.0 , label='', tipoEnlace = 'plano', longitud = '10.0' , inclinacion = '', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'True', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )

G.add_edge('23','13',weight=20.0 , label='', tipoEnlace = 'escalera', longitud = '20.0' , inclinacion = '-', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('23','22',weight=10.0 , label='', tipoEnlace = 'plano', longitud = '10.0' , inclinacion = '', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'True', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('23','24',weight=10.0 , label='', tipoEnlace = 'plano', longitud = '10.0' , inclinacion = '', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'True', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('23','32',weight=25.0 , label='', tipoEnlace = 'escalera', longitud = '25.0' , inclinacion = '+', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )

G.add_edge('24','23',weight=10.0 , label='', tipoEnlace = 'plano', longitud = '10.0' , inclinacion = '', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'True', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('24','25',weight=10.0 , label='', tipoEnlace = 'plano', longitud = '10.0' , inclinacion = '', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'True', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )

G.add_edge('25','15',weight=20.0 , label='', tipoEnlace = 'escalera', longitud = '20.0' , inclinacion = '-', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('25','24',weight=10.0 , label='', tipoEnlace = 'plano', longitud = '10.0' , inclinacion = '', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'True', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('25','33',weight=25.0 , label='', tipoEnlace = 'escalera', longitud = '25.0' , inclinacion = '+', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )



#Los del Nivel 23
G.add_edge('31','21',weight=25.0 , label='', tipoEnlace = 'escalera', longitud = '25.0' , inclinacion = '-', barandilla = 'True', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('31','32',weight=20.0 , label='', tipoEnlace = 'plano', longitud = '20.0' , inclinacion = '', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'False', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )

G.add_edge('32','23',weight=25.0 , label='', tipoEnlace = 'escalera', longitud = '25.0' , inclinacion = '-', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('32','31',weight=20.0 , label='', tipoEnlace = 'plano', longitud = '20.0' , inclinacion = '', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'False', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('32','33',weight=20.0 , label='', tipoEnlace = 'plano', longitud = '20.0' , inclinacion = '', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'False', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )

G.add_edge('33','25',weight=25.0 , label='', tipoEnlace = 'escalera', longitud = '25.0' , inclinacion = '-', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'False', pasilloVentildo = 'True', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )
G.add_edge('33','32',weight=20.0 , label='', tipoEnlace = 'plano', longitud = '20.0' , inclinacion = '', barandilla = 'False', pasilloBuenEstado = 'True',  pasilloAmplio = 'True', pasilloVentildo = 'False', pasilloSeco = 'True', pasilloIluminado = 'True' , ocupacion = '0.0' )







#Color de los grafos
color_map = []
for node in G:
    if str(node)[0] == "0":
         #print("aqui 0")
         color_map.append('cyan')
    elif str(node) == 'P1':
        color_map.append('green')
    elif str(node)[0] == "1":
         #print("aqui 1")
         color_map.append('sandybrown')
    elif str(node)[0] == "2":
         #print("aqui 2")
         color_map.append('yellow')
    else :
         #print("aqui3")
         color_map.append('pink')
         
         

sectores = Funciones.leerSectoresCSV(__location__ + "//Ficheros//Sectores.csv", G)


plotGeneral = Funciones.DibujarGrafoGeneral(G, color_map, True, sectores , 'weight')



#Se piden al espectador los datos para crearle un perfil
print("")
print("PERFIL DEL ESPECTADOR")
print("")
while True:
    try:
        sector = input("Sector [Formato S12]: ").upper()
        if sector in sectores:
            sectorEspectador = sectores[sector]
            break
        raise ValueError()
    except ValueError:
        print("El sector: " + sector + " no se encuentra en la grada.")
        



while True:
    try:
        fila = int(input("Fila: "))
        if 1 <= fila:
            break
        raise ValueError()
    except ValueError:
        print("Fila debe ser mayor o igual que 1")
        

while True:
    try:
        columna = int(input("Columna: "))
        if 1 <= columna:
            break
        raise ValueError()
    except ValueError:
        print("Columna debe ser mayor o igual que 1")


while True:
    puertaEntrada = input("Puerta de entrada (Por defecto P1 [ENTER])").upper()
    if not puertaEntrada:
        puertaEntrada = 'P1'
        break
    else: 
        if puertaEntrada != 'P1':
                print("Actualmente solo existe la puerta de entrada P1")


while True: 
    try:
        tieneProblemasDeMovilidadRespuesta = input("Tiene problemas de movilidad s/n : ")
        if tieneProblemasDeMovilidadRespuesta.lower() == 's':
            tieneProblemasDeMovilidad = True
            break
        elif tieneProblemasDeMovilidadRespuesta.lower() == 'n':
            tieneProblemasDeMovilidad = False
            break
        raise ValueError()
    except ValueError:
        print("Selecciones si(s) o no (n).")

        
        



espectador = Clases.Espectador(uuid.uuid4(), Clases.Asiento(sectorEspectador, fila, columna), puertaEntrada, tieneProblemasDeMovilidad)

origen = espectador.puertaEntrada
destino = espectador.nodoPrefinal


asiento = Clases.Asiento(sectorEspectador, fila, columna)

# Se dibuja el asiento en la figura
Funciones.dibujarAsientoGrafoGeneral(G, sectores, asiento, plotGeneral)      


#Se dibujan los datos del espectador
Funciones.dibujarDatosEspectadorGeneral(G, espectador, plotGeneral)



print("")
print("Se ha actualizado el grafo para mostrar su asiento.")
print("")




while True:
    
    #Pedimos que quire aplicar
    print ("")
    print ("¿Que algoritmo desea aplicar?")
    print ("    (1)    Ruta más corta.")
    print ("    (2)    Ruta más rapida.")
    print ("    (3)    Ruta según atributos.")
    print ("    (4)    Ruta con control de aglomeraciones.")
    print (" _________________________________")
    print ("    (E / END)    Salir.")
    print 
    seleccionado = input()
    if str(seleccionado) == '1':
        rutaMasCorta = True;
    elif str(seleccionado) == '2':
        rutaMasRapida = True;
    elif str(seleccionado) == '3':
        rutaSegunAtributos = True;
    elif str(seleccionado) == '4':
        simularRutaConControlDeOcupaciones = True;
    elif str(seleccionado).lower() == 'e' or str(seleccionado).lower() == 'end' : #Lower para ignorar que sea mayusculas o minusculas
        sys.exit()
    else:
        print("Error al seleccionar algoritmo.")
        

    
    if rutaMasCorta:    

        
        #Checkeo de que esta en el grafo
        if destino not in G.nodes():
            print("El nodo no esta en el grafo")
        else:
            
            #Se hace una copia del grafo G orginal para poder modificarlo
            G_MasCorta = G.copy()

            
            

            #Dijkstra_BIDIRECCIONAL
            try:
                djk_Ruta_MasCorta = nx.bidirectional_dijkstra (G_MasCorta, source=origen, target=destino, weight='weight')
                
            except nx.NetworkXNoPath:
                
                print("No existe ruta de: " + origen + " a " + destino)
                continue
            
           
            Funciones.DibujarGrafoMasCorta(G_MasCorta, False, origen, destino, djk_Ruta_MasCorta[1], espectador, sectores, asiento)
    
            
            #Limpieza de variables
            G_MasCorta = None
            djk_Ruta_MasCorta = None
    
            rutaMasCorta = False
            
            
            
#______________________________________________________________________________________________________________________________________________________________________

    if rutaMasRapida: 
        
        """
         ****************  ALGORITMO DE RUTA MAS RAPIDA  ****************
         """
        
       
        #Checkeo de que esta en el grafo
        if destino not in G.nodes():
            print("El nodo no esta en el grafo")
        else:
            
            #Se hace una copia del grafo G orginal para poder modificarlo
            G_MasRapida = G.copy()
            
        
            
            """
            ----------------------------------------------------------------------------------------------------------------------------------
            
            Se recorren los enlaces y se sustituye la distancia de este por el tiempo de rocorrerlo, en funcion de la formula:
            
                    tiempo_enlace = distancia_enlace / factor_subida_o_bajada
            
            (*) Donde factor_subida_o_bajada = FACTOR_SUBIDA_ESCALERAS o FACTOR_BAJADA_ESCALERAS o FACTOR_PLANOS
            
            ----------------------------------------------------------------------------------------------------------------------------------
            """
           
            for u, v, d in G_MasRapida.edges(data=True):
                if ( d['tipoEnlace'] == "escalera") and ( d['inclinacion'] == "+"  ):
                    d['weight'] =  float( d['longitud'] ) / FACTOR_SUBIDA_ESCALERAS 
                elif ( d['tipoEnlace'] == "escalera" ) and ( d['inclinacion'] == "-"  ):
                    d['weight'] =  float( d['longitud'] ) / FACTOR_BAJADA_ESCALERAS 
                else:
                    d['weight'] =  float( d['longitud'] ) / FACTOR_PLANOS 
            
            
            
            
            #Dijkstra
            try:
                djk_Ruta_MasRapida = nx.bidirectional_dijkstra(G_MasRapida, source=origen, target=destino, weight='weight')
            except nx.NetworkXNoPath:
                print("No existe ruta de: " + origen + " a " + destino)
                continue
            

            
            Funciones.DibujarGrafoMasRapida(G_MasRapida, False, origen, destino, djk_Ruta_MasRapida[1], espectador, sectores, asiento)
    
            
            #Limpieza de variables
            G_MasRapida = None
            djk_Ruta_MasRapida = None
    
            rutaMasRapida = False     
            
           
            
#______________________________________________________________________________________________________________________________________________________________________

    if rutaSegunAtributos:
        
        
        
        #Checkeo de que esta en el grafo
        if destino not in G.nodes():
            print("El nodo no esta en el grafo")
            print(destino)
        else:
            
           
            respuestasAtributosPersonales = Funciones.respuestas
            
            
            #Mostrar interfaz de respuestas
            ventanaAtributosPersonales = Funciones.ventanaAtributosPersonales()
            
    
            
            if not (getattr(respuestasAtributosPersonales, 'cancelado')):
                
                
                #Se hace una copia del grafo G orginal para poder modificarlo
                G_Atributos = G.copy()
                
                
                
                #Se saca el valor personal para cada atributo
                #Se calcula el factor segun la folmula Factor_i = 1 - (valoracionDelUsuario / 6)
                
                k_escalerascConBarandillas = getattr(respuestasAtributosPersonales, 'f_escalerasConBarandillas')
                k_escalerasEnBuenEstado = getattr(respuestasAtributosPersonales, 'f_escalerasEnBuenEstado')
                k_pasillosAmplios = getattr(respuestasAtributosPersonales, 'f_pasillosAmplios')
                k_pasillosVentilados = getattr(respuestasAtributosPersonales, 'f_pasillosVentilados')
                k_pasillosSecos = getattr(respuestasAtributosPersonales, 'f_pasillosSecos')
                k_pasilloIluminados = getattr(respuestasAtributosPersonales, 'f_pasilloIluminados')
                
                
    
                #Se leen del Grafo todos los enlaces
                #Si cumple la condicion se aplica ese factor, si el factor sera 1 o no se multiplicara 
                
                """
                    Es decir si el usuario quiere un pasilloVentilado y un enlace no es ventilado
                    El peso de ese enlace sera el original
                    
                    Mientras que si otro pasillo es ventilado a ese si se le multiplicará por el facto, de esta forma se favorece a los que cumplen la condicion del usuario.
                """
    
                for u, v, d in G_Atributos.edges(data=True):
                    factores = []
                    
                    factores.append(float( d['longitud'] ))
                    
                    #Si tiene barandillas
                    if (d['barandilla'] == 'True'):
                        factores.append(k_escalerascConBarandillas)
                    
                    #Si esta en buen estado
                    if (d['pasilloBuenEstado'] == 'True'):
                        factores.append(k_escalerasEnBuenEstado)
                        
                    #Si esta en buen estado
                    if (d['pasilloAmplio'] == 'True'):
                        factores.append(k_pasillosAmplios)
                        
                    #Si esta en buen estado
                    if (d['pasilloVentildo'] == 'True'):
                        factores.append(k_pasillosVentilados)
                        
                    #Si esta en buen estado
                    if (d['pasilloSeco'] == 'True'):
                        factores.append(k_pasillosSecos)
                        
                    #Si esta en buen estado
                    if (d['pasilloIluminado'] == 'True'):
                        factores.append(k_pasilloIluminados)
    
                    peso_modificado = 0.0
                    peso_modificado = numpy.prod(factores)
                    d['weight'] =  peso_modificado
    
    
    
                #Dijkstra
                try:
                    djk_Ruta_Atributos = nx.bidirectional_dijkstra(G_Atributos, source=origen, target=destino, weight='weight')

                except nx.NetworkXNoPath:
                    print("No existe ruta de: " + origen + " a " + destino)
                    continue
                

    
    
    
    
                Funciones.DibujarGrafoAtributos(G_Atributos, False, origen, destino,djk_Ruta_Atributos[1],espectador ,sectores, asiento)
    
                           
    
    
    
            else:
                print("Cancelada la ruta según atributos")
                
            
        #Limpieza de variables
        
        respuestasAtributosPersonales = None
        ventanaAtributosPersonales = None
        G_Atributos = None
         
        factores = None
        color_nodos_solucion  = None
        
        djk_Ruta_Atributos = None
        
        rutaSegunAtributos = False

    #______________________________________________________________________________________________________________________________________________________________________

    if simularRutaConControlDeOcupaciones: 
        
        """
         ****************  SIMULADOR DE RUTA CONTROL DE OCUPACIONES  ****************
         """
        
       
        #Checkeo de que esta en el grafo
        if destino not in G.nodes():
            print("El nodo no esta en el grafo")
        else:
            
            #Se hace una copia del grafo G orginal para poder modificarlo
            global G_ControlDeAglomeraciones 
            G_ControlDeAglomeraciones = G.copy()
            
            recorridoOcupacion = []
        
            
            """
            ----------------------------------------------------------------------------------------------------------------------------------
            
            Se recorren los enlaces y se sustituye el peso (weight) por el valor de la ocupacion
            
            ----------------------------------------------------------------------------------------------------------------------------------
            """
           
            for u, v, d in G_ControlDeAglomeraciones.edges(data=True):
                d['weight'] =  float( d['ocupacion'] ) 
            
            
            nodoParado = origen
            recorridoOcupacion.append(nodoParado)
            
            
            #Bucle hasta que no se llegue al nodo prefinal
            #Lanzar hilo con simulacion
            hilo = Clases.ThreadingOcupacion(G_ControlDeAglomeraciones)
            print(Fore.YELLOW + "\nEspere un momento. Se esta rellenando la grada para la sumulación.")
            time.sleep(3)
            
                 
            #Hasta que no se llegue al destino se sigue preguntando cuando quiere el usuario parar
            #Es decir el ENTER del usuario corresponde a que esta en ese nodo parado esperando indicaciones
            while(True):
                
                #Pauso el hilo hasta que el usuario diga
                hilo.pause()

            
                print(Fore.CYAN  + "\n\nEsta parado en el nodo " + str(nodoParado) )
                input(Fore.GREEN +"Presiona ENTER para obtener la siguiente dirección...")
                
                # se hace el calculo de la ruta en ese momento
                djk_Ruta_Ocupacion = nx.bidirectional_dijkstra(G_ControlDeAglomeraciones, source=nodoParado, target=destino, weight='weight')
                # se obtione el nodo siguiente en función de la ocupación en ese momento
                nodoParado = djk_Ruta_Ocupacion[1][1]
                
                recorridoOcupacion.append(nodoParado)
                
                if(nodoParado != destino):
                    print(Fore.BLUE + "\n   >>> Debe caminar hasta el nodo: " + nodoParado)
                    
                    #Se reanuda el hilo que simula la ocupacion
                    hilo.resume()
                    #Se duerme para simular el caminar
                    print(Fore.YELLOW + "Espere un momento. Se esta simulando su trayecto.")
                    time.sleep(3)                
                else:
                    break
                    
            
                
                
            # Se para el hilo que rellena el grafo con la ocupacion
            hilo.terminate()
            

            
            print(Fore.GREEN + "\n\nHas llegado al nodo prefinal a traves de la ruta: " + str(recorridoOcupacion))
            
            
            print(Fore.WHITE + "")
            
            #Limpieza de variables
            # G_ControlDeAglomeraciones = None
            

    
            rutaMasRapida = False     
            
           
    



