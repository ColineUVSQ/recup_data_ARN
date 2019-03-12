'''
Created on 10 déc. 2018

@author: coline
'''
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import os



def calcul_sim_raymond_avec_motif(graphe1, graphe2, graphe_commun):
    
    sim = ((graphe_commun.number_of_nodes() + graphe_commun.number_of_edges())*(graphe_commun.number_of_nodes() + graphe_commun.number_of_edges()))/((graphe1.number_of_nodes()+graphe1.number_of_edges())*(graphe2.number_of_nodes()+graphe2.number_of_edges()))
    
    return sim

def calcul_sim_raymond_sans_motif(graphe1, graphe2, graphe_commun):
    
    sim = ((graphe_commun.number_of_nodes() - 5 + graphe_commun.number_of_edges()-4)*(graphe_commun.number_of_nodes()-5 + graphe_commun.number_of_edges()-4))/((graphe1.number_of_nodes()-5+graphe1.number_of_edges()-4)*(graphe2.number_of_nodes()-5+graphe2.number_of_edges()-4))
    
    return sim

def calcul_sim_raymond_non_cov_avec_motif(graphe1, graphe2, graphe_commun) :
    compteur_arc = 0
    for (u, v, keys, t) in graphe1.edges(data="label", keys = True) :
        if t == "B53" :
            compteur_arc += 1
    compteur_arete_1 = (graphe1.number_of_edges() - compteur_arc)/2
    
    compteur_arc = 0
    for (u, v, keys, t) in graphe2.edges(data="label", keys = True) :
        if t == "B53" :
            compteur_arc += 1
    compteur_arete_2 = (graphe2.number_of_edges() - compteur_arc)/2
    
    
    compteur_arc = 0
    for (u, v, keys, t) in graphe_commun.edges(data="type", keys = True) :
        if t == "COV" :
            compteur_arc += 1
    compteur_arete_commun = graphe_commun.number_of_edges() - compteur_arc
    
    sim = ((graphe_commun.number_of_nodes() + compteur_arete_commun)*(graphe_commun.number_of_nodes() + compteur_arete_commun))/((graphe1.number_of_nodes()+compteur_arete_1)*(graphe2.number_of_nodes()+compteur_arete_2))
    
    return sim

def calcul_sim_raymond_non_cov_sans_motif(graphe1, graphe2, graphe_commun) :
    compteur_arc = 0
    for (u, v, keys, t) in graphe1.edges(data="label", keys = True) :
        if t == "B53" :
            compteur_arc += 1
    compteur_arete_1 = (graphe1.number_of_edges() - compteur_arc)/2 - 4
    
    compteur_arc = 0
    for (u, v, keys, t) in graphe2.edges(data="label", keys = True) :
        if t == "B53" :
            compteur_arc += 1
    compteur_arete_2 = (graphe2.number_of_edges() - compteur_arc)/2 - 4
    
    
    compteur_arc = 0
    for (u, v, keys, t) in graphe_commun.edges(data="type", keys = True) :
        if t == "COV" :
            compteur_arc += 1
    compteur_arete_commun = graphe_commun.number_of_edges() - compteur_arc -4
    
    sim = ((graphe_commun.number_of_nodes() - 5 + compteur_arete_commun)*(graphe_commun.number_of_nodes()-5 + compteur_arete_commun))/((graphe1.number_of_nodes()-5+compteur_arete_1)*(graphe2.number_of_nodes()-5+compteur_arete_2))
    
    return sim

def calcul_sim_non_cov_avec_motif(graphe1, graphe2, graphe_commun):
    
    compteur_arc = 0
    for (u, v, keys, t) in graphe1.edges(data="label", keys = True) :
        if t == "B53" :
            compteur_arc += 1

    compteur_arete_1 = (graphe1.number_of_edges() - compteur_arc)/2
#     if element1 == "fichier_5DM6_X_197_1" and element2 == "fichier_5DM6_X_48_9" :
#         print(compteur_arc)
    
    
    compteur_arc = 0
    for (u, v, keys, t) in graphe2.edges(data="label", keys = True) :
        if t == "B53" :
            compteur_arc += 1
    compteur_arete_2 = (graphe2.number_of_edges() - compteur_arc)/2
#     if element1 == "fichier_5DM6_X_197_1" and element2 == "fichier_5DM6_X_48_9" :
#         print(compteur_arc)

    compteur_arc = 0
    for (u, v, keys, t) in graphe_commun.edges(data="type", keys = True) :
        if t == "COV" :
            compteur_arc += 1
    compteur_arete_commun = graphe_commun.number_of_edges() - compteur_arc
    

    
    
#     if element1 == "fichier_5DM6_X_197_1" and element2 == "fichier_5DM6_X_48_9" :
#         print(compteur_arete_commun)
#         print(compteur_arete_1)
#         print(compteur_arete_2)
    
#     print(compteur_arete_1)
#     print(compteur_arete_2)
#     print(compteur_arete_commun)
    
    sim = compteur_arete_commun/max(compteur_arete_1, compteur_arete_2)
    return sim, compteur_arete_commun


def calcul_sim_non_cov_sans_motif(graphe1, graphe2, graphe_commun):
    compteur_arc = 0
    for (u, v, keys, t) in graphe1.edges(data="label", keys = True) :
        if t == "B53" :
            compteur_arc += 1

    compteur_arete_1 = (graphe1.number_of_edges() - compteur_arc)/2 - 4

    
    compteur_arc = 0
    for (u, v, keys, t) in graphe2.edges(data="label", keys = True) :
        if t == "B53" :
            compteur_arc += 1
    compteur_arete_2 = (graphe2.number_of_edges() - compteur_arc)/2 - 4


    compteur_arc = 0
    for (u, v, keys, t) in graphe_commun.edges(data="type", keys = True) :
        if t == "COV" :
            compteur_arc += 1
    compteur_arete_commun = graphe_commun.number_of_edges() - compteur_arc - 4

    if max(compteur_arete_1, compteur_arete_2) > 0 :
        sim = compteur_arete_commun/max(compteur_arete_1, compteur_arete_2)
    else :
        sim = 0.0
    return sim, compteur_arete_commun, compteur_arete_1, compteur_arete_2

def calcul_sim_non_cov_sans_motif_par_chaine(graphe1, graphe2, graphe_commun, chaines_1, chaines_2, chaines_commun, i):
    
    compteur_arete_1 = 0
    for (u, v, t) in graphe1.edges(data="label") :
        if (u in chaines_1[i] and v in chaines_1[i]) :
            if t != 'B53' :
                print((u,v))
                compteur_arete_1 += 1
                
#     if i == 2 or i == 3 :
#         compteur_arete_1 = compteur_arete_1 - 2
#     else :
#         compteur_arete_1 = compteur_arete_1 - 4
    compteur_arete_1 = compteur_arete_1/2
#     if element1 == "fichier_5DM6_X_197_1" and element2 == "fichier_5DM6_X_48_9" :

    compteur_arete_2 = 0
    for (u, v, t) in graphe2.edges(data="label") :
        if (u in chaines_2[i] and v in chaines_2[i]) :
            if t != 'B53' :
                compteur_arete_2 += 1
#     if i == 2 or i == 3 :
#         compteur_arete_2 = compteur_arete_2 - 2
#     else :
#         compteur_arete_2 = compteur_arete_2 - 4
    compteur_arete_2 = compteur_arete_2/2
#     if element1 == "fichier_5DM6_X_197_1" and element2 == "fichier_5DM6_X_48_9" :
    
    compteur_arete_commun = 0
    for (u, v, t) in graphe_commun.edges(data="type") :
        if (u in chaines_commun[i] and v in chaines_commun[i]) :
            if t != 'COV' :
                compteur_arete_commun += 1
#     if i == 2 or i == 3 :
#         compteur_arete_commun = compteur_arete_commun - 1
#     else :
#         compteur_arete_commun = compteur_arete_commun - 2
        
    #compteur_arete_commun = compteur_arete_commun/2
    
#     if element1 == "fichier_5DM6_X_197_1" and element2 == "fichier_5DM6_X_48_9" :
#         print(compteur_arete_commun)
#         print(compteur_arete_1)
#         print(compteur_arete_2)
    
#     print(compteur_arete_1)
#     print(compteur_arete_2)
#     print(compteur_arete_commun)
    if max(compteur_arete_1, compteur_arete_2) > 0 :
        sim = compteur_arete_commun/max(compteur_arete_1, compteur_arete_2)
    else :
        sim = 0.0
    return sim, compteur_arete_1, compteur_arete_2, compteur_arete_commun

def calcul_sommets_aretes_grands_graphes(graphe):
    
    somme_aretes = 0
    for u,v,data in graphe.edges(data=True) :
        if data["label"] != "B53" :
            somme_aretes += 1
    somme_aretes = somme_aretes/2 - 4
    
    return somme_aretes + graphe.number_of_nodes() - 5

def calcul_sommets_aretes_grands_graphes_commun(graphe):
    somme_aretes = 0
    for u,v,data in graphe.edges(data=True) :
        if data["type"] != "COV" :
            somme_aretes += 1
    somme_aretes = somme_aretes - 4
    
    return somme_aretes + graphe.number_of_nodes() - 5
    

##Calcul de la somme des poids des sommets et des aretes avec nouvelle metrique
def calcul_sommets_aretes_graphe(graphe, cle):
    somme_sommets = 0
    for noeud, data in graphe.nodes(data=True) :
        if data["type"] == 1 : ## si de type 1 on multiplie par le coeff 3
            if len(graphe[noeud]) <= 1 :
                somme_sommets += 3*data["poids"] ## cas ou le sommet de type 1 est lie a un nt qui nest pas present dans le graphe
            else  :
                voisin = -1
                for u,v, label in graphe.edges(data="label") :
                    if noeud == u or noeud == v :
                        if label != 'B53' :
                            if u == noeud :
                                voisin = v
                            if v == noeud :
                                voisin = u
                try :
                    if graphe.nodes[voisin]["type"] == 1 :            
                        somme_sommets += 3*data["poids"]/2 ## cas ou le sommet de type 1 est lie a un sommet qui est present dans le graphe et qui est aussi de type 1
                    else :
                        somme_sommets += data["poids"] 
                except KeyError :
                    with open("fichier_pas_bon.txt", 'a') as f :
                        f.write(str(cle) + "\n")
        else :
            somme_sommets += data["poids"]
            
    somme_sommets -= 5

    compteur_arete = 0
    for u,v, data in graphe.edges(data=True) :
        if data["label"] != 'B53' and (graphe.nodes[u]["type"] != 1 or graphe.nodes[v]["type"] != 1):
            compteur_arete += 1
    compteur_arete = compteur_arete/2 - 4
    

#     print(somme_sommets)
#     print(compteur_arete)
    
    return somme_sommets + compteur_arete

def calcul_sommets_graphe_commun(graphe1, graphe2, graphe_commun, cle):
    somme_sommets = 0
    for noeud in graphe_commun.nodes() :
        
        if graphe1.nodes[noeud[0]]["type"] == 1 and graphe2.nodes[noeud[1]]["type"] == 1 :
            if len(graphe1[noeud[0]]) <= 1 and len(graphe2[noeud[1]]) <= 1  : ## cas ou les deux sont des helices isolees du reste du graphe
                somme_sommets += 3*min(graphe1.nodes[noeud[0]]["poids"], graphe2.nodes[noeud[1]]["poids"])
#                 if cle[0] == "fichier_5J7L_DA_50_21" and cle[1] == "fichier_5J7L_DA_48_20" :
#                     print(noeud)
            else :
                if len(graphe1[noeud[0]]) == 2 and len(graphe2[noeud[1]]) == 2 : 
                    voisin = None
                    for u,v, data in graphe_commun.edges(data=True) :
                        if data["type"] == "CAN" :
                            if u == noeud :
                                voisin = v
                            if v == noeud :
                                voisin = u        
                    if voisin != None : ## cas ou les deux sont des helices au sein du graphe, entre les memes chaines
                        somme_sommets += 3*min(graphe1.nodes[noeud[0]]["poids"], graphe2.nodes[noeud[1]]["poids"])/2
                    else : ## cas ou les deux sont des helices au sein du graphe, pas entre les memes chaines
                        somme_sommets += min(graphe1.nodes[noeud[0]]["poids"], graphe2.nodes[noeud[1]]["poids"])
#                         if cle[0] == "fichier_4V9F_0_30_4" and cle[1] == "fichier_4V9F_0_48_21" :
                        #print("probleme")
#                             print(noeud)
#                             print(len(graphe1[noeud[0]]))
#                             print(len(graphe2[noeud[1]]))
#                         with open("fichier_pas_bon.txt", 'a') as f :
#                             f.write(str(cle) + "\n")
                        
                else : ## cas ou l une est une helice isolee l autre une helice au sein du graphe
                    somme_sommets += min(graphe1.nodes[noeud[0]]["poids"], graphe2.nodes[noeud[1]]["poids"])
            
        elif graphe1.nodes[noeud[0]]["type"] == 0 and graphe2.nodes[noeud[1]]["type"] == 0 :
            somme_sommets += min(graphe1.nodes[noeud[0]]["poids"], graphe2.nodes[noeud[1]]["poids"])
            
        else :
            somme_sommets += 1
    somme_sommets -= 5
    
    
    compteur_arete = 0    
    for noeud1,noeud2,typ in graphe_commun.edges(data="type") :
        if typ != 'COV' and (graphe1.nodes[noeud1[0]]["type"] != 1 and graphe1.nodes[noeud2[0]]["type"] != 1 and graphe2.nodes[noeud1[1]]["type"] != 1 and graphe2.nodes[noeud2[1]]["type"] != 1):
            compteur_arete += 1
#             if cle[0] == "fichier_5J7L_DA_50_21" and cle[1] == "fichier_5J7L_DA_48_20" :
#                 print(noeud1)
#                 print(noeud2)
    compteur_arete -= 4    
    
#     print(somme_sommets)
#     print(compteur_arete)
    
    return somme_sommets + compteur_arete


def calcul_sim_avec_poids(graphe1, graphe2, graphe_commun, cle):
    poids_sommets_aretes_1 = calcul_sommets_aretes_graphe(graphe1, cle)
    poids_sommets_aretes_2 = calcul_sommets_aretes_graphe(graphe2, cle)
    poids_sommets_aretes_commun = calcul_sommets_graphe_commun(graphe1, graphe2, graphe_commun, cle)

    sim = (poids_sommets_aretes_commun)/max(poids_sommets_aretes_1, poids_sommets_aretes_2)  
    return sim

def calcul_aretes_avec_coeff(graphe, cle, coeffc, coeffa, coeffn):
    somme_aretes = 0
    
    for u,v,data in graphe.edges(data=True) :
        if data["label"] != 'B53' :
            if data["label"] == '0' :
                if coeffa == 1 :
                    somme_aretes += graphe.nodes[u]["poids"]
            elif graphe.nodes[u]["type"] == 1 and graphe.nodes[v]["type"] == 1 :
                if coeffc == 1 :
                    somme_aretes += graphe.nodes[u]["poids"]
            else :
                if coeffn == 1 :
                    somme_aretes += graphe.nodes[u]["poids"]
    somme_aretes = somme_aretes/2 - 4
    
    return somme_aretes

def calcul_aretes_communes_avec_coeff(graphe_commun, graphe1, graphe2, cle, coeffc, coeffa, coeffn):
    somme_aretes = 0
    for u,v,data in graphe_commun.edges(data=True) :
        if data["type"] != 'COV' :
            if data["type"] == '0' :
                if coeffa == 1 :
                    somme_aretes += min(graphe1.nodes[u[0]]["poids"], graphe2.nodes[u[1]]["poids"]) 
            elif graphe1.nodes[u[0]]["type"] == 1 and graphe1.nodes[v[0]]["type"] == 1 :
                if coeffc == 1 :
                    somme_aretes += min(graphe1.nodes[u[0]]["poids"], graphe2.nodes[u[1]]["poids"]) 
            else :
                if coeffn == 1 :
                    somme_aretes += min(graphe1.nodes[u[0]]["poids"], graphe2.nodes[u[1]]["poids"]) 
                    
    somme_aretes = somme_aretes - 4
    
    return somme_aretes
       

def calcul_sim_aretes_avec_coeff(graphe1, graphe2, graphe_commun, cle, coeffc, coeffa, coeffn):
    aretes_1 = calcul_aretes_avec_coeff(graphe1, cle, coeffc, coeffa, coeffn)
    aretes_2 = calcul_aretes_avec_coeff(graphe2, cle, coeffc, coeffa, coeffn)
    aretes_commun = calcul_aretes_communes_avec_coeff(graphe_commun, graphe1, graphe2, cle, coeffc, coeffa, coeffn)
    
    return aretes_commun/max(aretes_1, aretes_2)
    

def calcul_sim_avec_poids_par_chaine(graphe1, graphe2, graphe_commun, chaines_1, chaines_2, chaines_commun, i):
    
    poids_sommets_1 = 0
    for u, poids in graphe1.nodes(data="poids") :
        if u in chaines_1[i] :
            poids_sommets_1 += poids
    poids_sommets_1 -= 1
    
    poids_aretes_1 = 0
    for u,v,typ in graphe1.edges(data="label") :
        if typ != 'B53' and (u in chaines_1[i] and v in chaines_1[i]):
            poids_aretes_1 += 1
    poids_aretes_1 = poids_aretes_1/2
#     if i == 0 or i == 1 :
#         poids_aretes_1 = poids_aretes_1/2 - 2
#     else :
#         poids_aretes_1 = poids_aretes_1/2 - 1
    
    poids_sommets_2 = 0
    for u, poids in graphe2.nodes(data="poids") :
        if u in chaines_2[i] :
            poids_sommets_2 += poids
    poids_sommets_2 -= 1
    
    poids_aretes_2 = 0
    for u,v,typ in graphe2.edges(data="label") :
        if typ != 'B53' and (u in chaines_2[i] and v in chaines_2[i]) :
            poids_aretes_2 += 1   
    poids_aretes_2 = poids_aretes_2/2   
#     if i == 0 or i == 1 :
#         poids_aretes_2 = poids_aretes_2/2 - 2
#     else :
#         poids_aretes_2 = poids_aretes_2/2 - 1
            
    poids_sommets_communs = 0
    for noeud in graphe_commun.nodes() :
        if noeud in chaines_commun[i] :
            poids_sommets_communs += min(graphe1.nodes[noeud[0]]["poids"], graphe2.nodes[noeud[1]]["poids"])
    poids_sommets_communs -= 1
    
    poids_aretes_communes = 0    
    for u,v,typ in graphe_commun.edges(data="type") :
        if typ != 'COV' and (u in chaines_commun[i] and v in chaines_commun[i]):
            poids_aretes_communes += 1
#     if i == 0 or i == 1 :
#         poids_aretes_communes -= 2
#     else :
#         poids_aretes_communes -= 1
    
#     print(poids_sommets_1)
#     print(poids_sommets_2)
#     print(poids_aretes_1)
#     print(poids_aretes_2)
#     print(poids_sommets_communs)
#     print(poids_aretes_communes)
    sim = (poids_sommets_communs + poids_aretes_communes)/max(poids_sommets_1 + poids_aretes_1, poids_sommets_2, poids_aretes_2)  
    return sim, poids_sommets_1, poids_aretes_1, poids_sommets_2, poids_aretes_2, poids_sommets_communs, poids_aretes_communes
    

liste = ['5J7L_DA_191_3', '5J7L_DA_191_4', '5FDU_1A_301_1', '5J7L_DA_301_2', '5DM6_X_334_1', '5FDU_1A_334_2', '4V9F_0_335_1', '5J7L_DA_335_2', '3JCS_1_137_4', '4V88_A5_290_1', '4V88_A6_314_2', '5J7L_DA_218_3', '4V9F_0_251_2', '1FJG_A_62_8', '5J7L_DA_137_1', '4V9F_0_118_1', '4V9F_0_62_2', '5J7L_DA_271_2', '4V9F_0_224_1', '5DM6_X_197_1', '3GX5_A_138_6', '1FJG_A_317_2', '5J5B_BA_317_1', '1FJG_A_326_1', '5DM6_X_137_3', '5J5B_BA_314_1', '4V9F_0_134_6', '4V9F_0_328_1', '4V9F_0_197_2', '4V9F_0_62_16', '5J7L_DA_282_2', '4V88_A5_137_2', '5FDU_1A_224_3', '5J7L_DA_326_2']

def generation_fichier_csv_sim(version, fichier, type_fic) :
    with open(fichier, 'rb') as fichier_graphe :
                mon_depickler = pickle.Unpickler(fichier_graphe)
                dico_graphe = mon_depickler.load()
            
#             with open("dico_sim.pickle", 'rb') as fichier_sim :
#                 mon_depickler_sim = pickle.Unpickler(fichier_sim)
#                 dico_sim = mon_depickler_sim.load()
                
#                 for fic in os.listdir("graphes_extension/fichiers_couples_epures") :
#                     if "pickle" in fic :
#                         elt1 = fic.split('_')[2] + '_' + fic.split('_')[3] + '_' + fic.split('_')[4] + '_' + fic.split('_')[5] + '_' + fic.split('_')[6]
#                         elt2 = fic.split('_')[7] + '_' + fic.split('_')[8] + '_' + fic.split('_')[9] + '_' + fic.split('_')[10] + '_' + fic.split('_')[11][:len(fic.split('_')[11])-7]
#                         
#                         if (elt1, elt2) not in dico_graphe.keys() :
#                             print(elt1)
#                             print(elt2)  
                
                
                tot_sim = []
                tot_sim_complet = []
                tot_sim_new = []
                
#                 print(len(dico_sim))
                
                for cle in dico_graphe.keys() :
                    element1 = cle[0]
                    element2 = cle[1]
                    print(element1)
                    print(element2)
                    if type_fic == 'structure' :
                        element1_1 = str(element1).split(",")[0][2:len(str(element1).split(",")[0])-1] + "_" + str(element1).split(",")[1][2:len(str(element1).split(",")[1])-1] + "_" + str(element1).split(",")[2][1:] + "_" + str(element1).split(",")[3][1:len(str(element1).split(",")[3])-1] 
                        element2_1 = str(element2).split(",")[0][2:len(str(element2).split(",")[0])-1] + "_" + str(element2).split(",")[1][2:len(str(element2).split(",")[1])-1] + "_" + str(element2).split(",")[2][1:] + "_" + str(element2).split(",")[3][1:len(str(element2).split(",")[3])-1]                 
                        element1 = "fichier_" + element1_1
                        element2 = "fichier_" + element2_1
                    print(element1)
                    print(element2)
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
                                if version == 'sans_motif' :
                                    sim = calcul_sim_raymond_sans_motif(graphe1, graphe2, dico_graphe[cle])
                                    tot_sim_complet.append(sim)
                                    sim = calcul_sim_raymond_non_cov_sans_motif(graphe1, graphe2, dico_graphe[cle])
                                    tot_sim.append(sim)
                                    sim = calcul_sim_non_cov_sans_motif(graphe1, graphe2, dico_graphe[cle])
                                    print(sim)
                                    tot_sim_new.append(sim[0])
                                else :
                                    sim = calcul_sim_raymond_avec_motif(graphe1, graphe2, dico_graphe[cle])
                                    tot_sim_complet.append(sim)
                                    sim = calcul_sim_raymond_non_cov_avec_motif(graphe1, graphe2, dico_graphe[cle])
                                    tot_sim.append(sim)
                                    sim = calcul_sim_non_cov_avec_motif(graphe1, graphe2, dico_graphe[cle])
                                    tot_sim_new.append(sim)
                               #                             if sim < float(dico_sim[cle]) :
    #                                 print("plus petit")
    #                                 print(dico_sim[cle])
    #                                 print(sim)
    #                             else :
    #                                 print("plus grand")
    #                                 print(dico_sim[cle])
    #                                 print(sim)
                                
    #                 else :
    #                     print(element1)
    #                     print(element2)
                            
            #print(len(tot_sim_complet))   
                print(len(tot_sim))
                with open(fichier[:len(fichier)-7]+"_sim_csv_tot_"+version+".csv", 'w', newline='') as fichier_csv :
                    csvwriter = csv.writer(fichier_csv, delimiter=',')  
                    i = 0
                    while i+1024 < len(tot_sim_complet) :
                        csvwriter.writerow(tot_sim_complet[i:i+1024])
                        i = i+1024
                    csvwriter.writerow(tot_sim_complet[i:])
                with open(fichier[:len(fichier)-7]+"_sim_csv_tot_new_"+version+".csv", 'w', newline='') as fichier_csv_2 :
                    csvwriter_2 = csv.writer(fichier_csv_2, delimiter=',')    
                    i = 0
                    while i+1024 < len(tot_sim) :
                        csvwriter_2.writerow(tot_sim[i:i+1024])
                        i = i+1024
                    csvwriter_2.writerow(tot_sim[i:])
                
                with open(fichier[:len(fichier)-7]+"_sim_csv_tot_non_raymond_"+version+".csv", 'w', newline='') as fichier_csv_3 :
                    csvwriter_3 = csv.writer(fichier_csv_3, delimiter=',')
                    i = 0
                    while i+1024 < len(tot_sim_new) :
                        csvwriter_3.writerow(tot_sim_new[i:i+1024])
                        i = i+1024
                    csvwriter_3.writerow(tot_sim_new[i:])
                
                
                
#             sns.distplot(tot_sim_new, bins=20)
#             plt.show()


def generation_fichier_pickle(version, type):
    with open("dico_graphe_epure_en_tout.pickle", 'rb') as fichier_graphe :
        mon_depickler = pickle.Unpickler(fichier_graphe)
        dico_graphe = mon_depickler.load()
        
        tot_sim = {}
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
                        if version == 'sans_motif' :
                            if type == 'raymond' : 
                                sim = calcul_sim_raymond_sans_motif(graphe1, graphe2, dico_graphe[cle])
                            elif type == 'raymond_non_cov' :
                                sim = calcul_sim_raymond_non_cov_sans_motif(graphe1, graphe2, dico_graphe[cle])
                            else : 
                                sim,compteur_arete_commun = calcul_sim_non_cov_sans_motif(graphe1, graphe2, dico_graphe[cle])
                        else :
                            if type == 'raymond' : 
                                sim = calcul_sim_raymond_avec_motif(graphe1, graphe2, dico_graphe[cle])
                            elif type == 'raymond_non_cov' :
                                sim = calcul_sim_raymond_non_cov_avec_motif(graphe1, graphe2, dico_graphe[cle])
                            else :
                                sim,compteur_arete_commun = calcul_sim_non_cov_avec_motif(graphe1, graphe2, dico_graphe[cle])
                        
                        tot_sim.update({(element1, element2) : sim})
                        
        with open("dico_sim_"+version+"_"+type+"en_tout.pickle", 'wb') as fichier_pickle :
            mon_pickler = pickle.Pickler(fichier_pickle)
            mon_pickler.dump(tot_sim)
            
            
def tri_par_insertion(deb, tab):
    pos_mini = deb
    mini = tab[deb][1]
    for i in range(deb+1, len(tab)) :
        if tab[i][1] < mini :
            mini = tab[i][1]
            pos_mini = i
    
    return pos_mini

def echange(tab, pos_mini, deb):
    temp = tab[deb]
    tab[deb] = tab[pos_mini]
    tab[pos_mini] = temp

def calcul_sim_par_element(element, version):
    
    with open("dico_graphe.pickle", 'rb') as fichier_graphe :
            mon_depickler = pickle.Unpickler(fichier_graphe)
            dico_graphe = mon_depickler.load()
            
            tot_sim_new = []
            tot_sim = []
            tab_cle = []
            for cle in dico_graphe.keys() :
                if cle[0] == element or cle[1] == element :
                    enlever = False 
                    for elt in liste : 
                        if elt in cle[0] or elt in cle[1] :
                            enlever = True
                    if enlever == False :
                        with open("graphes_extension/"+cle[0]+".pickle", 'rb') as fichier_graphe_1 :
                            mon_depickler_1 = pickle.Unpickler(fichier_graphe_1)
                            graphe1 = mon_depickler_1.load()
                            
                            with open("graphes_extension/"+cle[1]+".pickle", 'rb') as fichier_graphe_2 :
                                mon_depickler_2 = pickle.Unpickler(fichier_graphe_2)
                                graphe2 = mon_depickler_2.load()
                                
                                if version == "avec_motif" :
                                    sim, compteur_arete_commun = calcul_sim_non_cov_avec_motif(graphe1, graphe2, dico_graphe[cle])
                                else :
                                    sim, compteur_arete_commun = calcul_sim_non_cov_sans_motif(graphe1, graphe2, dico_graphe[cle])
                                
                                if cle[0] == element and cle[1] not in tab_cle :
                                    tot_sim_new.append((cle[1], sim, compteur_arete_commun))
                                    tab_cle.append(cle[1])
                                    tot_sim.append(sim)
                                elif cle[1] == element and cle[0] not in tab_cle :
                                    tot_sim_new.append((cle[0], sim, compteur_arete_commun))
                                    tab_cle.append(cle[0])
                                    tot_sim.append(sim)
            print(len(tot_sim_new))
            print(tot_sim_new)
            
            
            pos_mini = 0
            for i in range(0, len(tot_sim_new)) :
                pos_mini = tri_par_insertion(i, tot_sim_new)
                print(pos_mini)
                echange(tot_sim_new, pos_mini, i)
            
            print(tot_sim_new)
            
            with open("ordre_"+element+"_"+version+".txt", 'w') as fichier :
                for elt in tot_sim_new :
                    fichier.write(elt[0] + " " + str(elt[1]) + " "+ str(elt[2]) +"\n")
            
            with open("sim_"+element+"_"+version+".csv", 'w', newline="") as fichier_csv :
                csvwriter = csv.writer(fichier_csv, delimiter=',') 
                csvwriter.writerow(sorted(tot_sim))
                
     

def calcul_max_sim() :            
    with open("dico_graphe.pickle", 'rb') as fichier_graphe :
            mon_depickler = pickle.Unpickler(fichier_graphe)
            dico_graphe = mon_depickler.load()
            
            with open("dico_sim.pickle", 'rb') as fichier_sim :
                mon_depickler_sim = pickle.Unpickler(fichier_sim)
                dico_sim = mon_depickler_sim.load()
 
                #print(len(dico_sim))
                
                for cle in dico_graphe.keys() :
                    element1 = cle[0]
                    element2 = cle[1]
#                     print(element1)
#                     print(element2)
                    
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
                                
                                sim, compteur_arete_commun = calcul_sim_non_cov_sans_motif(graphe1, graphe2, dico_graphe[cle])
                                
                            if float(sim) >= 0.8:
                                print(element1)
                                print(element2)
                                print(sim)
 
def stockage_sim(typ, depart):
    if depart == "extensions" :
        with open("dico_comp_complet_metrique_toutes_aretes.pickle", 'rb') as fichier_graphe :
            mon_depickler = pickle.Unpickler(fichier_graphe)
            dico_graphe = mon_depickler.load()

#         with open("result_graphes_comp/graphe_comp_couples_possibles_fichier_1FJG_A_48_8_fichier_1FJG_A_138_3.pickle", 'rb') as fichier_graphe :
#             mon_depickler = pickle.Unpickler(fichier_graphe)
#             dico_graphe = mon_depickler.load()
             
            dico_sim = {}
            for cle in dico_graphe.keys() : 
                
                with open("graphes_extension/"+cle[0]+".pickle", 'rb') as fichier_graphe_1 :
                    mon_depickler_1 = pickle.Unpickler(fichier_graphe_1)
                    graphe1 = mon_depickler_1.load()
                
                    with open("graphes_extension/"+cle[1]+".pickle", 'rb') as fichier_graphe_2 :
                        mon_depickler_2 = pickle.Unpickler(fichier_graphe_2)
                        graphe2 = mon_depickler_2.load()
                
                        if typ == "raymond" :
                            sim = calcul_sim_raymond_sans_motif(graphe1, graphe2, dico_graphe[cle])
                            
                        elif typ == "longue_distance" :
                            sim = calcul_sim_non_cov_sans_motif(graphe1, graphe2, dico_graphe[cle])
                        
                        elif typ == "non_cov"  :
                            sim = calcul_sim_avec_poids(graphe1, graphe2, dico_graphe[cle], cle)   
#                             if cle[0] == "fichier_4V9F_0_30_4" and cle[1] == "fichier_4V9F_0_48_21" :
                            print(cle[0])
                            print(cle[1])
                            print(sim)
                            print(dico_graphe[cle].edges.data())
                        elif typ == "toutes_aretes" :
                            sim = calcul_sim_aretes_avec_coeff(graphe1, graphe2, dico_graphe[cle], cle, 1, 1, 1)
                            
                                        
                        dico_sim.update({(cle[0][8:], cle[1][8:]) : sim})

    else :
        with open("fichier_comp_grands_graphes_V2.pickle", 'rb') as fichier_graphe :
            mon_depickler = pickle.Unpickler(fichier_graphe)
            dico_graphe = mon_depickler.load()
             
            dico_sim = {}
            for cle in dico_graphe.keys() : 
                element1 = str(cle[0]).split(",")
                element2 = str(cle[1]).split(",")
                elt1 = element1[0][2:len(element1[0])-1] + "_" + element1[1][2:len(element1[1])-1] + "_" + element1[2][1:] + "_" + element1[3][1:len(element1[3])-1]
                elt2 = element2[0][2:len(element2[0])-1] + "_" + element2[1][2:len(element2[1])-1] + "_" + element2[2][1:] + "_" + element2[3][1:len(element2[3])-1]
#                 print(elt1)
#                 print(elt2)
                with open("grands_graphes.pickle", 'rb') as fichier_grands_graphes :
                    mon_depickler_grands_graphes = pickle.Unpickler(fichier_grands_graphes)
                    dico_grands_graphes = mon_depickler_grands_graphes.load()
                    
                    
                    if typ == "raymond" : 
                        sim = calcul_sim_raymond_sans_motif(dico_grands_graphes[cle[0]], dico_grands_graphes[cle[1]], dico_graphe[cle])
                        
                    elif typ == "non_cov" :
                        sim = calcul_sim_non_cov_sans_motif(dico_grands_graphes[cle[0]], dico_grands_graphes[cle[1]], dico_graphe[cle])
                        if sim[0] > 1.0 :
                            print(elt1)
                            print(elt2)
                            print(sim)
                            
                        if elt1 == "5J7L_DA_50_21" and elt2 == "5J7L_DA_48_20" :
                            print("ramou")
                            print(sim)
               
                        
                        
                    else : ## type=="non_cov_sommets"
                        sim = calcul_sommets_aretes_grands_graphes_commun(dico_graphe[cle])/max(calcul_sommets_aretes_grands_graphes(dico_grands_graphes[cle[0]]), calcul_sommets_aretes_grands_graphes(dico_grands_graphes[cle[1]]))
                    dico_sim.update({(elt1, elt2) : sim})    
    
    #print(dico_sim)                    
    with open("sim_"+depart+"_"+typ+"_metrique_toutes_aretes.pickle", 'wb') as fichier_sim :
        mon_pickler = pickle.Pickler(fichier_sim)
        mon_pickler.dump(dico_sim)
                    

if __name__ == '__main__':
    
    stockage_sim("toutes_aretes", "extensions")

    
    #generation_fichier_csv_sim("sans_motif", "fichier_comp_grands_graphes_V2.pickle", "structure")
#     with open("dico_graphe_epure_en_tout_test.pickle", 'rb') as fichier_graphe :
#         mon_depickler = pickle.Unpickler(fichier_graphe)
#         dico_graphe = mon_depickler.load()
#         
#         element1 = "fichier_5J5B_BA_294_2"
#         element2 = "fichier_5DM6_X_328_2"
#         print(dico_graphe.keys())
#         with open("graphes_extension/"+element1+".pickle", 'rb') as fichier_graphe_1 :
#             mon_depickler_1 = pickle.Unpickler(fichier_graphe_1)
#             graphe1 = mon_depickler_1.load()
#             
#             print(graphe1.nodes.data())
#             with open("graphes_extension/"+element2+".pickle", 'rb') as fichier_graphe_2 :
#                 mon_depickler_2 = pickle.Unpickler(fichier_graphe_2)
#                 graphe2 = mon_depickler_2.load()
#                 
#                 print(calcul_sim_avec_poids(graphe2, graphe1, dico_graphe[(element2, element1)]))
    #stockage_sim("longue_distance", "extensions")
    
    ## recherche difference entre les trois metriques
    with open("sim_extensions_longue_distance.pickle", 'rb') as fichier_sim_1 :
        mon_depickler_1 = pickle.Unpickler(fichier_sim_1)
        dico_sim_extensions_longue_distance = mon_depickler_1.load()
         
        with open("sim_extensions_non_cov_nouvelle_metrique.pickle", 'rb') as fichier_sim_2 :
            mon_depickler_2 = pickle.Unpickler(fichier_sim_2)
            dico_sim_extensions_non_cov = mon_depickler_2.load()
             
            with open("sim_grands_graphes_non_cov_sommets_nouvelle_metrique.pickle", 'rb') as fichier_sim_3 :
                mon_depickler_3 = pickle.Unpickler(fichier_sim_3)
                dico_sim_graphe_global_non_cov = mon_depickler_3.load()
                
                print(dico_sim_graphe_global_non_cov)
                 
                ordres = ["el,ec,gc", "el,gc,ec", "ec,el,gc", "ec,gc,el", "gc,el,ec", "gc,ec,el"]
                nombre_ordres = dict((el,0) for el in ordres)
                moyenne_ordres = dict((el,[0,0]) for el in ordres)
                print(nombre_ordres.keys())
                print(moyenne_ordres)
#                 print(dico_sim_extensions_longue_distance.keys())
#                 print(dico_sim_extensions_non_cov.keys())
#                 print(dico_sim_graphe_global_non_cov.keys())
                for cle in dico_sim_extensions_non_cov.keys() :
                    if cle not in dico_sim_extensions_longue_distance.keys() :
                        cle_ex_longue_distance = (cle[1], cle[0])
                    else :
                        cle_ex_longue_distance = cle
                    if cle not in dico_sim_graphe_global_non_cov.keys() :
                        cle_gg_non_cov = (cle[1], cle[0])
                    else :
                        cle_gg_non_cov = cle
                             
                    if dico_sim_extensions_longue_distance[cle_ex_longue_distance][0] <= dico_sim_extensions_non_cov[cle] and dico_sim_extensions_longue_distance[cle_ex_longue_distance][0] <= dico_sim_graphe_global_non_cov[cle_gg_non_cov] :
                        if dico_sim_extensions_non_cov[cle] < dico_sim_graphe_global_non_cov[cle_gg_non_cov] :
                            nombre_ordres["el,ec,gc"] += 1
                            moyenne_ordres["el,ec,gc"][0] += dico_sim_extensions_non_cov[cle] - dico_sim_extensions_longue_distance[cle_ex_longue_distance][0]
                            moyenne_ordres["el,ec,gc"][1] += dico_sim_graphe_global_non_cov[cle_gg_non_cov] - dico_sim_extensions_non_cov[cle]
                             
                        else :
                            nombre_ordres["el,gc,ec"] += 1
                            moyenne_ordres["el,gc,ec"][0] += dico_sim_graphe_global_non_cov[cle_gg_non_cov] - dico_sim_extensions_longue_distance[cle_ex_longue_distance][0]
                            moyenne_ordres["el,gc,ec"][1] += dico_sim_extensions_non_cov[cle] - dico_sim_graphe_global_non_cov[cle_gg_non_cov]
                             
                             
                            print(cle) 
#                             print(cle_ex_longue_distance)
#                             print(dico_sim_extensions_longue_distance[cle_ex_longue_distance][0])
#                             print(dico_sim_extensions_non_cov[cle])
#                             print(dico_sim_graphe_global_non_cov[cle_gg_non_cov])
                             
                    elif dico_sim_extensions_non_cov[cle] <= dico_sim_extensions_longue_distance[cle_ex_longue_distance][0] and dico_sim_extensions_non_cov[cle] <= dico_sim_graphe_global_non_cov[cle_gg_non_cov] :
                        if dico_sim_extensions_longue_distance[cle_ex_longue_distance][0] < dico_sim_graphe_global_non_cov[cle_gg_non_cov] :
                            nombre_ordres["ec,el,gc"] += 1
                            moyenne_ordres["ec,el,gc"][0] += dico_sim_extensions_longue_distance[cle_ex_longue_distance][0] - dico_sim_extensions_non_cov[cle]
                            moyenne_ordres["ec,el,gc"][1] += dico_sim_graphe_global_non_cov[cle_gg_non_cov] - dico_sim_extensions_longue_distance[cle_ex_longue_distance][0]
                             
                             
                        else :
                            nombre_ordres["ec,gc,el"] += 1
                            moyenne_ordres["ec,gc,el"][0] += dico_sim_graphe_global_non_cov[cle_gg_non_cov] - dico_sim_extensions_non_cov[cle]
                            moyenne_ordres["ec,gc,el"][1] += dico_sim_extensions_longue_distance[cle_ex_longue_distance][0] - dico_sim_graphe_global_non_cov[cle_gg_non_cov]
                             
                             
                    elif dico_sim_graphe_global_non_cov[cle_gg_non_cov] <= dico_sim_extensions_longue_distance[cle_ex_longue_distance][0] and dico_sim_graphe_global_non_cov[cle_gg_non_cov] <= dico_sim_extensions_non_cov[cle] :
                        if dico_sim_extensions_longue_distance[cle_ex_longue_distance][0] < dico_sim_extensions_non_cov[cle] :
                            nombre_ordres["gc,el,ec"] += 1
 
                            moyenne_ordres["gc,el,ec"][0] += dico_sim_extensions_longue_distance[cle_ex_longue_distance][0] - dico_sim_graphe_global_non_cov[cle_gg_non_cov]
                            moyenne_ordres["gc,el,ec"][1] += dico_sim_extensions_non_cov[cle] - dico_sim_extensions_longue_distance[cle_ex_longue_distance][0]
                             
                        else :
                            nombre_ordres["gc,ec,el"] += 1
                            moyenne_ordres["gc,ec,el"][0] += dico_sim_extensions_non_cov[cle] - dico_sim_graphe_global_non_cov[cle_gg_non_cov]
                            moyenne_ordres["gc,ec,el"][1] += dico_sim_extensions_longue_distance[cle_ex_longue_distance][0] - dico_sim_extensions_non_cov[cle]
                             
                             
                    else :
                        print("autre cas?")
                        print(dico_sim_graphe_global_non_cov[cle_gg_non_cov])
                        print(dico_sim_extensions_longue_distance[cle_ex_longue_distance][0])
                        print(dico_sim_extensions_non_cov[cle])
                         
                print(nombre_ordres)
                 
                moyenne_ordres["el,ec,gc"][0] = moyenne_ordres["el,ec,gc"][0]/nombre_ordres["el,ec,gc"]
                moyenne_ordres["el,ec,gc"][1] = moyenne_ordres["el,ec,gc"][1]/nombre_ordres["el,ec,gc"]
                 
                moyenne_ordres["ec,el,gc"][0] = moyenne_ordres["ec,el,gc"][0]/nombre_ordres["ec,el,gc"]
                moyenne_ordres["ec,el,gc"][1] = moyenne_ordres["ec,el,gc"][1]/nombre_ordres["ec,el,gc"]
                 
                moyenne_ordres["ec,gc,el"][0] = moyenne_ordres["ec,gc,el"][0]/nombre_ordres["ec,gc,el"]
                moyenne_ordres["ec,gc,el"][1] = moyenne_ordres["ec,gc,el"][1]/nombre_ordres["ec,gc,el"]
                 
                moyenne_ordres["el,gc,ec"][0] = moyenne_ordres["el,gc,ec"][0]/nombre_ordres["el,gc,ec"]
                moyenne_ordres["el,gc,ec"][1] = moyenne_ordres["el,gc,ec"][1]/nombre_ordres["el,gc,ec"]
                 
                moyenne_ordres["gc,el,ec"][0] = moyenne_ordres["gc,el,ec"][0]/nombre_ordres["gc,el,ec"]
                moyenne_ordres["gc,el,ec"][1] = moyenne_ordres["gc,el,ec"][1]/nombre_ordres["gc,el,ec"]
                 
                moyenne_ordres["gc,ec,el"][0] = moyenne_ordres["gc,ec,el"][0]/nombre_ordres["gc,ec,el"]
                moyenne_ordres["gc,ec,el"][1] = moyenne_ordres["gc,ec,el"][1]/nombre_ordres["gc,ec,el"]
                 
                print(moyenne_ordres)
                
                print(dico_sim_graphe_global_non_cov[('5DM6_X_48_9', '1FJG_A_109_6')])
                
                
                