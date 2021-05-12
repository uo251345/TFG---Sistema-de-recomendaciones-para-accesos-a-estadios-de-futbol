try:
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import ion

    
    

except:
    raise
 
import networkx as nx

import sys

#Variables para la ejecuccion del programa
rutaMasCorta = False
rutaMasRapida = False


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
G.add_edge('P1','12',weight=15, label='', tipoEnlace = 'escalera', longitud = '15', inclinacion = '+', barandilla = '', ocupacion = '' )
G.add_edge('P1','14',weight=15, label='', tipoEnlace = 'escalera', longitud = '15', inclinacion = '+', barandilla = '', ocupacion = '' )
G.add_edge('P1','22',weight=30, label='', tipoEnlace = 'escalera', longitud = '30', inclinacion = '+', barandilla = '', ocupacion = '' )
G.add_edge('P1','24',weight=30, label='', tipoEnlace = 'escalera', longitud = '30', inclinacion = '+', barandilla = '', ocupacion = '' )

#Los del Nivel 0
G.add_edge('01','12',weight=10, label='', tipoEnlace = 'escalera', longitud = '10', inclinacion = '+', barandilla = '', ocupacion = '' )
G.add_edge('01','02',weight=20, label='', tipoEnlace = 'plano', longitud = '20', inclinacion = '', barandilla = '', ocupacion = '' )
G.add_edge('02','01',weight=20, label='', tipoEnlace = 'plano', longitud = '20', inclinacion = '', barandilla = '', ocupacion = '' )
G.add_edge('02','14',weight=10, label='', tipoEnlace = 'escalera', longitud = '10', inclinacion = '+', barandilla = '', ocupacion = '' )


#Los del Nivel 1
G.add_edge('11','12',weight=10, label='', tipoEnlace = 'plano', longitud = '10', inclinacion = '', barandilla = '', ocupacion = '' )
G.add_edge('11','21',weight=20, label='', tipoEnlace = 'escalera', longitud = '20', inclinacion = '+', barandilla = '', ocupacion = '' )

G.add_edge('12','01',weight=10, label='', tipoEnlace = 'escalera', longitud = '10', inclinacion = '-', barandilla = '', ocupacion = '' )
G.add_edge('12','11',weight=10, label='', tipoEnlace = 'plano', longitud = '10', inclinacion = '', barandilla = '', ocupacion = '' )
G.add_edge('12','13',weight=10, label='', tipoEnlace = 'plano', longitud = '10', inclinacion = '', barandilla = '', ocupacion = '' )

G.add_edge('13','12',weight=10, label='', tipoEnlace = 'plano', longitud = '10', inclinacion = '', barandilla = '', ocupacion = '' )
G.add_edge('13','14',weight=10, label='', tipoEnlace = 'plano', longitud = '10', inclinacion = '', barandilla = '', ocupacion = '' )
G.add_edge('13','23',weight=20, label='', tipoEnlace = 'escalera', longitud = '20', inclinacion = '+', barandilla = '', ocupacion = '' )

G.add_edge('14','02',weight=10, label='', tipoEnlace = 'escalera', longitud = '10', inclinacion = '-', barandilla = '', ocupacion = '' )
G.add_edge('14','13',weight=10, label='', tipoEnlace = 'plano', longitud = '10', inclinacion = '', barandilla = '', ocupacion = '' )
G.add_edge('14','15',weight=10, label='', tipoEnlace = 'plano', longitud = '10', inclinacion = '', barandilla = '', ocupacion = '' )

G.add_edge('15','14',weight=10, label='', tipoEnlace = 'plano', longitud = '10', inclinacion = '', barandilla = '', ocupacion = '' )
G.add_edge('15','25',weight=20, label='', tipoEnlace = 'escalera', longitud = '20', inclinacion = '+', barandilla = '', ocupacion = '' )



#Los del Nivel 2
G.add_edge('21','11',weight=20, label='', tipoEnlace = 'escalera', longitud = '20', inclinacion = '-', barandilla = '', ocupacion = '' )
G.add_edge('21','22',weight=10, label='', tipoEnlace = 'plano', longitud = '10', inclinacion = '', barandilla = '', ocupacion = '' )
G.add_edge('21','31',weight=25, label='', tipoEnlace = 'escalera', longitud = '25', inclinacion = '+', barandilla = '', ocupacion = '' )

G.add_edge('22','21',weight=10, label='', tipoEnlace = 'plano', longitud = '10', inclinacion = '', barandilla = '', ocupacion = '' )
G.add_edge('22','23',weight=10, label='', tipoEnlace = 'plano', longitud = '10', inclinacion = '', barandilla = '', ocupacion = '' )

G.add_edge('23','13',weight=20, label='', tipoEnlace = 'escalera', longitud = '20', inclinacion = '-', barandilla = '', ocupacion = '' )
G.add_edge('23','22',weight=10, label='', tipoEnlace = 'plano', longitud = '10', inclinacion = '', barandilla = '', ocupacion = '' )
G.add_edge('23','24',weight=10, label='', tipoEnlace = 'plano', longitud = '10', inclinacion = '', barandilla = '', ocupacion = '' )
G.add_edge('23','32',weight=25, label='', tipoEnlace = 'escalera', longitud = '25', inclinacion = '+', barandilla = '', ocupacion = '' )

G.add_edge('24','23',weight=10, label='', tipoEnlace = 'plano', longitud = '10', inclinacion = '', barandilla = '', ocupacion = '' )
G.add_edge('24','25',weight=10, label='', tipoEnlace = 'plano', longitud = '10', inclinacion = '', barandilla = '', ocupacion = '' )

G.add_edge('25','15',weight=20, label='', tipoEnlace = 'escalera', longitud = '20', inclinacion = '-', barandilla = '', ocupacion = '' )
G.add_edge('25','24',weight=10, label='', tipoEnlace = 'plano', longitud = '10', inclinacion = '', barandilla = '', ocupacion = '' )
G.add_edge('25','33',weight=25, label='', tipoEnlace = 'escalera', longitud = '25', inclinacion = '+', barandilla = '', ocupacion = '' )



#Los del Nivel 23
G.add_edge('31','21',weight=25, label='', tipoEnlace = 'escalera', longitud = '25', inclinacion = '-', barandilla = '', ocupacion = '' )
G.add_edge('31','32',weight=20, label='', tipoEnlace = 'plano', longitud = '20', inclinacion = '', barandilla = '', ocupacion = '' )

G.add_edge('32','23',weight=25, label='', tipoEnlace = 'escalera', longitud = '25', inclinacion = '-', barandilla = '', ocupacion = '' )
G.add_edge('32','31',weight=20, label='', tipoEnlace = 'plano', longitud = '20', inclinacion = '', barandilla = '', ocupacion = '' )
G.add_edge('32','33',weight=20, label='', tipoEnlace = 'plano', longitud = '20', inclinacion = '', barandilla = '', ocupacion = '' )

G.add_edge('33','25',weight=25, label='', tipoEnlace = 'escalera', longitud = '25', inclinacion = '-', barandilla = '', ocupacion = '' )
G.add_edge('33','32',weight=20, label='', tipoEnlace = 'plano', longitud = '20', inclinacion = '', barandilla = '', ocupacion = '' )




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



elarge=[(u,v) for (u,v,d) in G.edges(data=True) ] # solid edge

 
# Retrieve the positions from graph nodes and save to a dictionary
pos=nx.get_node_attributes(G,'pos')
# Draw nodes
nx.draw_networkx_nodes(G,pos,node_size=450, node_color=color_map)

 
# Draw edges
nx.draw_networkx_edges(G,pos,edgelist=elarge, width=2, edge_color='g')
 
# Draw node labels
nx.draw_networkx_labels(G,pos,font_size=12,font_family='sans-serif')
 
# Draw edge labels
edge_labels =dict([((u, v), d['weight']) 
                   for u, v, d in G.edges(data=True)])
 
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
 
plt.axis('off')
plt.title("Grafo General")

plt.get_current_fig_manager().canvas.set_window_title('Grafo General - Pelayo Tiesta')


plt.show()
        



while True:
    
    #Pedimos que quire aplicar
    print ("")
    print ("¿Que algoritmo desea aplicar?")
    print ("    (1)    Ruta más corta.")
    print ("    (2)    Ruta más rapida.")
    print (" _________________________________")
    print ("    (E / END)    Salir.")
    print 
    seleccionado = input()
    if str(seleccionado) == '1':
        rutaMasCorta = True;
    elif str(seleccionado) == '2':
        rutaMasRapida = True;
    elif str(seleccionado).lower() == 'e' or str(seleccionado).lower() == 'end' : #Lower para ignorar que sea mayusculas o minusculas
        sys.exit()
    else:
        print("Error al seleccionar algoritmo.")
        
   
    
    if rutaMasCorta:    
        #print ("")
        #print ("Escriba el origen:")
        #origen = str(input())
        
        print ("")
        print ("Escriba el destino:")
        destino = str(input())
        #Checkeo de que esta en el grafo
        if destino not in G.nodes():
            print("El nodo no esta en el grafo")
        else:
            
            
            origen = 'P1'
            
            
            
            #Nueva ventana
            width1 = 9
            height1 = 9
            width_height_1 = (width1, height1)
            plt.figure(2,figsize=width_height_1)
            plt.figure(2).canvas.set_window_title('Ruta más rápida del nodo [' + origen + '] al [' + destino + ']' ) 
            
            elarge=[(u,v) for (u,v,d) in G.edges(data=True) ] # solid edge
            
             
            #Mismo grafico pero pintamos los nodos distinto
            # Retrieve the positions from graph nodes and save to a dictionary
            pos=nx.get_node_attributes(G,'pos')
            # Draw nodes
            nx.draw_networkx_nodes(G,pos,node_size=450, node_color=color_map)
            
             
            # Draw edges
            nx.draw_networkx_edges(G,pos,edgelist=elarge, width=2, edge_color='g')
             
            # Draw node labels
            nx.draw_networkx_labels(G,pos,font_size=12,font_family='sans-serif')
             
            # Draw edge labels
            edge_labels =dict([((u, v), d['weight']) 
                               for u, v, d in G.edges(data=True)])
             
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
             
            plt.axis('off')
        
        
        
     

            
            
            
            
            #Dijkstra
            try:
                djk_Ruta = nx.dijkstra_path(G, source=origen, target=destino, weight=True)
            except nx.NetworkXNoPath:
                print("No existe ruta de: " + origen + " a " + destino)
                continue
            
            #Una vez obtenida la ruta más rapida, coloreamos los nodos seleccionados de color
            color_nodos_solucion = []
            for node in G:
                #Si esta en la ruta lo pinto de color 
                if str(node) in djk_Ruta:
                     color_nodos_solucion.append('lawngreen')
                else :
                     #print("aqui3")
                     color_nodos_solucion.append('grey')
                     
            
            
            nx.draw_networkx_nodes(G,pos,node_size=450, node_color=color_nodos_solucion)
            
            
            #plt.get_current_fig_manager().window.showMaximized()
            
            plt.text(0, -1.5, 'La ruta más corta recomendada desde [' + origen + '] hasta  [' + destino + '] es la ruta que pasa por los nodos: ' + str(djk_Ruta), style='italic',
                    bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
            
            
            plt.show()

            
            
            
#______________________________________________________________________________________________________________________________________________________________________

    if rutaMasRapida: 
        
        """
         ****************  ALGORITMO DE RUTA MAS RAPIDA  ****************
         """
        
        print ("")
        print ("Escriba el destino:")
        destino = str(input())
        #Checkeo de que esta en el grafo
        if destino not in G.nodes():
            print("El nodo no esta en el grafo")
        else:
            
            origen = 'P1'
            
            
            
            #Nueva ventana
            width1 = 9
            height1 = 9
            width_height_1 = (width1, height1)
            plt.figure(3,figsize=width_height_1)
            plt.figure(3).canvas.set_window_title('Ruta más rápida del nodo [' + origen + '] al [' + destino + ']' ) 
            
            
            
            
            """
            ----------------------------------------------------------------------------------------------------------------------------------
            
            Se recorren los enlaces y se sustituye la distancia de este por el tiempo de rocorrerlo, en funcion de la formula:
            
                    tiempo_enlace = distancia_enlace / factor_subida_o_bajada
            
            (*) Donde factor_subida_o_bajada = FACTOR_SUBIDA_ESCALERAS o FACTOR_BAJADA_ESCALERAS o FACTOR_PLANOS
            
            ----------------------------------------------------------------------------------------------------------------------------------
            """
           
            for u, v, d in G.edges(data=True):
                if ( d['tipoEnlace'] == "escalera") and ( d['inclinacion'] == "+"  ):
                    d['weight'] = "{:.2f}".format( float( d['longitud'] ) / FACTOR_SUBIDA_ESCALERAS )
                elif ( d['tipoEnlace'] == "escalera" ) and ( d['inclinacion'] == "-"  ):
                    d['weight'] = "{:.2f}".format( float( d['longitud'] ) / FACTOR_BAJADA_ESCALERAS )
                else:
                    d['weight'] = "{:.2f}".format( float( d['longitud'] ) / FACTOR_PLANOS )
            
            
            
            
            
            
            
            elarge=[(u,v) for (u,v,d) in G.edges(data=True) ] # solid edge
            
             
            #Mismo grafico pero pintamos los nodos distinto
            # Retrieve the positions from graph nodes and save to a dictionary
            pos=nx.get_node_attributes(G,'pos')
            
            # Dibujamos los nodos del Grafo G
            nx.draw_networkx_nodes(G,pos,node_size=450, node_color=color_map)
            
             
            # Dibujamos los enlaces del Grafo G
            nx.draw_networkx_edges(G,pos,edgelist=elarge, width=2, edge_color='g', arrows = True)
             
            # Dibujamos los atributos del Grafo G
            nx.draw_networkx_labels(G,pos,font_size=12,font_family='sans-serif')
             
            
            
            
            
            # Cargamos el peso de los enlaces para poder mostarlo
            edge_labels =dict([((u, v), d['weight']) 
                               for u, v, d in G.edges(data=True)])
             
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
             
            plt.axis('off')

            
      
            
            
            #Dijkstra
            try:
                djk_Ruta = nx.dijkstra_path(G, source=origen, target=destino, weight=True)
            except nx.NetworkXNoPath:
                print("No existe ruta de: " + origen + " a " + destino)
                continue
            
            
            #Una vez obtenida la ruta más rapida, coloreamos los nodos seleccionados de color
            color_nodos_solucion = []
            for node in G:
                #Si esta en la ruta lo pinto de color 
                if str(node) in djk_Ruta:
                     color_nodos_solucion.append('lawngreen')
                else :
                     #print("aqui3")
                     color_nodos_solucion.append('grey')
                     
            
            
            nx.draw_networkx_nodes(G,pos,node_size=450, node_color=color_nodos_solucion)
            
            
            #plt.get_current_fig_manager().window.showMaximized()
            
            plt.text(0, -1.5, 'La ruta más rapida recomendada desde [' + origen + '] hasta  [' + destino + '] es la ruta que pasa por los nodos: ' + str(djk_Ruta), style='italic',
                    bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
            
            
            plt.show()
            
          
