# -*- coding: utf-8 -*-
"""
@author: Pelayo Tiesta
"""


from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import numpy



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
            
        Returns
        -------
        None.

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

        Returns
        -------
        None.

        """
        
        self.sector = sector
        self.fila = fila
        self.columna = columna


    def __repr__(self):
        return "El Asiento, esta en el sector %s fila: %s, columna: %s" % (self.sector.nombre, self.fila, self.columna)
        
    def nodoFinal(self, tieneProblemasDeMovilidad):
        divisorVertical = 2
        if(tieneProblemasDeMovilidad == True): divisorVertical = 0.75
        
       
       
        proyeccionHorizontal = None
        proyeccionVertical = None
        
        #NOTA: Las filas se enumeran de izquierda a derecha --------------------
        
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
        #Si tiene problemas de movilidad se subira hasta 3/4
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
                    
        
     
        
        if(proyeccionHorizontal == 'IZQ'):
            if(proyeccionVertical == 'ARR'): return self.sector.nodoArribaIzquierda
            else: return self.sector.nodoAbajoIzquierda
        else:
            if(proyeccionVertical == 'ARR'): return self.sector.nodoArribaDerecha
            else: return self.sector.nodoAbajoDerecha
        
        
        
        
        
class Espectador:
    """Clase para crear un objeto espectador al que se recomendara una ruta"""
    
    def __init__(self, ID, asiento, puertaEntrada, tieneProblemasDeMovilidad):
        """

        Parameters
        ----------
        ID : String
            Identificador de espectador.
        asiento : Asiento
            Asiento al que quiere llegar.
        puertaEntrada : String
            Puerta por la que accede al estadio
        tieneProblemasDeMovilidad: Boolean
            True si tiene problemas de movilidad, False en otro caso

        Returns
        -------
        None.

        """
        
        self.ID = ID
        self.asiento = asiento
        self.puertaEntrada = puertaEntrada
        self.tieneProblemasDeMovilidad = tieneProblemasDeMovilidad
        self.nodoPrefinal = self.asiento.nodoFinal(self.tieneProblemasDeMovilidad)
        
        
    def __repr__(self):
        return "Espectador: %s --> %s, Entra por la puerta: %s y llegará al nodo: %s" % (self.ID, self.asiento, self.puertaEntrada, self.nodoPrefinal)
        
        
        
class MenuSector(OptionMenu):
    def __init__(self, master, status, *options):
        self.var = StringVar(master)
        self.var.set(status)
        OptionMenu.__init__(self, master, self.var, *options)
        self.config(
            font=('calibri', (10)), bg='white', width=15, fg='dark red')
        self['menu'].config(font=('calibri', (10)), bg='white', fg='black')

    def callback():
        val = '{}'.format(self.var.get())
        return val
        # subprocess.call([val])
        
        
        
        
        
        
        
    