'''
Created on 6 déc. 2018

@author: coline
'''

'''
Created on 10 oct. 2018

@author: Coline Gi
'''
import pickle
import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes.function import get_node_attributes
import os
import numpy as np

liste = ['5J7L_DA_191_3', '5J7L_DA_191_4', '5FDU_1A_301_1', '5J7L_DA_301_2', '5DM6_X_334_1', '5FDU_1A_334_2', '4V9F_0_335_1', '5J7L_DA_335_2', '3JCS_1_137_4', '4V88_A5_290_1', '4V88_A6_314_2', '5J7L_DA_218_3', '4V9F_0_251_2', '1FJG_A_62_8', '5J7L_DA_137_1', '4V9F_0_118_1', '4V9F_0_62_2', '5J7L_DA_271_2', '4V9F_0_224_1', '5DM6_X_197_1', '3GX5_A_138_6', '1FJG_A_317_2', '5J5B_BA_317_1', '1FJG_A_326_1', '5DM6_X_137_3', '5J5B_BA_314_1', '4V9F_0_134_6', '4V9F_0_328_1', '4V9F_0_197_2', '4V9F_0_62_16', '5J7L_DA_282_2', '4V88_A5_137_2', '5FDU_1A_224_3', '5J7L_DA_326_2']

def contient_sommet(sommet, graphe_commun, num ):
    for noeud in graphe_commun.nodes() :
        if noeud[num] == sommet :
            return True
    return False

def contient_arete(arete, graphe_commun, num):
    for edge in graphe_commun.edges() :
        if edge[0][num] == arete[0] and edge[1][num] == arete[1] or edge[1][num] == arete[0] and edge[0][num] == arete[1]   :
            return True
    return False

with open("fichier_affichage_isomorphisme_new.txt", 'w') as fichier :
#     with open("dico_graphe_epure_en_tout.pickle", 'rb') as fichier_graphe :
#         mon_depickler = pickle.Unpickler(fichier_graphe)
#         dico_graphe = mon_depickler.load()
    with open("dico_graphe_epure_en_tout_test.pickle", 'rb') as fichier_graphe :
        mon_depickler = pickle.Unpickler(fichier_graphe)
        dico_graphe = mon_depickler.load()
        with open("dico_graphe_epure_en_tout_test_sim.pickle", 'rb') as fichier_sim : 
            mon_depickler_sim = pickle.Unpickler(fichier_sim)
            dico_sim = mon_depickler_sim.load()
            
        for elt in dico_graphe.keys() :
                #elt = ('fichier_1FJG_A_48_8', 'fichier_5J5B_BA_48_23')
                
                enlever = False 
                for l in liste : 
                    if l in elt[0] or l in elt[1] :
                        enlever = True
                #print(enlever)
                
                if enlever == False :
                    if "_" + str(elt[0]) + "_" + str(elt[1]) + ".png" not in os.listdir("graphes_comparaison_new") :
                        GC = dico_graphe[elt].copy()
#             
#                         print(GC.nodes.data())
#                         
                        compteur = 0
#                         
                        fig, axs=plt.subplots(figsize=(10, 12), nrows=1, ncols=2)
#                         #fig=plt.figure()
#             
                        columns = 2
                        rows = 1
#                         
                        nom = ""
                        #elt = ('fichier_5FDU_1A_197_3', 'fichier_5DM6_X_48_9')
                        for element in elt :
                            
                            fig.suptitle('sim = '+str(round(dico_sim[elt],2)), fontsize=16)
                            fig.add_subplot(rows, columns, compteur%2+1)
                            #fig.axis('off')
                            #axs[compteur%2].xaxis.set_visible(False)
                            axs[compteur%2].axis("off")
                            axs[compteur%2].set_title(element)
                            
                            with open("graphes_extension/"+element+".pickle", 'rb') as fichier_entree :
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
                                                        fichier.write("probleme\n")
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
                                                        fichier.write("probleme\n")
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
                                                        fichier.write("probleme\n")
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
                                                        fichier.write("probleme\n")
                                                        print("probleme") 
                                                    
                                
                                for noeud in G.nodes() :
                                    fichier.write(str(noeud) + " " + str(G.nodes[noeud])+"\n")
                                for u,v,edata in G.edges(data=True) :
                                    fichier.write(str(u)+ "'" +str(v) + " " + str(edata["label"])+"\n")
                                
                                #fichier.write(str(G.nodes.data())+"\n")
                                #fichier.write(str(G.edges.data())+"\n")                
                                pos = get_node_attributes(G, 'coordonnees')
                                #print(pos)
                                
                                #plt.figure(figsize =(5,12))
                                           
                                red_edges = [(1,2),(2,1),(1,3),(3,1),(1,5),(5,1),(2,4),(4,2),(3,4),(4,3),(2,5),(5,2)]
                                green_edges = []
                                blue_edges = []
                                black_edges = []
                                weights = []
                                #black_edges = [edge for edge in G.edges() if edge not in red_edges]
                                for u,v,edata, in G.edges(data=True) :
                                    if (u,v) not in red_edges :
            #                             if contient_arete((u,v), GC, compteur%2) :
            #                                 orange_edges.append((u,v))
                                        if edata["label"] == "B53" :
                                            green_edges.append((u,v))
                                        elif edata["label"] == "CWW" :
                                            blue_edges.append((u,v)) 
                                        else :
                                            black_edges.append((u,v))
                                    
                                    if contient_arete((u,v), GC, compteur%2) :
                                        weights.append(3)
                                    else :
                                        weights.append(1)
                            
                                #edge_labels=dict([((u,v,),d["label"])for u,v,d in G.edges(data=True)])
                                #print(edge_labels)
                               # node_labels=dict([(u,(d["nt"], d["type"]))for u,d in G.nodes(data=True)])## if d["type"] != None])
                                node_labels=dict([(u, (d["type"], d["poids"]))for u,d in G.nodes(data=True) if d["type"] != None])
                                print(node_labels)
                                
                                orange_nodes = []
                                pink_nodes = []
                                for noeud in G.nodes() :
                                    if contient_sommet(noeud, GC, compteur%2) :
                                        orange_nodes.append(noeud)
                                    else :
                                        pink_nodes.append(noeud)
                                node_colors = ['pink' if node in pink_nodes else 'orange' for node in G.nodes()]
                                
                                
                                nx.draw_networkx_nodes(G, pos, node_size=150, node_color=node_colors)
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
                                #nx.draw_networkx_edge_labels(G,pos)
                                nx.draw_networkx_edges(G,pos,edge_color=edge_colors, width=weights)
                                #axs[compteur%2].set_axis_off()
                                #plt.savefig("graphes_extension/"+element[:len(element)-7]+".png") # save as png
                                #plt.savefig("graphes_extension/fichier_1FJG_A_48_8.png") # save as png
                                nom = nom + "_" +element
                                compteur = compteur+1
                                
                                
                                plt.axis('off')              
                        #plt.show()
                        if nom+".png" not in os.listdir("graphes_comparaison_new") :
                            plt.savefig("graphes_comparaison_new/"+nom+".png") # save as png
                        plt.clf()
                        plt.close()
                    
                
    