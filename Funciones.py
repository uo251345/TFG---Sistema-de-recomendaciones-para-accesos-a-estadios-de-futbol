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

import copy

from sys import exit



    

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
        
    
    def rellenar(self, escalerasConBarandillas, escalerasEnBuenEstado, pasillosAmplios, pasillosVentilados, pasillosSecos, pasilloIluminados):
        self.cancelado = False
        self.escalerasConBarandillas = escalerasConBarandillas
        self.escalerasEnBuenEstado = escalerasEnBuenEstado
        self.pasillosAmplios = pasillosAmplios
        self.pasillosVentilados = pasillosVentilados
        self.pasillosSecos = pasillosSecos
        self.pasilloIluminados = pasilloIluminados
    
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




        self.root.geometry("600x300")
        self.root.title("Recomendación personal según atributos de los pasillos.")
        #self.root.resizable(False, False)
        Label(self.root, text="Puntua del 0 al 5 los atributos de la ruta recomendada.", font="ar 15 bold").place(x=5, y=5)
        Label(self.root, text="[0 - Sin importancia, 5 - Muy importante]", font="ar 12 normal").place(x=10, y=30)
        
        
        
        
        #Preguntas de los atributos
        
        escalerasConBarandillas_Label = Label(self.root, text="Escaleras con barandillas: ", font="ar 12 normal", relief=RIDGE, width=25, anchor='e').place(x=40, y=81)
        escalerasEnBuenEstado_Label = Label(self.root, text="Escaleras en buen estado: ", font="ar 12 normal", relief=RIDGE, width=25, anchor='e').place(x=40, y=111)
        pasillosAmplios_Label = Label(self.root, text="Pasillos amplios: ", font="ar 12 normal", relief=RIDGE, width=25, anchor='e').place(x=40, y=141)
        pasillosVentilados_Label = Label(self.root, text="Pasillos ventilados: ", font="ar 12 normal", relief=RIDGE, width=25, anchor='e').place(x=40, y=171)
        pasillosSecos_Label = Label(self.root, text="Pasillos secos: ", font="ar 12 normal", relief=RIDGE, width=25, anchor='e').place(x=40, y=201)
        pasillosSecos_Label = Label(self.root, text="Pasillos bien iluminados: ", font="ar 12 normal", relief=RIDGE, width=25, anchor='e').place(x=40, y=231)
        
    
        
        
        #Desplegables para seleccionar valores
        
        escalerasConBarandillas_combo = MenuAtributosPersonales(self.root, "0","0","1","2","3","4","5")
        escalerasConBarandillas_combo.place(x=270, y=80)
            
        
        escalerasEnBuenEstado_combo = MenuAtributosPersonales(self.root, "0","0","1","2","3","4","5")
        escalerasEnBuenEstado_combo.place(x=270, y=110)
    
            
        pasillosAmplios_combo = MenuAtributosPersonales(self.root, "0","0","1","2","3","4","5")
        pasillosAmplios_combo.place(x=270, y=140)  
    
    
        pasillosVentilados_combo = MenuAtributosPersonales(self.root, "0","0","1","2","3","4","5")
        pasillosVentilados_combo.place(x=270, y=170)
    
            
        pasillosSecos_combo = MenuAtributosPersonales(self.root, "0","0","1","2","3","4","5")
        pasillosSecos_combo.place(x=270, y=200)
        
                
        pasillosiluminados_combo = MenuAtributosPersonales(self.root, "0","0","1","2","3","4","5")
        pasillosiluminados_combo.place(x=270, y=230)
    
        
        # respuestas['escalerasConBarandillas'] = escalerasConBarandillas_combo.var.get()
        
        #Boton para confirmar
        botonConfirmar = Button(text="Confirmar", width = 20, bg="green" ,command=lambda:botonAtributosPersonalesClick(self,escalerasConBarandillas_combo.var.get(),escalerasEnBuenEstado_combo.var.get() ,pasillosAmplios_combo.var.get() ,pasillosVentilados_combo.var.get() ,pasillosSecos_combo.var.get(),pasillosiluminados_combo.var.get()))
        
        botonConfirmar.place(x=270, y=260)
        
        self.center(self.root)
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        self.root.mainloop()
        
    
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
        
        self.root.destroy()
        
    def close_window(self):
        respusta_cerrar = messagebox.askokcancel(message="¿Desea terminar la ejecución del programa?", title="Terminar ejecución")
        
        if respusta_cerrar:
            self.quit()
    
    
    
    

    
        

def DibujarGrafo(Grafo, colorNodos, colorEnlaces, mostrarPesos, peso='weight'):
    """

    Parameters
    ----------
    Grafo : networkx.classes.multidigraph.MultiDiGraph
        Grafo a dibujar.
    colorNodos : list
        Lista con el color de los nodos.
    colorEnlaces : string
        String con el color de los enlaces.
    mostrarPesos : bool
        Boolean - True si se muestran los Pesos
    peso : string, optional
        String con el la etiqueta peso. (Default: weight)

    Returns
    -------
    None.

    """
    
    
    for u, v, d in Grafo.edges(data=True):
        d['weight'] = float( d[peso] ) 
                    
    

 
    # Retrieve the positions from graph nodes and save to a dictionary
    pos=nx.get_node_attributes(Grafo,'pos')
    # Draw nodes
    nx.draw_networkx_nodes(Grafo,pos,node_size=450, node_color=colorNodos)
    
     
    # Draw edges
    nx.draw_networkx_edges(Grafo,pos, width=2, edge_color=colorEnlaces)
     
    # Draw node labels
    nx.draw_networkx_labels(Grafo,pos,font_size=12,font_family='sans-serif')



    if mostrarPesos:
        # Dibujar los pesos
        edge_labels =dict([((u, v), d['weight']) 
                       for u, v, d in Grafo.edges(data=True)])
     
        nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=edge_labels)
        
    else:
        nx.draw_networkx_edge_labels(Grafo, pos)
     
    plt.axis('off')
    plt.title("Grafo General")
    
    plt.get_current_fig_manager().set_window_title('Grafo General - Pelayo Tiesta')
    
    
    plt.show()
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




        
        
        

