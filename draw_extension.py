'''
Created on 10 oct. 2018

@author: Coline Gi
'''
import pickle
import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes.function import get_node_attributes
import os

with open("fichier_affichage_version3_avec_boucles_test_avec_digraph_plus_type_de_liens.txt", 'w') as fichier :
    for element in os.listdir('graphes_extension/'):
        if "pickle" in element :
# element = "fichier_3JCS_1_48_18.pickle"
            with open("graphes_extension/"+element, 'rb') as fichier_entree :
                print(element)
                
                mon_depickler = pickle.Unpickler(fichier_entree)
                G = mon_depickler.load()
                print(G.nodes.data())
                
                nx.set_node_attributes(G, (33,33), "coordonnees")
                G.nodes[1]["coordonnees"] = (0.0,0.5)
                G.nodes[2]["coordonnees"] = (2.0,0.5)
                G.nodes[3]["coordonnees"] = (0.0,0.0)
                G.nodes[4]["coordonnees"] = (2.0,0.0)
                G.nodes[5]["coordonnees"] = (3.0,0.5)
                 
                fichier.write(str(element)+"\n") 
                fichier.write(str(G.number_of_nodes())+"\n") 
                #print(G.nodes())
                
                for noeud in G.nodes() :
                    #voisins = G[noeud]
                    coordonnees_noeud = G.nodes[noeud]["coordonnees"]
                    for pred in G.predecessors(noeud) :
                        if G.nodes[pred]["coordonnees"] == (33,33) :
                            coordonnees = []
                            for node in G.nodes() :
                                coordonnees.append(G.nodes[node]["coordonnees"])
                            for edge in G[pred][noeud] :
                                if G[pred][noeud][edge]["label"] == "B53" :
                                    if (coordonnees_noeud[0], coordonnees_noeud[1]-0.5) not in coordonnees :
                                        G.nodes[pred]["coordonnees"] = (coordonnees_noeud[0], coordonnees_noeud[1]-0.5)
                                    elif (coordonnees_noeud[0], coordonnees_noeud[1]+0.5) not in coordonnees :
                                        G.nodes[pred]["coordonnees"] = (coordonnees_noeud[0], coordonnees_noeud[1]+0.5)
                                    elif (coordonnees_noeud[0]-0.5, coordonnees_noeud[1]) not in coordonnees :
                                        G.nodes[pred]["coordonnees"] = (coordonnees_noeud[0]-0.5, coordonnees_noeud[1])
                                    elif (coordonnees_noeud[0]+0.5, coordonnees_noeud[1]) not in coordonnees :
                                        G.nodes[pred]["coordonnees"] = (coordonnees_noeud[0]+0.5, coordonnees_noeud[1])
                                    elif (coordonnees_noeud[0]+0.25, coordonnees_noeud[1]+0.25) not in coordonnees:
                                        G.nodes[pred]["coordonnees"] = (coordonnees_noeud[0]+0.25, coordonnees_noeud[1]+0.25)
                                    elif (coordonnees_noeud[0]-0.25, coordonnees_noeud[1]) not in coordonnees: 
                                        G.nodes[pred]["coordonnees"] = (coordonnees_noeud[0]-0.25, coordonnees_noeud[1])
                                    else :
                                        #fichier.write("probleme\n")
                                        print("probleme")
                                else :
                                    if (coordonnees_noeud[0]-0.75, coordonnees_noeud[1]) not in coordonnees :
                                        G.nodes[pred]["coordonnees"] = (coordonnees_noeud[0]-0.75, coordonnees_noeud[1])
                                    elif (coordonnees_noeud[0]+0.75, coordonnees_noeud[1]) not in coordonnees :
                                        G.nodes[pred]["coordonnees"] = (coordonnees_noeud[0]+0.75, coordonnees_noeud[1])
                                    elif (coordonnees_noeud[0], coordonnees_noeud[1]-0.75) not in coordonnees :
                                        G.nodes[pred]["coordonnees"] = (coordonnees_noeud[0], coordonnees_noeud[1]-0.75)
                                    elif (coordonnees_noeud[0], coordonnees_noeud[1]+0.75) not in coordonnees :
                                        G.nodes[pred]["coordonnees"] = (coordonnees_noeud[0], coordonnees_noeud[1]+0.75)
                                    elif (coordonnees_noeud[0]+0.25, coordonnees_noeud[1]+0.25) not in coordonnees:
                                        G.nodes[pred]["coordonnees"] = (coordonnees_noeud[0]+0.25, coordonnees_noeud[1]+0.25)
                                    elif (coordonnees_noeud[0]-0.25, coordonnees_noeud[1]) not in coordonnees: 
                                        G.nodes[pred]["coordonnees"] = (coordonnees_noeud[0]-0.25, coordonnees_noeud[1])
                                    else : 
                                        #fichier.write("probleme\n")
                                        print("probleme") 
                    for succ in G.successors(noeud) :
                        if G.nodes[succ]["coordonnees"] == (33,33) :
                            coordonnees = []
                            for node in G.nodes() :
                                coordonnees.append(G.nodes[node]["coordonnees"])
                            for edge in G[noeud][succ] :
                                if G[noeud][succ][edge]["label"] == "B53" :
                                    if (coordonnees_noeud[0], coordonnees_noeud[1]-0.5) not in coordonnees :
                                        G.nodes[succ]["coordonnees"] = (coordonnees_noeud[0], coordonnees_noeud[1]-0.5)
                                    elif (coordonnees_noeud[0], coordonnees_noeud[1]+0.5) not in coordonnees :
                                        G.nodes[succ]["coordonnees"] = (coordonnees_noeud[0], coordonnees_noeud[1]+0.5)
                                    elif (coordonnees_noeud[0]-0.5, coordonnees_noeud[1]) not in coordonnees :
                                        G.nodes[succ]["coordonnees"] = (coordonnees_noeud[0]-0.5, coordonnees_noeud[1])
                                    elif (coordonnees_noeud[0]+0.5, coordonnees_noeud[1]) not in coordonnees :
                                        G.nodes[succ]["coordonnees"] = (coordonnees_noeud[0]+0.5, coordonnees_noeud[1])
                                    elif (coordonnees_noeud[0]+0.25, coordonnees_noeud[1]+0.25) not in coordonnees:
                                        G.nodes[succ]["coordonnees"] = (coordonnees_noeud[0]+0.25, coordonnees_noeud[1]+0.25)
                                    elif (coordonnees_noeud[0]-0.25, coordonnees_noeud[1]) not in coordonnees: 
                                        G.nodes[succ]["coordonnees"] = (coordonnees_noeud[0]-0.25, coordonnees_noeud[1])
                                    else :
                                        #fichier.write("probleme\n")
                                        print("probleme")
                                else :
                                    if (coordonnees_noeud[0]-0.75, coordonnees_noeud[1]) not in coordonnees :
                                        G.nodes[succ]["coordonnees"] = (coordonnees_noeud[0]-0.75, coordonnees_noeud[1])
                                    elif (coordonnees_noeud[0]+0.75, coordonnees_noeud[1]) not in coordonnees :
                                        G.nodes[succ]["coordonnees"] = (coordonnees_noeud[0]+0.75, coordonnees_noeud[1])
                                    elif (coordonnees_noeud[0], coordonnees_noeud[1]-0.75) not in coordonnees :
                                        G.nodes[succ]["coordonnees"] = (coordonnees_noeud[0], coordonnees_noeud[1]-0.75)
                                    elif (coordonnees_noeud[0], coordonnees_noeud[1]+0.75) not in coordonnees :
                                        G.nodes[succ]["coordonnees"] = (coordonnees_noeud[0], coordonnees_noeud[1]+0.75)
                                    elif (coordonnees_noeud[0]+0.25, coordonnees_noeud[1]+0.25) not in coordonnees:
                                        G.nodes[succ]["coordonnees"] = (coordonnees_noeud[0]+0.25, coordonnees_noeud[1]+0.25)
                                    elif (coordonnees_noeud[0]-0.25, coordonnees_noeud[1]) not in coordonnees: 
                                        G.nodes[succ]["coordonnees"] = (coordonnees_noeud[0]-0.25, coordonnees_noeud[1])
                                    else : 
                                        #fichier.write("probleme\n")
                                        print("probleme") 
                                    
                
                for noeud in G.nodes() :
                    fichier.write(str(noeud) + " " + str(G.nodes[noeud])+"\n")
                for u,v,edata in G.edges(data=True) :
                    fichier.write(str(u)+ "'" +str(v) + " " + str(edata["label"])+"\n")
                              
                pos = get_node_attributes(G, 'coordonnees')
                #print(pos)
                
                plt.figure(figsize =(5,12))
                           
                red_edges = [(1,2),(2,1),(1,3),(3,1),(1,5),(5,1),(2,4),(4,2),(3,4),(4,3),(2,5),(5,2)]
                green_edges = []
                blue_edges = []
                black_edges = []
                #black_edges = [edge for edge in G.edges() if edge not in red_edges]
                for u,v,edata, in G.edges(data=True) :
                    if (u,v) not in red_edges :
                        if edata["label"] == "B53" :
                            green_edges.append((u,v))
                        elif edata["label"] == "CWW" :
                            blue_edges.append((u,v)) 
                        else :
                            black_edges.append((u,v))

                #edge_labels=dict([((u,v,),d["label"])for u,v,d in G.edges(data=True)])
                #print(edge_labels)
               # node_labels=dict([(u,(d["nt"], d["type"]))for u,d in G.nodes(data=True)])## if d["type"] != None])
                node_labels=dict([(u, (d["type"], d["poids"])) for u,d in G.nodes(data=True) if d["type"] != None ]) #else (u, (u)) for u,d in G.nodes(data=True) ])
                #node_labels=dict([(u, (u)) for u,d in G.nodes(data=True) ])
                print(node_labels)
                nx.draw_networkx_nodes(G, pos, node_size=150, node_color='pink')
                            #nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
                            #           node_color = values, node_size = 500)
                nx.draw_networkx_labels(G, pos, labels = node_labels)
                #nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', edge_labels = edge_labels)
                #nx.draw_networkx_edges(G, pos, edgelist=blue_edges, edge_color='b', edge_labels = edge_labels)
                #nx.draw_networkx_edges(G, pos, edgelist=green_edges, edge_color='g', edge_labels = edge_labels)
                #nx.draw_networkx_edges(G, pos, edgelist=black_edges, edge_labels = edge_labels)
                
                edge_colors = ['black' if edge in black_edges else 'red' if edge in red_edges else 'blue' if edge in blue_edges else 'green' for edge in G.edges()]
                print(black_edges)
                print(red_edges)
                print(edge_colors)
                #edge_labels = dict([((u,v), (d["long_range"])) for u,v,d in G.edges(data=True)])
                #nx.draw_networkx_edge_labels(G,pos, edge_labels=edge_labels)
                nx.draw_networkx_edges(G,pos,edge_color=edge_colors)
                plt.axis('off')
                plt.savefig("graphes_extension/"+element[:len(element)-7]+".png") # save as png
                #plt.savefig("graphes_extension/fichier_1FJG_A_48_8.png") # save as png
                #plt.show()
                plt.clf()
                plt.close()
                
    