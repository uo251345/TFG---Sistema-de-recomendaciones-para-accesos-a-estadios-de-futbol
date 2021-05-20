# -*- coding: utf-8 -*-
"""
@author: Pelayo Tiesta
"""



try:
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import ion

    
    

except:
    raise
 
import networkx as nx
from networkx.readwrite import json_graph


from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

import json

import uuid

import threading
import time


import numpy


import Clases

import copy

import sys

import csv


from sys import exit


#Divisor atributos
divisior_atributos = 6
    

#Clases auxiliares para las funciones (Deben estar en este fichero por problemas de accesibilidad de python)
class MenuAtributosPersonales(OptionMenu):
    """
    Clase para crear un menú de atributos a puntuar
    """
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
    
    

class Respuestas:
    """
    Clase para las respuestas del menú de atributos
    """
    
    def __init__(self):
        self.cancelado = True
        self.escalerasConBarandillas = 0
        self.escalerasEnBuenEstado = 0
        self.pasillosAmplios = 0
        self.pasillosVentilados = 0
        self.pasillosSecos = 0
        self.pasilloIluminados = 0
        
        self.f_escalerasConBarandillas = 1
        self.f_escalerasEnBuenEstado = 1
        self.f_pasillosAmplios = 1
        self.f_pasillosVentilados = 1
        self.f_pasillosSecos = 1
        self.f_pasilloIluminados = 1
        
        
    
    def rellenar(self, escalerasConBarandillas, escalerasEnBuenEstado, pasillosAmplios, pasillosVentilados, pasillosSecos, pasilloIluminados):
        """
        Función para rellenar los campos de las respuestas

        Parameters
        ----------
        escalerasConBarandillas : Integer
            Valor respondido para este campo.
        escalerasEnBuenEstado : Integer
            Valor respondido para este campo.
        pasillosAmplios : Integer
            Valor respondido para este campo.
        pasillosVentilados : Integer
            Valor respondido para este campo.
        pasillosSecos : Integer
            Valor respondido para este campo.
        pasilloIluminados : Integer
            Valor respondido para este campo.

        Returns
        -------
        None.

        """
        self.cancelado = False
        self.escalerasConBarandillas = escalerasConBarandillas
        self.escalerasEnBuenEstado = escalerasEnBuenEstado
        self.pasillosAmplios = pasillosAmplios
        self.pasillosVentilados = pasillosVentilados
        self.pasillosSecos = pasillosSecos
        self.pasilloIluminados = pasilloIluminados
        
        self.f_escalerasConBarandillas = 1 - (int(self.escalerasConBarandillas)/divisior_atributos)
        self.f_escalerasEnBuenEstado = 1 - (int(self.escalerasEnBuenEstado)/divisior_atributos)
        self.f_pasillosAmplios = 1 - (int(self.pasillosAmplios)/divisior_atributos)
        self.f_pasillosVentilados = 1 - (int(self.pasillosVentilados)/divisior_atributos)
        self.f_pasillosSecos = 1 - (int(self.pasillosSecos)/divisior_atributos)
        self.f_pasilloIluminados = 1 - (int(self.pasilloIluminados)/divisior_atributos)
        
        print("Escaleras con barandillas: " + str(escalerasConBarandillas))
        print("Escaleras en buen estado: " + str(escalerasEnBuenEstado))
        print("Pasillos amplios: " + str(pasillosAmplios))
        print("Pasillos Ventilados: " + str(pasillosVentilados))
        print("Pasillos secos: " + str(pasillosSecos))
        print("Pasillos iluminados: " + str(pasilloIluminados))
    
    def __repr__(self):
        if(self.cancelado): 
            return "Sin rellenar." 
        
        else:
            return "escalerasConBarandillas:%s escalerasEnBuenEstado:%s pasillosAmplios:%s pasillosVentilados:%s pasillosSecos:%s pasilloIluminados:%s" % (self.escalerasConBarandillas, self.escalerasEnBuenEstado, self.pasillosAmplios, self.pasillosVentilados, self.pasillosSecos, self.pasilloIluminados)
        
    


class ventanaAtributosPersonales():
    """
    Clase para dibujar una ventana con los atributos a puntuar
    """
    
    def __init__(self):

        #Mostramos el formulario de consulta
        self.root = Tk()
        
        #Sacamos las dimensiones de la pantilla
        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()

        #Se saca la mitar horizontal y verticar de la pantalla para centrarla
        posicionDerecha = int(self.root.winfo_screenwidth()/2 - windowWidth/2)
        posicionAbajo = int(self.root.winfo_screenheight()/2 - windowHeight/2)
         
        #Se centra la pantalla
        self.root.geometry("+{}+{}".format(posicionDerecha, posicionAbajo))

        #Se da el tamaño a la ventana y el título
        self.root.geometry("600x400")
        self.root.title("Recomendación personal según atributos de los pasillos.")
        #self.root.resizable(False, False)
        Label(self.root, text="Puntue del 0 al 5 los atributos de la ruta recomendada.", font="ar 15 bold").place(x=5, y=25)
        Label(self.root, text="[0 - Sin importancia, 5 - Muy importante]", font="ar 12 normal").place(x=10, y=50)
        
        #Se muestarn las preguntas de los atributos en labels 
        escalerasConBarandillas_Label = Label(self.root, text="Escaleras con barandillas: ", font="ar 12 normal", relief=RIDGE, width=25, anchor='e').place(x=40, y=101)
        escalerasEnBuenEstado_Label = Label(self.root, text="Escaleras en buen estado: ", font="ar 12 normal", relief=RIDGE, width=25, anchor='e').place(x=40, y=131)
        pasillosAmplios_Label = Label(self.root, text="Pasillos amplios: ", font="ar 12 normal", relief=RIDGE, width=25, anchor='e').place(x=40, y=161)
        pasillosVentilados_Label = Label(self.root, text="Pasillos ventilados: ", font="ar 12 normal", relief=RIDGE, width=25, anchor='e').place(x=40, y=191)
        pasillosSecos_Label = Label(self.root, text="Pasillos secos: ", font="ar 12 normal", relief=RIDGE, width=25, anchor='e').place(x=40, y=221)
        pasillosSecos_Label = Label(self.root, text="Pasillos bien iluminados: ", font="ar 12 normal", relief=RIDGE, width=25, anchor='e').place(x=40, y=251)

        #Desplegables para seleccionar valores
        escalerasConBarandillas_combo = MenuAtributosPersonales(self.root, "0","0","1","2","3","4","5")
        escalerasConBarandillas_combo.place(x=270, y=101)
        escalerasEnBuenEstado_combo = MenuAtributosPersonales(self.root, "0","0","1","2","3","4","5")
        escalerasEnBuenEstado_combo.place(x=270, y=131)
        pasillosAmplios_combo = MenuAtributosPersonales(self.root, "0","0","1","2","3","4","5")
        pasillosAmplios_combo.place(x=270, y=161) 
        pasillosVentilados_combo = MenuAtributosPersonales(self.root, "0","0","1","2","3","4","5")
        pasillosVentilados_combo.place(x=270, y=191)   
        pasillosSecos_combo = MenuAtributosPersonales(self.root, "0","0","1","2","3","4","5")
        pasillosSecos_combo.place(x=270, y=221)
        pasillosiluminados_combo = MenuAtributosPersonales(self.root, "0","0","1","2","3","4","5")
        pasillosiluminados_combo.place(x=270, y=251)
        
        #Boton para confirmar
        botonConfirmar = Button(self.root, text="Confirmar", width = 20, bg="green" ,command=lambda:botonAtributosPersonalesClick(self,escalerasConBarandillas_combo.var.get(),escalerasEnBuenEstado_combo.var.get() ,pasillosAmplios_combo.var.get() ,pasillosVentilados_combo.var.get() ,pasillosSecos_combo.var.get(),pasillosiluminados_combo.var.get()))
        botonConfirmar.place(x=270, y=300)
        
        self.center(self.root)
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        self.root.mainloop()
   
        
        return
    
    def center(self, window):
        """
        Función para centrar la ventana
        """
        window.update_idletasks()
        width = window.winfo_width()
        frm_width = window.winfo_rootx() - window.winfo_x()
        win_width = width + 2 * frm_width
        height = window.winfo_height()
        titlebar_height = window.winfo_rooty() - window.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = window.winfo_screenwidth() // 2 - win_width // 2
        y = window.winfo_screenheight() // 2 - win_height // 2
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        window.deiconify()
    
    
    def quit(self):
        self.root.quit()
        self.root.destroy()
        
    def close_window(self):
        respusta_cerrar = messagebox.askokcancel(message="¿Desea terminar la ejecución de esta ventana?", title="Terminar ejecución")
        
        if respusta_cerrar:
            self.quit()
    
    

        

def DibujarGrafoGeneral(Grafo, mostrarPesos, sectores, peso='weight'):
    """
    Función para dibujar el grafo General

    Parameters
    ----------
    Grafo : networkx.classes.multidigraph.MultiDiGraph
        Grafo a dibujar.
    mostrarPesos : bool
        Boolean - True si se muestran los Pesos
    sectores : Lista
        Sectores del grafo
    peso : string, optional
        String con el la etiqueta peso. (Default: weight)


    """
    #Nueva ventana
    width0 = 9
    height0 = 9
    width_height_0 = (width0, height0)
    plt.figure(1,figsize=width_height_0)
    plt.clf()
    
    plt.figure(1).canvas.set_window_title('Grafo General - Pelayo Tiesta') 

    for u, v, d in Grafo.edges(data=True):
        d['weight'] = float( d[peso] ) 
                    
    
    #Para pintar los diferentes enlaces
    enlacesPasillos = []
    enlacesPasillosConBarandillas = []
    enlacesEscaleras = []
    enlacesEscalerasConBarandillas = []
    
    for u, v, d in Grafo.edges(data=True):
        if d['tipoEnlace'] == 'plano':
            if d['barandilla'] == 'True':
                enlacesPasillosConBarandillas.append((u, v))
            else: enlacesPasillos.append((u, v))
            
        if d['tipoEnlace'] == 'escalera':
            if d['barandilla'] == 'True':
                enlacesEscalerasConBarandillas.append((u, v))
            else: enlacesEscaleras.append((u, v))
            
            
    #Color de los grafos
    color_map = []
    for node in Grafo:
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
        elif str(node) == 'NP':
            color_map.append('lavender')
        else :
             #print("aqui3")
             color_map.append('pink')
    
    
    # Se sacan las posiciones de los nodos
    pos=nx.get_node_attributes(Grafo,'pos')
    
    # Se dibujan los nodos
    nx.draw_networkx_nodes(Grafo,pos,node_size=400, node_color=color_map)
    
    # Se dibujan los 4 tipos de enlaces
    # Pasillos sin barandilla (color Verde)
    nx.draw_networkx_edges(Grafo,pos,edgelist=enlacesPasillos,    edge_color='springgreen', arrows = True)
    # Pasillos con barandilla (color verde Oscuro)
    nx.draw_networkx_edges(Grafo,pos,edgelist=enlacesPasillosConBarandillas,   edge_color='darkgreen', arrows = True)
    # Escaleras sin barandilla (color Verde)
    nx.draw_networkx_edges(Grafo,pos,edgelist=enlacesEscaleras,   edge_color='deepskyblue', arrows = True,)
    # Escaleras con barandilla (color verde Oscuro)
    nx.draw_networkx_edges(Grafo,pos,edgelist=enlacesEscalerasConBarandillas,   edge_color='darkblue', arrows = True)
     
    # Se dibujan las etiquetas del grafo
    nx.draw_networkx_labels(Grafo,pos,font_size=12,font_family='sans-serif')

    # Se muestran los pesos si esta True la variable
    if mostrarPesos:
        # Dibujar los pesos
        edge_labels =dict([((u, v), "{:.2f}".format( float( d['weight'] )) ) 
                       for u, v, d in Grafo.edges(data=True)])
     
        nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=edge_labels, font_size=7)
        
    else:
        nx.draw_networkx_edge_labels(Grafo, pos)
        
        
    #Se muestran los sectores en textos
    for key in sectores:
        plt.text(getattr(sectores[key],'posicion')[0]-0.35, getattr(sectores[key],'posicion')[1]-0.2, key + "\nFilas: " + str(getattr(sectores[key],'filas')) + "\nColumnas: " + str(getattr(sectores[key],'columnas')) , style='italic', fontweight='bold',
                    bbox={'facecolor': 'yellow', 'alpha': 0.2, 'pad': 1})
        

    #Leyenda con los datos
    plt.text(0, -0.8, 'LEYENDA\n' + '\nPasillos planos sin barandilla: Verde Claro' + '\nPasillos planos con barandilla: Verde Oscuro' + '\nPasillos con escaleras sin barandilla: Azul Claro' + '\nPasillos con escaleras con barandilla: Azul Oscuro' + '\n\nAsiento: Asterisco Rojo ' , style='italic', fontweight='normal',bbox={'facecolor': 'orange', 'alpha': 0.2, 'pad': 2})
    
    plt.axis('off')
    plt.title("Grafo General")
    plt.ion()
    plt.show(block=False)
    plt.pause(1)


    return plt


def addnodoPrefinal(G, posicionUnion, sectorEspectador, enlacePreFinal, fila, nombreNodoPrefinal = 'NP' ):
    """
    Función para agregar al Grafo un nodo prefinal equivalente a la proyección del asiento en las escaleras.

    Parameters
    ----------
    G : networkx.classes.multidigraph.MultiDiGraph
        Grafo a actualizar.
    posicionUnion : Tupla
        Posicion de la proyeccion del asiento sobre el enlace de su derecha o izquierda.
    sectorEspectador : Sector
        Sector sobre el que se encuentra el asiento del espectador.
    enlacePreFinal : Tupla
        Enlace actual del grafo que se borrara para agregar el nuevo nodo Prefinal.
    fila : Integer
        Valor de la fila donde esta el asiento.
    nombreNodoPrefinal : String, optional
        Nombre del nodo prefinal resultante. Valor por defecto 'NP'.

    Returns
    -------
    nombreNodoPrefinal : String
        Nombre del nodo prefinal.

    """

    #Se redondea la posicion de la proyeccion con dos decimales
    posicionUnion_redondeada = [round(num, 2) for num in posicionUnion]

    #Se saca los datos de filas del sector y la longitud enlace,
    filas_Sector = float(getattr(sectorEspectador, 'filas'))
    longitud_Enlace = float(G.get_edge_data( enlacePreFinal[0], enlacePreFinal[1] )[0]['longitud'])
    #Se calcula la nueva longitud desde el nodo prefinal hasta el nodo superior e inferior
    longitudSuperior = ( filas_Sector - fila ) * ( longitud_Enlace / filas_Sector  )
    longitudInferior = ( fila ) * ( longitud_Enlace / filas_Sector )
    
    #Datos para el nuevo nodo como copia del que se borrara (actual)
    dataSuperior = G.get_edge_data( enlacePreFinal[0], enlacePreFinal[1] )[0]
    dataInferior = G.get_edge_data( enlacePreFinal[1], enlacePreFinal[0] )[0]
    
    #Se agrega el nodo nuevo
    G.add_node(nombreNodoPrefinal, pos=posicionUnion_redondeada)
    
    #Nuevo Nodo al superior
    G.add_edge(enlacePreFinal[0] , nombreNodoPrefinal , weight = longitudSuperior, label = '', tipoEnlace = dataSuperior['tipoEnlace'], longitud = longitudSuperior , inclinacion ='-', barandilla = dataSuperior['barandilla'], pasilloBuenEstado = dataSuperior['pasilloBuenEstado'],  pasilloAmplio = dataSuperior['pasilloAmplio'], pasilloVentildo = dataSuperior['pasilloVentildo'], pasilloSeco = dataSuperior['pasilloSeco'], pasilloIluminado = dataSuperior['pasilloIluminado'] , ocupacion = dataSuperior['ocupacion'] )
    G.add_edge(nombreNodoPrefinal, enlacePreFinal[0] , weight = longitudSuperior, label = '', tipoEnlace = dataSuperior['tipoEnlace'], longitud = longitudSuperior , inclinacion = '+', barandilla = dataSuperior['barandilla'], pasilloBuenEstado = dataSuperior['pasilloBuenEstado'],  pasilloAmplio = dataSuperior['pasilloAmplio'], pasilloVentildo = dataSuperior['pasilloVentildo'], pasilloSeco = dataSuperior['pasilloSeco'], pasilloIluminado = dataSuperior['pasilloIluminado'] , ocupacion = dataSuperior['ocupacion'] )
    
    #Nuevo Nodo al inferior
    G.add_edge(nombreNodoPrefinal, enlacePreFinal[1], weight = longitudInferior, label = '', tipoEnlace = dataInferior['tipoEnlace'], longitud = longitudInferior , inclinacion = '-', barandilla = dataInferior['barandilla'], pasilloBuenEstado = dataInferior['pasilloBuenEstado'],  pasilloAmplio = dataInferior['pasilloAmplio'], pasilloVentildo = dataInferior['pasilloVentildo'], pasilloSeco = dataInferior['pasilloSeco'], pasilloIluminado = dataInferior['pasilloIluminado'] , ocupacion = dataInferior['ocupacion'] )
    G.add_edge(enlacePreFinal[1], nombreNodoPrefinal, weight = longitudInferior, label = '', tipoEnlace = dataInferior['tipoEnlace'], longitud = longitudInferior , inclinacion = '+', barandilla = dataInferior['barandilla'], pasilloBuenEstado = dataInferior['pasilloBuenEstado'],  pasilloAmplio = dataInferior['pasilloAmplio'], pasilloVentildo = dataInferior['pasilloVentildo'], pasilloSeco = dataInferior['pasilloSeco'], pasilloIluminado = dataInferior['pasilloIluminado'] , ocupacion = dataInferior['ocupacion'] )
    
    #Se comprueba que existen los enlaces a borrar y se borras de Nodo A a Nodo B y viceversa    
    if(G.has_edge(enlacePreFinal[0], enlacePreFinal[1]) ):
       G.remove_edge(enlacePreFinal[0], enlacePreFinal[1])
    if(G.has_edge(enlacePreFinal[1], enlacePreFinal[0]) ):
       G.remove_edge(enlacePreFinal[1], enlacePreFinal[0])


    return nombreNodoPrefinal



def obtenerPosicionAsiento(Grafo, sectores, asiento, nodoPrefinal, plot):
    """
    Función para sacar la posicion X e Y del asiento dibujado. 
    Ademas se saca la posion del nodoPrefinal y de la union de ambos
    
    Parameters
    ----------
    Grafo : networkx.classes.multidigraph.MultiDiGraph
        Grafo.
    sectores : List
        Lista de Sectores.
    asiento : Asiento
        Asiento del espectador.
    nodoPrefinal : Tupla
        Nodo prefinal.
    plot : module
        plt donde se dibuja.

    Returns
    -------
    List( posicion_NodoPrefinal, posicion_Union, posicionX_asiento, posicionY_asiento )
    """
    
    
    #Se sacan los atributos necesarios para los calculos   
    sector_asiento = getattr(asiento, 'sector')
    filas_sector = getattr(sector_asiento, 'filas')
    columnas_sector = getattr(sector_asiento, 'columnas')
    nodo_ArribaIzquierda = getattr(sector_asiento, 'nodoArribaIzquierda')
    nodo_ArribaDerecha = getattr(sector_asiento, 'nodoArribaDerecha')
    nodo_AbajoIzquierda = getattr(sector_asiento, 'nodoAbajoIzquierda')
    nodo_AbajoDerecha = getattr(sector_asiento, 'nodoAbajoDerecha')
    fila_asiento = getattr(asiento, 'fila')
    columna_asiento = getattr(asiento, 'columna')
    
    
    longitud_enlace_arriba1 = None
    longitud_enlace_arriba2 = None
    longitud_enlace_derecha1 = None
    longitud_enlace_derecha2 = None


    #Se verifica que el asiento no esta fuera del sector
    if (fila_asiento > filas_sector): 
        print("\n\n\nError: La fila del asiento esta fuera de las filas del sector. El sector tiene solo: " + str(filas_sector) + " filas.")
        input("Presiona ENTER para terminar la ejecuccion...")
        sys.exit()
        
    if(columna_asiento > columnas_sector): 
        print("\n\n\nError: La columna del asiento esta fuera de las columnas del sector. El sector tiene solo: " + str(columnas_sector) + " columnas.")
        input("Presiona ENTER para terminar la ejecucción...")
        sys.exit()
    
    try:
        longitud_enlace_arriba1 = Grafo.nodes()[nodo_ArribaDerecha]['pos'][0] - Grafo.nodes()[nodo_ArribaIzquierda]['pos'][0]
    except:
        IgnorarError = ''
     
    try:
        longitud_enlace_arriba2 = Grafo.nodes()[nodo_AbajoDerecha]['pos'][0]- Grafo.nodes()[nodo_AbajoIzquierda]['pos'][0]
    except:
        IgnorarError = ''
        
    longitud_enlace_arriba = None
    if(longitud_enlace_arriba1 != None): longitud_enlace_arriba = longitud_enlace_arriba1    
    else: longitud_enlace_arriba = longitud_enlace_arriba2
    
    
    proyeccionHorizontal = ''
    
    try:
        longitud_enlace_derecha1 = Grafo.nodes()[nodo_ArribaDerecha]['pos'][1] - Grafo.nodes()[nodo_AbajoDerecha]['pos'][1]
    except:
        IgnorarError = ''
     
    try:
        longitud_enlace_derecha2 = Grafo.nodes()[nodo_ArribaIzquierda]['pos'][1]- Grafo.nodes()[nodo_AbajoIzquierda]['pos'][1]
    except:
        IgnorarError = ''
        
    longitud_enlace_derecha = None
    if(longitud_enlace_derecha1 != None): 
        longitud_enlace_derecha = longitud_enlace_derecha1   
    else: 
        longitud_enlace_derecha = longitud_enlace_derecha2
    
    #Se saca la equivalencia entre el tamaño del pasillo y el numero de filas de este
    unidadesVertical = longitud_enlace_derecha/filas_sector
    unidadesHorizontal = longitud_enlace_arriba/columnas_sector
    
    # Se saca la posicion del asiento 
    posicionX_asiento = Grafo.nodes()[nodo_ArribaIzquierda]['pos'][0] + (unidadesHorizontal * columna_asiento)
    posicionY_asiento = Grafo.nodes()[nodo_ArribaIzquierda]['pos'][1] - (unidadesVertical * (filas_sector - fila_asiento)) 
    
   
    
    # Se saca la posicion del asiento en el enlace izquierdo o derecho
    posicion_Union = ( Grafo.nodes()[nodoPrefinal]['pos'][0] , numpy.round(posicionY_asiento, 2) )
    posicion_NodoPrefinal = (Grafo.nodes()[nodoPrefinal]['pos'][0], Grafo.nodes()[nodoPrefinal]['pos'][1])
    
    #Se actualiza el asiento añadiendo su posicion
    asiento.setPosicion(numpy.round( posicionX_asiento, 2 ), numpy.round( posicionY_asiento, 2) )
    
    
    return ( posicion_NodoPrefinal, posicion_Union ,(numpy.round( posicionX_asiento, 2 ), numpy.round( posicionY_asiento,2 )) )


def dibujarAsientoGrafoGeneral(posicionX_asiento, posicionY_asiento, plt):
    #Se dibuja el asientocon un * rojo
    plt.ion()
    plt.draw()
    plt.pause(0.0001)
    plt.plot(posicionX_asiento, posicionY_asiento, marker="*", markersize=10, color="red")
    plt.pause(0.0001)

def dibujarRectaNodoPrefinal_Asiento(NodoPrefinal_pos, Asiento_pos, plot):
    """
    Funcion para dibujar una línea que emule el camino desde la escalera hasta el asiento.

    Parameters
    ----------
    NodoPrefinal_pos : Tupla
        Posiciones del nodo Prefinal.
    Asiento_pos : Tupla
        Posiciones del asiento.
    plot : module
        Plt donde se dubujara la linea.



    """
    
    #Recta nodo Prefinal hasta el asiento 
    valores_x_escaleras = [NodoPrefinal_pos[0] , Asiento_pos[0] ] 
    valores_y_escaleras = [NodoPrefinal_pos[1], Asiento_pos[1]]
    plot.plot(valores_x_escaleras , valores_y_escaleras, linestyle = ':', color = 'red')
    

    
    plot.ion()
    plot.draw()
    plot.pause(0.0001)
    plot.show()
    

def dibujarDatosEspectadorGeneral(Grafo, espectador, plot):
    """
    Función para dibujar los datos del espectador en el plot
    
    Parameters
    ----------
    Grafo : networkx.classes.multidigraph.MultiDiGraph
        Grafo General.
    espectador : Espectador
        Espectador.
    plot : mdoule
        Plt donde se dibuja.



    """
    ID = "\nID: " + str(getattr(espectador, 'ID'))
    PuertaEntrada = "\nPuerta de entrada: " + str(getattr(espectador, 'puertaEntrada'))
    NodoPrefinal = "\nNodo prefinal: " + str(getattr(espectador, 'nodoPrefinal'))
    
    
    plt.ion()
    plt.draw()
    plt.pause(0.0001)
    
    plot.text(3.5, -0.5, 'DATOS ESPECTADOR\n' + ID + PuertaEntrada + NodoPrefinal, style='italic', fontweight='normal',bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 2})
    plt.pause(0.0001)


def dibujarDatosEspectadorAtributos(Grafo, espectador, plot):
    """
    Función para dibujar los datos del espectador en el plot
    
    Parameters
    ----------
    Grafo : networkx.classes.multidigraph.MultiDiGraph
        Grafo General.
    espectador : Espectador
        Espectador.
    plot : mdoule
        Plt donde se dibuja.



    """
    ID = "\nID: " + str(getattr(espectador, 'ID'))
    PuertaEntrada = "\nPuerta de entrada: " + str(getattr(espectador, 'puertaEntrada'))
    NodoPrefinal = "\nNodo prefinal: " + str(getattr(espectador, 'nodoPrefinal'))

    
    plt.ion()
    plt.draw()
    plt.pause(0.0001)
    
    plot.text(3.5, -0.5, 'DATOS ESPECTADOR\n' + ID + PuertaEntrada + NodoPrefinal , style='italic', fontweight='normal',bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 2})
    plt.pause(0.0001)


def dibujarDatosEspectadorMasRapida(Grafo, espectador, plot):
    """
    Función para dibujar los datos del espectador en el plot
    
    Parameters
    ----------
    Grafo : networkx.classes.multidigraph.MultiDiGraph
        Grafo General.
    espectador : Espectador
        Espectador.
    plot : mdoule
        Plt donde se dibuja.



    """
    ID = "\nID: " + str(getattr(espectador, 'ID'))
    PuertaEntrada = "\nPuerta de entrada: " + str(getattr(espectador, 'puertaEntrada'))
    NodoPrefinal = "\nNodo prefinal: " + str(getattr(espectador, 'nodoPrefinal'))

    plt.ion()
    plt.draw()
    plt.pause(0.0001)
    
    plot.text(3.5, -0.5, 'DATOS ESPECTADOR\n' + ID + PuertaEntrada + NodoPrefinal , style='italic', fontweight='normal',bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 2})
    plt.pause(0.0001)


def dibujarDatosEspectadorMasCorta(Grafo, espectador, plot):
    """
    Función para dibujar los datos del espectador en el plot
    
    Parameters
    ----------
    Grafo : networkx.classes.multidigraph.MultiDiGraph
        Grafo General.
    espectador : Espectador
        Espectador.
    plot : mdoule
        Plt donde se dibuja.



    """
    ID = "\nID: " + str(getattr(espectador, 'ID'))
    PuertaEntrada = "\nPuerta de entrada: " + str(getattr(espectador, 'puertaEntrada'))
    NodoPrefinal = "\nNodo prefinal: " + str(getattr(espectador, 'nodoPrefinal'))

    
    plt.ion()
    plt.draw()
    plt.pause(0.0001)
    
    plot.text(3.5, -0.5, 'DATOS ESPECTADOR\n' + ID + PuertaEntrada + NodoPrefinal , style='italic', fontweight='normal',bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 2})
    plt.pause(0.0001)
    




def botonAtributosPersonalesClick(ventana_self,escalerasConBarandillas,escalerasEnBuenEstado,pasillosAmplios, pasillosVentilados,  pasillosSecos, pasilloIluminados):
    """
    Metodo auxiliar para capturar el click del boton Confirmar en el formulario de atributos
    
    y modificar el diccionario respuestas

    """
    
    
    respuestas.rellenar(escalerasConBarandillas, escalerasEnBuenEstado, pasillosAmplios, pasillosVentilados, pasillosSecos, pasilloIluminados)


    ventana_self.quit()


def DibujarGrafoOcupacion(Grafo, mostrarPesos, origen, destino,  espectador, sectores, asiento, nodoParado, dibujarEnlacePrefinalAsiento = False, NodoPrefinal_pos = None, Asiento_pos = None ,peso='weight'):
    """
    Funcion para dibujar el grafo de atributos
    
    Parameters
    ----------
    Grafo : networkx.classes.multidigraph.MultiDiGraph
        Grafo a dibujar.
    mostrarPesos : bool
        Boolean - True si se muestran los Pesos.
    origen : string
        String - Nodo inicial de la solucion.
    destino : string
        String - Nodo final de la solucion.
    espectador : Espectador
        Espectador que accede a un asiento.
    sectores : Lista
        Lista de Sector.
    asiento : Asiento
        Asiento al que se accede.
    nodoParado : String
        Nodo en el que esta parado el usuario.
    dibujarEnlacePrefinalAsiento : Boolean, optional
        Bool para dibujar el enlace del nodo prefinal al asiento. (Default: False)
    NodoPrefinal_pos : Tupla, optional
        Posicion del nodo Prefinal. (Default: None)
    Asiento_pos : Tupla, optional
        Posicion del asiento. (Default: None)
    peso : string, optional
        String con el la etiqueta peso. (Default: weight)
        
    Returns
    -------
    Plt donde se dibujo.
        
    """

    #Nueva ventana
    width1 = 9
    height1 = 9
    width_height_1 = (width1, height1)
    plt.figure(5,figsize=width_height_1)
    plt.figure(5).canvas.set_window_title('Grafo de ocupaciones' ) 
    plt.clf()
            
    # Se rellena el peso del grafo 
    for u, v, d in Grafo.edges(data=True):
        d['weight'] = float( d[peso] ) 
                    
    
    #Se pintan los nodos de la solucion
    colorNodosSolucion = []
    for node in Grafo:
        #Si es el nodo parado
        if str(node) == nodoParado:
             colorNodosSolucion.append('lawngreen')
        else :
             colorNodosSolucion.append('grey')
    
    
    #Para pintar los enlaces que no son solucion
    enlacesNoSolucion= []
    for (u,v,d) in Grafo.edges(data=True):
        enlacesNoSolucion.append((u, v))
    
    
             
    #Se sacan las posiciones de los nodso
    pos=nx.get_node_attributes(Grafo,'pos')
    
    # Dibujamos los enlaces del Grafo 
    nx.draw_networkx_edges(Grafo,pos,edgelist=enlacesNoSolucion, width=1, arrowsize=10,  edge_color='black', arrows = True)
     
    # Dibujamos los atributos del Grafo 
    nx.draw_networkx_labels(Grafo,pos,font_size=12,font_family='sans-serif')
      
    
    enlaces_etiquetas = dict()
    # Cargamos el peso de los enlaces para poder mostarlo
    enlaces_etiquetas =dict([((u, v), str(int( d['weight'] )) ) 
                       for u, v, d in Grafo.edges(data=True)])
    
    #Se dibujan las etiquetas
    nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=enlaces_etiquetas)
     
    plt.axis('off')
    plt.title("Grafo con ocupaciones")
    
    #Se pintan los nodos
    nx.draw_networkx_nodes(Grafo,pos,node_size=450, node_color=colorNodosSolucion)

    # Se muestran los sectores
    for key in sectores:
   
       plt.text(getattr(sectores[key],'posicion')[0], getattr(sectores[key],'posicion')[1], key, style='italic', fontweight='bold',
                   bbox={'facecolor': 'yellow', 'alpha': 0.2, 'pad': 15})


    # Se pinta el asiento
    dibujarAsientoGrafoGeneral(getattr(asiento, 'posicion_X'), getattr(asiento, 'posicion_Y') , plt)

    #Si esta a True se muestra en enlace desde las escaleras hasta el asiento
    if(dibujarEnlacePrefinalAsiento):
        # Se dibujan los enlaces del nodo prefinal al asiento
        dibujarRectaNodoPrefinal_Asiento(NodoPrefinal_pos, Asiento_pos, plt)

    plt.ion()
    plt.show(block=False)
    plt.pause(1)

    return plt



def DibujarGrafoAtributos(Grafo, mostrarPesos, origen, destino, ruta, espectador, sectores, asiento, NodoPrefinal_pos, Asiento_pos , peso='weight'):
    """
    Función pará pintar el grafo segun atributos.
    
    Parameters
    ----------
    Grafo : networkx.classes.multidigraph.MultiDiGraph
        Grafo a dibujar.
    mostrarPesos : bool
        Boolean - True si se muestran los Pesos.
    origen : string
        String - Nodo inicial de la solucion.
    destino : string
        String - Nodo final de la solucion.
    ruta : lista
        Lista - (Longitud [Nodos_Solucion])
    espectador : Espectador
        Espectador que accede a un asiento.
    sectores : Lista
        Lista de Sector.
    asiento : Asiento
        Asiento al que se accede.
    NodoPrefinal_pos : List
        Posición del nodo Prefinal.
    Asiento_pos : List
        Posción del asiento.
    peso : string, optional
        String con el la etiqueta peso. (Default: weight)
        
    Returns
    -------
    Plt donde se dibuja : module
    """

    #Nueva ventana
    width1 = 9
    height1 = 9
    width_height_1 = (width1, height1)
    plt.figure(4,figsize=width_height_1)
    plt.figure(4).canvas.set_window_title('Ruta según atributos personales desde el nodo [' + origen + '] hasta [' + destino + ']' ) 
    plt.clf()
            
            
    #Se rellenan los pesos del grafo
    for u, v, d in Grafo.edges(data=True):
        d['weight'] = float( d[peso] ) 
                    
    
    #Color de los grafos
    color_map = []
    for node in Grafo:
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
    
    
    #Se pintan los nodos de la solucion
    colorNodosSolucion = []
    for node in Grafo:
        #Si esta en la ruta lo pinto de color 
        if str(node) in ruta:
             colorNodosSolucion.append('lawngreen')
        else :
             colorNodosSolucion.append('grey')
    
    #Para pintar los enlaces solucion
    enlacesSolucion = []
    for indiceSolucion, objetoSolucion in enumerate(ruta):
        if indiceSolucion < len(ruta)-1:
            enlacesSolucion.append( ( ruta[indiceSolucion], ruta[indiceSolucion+1]) )
    
    
    #Para pintar los enlaces que no son solucion
    enlacesNoSolucion= []
    for (u,v,d) in Grafo.edges(data=True):
        if (u, v) not in enlacesSolucion:
            enlacesNoSolucion.append((u, v))
    
    
    #Se sacan las posiciones de los nodos
    pos=nx.get_node_attributes(Grafo,'pos')
    
    # Dibujamos los nodos del Grafo 
    nx.draw_networkx_nodes(Grafo,pos,node_size=450, node_color=color_map)
    
    # Dibujamos los enlaces del Grafo 
    nx.draw_networkx_edges(Grafo,pos,edgelist=enlacesNoSolucion, width=1, arrowsize=10,  edge_color='black', arrows = True)
    # Dibujamos los enlaces Solucion del Grafo (Color Verde)
    nx.draw_networkx_edges(Grafo,pos,edgelist=enlacesSolucion, width=3.5, edge_color='green', arrows = True)
     
    # Dibujamos los atributos del Grafo 
    nx.draw_networkx_labels(Grafo,pos,font_size=12,font_family='sans-serif')
     
    
    enlaces_etiquetas = dict()
    # Cargamos el peso de los enlaces para poder mostarlo
    enlaces_etiquetas =dict([((u, v),"{:.2f}".format( float( d['weight'] )) ) 
                       for u, v, d in Grafo.edges(data=True)])
    
    
    nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=enlaces_etiquetas)
     
    plt.axis('off')
    plt.title("Grafo según Atributos Personales")
    
    plt.text(0, -1.5, 'La ruta, según criterios del usuaruio, recomendada desde [' + origen + '] hasta  [' + destino + '] es la ruta que pasa por los nodos: ' + str(ruta), style='italic',
                    bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
           
    
    #Se pintan los nodos
    nx.draw_networkx_nodes(Grafo,pos,node_size=450, node_color=colorNodosSolucion)

    #Se pintan los sectores
    for key in sectores:
   
       plt.text(getattr(sectores[key],'posicion')[0], getattr(sectores[key],'posicion')[1], key, style='italic', fontweight='bold',
                   bbox={'facecolor': 'yellow', 'alpha': 0.2, 'pad': 15})

    # Se pinta la leyenda 
    plt.text(0, -0.8, 'LEYENDA\n' + '\nEnlaces solución: Verde' + '\n\nAsiento: Asterisco Rojo ' + '\nCamino nodo prefinal - asiento: Línea Roja a puntos'  , style='italic', fontweight='normal',bbox={'facecolor': 'orange', 'alpha': 0.2, 'pad': 2})

    # Se pinta el asiento
    dibujarAsientoGrafoGeneral(getattr(asiento, 'posicion_X'), getattr(asiento, 'posicion_Y') , plt)

    # Se pintan los datos del grafo
    dibujarDatosEspectadorMasRapida(Grafo, espectador, plt)


    # Se pintan los datos del grafo
    dibujarDatosEspectadorAtributos(Grafo, espectador, plt)
    
    

    plt.ion()
    plt.show(block=False)
    plt.pause(1)

    return plt


def DibujarGrafoMasRapida(Grafo, mostrarPesos, origen, destino, ruta, espectador, sectores, asiento, NodoPrefinal_pos, Asiento_pos, peso='weight'):
    """
    Función pará pintar el grafo con la ruta más rapida.
    
    Parameters
    ----------
    Grafo : networkx.classes.multidigraph.MultiDiGraph
        Grafo a dibujar.
    mostrarPesos : bool
        Boolean - True si se muestran los Pesos.
    origen : string
        String - Nodo inicial de la solucion.
    destino : string
        String - Nodo final de la solucion.
    ruta : lista
        Lista - (Longitud [Nodos_Solucion])
    espectador : Espectador
        Espectador que accede a un asiento.
    sectores : Lista
        Lista de Sector.
    asiento : Asiento
        Asiento al que se accede.
    NodoPrefinal_pos : List
        Posición del nodo Prefinal.
    Asiento_pos : List
        Posción del asiento.
    peso : string, optional
        String con el la etiqueta peso. (Default: weight)
    
    Returns
    -------
    Plt donde se dibuja : module
        
    """

    #Nueva ventana
    width1 = 9
    height1 = 9
    width_height_1 = (width1, height1)
    plt.figure(3,figsize=width_height_1)
    plt.figure(3).canvas.set_window_title('Ruta más rápida desde el nodo [' + origen + '] hasta [' + destino + ']' ) 
    plt.clf()
            

    for u, v, d in Grafo.edges(data=True):
        d['weight'] = float( d[peso] ) 
                    
    
    #Se pintan los nodos de la solucion
    colorNodosSolucion = []
    for node in Grafo:
        #Si esta en la ruta lo pinto de color 
        if str(node) in ruta:
             colorNodosSolucion.append('lawngreen')
        else :
             colorNodosSolucion.append('grey')
    
    #Para pintar los enlaces solucion
    enlacesSolucion = []
    for indiceSolucion, objetoSolucion in enumerate(ruta):
        if indiceSolucion < len(ruta)-1:
            enlacesSolucion.append( ( ruta[indiceSolucion], ruta[indiceSolucion+1]) )
    
    
    #Para pintar los enlaces que no son solucion
    enlacesNoSolucion= []
    for (u,v,d) in Grafo.edges(data=True):
        if (u, v) not in enlacesSolucion:
            enlacesNoSolucion.append((u, v))
       
    #Se saca la posicion de los nodos
    pos=nx.get_node_attributes(Grafo,'pos')
     
    # Dibujamos los enlaces del Grafo 
    nx.draw_networkx_edges(Grafo,pos,edgelist=enlacesNoSolucion, width=1, arrowsize=10,  edge_color='black', arrows = True)
    # Dibujamos los enlaces Solucion del Grafo (Color Verde)
    nx.draw_networkx_edges(Grafo,pos,edgelist=enlacesSolucion, width=3.5, edge_color='green', arrows = True)
     
    # Dibujamos los atributos del Grafo 
    nx.draw_networkx_labels(Grafo,pos,font_size=12,font_family='sans-serif')
      
    enlaces_etiquetas = dict()
    # Cargamos el peso de los enlaces para poder mostarlo
    enlaces_etiquetas =dict([((u, v),"{:.2f}".format( float( d['weight'] )) ) 
                       for u, v, d in Grafo.edges(data=True)])
    
     
    nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=enlaces_etiquetas)
     
    plt.axis('off')
    plt.title("Grafo ruta más rápida")
    
    plt.text(0, -1.5, 'La ruta más rápida recomendada desde [' + origen + '] hasta  [' + destino + '] es la ruta que pasa por los nodos: ' + str(ruta), style='italic',
                    bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
           
    
    #Se pintan los nodos
    nx.draw_networkx_nodes(Grafo,pos,node_size=450, node_color=colorNodosSolucion)

    #Se muestran los sectores
    for key in sectores:
   
       plt.text(getattr(sectores[key],'posicion')[0], getattr(sectores[key],'posicion')[1], key, style='italic', fontweight='bold',
                   bbox={'facecolor': 'yellow', 'alpha': 0.2, 'pad': 15})

    # Se pinta la leyenda 
    plt.text(0, -0.8, 'LEYENDA\n' + '\nEnlaces solución: Verde' + '\n\nAsiento: Asterisco Rojo ' + '\nCamino nodo prefinal - asiento: Línea Roja a puntos'   , style='italic', fontweight='normal',bbox={'facecolor': 'orange', 'alpha': 0.2, 'pad': 2})

    # Se pinta el asiento
    dibujarAsientoGrafoGeneral(getattr(asiento, 'posicion_X'), getattr(asiento, 'posicion_Y') , plt)

    #Se dibuja una linea para simular el camino desde las escaleras hasta el  asiento
    dibujarRectaNodoPrefinal_Asiento(NodoPrefinal_pos, Asiento_pos, plt)

    # Se pintan los datos del grafo
    dibujarDatosEspectadorMasRapida(Grafo, espectador, plt)

    plt.ion()
    plt.show(block=False)
    plt.pause(1)

    return plt


def DibujarGrafoMasCorta(Grafo, mostrarPesos, origen, destino, ruta, espectador, sectores, asiento, NodoPrefinal_pos, Asiento_pos, peso='weight'):
    """
    Función para dibujar el grafo con la ruta más corta
    
    Parameters
    ----------
    Grafo : networkx.classes.multidigraph.MultiDiGraph
        Grafo a dibujar.
    mostrarPesos : bool
        Boolean - True si se muestran los Pesos.
    origen : string
        String - Nodo inicial de la solucion.
    destino : string
        String - Nodo final de la solucion.
    ruta : lista
        Lista - (Longitud [Nodos_Solucion])
    espectador : Espectador
        Espectador que accede a un asiento.
    sectores : Lista
        Lista de Sector.
    asiento : Asiento
        Asiento del espectador.
    NodoPrefinal_pos : List
        Posición del nodo Prefinal.
    Asiento_pos : List
        Posción del asiento.
    peso : string, optional
        String con el la etiqueta peso. (Default: weight)
        
    Returns
    -------
    Plt donde se dibuja : module
        
    """

    #Nueva ventana
    width1 = 9
    height1 = 9
    width_height_1 = (width1, height1)
    plt.figure(3,figsize=width_height_1)
    plt.figure(3).canvas.set_window_title('Ruta más corta desde el nodo [' + origen + '] hasta [' + destino + ']' ) 
    plt.clf()
            
    #Se rellenan los pesos del grafo
    for u, v, d in Grafo.edges(data=True):
        d['weight'] = float( d[peso] ) 
                    
    
    #Se pintan los nodos de la solucion
    colorNodosSolucion = []
    for node in Grafo:
        #Si esta en la ruta lo pinto de color 
        if str(node) in ruta:
             colorNodosSolucion.append('lawngreen')
        else :
             colorNodosSolucion.append('grey')
    
    #Para pintar los enlaces solucion
    enlacesSolucion = []
    for indiceSolucion, objetoSolucion in enumerate(ruta):
        if indiceSolucion < len(ruta)-1:
            enlacesSolucion.append( ( ruta[indiceSolucion], ruta[indiceSolucion+1]) )
    
    
    #Para pintar los enlaces que no son solucion
    enlacesNoSolucion= []
    for (u,v,d) in Grafo.edges(data=True):
        if (u, v) not in enlacesSolucion:
            enlacesNoSolucion.append((u, v))
    

    #Se saca la posicion de los nodos
    pos=nx.get_node_attributes(Grafo,'pos')

    # Dibujamos los enlaces del Grafo 
    nx.draw_networkx_edges(Grafo,pos,edgelist=enlacesNoSolucion, width=1, arrowsize=10,  edge_color='black', arrows = True)
    # Dibujamos los enlaces Solucion del Grafo (Color Verde)
    nx.draw_networkx_edges(Grafo,pos,edgelist=enlacesSolucion, width=3.5, edge_color='green', arrows = True)
     
    # Dibujamos los atributos del Grafo 
    nx.draw_networkx_labels(Grafo,pos,font_size=12,font_family='sans-serif')
      
    
    enlaces_etiquetas = dict()
    # Cargamos el peso de los enlaces para poder mostarlo
    enlaces_etiquetas =dict([((u, v),"{:.2f}".format( float( d['weight'] )) ) 
                       for u, v, d in Grafo.edges(data=True)])
    
     
    nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=enlaces_etiquetas)
     
    plt.axis('off')
    plt.title("Grafo ruta más corta")
    
    plt.text(0, -1.5, 'La ruta más corta recomendada desde [' + origen + '] hasta  [' + destino + '] es la ruta que pasa por los nodos: ' + str(ruta), style='italic',
                    bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
           
    
    #Se pintan los nodos
    nx.draw_networkx_nodes(Grafo,pos,node_size=450, node_color=colorNodosSolucion)

    #Se pintan los sectores
    for key in sectores:
   
       plt.text(getattr(sectores[key],'posicion')[0], getattr(sectores[key],'posicion')[1], key, style='italic', fontweight='bold',
                   bbox={'facecolor': 'yellow', 'alpha': 0.2, 'pad': 15})

    # Se pinta la leyenda 
    plt.text(0, -0.8, 'LEYENDA\n' + '\nEnlaces solución: Verde' + '\n\nAsiento: Asterisco Rojo ' + '\nCamino nodo prefinal - asiento: Línea Roja a puntos'  , style='italic', fontweight='normal',bbox={'facecolor': 'orange', 'alpha': 0.2, 'pad': 2})
    
    # Se pinta el asiento
    dibujarAsientoGrafoGeneral(getattr(asiento, 'posicion_X'), getattr(asiento, 'posicion_Y') , plt)
    
    
    # Se dibujan el enlace del nodo Prefinal al asiento
    dibujarRectaNodoPrefinal_Asiento(NodoPrefinal_pos, Asiento_pos, plt)
    

    # Se pintan los datos del grafo
    dibujarDatosEspectadorMasCorta(Grafo, espectador, plt)

    plt.ion()
    plt.show(block=False)
    plt.pause(1)


    return plt



                
    
    


    

#Variable con las repuestas (Se usa para el formulario de atributos)
"""
Por defecto son todas 0
"""

        
respuestas = Respuestas()  





def leerSectoresCSV(fichero, Grafo):
    """
    Función para leer los Sectores de la grada de un fichero CSV

    Parameters
    ----------
    fichero : String
        Fichero .csv con los sectores.
    Grafo : networkx.classes.multidigraph.MultiDiGraph
        Grafo del estadio.

    Returns
    -------
    sectores : Lista
        Lista con los sectores leidos.

    """
    sectores = {}
    
    
    with open(fichero) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader, None)
        for row in csv_reader:

            pos1 = None
            pos2 = None
            
            posArribaIzquierda = None
            posArribaDerecha = None
            posAbajoIzquierda = None
            posAbajoDerecha = None

            if row[1] != 'None': 
                posArribaIzquierda = Grafo.nodes.data()[row[1]]['pos']
            if row[2] != 'None': 
                posArribaDerecha = Grafo.nodes.data()[row[2]]['pos']
            if row[3] != 'None':
                posAbajoIzquierda = Grafo.nodes.data()[row[3]]['pos']
            if row[4] != 'None':
                posAbajoDerecha = Grafo.nodes.data()[row[4]]['pos']
            try:
                pos1 = ((posArribaIzquierda[0] + posAbajoDerecha[0])/2, (posArribaIzquierda[1] + posAbajoDerecha[1])/2)
            except:
                IgnorarError = ''
            
            try:
                pos2 = ((posArribaDerecha[0] + posAbajoIzquierda[0])/2, (posArribaDerecha[1] + posAbajoIzquierda[1])/2)
            except:
                IgnorarError = ''
            
            
            if pos1 != None: pos = pos1
            else: pos = pos2
            
            sector = Clases.Sector(row[0], row[1], row[2], row[3], row[4], int(row[5]), int(row[6]), pos)
            sectores[row[0]]= sector
        
    return sectores
        


def exportarGrafoJSON(Grafo):
    """
    Funcion para generar un fichero JSON a partir del grafo dado.
    
    Parameters
    ----------
    Grafo : networkx.classes.multidigraph.MultiDiGraph
        Grafo a exportar.

    Returns
    -------
    None.

    """
    data1 = json_graph.node_link_data(Grafo)
    with open('nodosExportados.json', 'w') as fp:
        json.dump(data1, fp)
    return data1
        
def importarGrafoJSON(Fichero):
    """
    Funcion para leer el grafo a parti de un fichero JSON

    Parameters
    ----------
    Fichero : String
        Fichero de extension .json.

    Returns
    -------
    Grafo: networkx.classes.multidigraph.MultiDiGraph
        Grafo leido del fichero JSON.

    """
    
    Grafo = nx.MultiDiGraph()
    
    with open(Fichero) as f:
        json_data = json.loads(f.read())


    for nodo in json_data['nodes']:
        Grafo.add_node(nodo['id'], pos = nodo['pos'])

    for enlace in json_data['links']:
        Grafo.add_edge(enlace['source'], enlace['target'], weight = enlace['weight'], label = '', tipoEnlace = enlace['tipoEnlace'], longitud = enlace['longitud'] , inclinacion = enlace['inclinacion'], barandilla = enlace['barandilla'], pasilloBuenEstado = enlace['pasilloBuenEstado'],  pasilloAmplio = enlace['pasilloAmplio'], pasilloVentildo = enlace['pasilloVentildo'], pasilloSeco = enlace['pasilloSeco'], pasilloIluminado = enlace['pasilloIluminado'] , ocupacion = enlace['ocupacion'] )

    return Grafo

   
    
    

