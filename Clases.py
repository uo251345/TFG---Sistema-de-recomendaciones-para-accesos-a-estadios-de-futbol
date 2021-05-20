# -*- coding: utf-8 -*-
"""
@author: Pelayo Tiesta
"""


from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import numpy
import threading
import time
import random




class Sector():
    """Clase para crear un objeto sector en el estadio"""
    
    def __init__(self, nombre, nodoArribaIzquierda, nodoArribaDerecha, nodoAbajoIzquierda, nodoAbajoDerecha, filas, columnas, posicion):
        """

        Parameters
        ----------
        nombre : String
            Nombre del sector.
        nodoArribaIzquierda : String
            Nodo arriba izquierda.
        nodoArribaDerecha : String
            Nodo arriba derecha.
        nodoAbajoIzquierda : String
            Nodo abajo izquierda.
        nodoAbajoDerecha : String
            Nodo abajo derecha.
        filas : Integer
            Numero de filas del sector.
        columnas : Integer
            Numero de columnas del sector.
        posicion : Tupla
            Posicion.
            



        """
        self.nombre = nombre
        self.nodoArribaIzquierda = nodoArribaIzquierda
        self.nodoArribaDerecha = nodoArribaDerecha
        self.nodoAbajoIzquierda = nodoAbajoIzquierda
        self.nodoAbajoDerecha = nodoAbajoDerecha
        self.filas = filas
        self.columnas = columnas
        self.posicion = posicion


    def __repr__(self):
        return "El Sector %s tiene los nodos: %s %s %s %s, posicion: (%s, %s)" % (self.nombre, self.nodoArribaIzquierda, self.nodoArribaDerecha, self.nodoAbajoIzquierda, self.nodoAbajoDerecha, self.posicion[0], self.posicion[1])
        
    def existeEnlaceIzquierdo(self):
        if(self.nodoArribaIzquierda != 'None' and self.nodoAbajoIzquierda != 'None'): return True
        else: return False
    def existeEnlaceDerecho(self):
        if(self.nodoArribaDerecha != 'None 'and self.nodoAbajoDerecha != 'None'): return True
        else: return False
    def existeEnlaceArriba(self):
        if(self.nodoArribaIzquierda != 'None' and self.nodoArribaDerecha != 'None'): return True
        else: return False
    def existeEnlaceAbajo(self):
        if(self.nodoAbajoIzquierda != 'None' and self.nodoAbajoDerecha != 'None'): return True
        else: return False    

    

class Asiento():
    """Clase para crear un objeto asiento ubicado en el estadio"""
    
    
    #Las filas se enumeran de izquierda a derecha
    proyeccionHorizontal = None
    
    def __init__(self, sector, fila, columna):
        """

        Parameters
        ----------
        sector : Sector
            Sector donde esta el asiento.
        fila : Integer
            Numero de fila donde esta el asiento.
        columna : Integer
            Numero de columna donde esta el asiento.


        """
        
        self.sector = sector
        self.fila = fila
        self.columna = columna
        self.posicion_X = None
        self.posicion_Y = None
        self.enlaceProyeccion = self.enlaceProyeccion()


    def __repr__(self):
        return "El Asiento, esta en el sector %s fila: %s, columna: %s" % (self.sector.nombre, self.fila, self.columna)
    
    def setPosicion(self, posicion_X, posicion_Y):
        self.posicion_X = posicion_X
        self.posicion_Y = posicion_Y
        
    def enlaceProyeccion(self):
        """
        Función para obtener el enlace de la proyección del asiento.

        Raises
        ------
        Exception
            Produce Excepcion si no existe pasillo derecho ni izquierdo.

        Returns
        -------
        Enlace - Tupla

        """
        proyeccionHorizontal = None
         #Primero se mira si tiene enlaces derecha o izquierda        
        
        if (self.sector.existeEnlaceIzquierdo() == True or self.sector.existeEnlaceDerecho() == True):
        
            #Se mira cual es el lado mas próximo (izquierda o derecha)
            #Si es menor que la mitad de las columnas lado izquierdo (SI EXISTE)
            if (self.columna < (self.sector.columnas/2)) and self.sector.existeEnlaceIzquierdo():
                proyeccionHorizontal = 'IZQ'
                
            #Si no existe el izquierdo sera el derecho
            if (self.columna < (self.sector.columnas/2)) and self.sector.existeEnlaceIzquierdo() == False:
                proyeccionHorizontal = 'DER'
                
            
            #Sino lado derecho (Si existe)
            if (self.columna >= (self.sector.columnas/2)) and self.sector.existeEnlaceDerecho():
                proyeccionHorizontal = 'DER'
                
            
            #Si no existe al izquierda
            if (self.columna >= (self.sector.columnas/2)) and self.sector.existeEnlaceDerecho() == False:
                proyeccionHorizontal = 'IZQ'
                
                    
                    
        else:
            raise Exception("ERROR, No tiene enlace derecho ni izquierdo.")
            return
        
        if(proyeccionHorizontal == 'IZQ'): return (self.sector.nodoArribaIzquierda, self.sector.nodoAbajoIzquierda)
        else: return (self.sector.nodoArribaDerecha, self.sector.nodoAbajoDerecha)
        
        
    
    def nodoPrePreFinal(self):
        """
        Función para rellenar el nodoPrePrefinal
        Se calcula primero si se ira al lado derecho o izquierdo en funcion de la ubicacion horizontal del asiento.
        Posteriormente se calcula si el nodoPrePrefinal sera el nodo superior o inferior

        Raises
        ------
        Exception
            Se produce si no tiene enlace derecho o izquierdo (Asiento no accesible).

        Returns
        -------
        String - Nodo PrePrefinal

        """
        divisorVertical = 0.5
        
       
       
        proyeccionHorizontal = None
        proyeccionVertical = None
        
        #NOTA: Las filas se enumeran de izquierda a derecha ***********************
        
        #Primero se mira si tiene enlaces derecha o izquierda        
        if (self.sector.existeEnlaceIzquierdo() == True or self.sector.existeEnlaceDerecho() == True):
        
            #Se mira cual es el lado mas próximo (izquierda o derecha)
            #Si es menor que la mitad de las columnas lado izquierdo (SI EXISTE)
            if (self.columna < (self.sector.columnas/2)) and self.sector.existeEnlaceIzquierdo():
                proyeccionHorizontal = 'IZQ'
                
            #Si no existe el izquierdo sera el derecho
            if (self.columna < (self.sector.columnas/2)) and self.sector.existeEnlaceIzquierdo() == False:
                proyeccionHorizontal = 'DER'
                
            
            #Sino lado derecho (Si existe)
            if (self.columna >= (self.sector.columnas/2)) and self.sector.existeEnlaceDerecho():
                proyeccionHorizontal = 'DER'
                
            
            #Si no existe al izquierda
            if (self.columna >= (self.sector.columnas/2)) and self.sector.existeEnlaceDerecho() == False:
                proyeccionHorizontal = 'IZQ'
                
                   
        else:
            raise Exception("ERROR, No tiene enlace derecho ni izquierdo.")
            return
        
        
        #Para la proyeccion vertical no hace falta mirar si el nodo existe, puesto que si ya se proyecto tiene que existir
        
        #Se mira cual es el lado mas próximo (arriba o abajo)
        #Si es menor que la mitad de las columnas lado abajo (SI EXISTE)
        filaLimiteFloatNumpy = numpy.around(self.sector.filas*divisorVertical, decimals=0 )
        filaLimiteIntNumpy = filaLimiteFloatNumpy.astype(int)
        filaLimiteVertical = filaLimiteIntNumpy.item()
        
        if (self.fila <  filaLimiteVertical ):
            if(self.sector.existeEnlaceAbajo()):
                proyeccionVertical = 'ABA'
            else:    
                proyeccionVertical = 'ARR'
            
        elif (self.fila >= filaLimiteVertical ):    
            if(self.sector.existeEnlaceArriba()):
                proyeccionVertical = 'ARR'
            else:
                proyeccionVertical = 'ABA'
           
        else:
            raise Exception("ERROR, No tiene enlace arriba ni abajo.")
            return
                    
        
        
        #Para evitar un problema con el sector S12 se ha modificado la seleccion del nodo prefinal
        # si es un asiento del S12 se recomendara siempre un nodo prefinal de la parte superior izquierda o derecha
        if self.sector.nombre == 'S12': #CASO ESPECIAL
            if(proyeccionHorizontal == 'IZQ'): return self.sector.nodoArribaIzquierda
            else: return self.sector.nodoArribaDerecha
        else:
            if(proyeccionHorizontal == 'IZQ'):
                if(proyeccionVertical == 'ARR'): return self.sector.nodoArribaIzquierda
                else: return self.sector.nodoAbajoIzquierda
            else:
                if(proyeccionVertical == 'ARR'): return self.sector.nodoArribaDerecha
                else: return self.sector.nodoAbajoDerecha
            
        
        
        
        
class Espectador:
    """Clase para crear un objeto espectador al que se recomendara una ruta"""
    
    def __init__(self, ID, asiento, puertaEntrada):
        """

        Parameters
        ----------
        ID : String
            Identificador de espectador.
        asiento : Asiento
            Asiento al que quiere llegar.
        puertaEntrada : String
            Puerta por la que accede al estadio

        """
        
        self.ID = ID
        self.asiento = asiento
        self.puertaEntrada = puertaEntrada
        self.nodoPrePrefinal = self.asiento.nodoPrePreFinal()
        self.nodoPrefinal = None
        
    def __repr__(self):
        return "Espectador: %s --> %s, Entra por la puerta: %s y llegará al nodo: %s" % (self.ID, self.asiento, self.puertaEntrada, self.nodoPrefinal)
        
        
    def setNodoPreFinal(self, nodoPrefinal):
        self.nodoPrefinal = nodoPrefinal
        

        
        


class ThreadingOcupacion(object):
    """ 
    Clase para crear un hilo que simule la entrada de personas en la grada
    """

    def __init__(self, Grafo):
        """

        Parameters
        ----------
        Grafo : Grafo
            Grafo del estadio.
        

        """
        
        self.Grafo = Grafo
        self._running = True
        self._paused = False

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            
        thread.start()                                  

    def run(self):
        """ Metodo para corren en segundo plano y modificar el peso del grafo con la ocupacion """
        """ Si dado = 1 añado de 0 - 10 personsas si sale 0 resto de 0 - 10 (siempre que no sea menor que cero) """
        while self._running:
            if not self._paused:
                for u, v, d in self.Grafo.edges(data=True):
                    sumarOrestar = random.randint(0, 1)
                    ocupacionOriginal = int(d['weight'])
                    if sumarOrestar == 0: #Resto 
                        if(ocupacionOriginal != 0):
                            d['weight'] = int ( ocupacionOriginal - random.randint(0, 10) )
                            if( d['weight']  <= 0):
                                d['weight'] = 1
                        else:
                            d['weight'] = 1
                    else:
                        d['weight'] = int( ocupacionOriginal + random.randint(0, 10) )
                #Porque un enlace A --> B no puede tener distintas personas que el mismo enlace en el otro sentido (B --> A)
                for u, v, d in self.Grafo.edges(data=True):
                    if(self.Grafo.has_edge(u, v) and self.Grafo.has_edge(v,u)):
                        if (self.Grafo.get_edge_data(u,v)[0]['weight'] != self.Grafo.get_edge_data(v, u)[0]['weight'] ):
                            d['weight'] = self.Grafo.get_edge_data(v, u)[0]['weight']
                
                time.sleep(0.2)
        

    def terminate(self):
        """ Función para terminar el hilo  """
        self._running = False
        return self.Grafo
        
    def pause(self):
        self._paused = True
        return self.Grafo
        
    def resume(self):
        self._paused = False
       
        

        
        
        
    

        
    