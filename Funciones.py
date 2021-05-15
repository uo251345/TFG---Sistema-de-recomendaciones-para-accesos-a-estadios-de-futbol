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


from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

import uuid



import Clases

import copy

import csv


from sys import exit


#Divisor atributos
divisior_atributos = 6
    

class MenuAtributosPersonales(OptionMenu):
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
    
    def __repr__(self):
        if(self.cancelado): 
            return "Sin rellenar." 
        
        else:
            return "escalerasConBarandillas:%s escalerasEnBuenEstado:%s pasillosAmplios:%s pasillosVentilados:%s pasillosSecos:%s pasilloIluminados:%s" % (self.escalerasConBarandillas, self.escalerasEnBuenEstado, self.pasillosAmplios, self.pasillosVentilados, self.pasillosSecos, self.pasilloIluminados)
        
    


class ventanaAtributosPersonales():
    
    
    def __init__(self):

        #Mostramos el formulario de consulta
        self.root = Tk()
        
        
        # Sacamos las dimensiones de la pantilla
        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()
        
         
        # Gets both half the screen width/height and window width/height
        posicionDerecha = int(self.root.winfo_screenwidth()/2 - windowWidth/2)
        posicionAbajo = int(self.root.winfo_screenheight()/2 - windowHeight/2)
         
        # Positions the window in the center of the page.
        self.root.geometry("+{}+{}".format(posicionDerecha, posicionAbajo))




        self.root.geometry("600x400")
        self.root.title("Recomendación personal según atributos de los pasillos.")
        #self.root.resizable(False, False)
        Label(self.root, text="Puntua del 0 al 5 los atributos de la ruta recomendada.", font="ar 15 bold").place(x=5, y=25)
        Label(self.root, text="[0 - Sin importancia, 5 - Muy importante]", font="ar 12 normal").place(x=10, y=50)
        
        
        
        
        #Preguntas de los atributos
        
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
    
        
        # respuestas['escalerasConBarandillas'] = escalerasConBarandillas_combo.var.get()
        
        #Boton para confirmar
        botonConfirmar = Button(self.root, text="Confirmar", width = 20, bg="green" ,command=lambda:botonAtributosPersonalesClick(self,escalerasConBarandillas_combo.var.get(),escalerasEnBuenEstado_combo.var.get() ,pasillosAmplios_combo.var.get() ,pasillosVentilados_combo.var.get() ,pasillosSecos_combo.var.get(),pasillosiluminados_combo.var.get()))
        botonConfirmar.place(x=270, y=300)
        
        self.center(self.root)
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        self.root.mainloop()
   
        
        return
    
    def center(self, window):
        """
        Para centrar la ventana
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
        respusta_cerrar = messagebox.askokcancel(message="¿Desea terminar la ejecución del programa?", title="Terminar ejecución")
        
        if respusta_cerrar:
            self.quit()
    
    
    

class ventanaPerfilEspectador():
    
    
    
    def __init__(self):

        #Mostramos el formulario de consulta
        self.root = Tk()
        
        
        # Sacamos las dimensiones de la pantilla
        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()
        
         
        # Gets both half the screen width/height and window width/height
        posicionDerecha = int(self.root.winfo_screenwidth()/2 - windowWidth/2)
        posicionAbajo = int(self.root.winfo_screenheight()/2 - windowHeight/2)
         
        # Positions the window in the center of the page.
        self.root.geometry("+{}+{}".format(posicionDerecha, posicionAbajo))




        self.root.geometry("600x300")
        self.root.title("Perfil del espectador.")
        #self.root.resizable(False, False)
        Label(self.root, text="Datos del espectador.", font="ar 15 bold").place(x=5, y=25)

        #Datos
        Label(self.root, text="Sector:", font="ar 12 normal").place(x=10, y=50)
        sector = Clases.MenuSector(self.root, "S11","S11","S12","S21","S22","S31","S32").place(x=80, y=50)
        Label(self.root, text="Fila:", font="ar 12 normal").place(x=10, y=100)
        fila = Entry(self.root).place(x=80, y=100)
        Label(self.root, text="Columna:", font="ar 12 normal").place(x=10, y=150)
        columna = Entry(self.root).place(x=80, y=150)
        Label(self.root, text="Puerta:", font="ar 12 normal").place(x=10, y=200)
        puerta = Entry(self.root).place(x=80, y=200)
        


        
        #Boton para confirmar
        botonConfirmar = Button(self.root, text="Confirmar", width = 20, bg="green" ,command=self.root.destroy)
        botonConfirmar.place(x=270, y=250)
        
        self.center(self.root)
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        self.root.mainloop()
        
        
        print(sector.var.get())
             
        
        self.espectador = Clases.Espectador(uuid.uuid4(), Clases.Asiento(self.sector.var.get(), self.fila.get(), self.columna.get()), self.puerta.get())
        
        print(self.espectador)
        
        
        
        
        return
    
    def center(self, window):
        """
        Para centrar la ventana
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
        respusta_cerrar = messagebox.askokcancel(message="¿Desea terminar la ejecución del programa?", title="Terminar ejecución")
        
        if respusta_cerrar:
            self.quit()
    
    

    
        

def DibujarGrafoGeneral(Grafo, colorNodos, mostrarPesos, sectores, peso='weight'):
    """

    Parameters
    ----------
    Grafo : networkx.classes.multidigraph.MultiDiGraph
        Grafo a dibujar.
    colorNodos : list
        Lista con el color de los nodos.
    mostrarPesos : bool
        Boolean - True si se muestran los Pesos
    peso : string, optional
        String con el la etiqueta peso. (Default: weight)

    Returns
    -------
    None.

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
                    
    
    #Para pintar los enlaces solucion
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
            
    
    
     
    # Se sacan las posiciones de los nodos
    pos=nx.get_node_attributes(Grafo,'pos')
    
    # Se dibujan los nodos
    nx.draw_networkx_nodes(Grafo,pos,node_size=450, node_color=colorNodos)
    
    # Se dibujan los 4 tipos de enlaces
    # Pasillos sin barandilla (color Verde)
    nx.draw_networkx_edges(Grafo,pos,edgelist=enlacesPasillos,    edge_color='springgreen', arrows = True)
    # Pasillos con barandilla (color verde Oscuro)
    nx.draw_networkx_edges(Grafo,pos,edgelist=enlacesPasillosConBarandillas,   edge_color='darkgreen', arrows = True)
    # Escaleras sin barandilla (color Verde)
    nx.draw_networkx_edges(Grafo,pos,edgelist=enlacesEscaleras,   edge_color='deepskyblue', arrows = True,)
    # Escaleras con barandilla (color verde Oscuro)
    nx.draw_networkx_edges(Grafo,pos,edgelist=enlacesEscalerasConBarandillas,   edge_color='darkblue', arrows = True)
     
    # Draw node labels
    nx.draw_networkx_labels(Grafo,pos,font_size=12,font_family='sans-serif')



    if mostrarPesos:
        # Dibujar los pesos
        edge_labels =dict([((u, v), d['weight']) 
                       for u, v, d in Grafo.edges(data=True)])
     
        nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=edge_labels)
        
    else:
        nx.draw_networkx_edge_labels(Grafo, pos)
        
        
        
    #Se muestran los sectores
    for key in sectores:
    
        plt.text(getattr(sectores[key],'posicion')[0], getattr(sectores[key],'posicion')[1], key, style='italic', fontweight='bold',
                    bbox={'facecolor': 'yellow', 'alpha': 0.2, 'pad': 15})
        
    
    #Leyenda con los datos
    plt.text(0, -0.5, 'LEYENDA\n' + '\nPasillos planos sin barandilla: Verde Claro' + '\nPasillos planos con barandilla: Verde Oscuro' + '\nPasillos con escaleras sin barandilla: Azul Claro' + '\nPasillos con escaleras con barandilla: Azul Oscuro' + '\n\nAsiento: Cuadrado Rojo [x]'  , style='italic', fontweight='normal',bbox={'facecolor': 'orange', 'alpha': 0.2, 'pad': 2})
    

    
    plt.axis('off')
    plt.title("Grafo General")
    
    
    
    plt.ion()
    plt.show(block=False)
    plt.pause(1)


    return plt




def dibujarAsientoGrafoGeneral(Grafo, sectores, asiento, plot):
    
    
    
    #Dibujar asiento    
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
    if (fila_asiento > filas_sector): raise Exception("Error: La fila del aseinto esta fuera de las filas del sector. El sector tiene solo: " + str(filas_sector) + " filas.")
    
    if(columna_asiento > columnas_sector): raise Exception("Error: La columna del aseinto esta fuera de las columnas del sector. El sector tiene solo: " + str(columnas_sector) + " columnas.")
    
    
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
    
    
    
    try:
        longitud_enlace_derecha1 = Grafo.nodes()[nodo_ArribaDerecha]['pos'][1] - Grafo.nodes()[nodo_AbajoDerecha]['pos'][1]
    except:
        IgnorarError = ''
     
    try:
        longitud_enlace_derecha2 = Grafo.nodes()[nodo_ArribaIzquierda]['pos'][1]- Grafo.nodes()[nodo_AbajoIzquierda]['pos'][1]
    except:
        IgnorarError = ''
        
    longitud_enlace_derecha = None
    if(longitud_enlace_derecha1 != None): longitud_enlace_derecha = longitud_enlace_derecha1    
    else: longitud_enlace_derecha = longitud_enlace_derecha2
    
    unidadesVertical = longitud_enlace_derecha/filas_sector
    unidadesHorizontal = longitud_enlace_arriba/columnas_sector
    
    posicionX_asiento = Grafo.nodes()[nodo_ArribaIzquierda]['pos'][0] + (unidadesHorizontal * columna_asiento)
    posicionY_asiento = Grafo.nodes()[nodo_ArribaIzquierda]['pos'][1] - (unidadesVertical * (filas_sector - fila_asiento)) 
    
    #Se dibuja el asiento (Se resta un offset a cada componente espacial para ajustar la posicion en la figura)
    plt.ion()
    plt.draw()
    plt.pause(0.0001)
    plot.text(posicionX_asiento - 0.08, posicionY_asiento - 0.1, 'x', style='italic', fontweight='bold',bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 0.5})
    plt.pause(0.0001)
    
    
    


def dibujarDatosEspectadorGeneral(Grafo, espectador, plot):
    
    ID = "\nID: " + str(getattr(espectador, 'ID'))
    PuertaEntrada = "\nPuerta de entrada: " + str(getattr(espectador, 'puertaEntrada'))
    NodoPrefinal = "\nNodo prefinal: " + str(getattr(espectador, 'nodoPrefinal'))
    
    plt.ion()
    plt.draw()
    plt.pause(0.0001)
    plot.text(3.5, -0.5, 'DATOS ESPECTADOR\n' + ID + PuertaEntrada + NodoPrefinal , style='italic', fontweight='normal',bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 2})
    plt.pause(0.0001)


def DibujarGrafoAtributos(Grafo, colorNodosSolucion, colorEnlaces, mostrarPesos, origen, destino, ruta, peso='weight'):
    """
    
    Parameters
    ----------
    Grafo : networkx.classes.multidigraph.MultiDiGraph
        Grafo a dibujar.
    colorNodosSolucion : string
        Lista con el color de los nodos.
    colorEnlaces : string
        String con el color de los enlaces.
    mostrarPesos : bool
        Boolean - True si se muestran los Pesos.
    origen : string
        String - Nodo inicial de la solucion.
    destino : string
        String - Nodo final de la solucion.
    ruta : lista
        Lista - (Longitud [Nodos_Solucion])
    peso : string, optional
        String con el la etiqueta peso. (Default: weight)
        
    """

  
    
    
    #Nueva ventana
    width1 = 9
    height1 = 9
    width_height_1 = (width1, height1)
    plt.figure(4,figsize=width_height_1)
    plt.figure(4).canvas.set_window_title('Ruta según atributos personales desde el nodo [' + origen + '] hasta [' + destino + ']' ) 
    
            
            
            
    
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
    
     
    elarge=[(u,v) for (u,v,d) in Grafo.edges(data=True) ] # solid edge
    
    #Para pintar los enlaces solucion
    enlacesSolucion = []
    for indiceSolucion, objetoSolucion in enumerate(ruta):
        if indiceSolucion < len(ruta)-1:
            enlacesSolucion.append( ( ruta[indiceSolucion], ruta[indiceSolucion+1]) )
    
    
             
    #Mismo grafo pero pintamos los nodos distinto
    # Retrieve the positions from graph nodes and save to a dictionary
    pos=nx.get_node_attributes(Grafo,'pos')
    
    # Dibujamos los nodos del Grafo 
    nx.draw_networkx_nodes(Grafo,pos,node_size=450, node_color=color_map)
    
     
    # Dibujamos los enlaces del Grafo 
    nx.draw_networkx_edges(Grafo,pos,edgelist=elarge, width=1, arrowsize=10,  edge_color='black', arrows = True)
     
    # Dibujamos los atributos del Grafo 
    nx.draw_networkx_labels(Grafo,pos,font_size=12,font_family='sans-serif')
     
    
    
    # Dibujamos los enlaces Solucion del Grafo 
    nx.draw_networkx_edges(Grafo,pos,edgelist=enlacesSolucion, width=3.5, edge_color='red', arrows = True)
    
    
    enlaces_etiquetas = dict()
    # Cargamos el peso de los enlaces para poder mostarlo
    enlaces_etiquetas =dict([((u, v),"{:.2f}".format( float( d['weight'] )) ) 
                       for u, v, d in Grafo.edges(data=True)])
    
    
     
    nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=enlaces_etiquetas)
     
    plt.axis('off')
    plt.title("Grafo Segun atributos personales")
    
    plt.text(0, -1.5, 'La ruta, según criterios del usuaruio, recomendada desde [' + origen + '] hasta  [' + destino + '] es la ruta que pasa por los nodos: ' + str(ruta), style='italic',
                    bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
           
    
    
    nx.draw_networkx_nodes(Grafo,pos,node_size=450, node_color=colorNodosSolucion)



    plt.ion()
    
    plt.show(block=False)

    plt.pause(1)





def botonAtributosPersonalesClick(ventana_self,escalerasConBarandillas,escalerasEnBuenEstado,pasillosAmplios, pasillosVentilados,  pasillosSecos, pasilloIluminados):
    """
    Metodo auxiliar para capturar el click del boton Confirmar en el formulario de atributos
    
    y modificar el diccionario respuestas


    """
    
    
    respuestas.rellenar(escalerasConBarandillas, escalerasEnBuenEstado, pasillosAmplios, pasillosVentilados, pasillosSecos, pasilloIluminados)


    ventana_self.quit()



    

   
    

#Variable con las repuestas (Se usa para el formulario de atributos)
"""
Por defecto son todas 0
"""

        
respuestas = Respuestas()  





def leerSectoresCSV(fichero, Grafo):
    
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
        

