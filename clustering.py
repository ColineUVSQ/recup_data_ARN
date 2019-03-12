'''
Created on 18 déc. 2018

@author: coline
'''
import pickle
import networkx as nx
import os
from recup_data.calcul_sim import calcul_sim_non_cov_sans_motif
from recup_data.calcul_sim import calcul_sim_non_cov_avec_motif
import attr
import csv

liste = ['5J7L_DA_191_3', '5J7L_DA_191_4', '5FDU_1A_301_1', '5J7L_DA_301_2', '5DM6_X_334_1', '5FDU_1A_334_2', '4V9F_0_335_1', '5J7L_DA_335_2', '3JCS_1_137_4', '4V88_A5_290_1', '4V88_A6_314_2', '5J7L_DA_218_3', '4V9F_0_251_2', '1FJG_A_62_8', '5J7L_DA_137_1', '4V9F_0_118_1', '4V9F_0_62_2', '5J7L_DA_271_2', '4V9F_0_224_1', '5DM6_X_197_1', '3GX5_A_138_6', '1FJG_A_317_2', '5J5B_BA_317_1', '1FJG_A_326_1', '5DM6_X_137_3', '5J5B_BA_314_1', '4V9F_0_134_6', '4V9F_0_328_1', '4V9F_0_197_2', '4V9F_0_62_16', '5J7L_DA_282_2', '4V88_A5_137_2', '5FDU_1A_224_3', '5J7L_DA_326_2']


def construction_graphe_complet_pondere():
    graphe_complet = nx.Graph()
    i = 0
    
    for fic in os.listdir("graphes_extension") :
        if "pickle" in fic :
            #print(fic)
            graphe_complet.add_node(i, nom=fic[8:len(fic)-7])
            i = i+1
    
    print(graphe_complet.nodes.data())        
    with open("dico_graphe_epure_en_tout.pickle", 'rb') as fichier_graphe :
        mon_depickler = pickle.Unpickler(fichier_graphe)
        dico_graphe = mon_depickler.load()
        
        
        for cle in dico_graphe.keys() :
            element1 = cle[0]
            element2 = cle[1]
            #print(element1)
            #print(element2)
            
            enlever = False 
            for elt in liste : 
                if elt in element1 or elt in element2 :
                    enlever = True
            #print(enlever)
            
            if enlever == False :
                        
                with open("graphes_extension/"+element1+".pickle", 'rb') as fichier_graphe_1 :
                    mon_depickler_1 = pickle.Unpickler(fichier_graphe_1)
                    graphe1 = mon_depickler_1.load()
                    
                    with open("graphes_extension/"+element2+".pickle", 'rb') as fichier_graphe_2 :
                        mon_depickler_2 = pickle.Unpickler(fichier_graphe_2)
                        graphe2 = mon_depickler_2.load()
        
                        sim = calcul_sim_non_cov_sans_motif(graphe1, graphe2, dico_graphe[cle])
                        
                        num_1 = -1
                        num_2 = -1
                        
                        for noeud, attr in graphe_complet.nodes(data="nom") :
                            #print(attr)
                            if attr == element1[8:] :
                                num_1 = noeud
                            elif attr == element2[8:] :
                                num_2 = noeud
                        
                        graphe_complet.add_edge(num_1, num_2, poids = float(sim[0]))     
    
    with open("graphe_complet_pondere_sim.pickle", 'wb') as fichier_graphe_complet :
        mon_pickler_complet = pickle.Pickler(fichier_graphe_complet)
        mon_pickler_complet.dump(graphe_complet)
    return graphe_complet

def premier_clustering(graphe_complet, val_min, fichier_ecriture, depart, typ):
    with open("sim_"+depart+"_"+typ+".pickle", 'rb') as fichier_sim :
        mon_depickler = pickle.Unpickler(fichier_sim)
        dico_sim = mon_depickler.load()
        with open("fichier_csv_sans_motif_"+depart+"_"+typ+"_"+str(val_min)+".csv", 'w', newline='') as fichier_csv :
            csvwriter = csv.writer(fichier_csv, delimiter=',')
            
            tab_csv = []
            
            graphe_sortie = nx.Graph(graphe_complet)
        #     print(graphe_sortie.number_of_edges())
            a_enlever = []
            for u,v in graphe_sortie.edges() :
                if (graphe_sortie.nodes[u]["nom"], graphe_sortie.nodes[v]["nom"]) in dico_sim.keys() :
                    if float(dico_sim[(graphe_sortie.nodes[u]["nom"], graphe_sortie.nodes[v]["nom"])][0]) < val_min :
                        a_enlever.append((u,v))
                else :
                    if float(dico_sim[(graphe_sortie.nodes[v]["nom"], graphe_sortie.nodes[u]["nom"])][0]) < val_min :
                        a_enlever.append((u,v))
        #     print(a_enlever)
            for elt in a_enlever :
                graphe_sortie.remove_edge(elt[0], elt[1])
        #     print(graphe_sortie.number_of_edges())
               
            ## recherche composantes connexes 
            deja_vu = []
            composantes_connexes = []
            for noeud in graphe_sortie.nodes() :
                if noeud not in deja_vu :
                    composantes_connexes.append([noeud])
                    deja_vu.append(noeud)
                     
                    #parcours en largeur
                    file_sommets = [noeud]
                    while len(file_sommets) > 0:
                        sommet_courant = file_sommets.pop(0)
                        enfants_courant = graphe_sortie[sommet_courant]  
                        #print(len(file_sommets))
                        for enfant in enfants_courant:
                            if enfant not in deja_vu :
                                composantes_connexes[len(composantes_connexes)-1].append(enfant)
                                file_sommets.append(enfant)
                            deja_vu.append(enfant)
        #                 print("sommet_courant")
        #                 print(sommet_courant)
        #                 print(file_sommets)
            print("composantes connexes")
            print(composantes_connexes)
            print(len(composantes_connexes))
            
            with open("composantes_connexes_"+depart+"_"+typ+"_"+str(i)+".pickle", 'wb') as fichier_comp:
                mon_pickler = pickle.Pickler(fichier_comp)
                mon_pickler.dump(composantes_connexes)
            
            fichier_ecriture.write("Nombre de comp conn :" +str(len(composantes_connexes))+'\n')
            fichier_ecriture.write(str(composantes_connexes))
            fichier_ecriture.write("\n")
            fichier_ecriture.write("Tailles \n")
            tab_csv.append(len(composantes_connexes))
            
            tab_temp_taille = []
            tab_temp_densite = []
            for composante in composantes_connexes :
                tab_temp_taille.append(len(composante))
                if len(composante) > 1 :
                    tab_temp_densite.append(graphe_sortie.subgraph(composante).number_of_edges()/((len(composante)*(len(composante)-1))/2))
                else :
                    tab_temp_densite.append(None)
                fichier_ecriture.write(str(len(composante)) + '\n')
                
                if len(composante) < 10 :
                    print("nombre d'aretes")
                    print(graphe_sortie.subgraph(composante).number_of_edges())
                    print(graphe_sortie.subgraph(composante).number_of_edges()/graphe_complet.number_of_edges())
                    print(composante)
                    print("taille composante")
                    print(len(composante))
                    for elt in composante :
                        print(graphe_sortie.nodes[elt]["nom"])
                        fichier_ecriture.write(str(graphe_sortie.nodes[elt]["nom"])+ '\n')
                        
                    for u,v in graphe_sortie.subgraph(composante).edges() :
                        fichier_ecriture.write(str(graphe_sortie.nodes[u]["nom"])+ ' ')
                        fichier_ecriture.write(str(graphe_sortie.nodes[v]["nom"])+ ' ')
                        
                        cle1 = graphe_sortie.subgraph(composante).nodes[u]["nom"]
                        cle2 = graphe_sortie.subgraph(composante).nodes[v]["nom"]
                        if (cle1, cle2) in dico_sim.keys() :
                            fichier_ecriture.write(str(dico_sim[(cle1,cle2)][0]) + '\n')
                        else :
                            fichier_ecriture.write(str(dico_sim[(cle2,cle1)][0]) + '\n')
                        
                    
                somme_sim = 0
                nombre = 0
                for u,v in graphe_sortie.edges() :
                    if u in composante and v in composante :
                        cle1 = graphe_sortie.nodes[u]["nom"]
                        cle2 = graphe_sortie.nodes[v]["nom"]
                        if (cle1, cle2) in dico_sim.keys() :
                            somme_sim += dico_sim[(cle1,cle2)][0]
                        else :
                            somme_sim += dico_sim[(cle2,cle1)][0]
                        nombre += 1
                if nombre != 0 :
                    moy_sim = somme_sim/nombre
                else :
                    moy_sim = None
                
                fichier_ecriture.write("Moyenne sim : "+ str(moy_sim) + "\n")
    #             tab_csv.append(len(composante))
    #             tab_csv.append(graphe_sortie.subgraph(composante).number_of_edges()/graphe_complet.number_of_edges())
                dico = {}
                for elt in composante :
                    if elt not in dico.keys() :
                        dico.update({elt : 1})
                    else :
                        dico[elt]+=1
                     
        #             print("elt")
        #             print(elt)
        #             print("voisin")
                    for voisin in graphe_sortie[elt] :
        #                 print(voisin)
                        if voisin not in composante : 
                            print("probleme")
                        
        #         print(dico)
        #         print(len(dico))
            for elt in tab_temp_taille :
                tab_csv.append(elt)
            for elt in tab_temp_densite :
                tab_csv.append(elt)
            
            csvwriter.writerow(tab_csv)



if __name__ == '__main__':
    graphe_complet = construction_graphe_complet_pondere() 
    #print(graphe_complet.edges.data()) 
    print(graphe_complet.number_of_nodes())
    print(graphe_complet.number_of_edges())
    
#     clique_number = nx.graph_clique_number(graphe_complet, cliques=None)
#     print(clique_number)
    
#     compteur = 0
#     for noeud in graphe_complet.nodes() :
#         print(graphe_complet.nodes[noeud]["nom"])
#         print(len(graphe_complet[noeud]))
#         if len(graphe_complet[noeud]) > 94 :
#             compteur += 1 
#     print(compteur)
#     cliques = nx.find_cliques(graphe_complet)
#     taille_max = 0
#     clique_max = []
#     for elt in cliques :
#         if taille_max < len(elt) :
#             taille_max = len(elt)
#             clique_max = elt 
#     print(taille_max)
#     print(clique_max)
#     
#     with open("fichier_petits_groupes_sans_motif.txt", 'w') as fichier_ecriture :
#         i = 0.1
#         while i <= 1.0 :
#             print(i)
#             fichier_ecriture.write("Valeur: "+str(i)+"\n")
#             premier_clustering(graphe_complet, i, fichier_ecriture)
#             i = i+0.1
                
    with open("fichier_petits_groupes_sans_motif_graphe_global_non_cov.txt", 'w') as fichier_ecriture :
        i = 0.1
        while i <= 1.0 :
            print(i)
            fichier_ecriture.write("Valeur: "+str(i)+"\n")
            premier_clustering(graphe_complet, i, fichier_ecriture, "graphe_global", "non_cov")
            i = i+0.1 
            
    
     
    print("ramousnif")

                        