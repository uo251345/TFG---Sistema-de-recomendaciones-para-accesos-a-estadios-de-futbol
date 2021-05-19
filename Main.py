try:
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import ion

    

except:
    raise
 
import networkx as nx
import numpy
import threading

import uuid
import time
import sys
import os

import Funciones 
import Clases

import colorama
from colorama import Fore, Style, Back, init


#Para ignorar algunos warning de libreia deprecated
import warnings
warnings.filterwarnings("ignore")


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


#Se lee el grafo del fichero JSON
G = Funciones.importarGrafoJSON(__location__ + "\\Ficheros\\nodosExportados.json",)

#Se leen los sectores del fichero Sectores    
sectores = Funciones.leerSectoresCSV(__location__ + "\\Ficheros\\Sectores.csv", G)

#Se muestra el grafo G con los sectores y el peso
plot_General = Funciones.DibujarGrafoGeneral(G, True, sectores , 'weight')


"""
Se crea un perfil del espectador para obtener la puerta de acceso y la ubicacion de su asiento
"""

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


#Se crea un asiento con el sector donde esta, la fila y columna dentro de este
asiento = Clases.Asiento(sectorEspectador, fila, columna)

#Se crea el espectador con un ID, un asiento y una puerta de entrada
espectador = Clases.Espectador(uuid.uuid4(), asiento, puertaEntrada)

#El origen de la ruta sera la puerta de entrada
origen = espectador.puertaEntrada

#Se saca un nodoPrePrefinal que servira para sacar el nodo Prefinal ubicado en el pasillo vertical del sector
destinoPrePrefinal = espectador.nodoPrePrefinal

#Se saca el enlace donde estarará el nodoPrefinal
enlacePreFinal = asiento.enlaceProyeccion

# Se obtien la posicion del asiento, asi como la del nodo prefinal y de la union de ambos
posiconNodoPrefinal, posicionUnion, posicionAsiento = Funciones.obtenerPosicionAsiento(G, sectores, asiento, destinoPrePrefinal, plot_General)  

#Se agrega el nodo prefinal en el enlace previamente calculado,
# ademas de añadir los enlaces de este nodo con su nodo superior e inferior
nombreNodoPrefinal = Funciones.addnodoPrefinal(G, posicionUnion, sectorEspectador, enlacePreFinal, fila )

#Se asigna el nodo prefinal al espectador
espectador.setNodoPreFinal(nombreNodoPrefinal)

#El destino de las rutas sera este nodo prefinal
destino = None
destino = espectador.nodoPrefinal


#Se sacan las posiciones del asiento y del nodo NP
NodoPrefinal_pos = nx.get_node_attributes(G, 'pos')[destino]
Asiento_pos = posicionAsiento


#Se actualiza el grafo, ya que ahora se agrego un nodo nuevo
Funciones.DibujarGrafoGeneral(G, True, sectores , 'weight')

#Se dibuja una linea para simular el camino desde las escaleras hasta el  asiento
Funciones.dibujarRectaNodoPrefinal_Asiento(NodoPrefinal_pos, Asiento_pos, plot_General)

#Se dibujan los datos del espectador
Funciones.dibujarDatosEspectadorGeneral(G, espectador, plot_General)

#Se dibuja el asiento
Funciones.dibujarAsientoGrafoGeneral(posicionAsiento[0], posicionAsiento[1], plot_General)  



print("")
print("Se ha actualizado el grafo para representar su asiento.")
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
        

    #Si ruta más corta    
    if rutaMasCorta:  
        
        """
         ****************  ALGORITMO DE RUTA MAS CORTA  ****************
         """
        
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
            
           
            # Se dibuja el grafo con las soluciones
            plot_MasCorta = Funciones.DibujarGrafoMasCorta(G_MasCorta, False, origen, destino, djk_Ruta_MasCorta[1], espectador, sectores, asiento, NodoPrefinal_pos, Asiento_pos)
    

            
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
            

            # Se dibuja el grafo con las soluciones
            plot_MasRapida = Funciones.DibujarGrafoMasRapida(G_MasRapida, False, origen, destino, djk_Ruta_MasRapida[1], espectador, sectores, asiento, NodoPrefinal_pos, Asiento_pos)
    
           
            #Limpieza de variables
            G_MasRapida = None
            djk_Ruta_MasRapida = None
    
            rutaMasRapida = False     
            
           
            
#______________________________________________________________________________________________________________________________________________________________________

    if rutaSegunAtributos:
        
        """
         ****************  ALGORITMO DE RUTA SEGÚN ATRIBUTOS PERSONALES  ****************
         """
        
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
                

                # Se dibuja el grafo con las soluciones
                plot_Atributos = Funciones.DibujarGrafoAtributos(G_Atributos, False, origen, destino,djk_Ruta_Atributos[1],espectador ,sectores, asiento, NodoPrefinal_pos, Asiento_pos)


                           
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
            G_ControlDeAglomeraciones  = None
            G_ControlDeAglomeraciones = G.copy()
            
            #Para almacenar los nodos recorridos
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
            #Se lanza un hilo con la simulacion de la ocupacion de los pasillo
            hilo = Clases.ThreadingOcupacion(G_ControlDeAglomeraciones)
            print(Fore.YELLOW + "\n\n\nEspere un momento. Se esta rellenando la grada para la simulación.")
            time.sleep(5)
            
            init(autoreset=True)
            print("Listo. Su nodo prefinal es el nodo: " + destino )
                 
            #Hasta que no se llegue al destino se sigue preguntando cuando quiere el usuario parar
            #Es decir el ENTER del usuario corresponde a que esta en ese nodo parado esperando indicaciones
            while(nodoParado != destino):
                
                #Pauso el hilo hasta que el usuario diga
                G_ControlDeAglomeracionesParado = hilo.terminate()
        
                #Se dibuja el grafo en ese momento
                plot_Ocupacion = Funciones.DibujarGrafoOcupacion(G_ControlDeAglomeracionesParado, False, origen, destino, espectador ,sectores, asiento, nodoParado)

            
                print(Fore.CYAN  + "\n\nEsta parado en el nodo " + str(nodoParado) )
                init(autoreset=True)
            
                # se hace el calculo de la ruta en ese momento
                djk_Ruta_Ocupacion = nx.bidirectional_dijkstra(G_ControlDeAglomeracionesParado, source=nodoParado, target=destino, weight='weight')
                
                
                #Se tiene que borrar un enlace (en ambos sentidos) una vez realizado [sino podriamos tener ciclos infinitos]
                G_ControlDeAglomeracionesParado.remove_edge(djk_Ruta_Ocupacion[1][0], djk_Ruta_Ocupacion[1][1])
                
                if(G_ControlDeAglomeracionesParado.has_edge(djk_Ruta_Ocupacion[1][1], djk_Ruta_Ocupacion[1][0])):
                    G_ControlDeAglomeracionesParado.remove_edge(djk_Ruta_Ocupacion[1][1], djk_Ruta_Ocupacion[1][0])
                
                
                # se obtione el nodo siguiente en función de la ocupación en ese momento
                nodoParado = djk_Ruta_Ocupacion[1][1]
               
                recorridoOcupacion.append(nodoParado)
                
                print(Fore.BLUE + "\n>>>>>Debe caminar hasta el nodo: " + nodoParado )
                init(autoreset=True)
                
                input("Presione ENTER para simular la acción de caminar...")
                
                #Se reanuda el hilo que simula la ocupacion
                hilo = Clases.ThreadingOcupacion(G_ControlDeAglomeracionesParado)

                
                #Se duerme para simular el caminar
                print(Fore.YELLOW + "Espere un momento. Se esta simulando su trayecto.")
                init(autoreset=True)
                time.sleep(5)  
                
                
            
                
                
            # Se para el hilo que rellena el grafo con la ocupacion
            G_ControlDeAglomeracionesParado = hilo.terminate()
        
        
            # Se dibuja el grafo con las soluciones
            plot_Ocupacion = Funciones.DibujarGrafoOcupacion(G_ControlDeAglomeracionesParado, False, origen, destino, espectador ,sectores, asiento, nodoParado, True, NodoPrefinal_pos, Asiento_pos)
            

            
            print(Fore.GREEN + "\n\nHas llegado al nodo prefinal a traves de la ruta: " + str(recorridoOcupacion))
            init(autoreset=True)
            
            
            
            #Limpieza de variables
            G_ControlDeAglomeracionesParado = None
            

    
            simularRutaConControlDeOcupaciones = False     
            
           
    



