
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
'El Nivel 0 tiene Nodos de la puerta de enlace 00, 01, 02, 03'
G.add_weighted_edges_from(
    [
    ('00', '12', {'weight':15.0} ), ('00', '14', {'weight':15.0} ), ('00', '22' , {'weight':30.0} ), ('00', '24', {'weight':30.0} ),
    ('01', '02', {'weight':15.0}), ('01', '12', {'weight':10.0}),
    ('02', '01', {'weight':15.0}), ('02', '24', {'weight':10.0}),
    ('11', '12', {'weight':10.0}), ('11', '21', {'weight':12.0}),
    ('12', '00', {'weight':15.0}), ('12', '01', {'weight':10.0}), ('12', '11', {'weight':10.0}), ('12', '13', {'weight':10.0}),
    ('13', '12', {'weight':10.0}), ('13', '14', {'weight':10.0}), ('13', '23', {'weight':12.0}),
    ('14', '00', {'weight':15.0}), ('14', '02', {'weight':10.0}), ('14', '13', {'weight':10.0}), ('14', '15', {'weight':10.0}),
    ('15', '14', {'weight':10.0}), ('15', '25', {'weight':12.0}),
    ('21', '11', {'weight':12.0}), ('21', '22', {'weight':10.0}), ('21', '31', {'weight':20.0}),
    ('22', '00', {'weight':30.0}), ('22', '21', {'weight':10.0}), ('22', '23', {'weight':10.0}),
    ('23', '13', {'weight':12.0}), ('23', '22', {'weight':10.0}), ('23', '24', {'weight':10.0}), ('23', '32', {'weight':30.0}),
    ('24', '00', {'weight':30.0}), ('23', '22', {'weight':10.0}), ('24', '25', {'weight':10.0}),
    ('25', '15', {'weight':12.0}), ('25', '24', {'weight':10.0}), ('25', '33', {'weight':20.0}),
    ('31', '21', {'weight':20.0}), ('31', '32', {'weight':20.0}),
    ('32', '31', {'weight':20.0}), ('32', '23', {'weight':20.0}), ('32', '33', {'weight':20.0}),
    ('33', '32', {'weight':20.0}),('32', '25', {'weight':20.0}),
    ])

G.edges(data=True)

color_map = []
for node in G:
    print(str(node)[0] )
    if str(node)[0] == "0":
         #print("aqui 0")
         color_map.append('blue')
    elif str(node)[0] == "1":
         #print("aqui 1")
         color_map.append('green')
    elif str(node)[0] == "2":
         #print("aqui 2")
         color_map.append('yellow')
    else :
         #print("aqui3")
         color_map.append('pink')
         
    

red_edges = [('00', '12'), ('00', '14'), ('00', '22'), ('00', '24')]


     
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color = color_map, node_size = 500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color=color_map, arrows=True)
plt.show()

    
#pos =nx.get_node_attributes(G,'pos')
#nx.draw(G,pos)

#longitudes = nx.get_edge_attributes(G,'longitud')
#nx.draw_networkx_edge_labels(G,with_labels=True, node_color = color_map, edge_labels = longitudes)
#nx.draw(G, node_color = color_map,with_labels=True, arrows=True)
#plt.show()


