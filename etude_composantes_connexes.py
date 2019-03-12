'''
Created on 9 janv. 2019

@author: coline
'''
import pickle
import networkx as nx
import matplotlib.pyplot as plt   
from recup_data.calcul_sim import calcul_sim_non_cov_sans_motif,\
    calcul_sim_avec_poids, calcul_sim_non_cov_sans_motif_par_chaine,\
    calcul_sim_avec_poids_par_chaine
from recup_data.sous_graphe_commun_max_version_grands_graphes import ajout_attribut_chaine,\
    recup_chaines
from recup_data.ajout_nts_lies_motif import dico_sim


def ajout_chaines_grands_graphes(graphe, occ_a_minor): 
    nx.set_node_attributes(graphe, -1, "chaine")
    chaine = recup_chaines(graphe, occ_a_minor)
    
    for i in range(4) :
        for e in chaine[i] :
#             print(e)
            if graphe.nodes[e]["chaine"] == -1 :
                graphe.nodes[e]["chaine"] = []
            if i+1 not in graphe.nodes[e]["chaine"] :

                graphe.nodes[e]["chaine"].append(i+1)

#             print("voisins")
            for voisin in graphe[e] :
#                 print(voisin)
                if graphe.nodes[voisin]["chaine"] == -1 :
                    graphe.nodes[voisin]["chaine"] = []
                if i+1 not in graphe.nodes[voisin]["chaine"] and voisin not in occ_a_minor :
                    graphe.nodes[voisin]["chaine"].append(i+1)
    
    for noeud in graphe.nodes() :
        if graphe.nodes[noeud]["chaine"] == -1 :
            print(noeud)
            
    return graphe
        

def nombre_arc_arete_graphe(graphe):
    compteur_arc = 0
    compteur_arete = 0
    for (u, v, t) in graphe.edges(data="label") :
        if t == 'B53' :
            compteur_arc += 1
        else :
            compteur_arete += 1
    return compteur_arc, compteur_arete


def recherche_chaines_par_morceau(u,v,graphe_comp,depart):
    if depart == "extensions" :
        with open("graphes_extension/fichier_"+graphe_comp.nodes[u]["nom"]+".pickle", 'rb') as fichier_graphe1 :
            mon_depickler_graphe1 = pickle.Unpickler(fichier_graphe1)
            graphe1 = mon_depickler_graphe1.load()
            with open("graphes_extension/fichier_"+graphe_comp.nodes[v]["nom"]+".pickle", 'rb') as fichier_graphe2 :
                mon_depickler_graphe2 = pickle.Unpickler(fichier_graphe2)
                graphe2 = mon_depickler_graphe2.load()
                
                chaines_1 = [[],[],[],[]]
                
                for noeud,ch in graphe1.nodes(data="chaine") :

                    if 1 in ch :
                        chaines_1[0].append(noeud)
                    if 2 in ch :
                        chaines_1[1].append(noeud)
                    if 3 in ch :
                        chaines_1[2].append(noeud)
                    if 4 in ch :
                        chaines_1[3].append(noeud)
         
                chaines_2 = [[],[],[],[]]
                
                for noeud,ch in graphe2.nodes(data="chaine") :
                    
                    if 1 in ch :
                        chaines_2[0].append(noeud)
                    if 2 in ch :
                        chaines_2[1].append(noeud)
                    if 3 in ch :
                        chaines_2[2].append(noeud)
                    if 4 in ch :
                        chaines_2[3].append(noeud)
                        
                with open("dico_graphe_epure_en_tout_test.pickle", 'rb') as fichier_commun :
                    mon_depickler_commun = pickle.Unpickler(fichier_commun)
                    dico_graphe = mon_depickler_commun.load()
                    
                    chaines_commun = [[],[],[],[]]
                    if ("fichier_"+graphe_comp.nodes[u]["nom"],"fichier_"+graphe_comp.nodes[v]["nom"]) in dico_graphe.keys() :
                        graphe_commun = dico_graphe[("fichier_"+graphe_comp.nodes[u]["nom"],"fichier_"+graphe_comp.nodes[v]["nom"])]
                        
                        for noeud in graphe_commun.nodes() :
                        
                            for j in range(4) :
                                if noeud[0] in chaines_1[j] and noeud[1] in chaines_2[j] :
                                    chaines_commun[j].append(noeud)

                        return chaines_1, chaines_2, chaines_commun
                    else :
                        graphe_commun = dico_graphe[("fichier_"+graphe_comp.nodes[v]["nom"], "fichier_"+graphe_comp.nodes[u]["nom"])]
                        for noeud in graphe_commun.nodes() :
                        
                            for j in range(4) :
                                if noeud[0] in chaines_2[j] and noeud[1] in chaines_1[j] :
                                    chaines_commun[j].append(noeud)

                        return chaines_1, chaines_2, chaines_commun
                    
    else :
        with open("grands_graphes.pickle", 'rb') as fichier_graphes :
            mon_depickler_graphes = pickle.Unpickler(fichier_graphes)
            graphes = mon_depickler_graphes.load()
            
            elt1 = (graphe_comp.nodes[u]["nom"].split("_")[0], graphe_comp.nodes[u]["nom"].split("_")[1], int(graphe_comp.nodes[u]["nom"].split("_")[2]), int(graphe_comp.nodes[u]["nom"].split("_")[3]))
            elt2 = (graphe_comp.nodes[v]["nom"].split("_")[0], graphe_comp.nodes[v]["nom"].split("_")[1], int(graphe_comp.nodes[v]["nom"].split("_")[2]), int(graphe_comp.nodes[v]["nom"].split("_")[3]))
            
   
            chaines_1 = [[],[],[],[]]
                
            for noeud,ch in graphes[elt1].nodes(data="chaine") :
                if 1 in ch :
                    chaines_1[0].append(noeud)
                if 2 in ch :
                    chaines_1[1].append(noeud)
                if 3 in ch :
                    chaines_1[2].append(noeud)
                if 4 in ch :
                    chaines_1[3].append(noeud)
     
            chaines_2 = [[],[],[],[]]
            
            for noeud,ch in graphes[elt2].nodes(data="chaine") :
                if 1 in ch :
                    chaines_2[0].append(noeud)
                if 2 in ch :
                    chaines_2[1].append(noeud)
                if 3 in ch :
                    chaines_2[2].append(noeud)
                if 4 in ch :
                    chaines_2[3].append(noeud)

            with open("fichier_comp_grands_graphes_V2.pickle", 'rb') as fichier_commun :
                mon_depickler_commun = pickle.Unpickler(fichier_commun)
                dico_graphe = mon_depickler_commun.load()
                
                chaines_commun = [[],[],[],[]]
#                 print(dico_graphe.keys())
                if (elt1, elt2) in dico_graphe.keys() :
                    graphe_commun = dico_graphe[(elt1, elt2)]
                    
                    for noeud in graphe_commun.nodes() :
                        for j in range(4) :
                            if noeud[0] in chaines_1[j] and noeud[1] in chaines_2[j] :
                                chaines_commun[j].append(noeud)
                    
                    return chaines_1, chaines_2, chaines_commun
                else :
                    graphe_commun = dico_graphe[(elt2, elt1)]
                
                    for noeud in graphe_commun.nodes() :
                        for j in range(4) :
                            if noeud[0] in chaines_2[j] and noeud[1] in chaines_1[j] :
                                chaines_commun[j].append(noeud)
                    
                    return chaines_2, chaines_1, chaines_commun
            
   
    
def calcul_sim_morceau(typ, depart, type_comp) :
    if depart == "extensions" :
        with open("graphe_complet_pondere_sim.pickle", 'rb') as fichier_graphe_complet :
            mon_depickler_complet = pickle.Unpickler(fichier_graphe_complet)
            graphe_complet = mon_depickler_complet.load()
            dico_sim_par_chaine = {}
            
            i = 0.1
            #i = 0.4
            while i <= 1.0 :
                with open("composantes_connexes_"+type_comp+"_"++str(i)+".pickle", 'rb') as fichier_comp:
                    mon_depickler_comp = pickle.Unpickler(fichier_comp)
                    composantes_connexes = mon_depickler_comp.load()
                    
                    for composante in composantes_connexes :
                        if len(composante) < 10 and len(composante) > 2 :
                            graphe_comp = graphe_complet.subgraph(composante)
                            for u,v in graphe_comp.edges() :
                                chaines_1, chaines_2, chaines_commun = recherche_chaines_par_morceau(u,v,graphe_comp, depart)
                                with open("graphes_extension/fichier_"+graphe_comp.nodes[u]["nom"]+".pickle", 'rb') as fichier_graphe1 :
                                    mon_depickler_graphe1 = pickle.Unpickler(fichier_graphe1)
                                    graphe1 = mon_depickler_graphe1.load()
                                    with open("graphes_extension/fichier_"+graphe_comp.nodes[v]["nom"]+".pickle", 'rb') as fichier_graphe2 :
                                        mon_depickler_graphe2 = pickle.Unpickler(fichier_graphe2)
                                        graphe2 = mon_depickler_graphe2.load()
                                        
                                        with open("dico_graphe_epure_en_tout_test.pickle", 'rb') as fichier_commun :
                                            mon_depickler_commun = pickle.Unpickler(fichier_commun)
                                            dico_graphe = mon_depickler_commun.load()
                                        tab_sim = []
                                        if ("fichier_"+graphe_comp.nodes[u]["nom"],"fichier_"+graphe_comp.nodes[v]["nom"]) in dico_graphe.keys() :
                                            cle = ("fichier_"+graphe_comp.nodes[u]["nom"],"fichier_"+graphe_comp.nodes[v]["nom"])
                                            graphe_commun = dico_graphe[cle]
                                            for j in range(4) :
                                                if typ == "longue_distance" :
                                                    sim = calcul_sim_non_cov_sans_motif(graphe1, graphe2, graphe_commun, chaines_1, chaines_2, chaines_commun, j)
                                                if typ == "non_cov" :
                                                    sim = calcul_sim_avec_poids_par_chaine(graphe1, graphe2, graphe_commun, chaines_1, chaines_2, chaines_commun, j)
                                                #print(sim)                    
                                                tab_sim.append(sim)
                                            dico_sim_par_chaine.update({(graphe_comp.nodes[u]["nom"], graphe_comp.nodes[v]["nom"]): tab_sim})
                                            
                                        else :
                                            cle = ("fichier_"+graphe_comp.nodes[v]["nom"], "fichier_"+graphe_comp.nodes[u]["nom"])
                                            graphe_commun = dico_graphe[cle]
                                            for j in range(4) :
                                                if typ == "longue_distance" :
                                                    sim = calcul_sim_non_cov_sans_motif(graphe2, graphe1, graphe_commun, chaines_2, chaines_1, chaines_commun, j)
                                                if typ == "non_cov" :
                                                    sim = calcul_sim_avec_poids_par_chaine(graphe2, graphe1, graphe_commun, chaines_2, chaines_1, chaines_commun, j)
                                                #print(sim)                    
                                                tab_sim.append(sim)
                                                
                                            dico_sim_par_chaine.update({(graphe_comp.nodes[v]["nom"], graphe_comp.nodes[u]["nom"]): tab_sim})

                                        
                                        
                                            
                i = i+0.1
    else :
        with open("graphe_complet_pondere_sim.pickle", 'rb') as fichier_graphe_complet :
            mon_depickler_complet = pickle.Unpickler(fichier_graphe_complet)
            graphe_complet = mon_depickler_complet.load()
            dico_sim_par_chaine = {}
            i = 0.1
            #i = 0.4
            while i <= 1.0 :
                with open("composantes_connexes_"+type_comp+"_"+str(i)+".pickle", 'rb') as fichier_comp:
                    mon_depickler_comp = pickle.Unpickler(fichier_comp)
                    composantes_connexes = mon_depickler_comp.load()
                    
                    for composante in composantes_connexes :
                        if len(composante) < 10 and len(composante) > 2 :
                            graphe_comp = graphe_complet.subgraph(composante)
                            for u,v in graphe_comp.edges() :
#                                 if (graphe_comp.nodes[u]["nom"] == '4V9F_0_48_26' and graphe_comp.nodes[v]["nom"] == '5J7L_DA_48_30') or  (graphe_comp.nodes[v]["nom"] == '4V9F_0_48_26' and graphe_comp.nodes[u]["nom"] == '5J7L_DA_48_30') :
#                                 
                                    chaines_1, chaines_2, chaines_commun = recherche_chaines_par_morceau(u,v,graphe_comp, depart)
                                    print(u)
                                    print(v)
                                    print(chaines_commun)
                                    with open("grands_graphes.pickle", 'rb') as fichier_graphes :
                                        mon_depickler_graphes = pickle.Unpickler(fichier_graphes)
                                        graphes = mon_depickler_graphes.load()
                                        with open("fichier_comp_grands_graphes_V2.pickle", 'rb') as fichier_commun :
                                            mon_depickler_commun = pickle.Unpickler(fichier_commun)
                                            dico_graphe = mon_depickler_commun.load()
                                            
                                            elt1 = (graphe_comp.nodes[u]["nom"].split("_")[0], graphe_comp.nodes[u]["nom"].split("_")[1], int(graphe_comp.nodes[u]["nom"].split("_")[2]), int(graphe_comp.nodes[u]["nom"].split("_")[3]))
                                            elt2 = (graphe_comp.nodes[v]["nom"].split("_")[0], graphe_comp.nodes[v]["nom"].split("_")[1], int(graphe_comp.nodes[v]["nom"].split("_")[2]), int(graphe_comp.nodes[v]["nom"].split("_")[3]))
                
                                            
                                            if (elt1, elt2) in dico_graphe.keys() :
                                                cle = (elt1, elt2)
                                                cle_sim = (graphe_comp.nodes[u]["nom"], graphe_comp.nodes[v]["nom"])
                                            else :
                                                cle = (elt2, elt1)
                                                cle_sim = (graphe_comp.nodes[v]["nom"], graphe_comp.nodes[u]["nom"])
                                                
                                            if cle_sim not in dico_sim_par_chaine.keys() :
                                                
                                                graphe_commun = dico_graphe[cle]
                                                tab_sim = []
                                                for j in range(4) :
                                                    if typ == "non_cov" :
                                                        sim = calcul_sim_non_cov_sans_motif_par_chaine(graphes[cle[0]], graphes[cle[1]], graphe_commun, chaines_1, chaines_2, chaines_commun, j)
                                                        if (elt1 == ('4V9F', '0', 48, 26) and elt2 == ('5J7L', 'DA', 48, 30)) or (elt2 == ('4V9F', '0', 48, 26) and elt1 == ('5J7L', 'DA', 48, 30))  :
                                                            print(cle[0])
                                                            print(cle[1])
                                                            print(j)
                                                            print(sim)
                                                    #print(sim)                    
                                                    tab_sim.append(sim)
                                                    dico_sim_par_chaine.update({cle_sim : tab_sim})
                                            
                i = i+0.1
        
    with open("sim_"+depart+"_"+typ+"par_chaine.pickle", 'wb') as fichier_graphe_complet_plus :
        mon_pickler_complet = pickle.Pickler(fichier_graphe_complet_plus)
        mon_pickler_complet.dump(dico_sim_par_chaine)


def draw_composantes(typ_sim, depart_sim, *args, **kwargs) :
    par_chaine = kwargs.get('par_chaine', False)
    type_comp = kwargs.get('type_comp', "")
    
    if par_chaine == False :
        with open("sim_"+depart_sim+"_"+typ_sim+".pickle", 'rb') as fichier_sim :
            mon_depickler = pickle.Unpickler(fichier_sim)
            dico_sim = mon_depickler.load()
            print(dico_sim.keys())
            
            with open("graphe_complet_pondere_sim.pickle", 'rb') as fichier_graphe_complet :
                mon_depickler_complet = pickle.Unpickler(fichier_graphe_complet)
                graphe_complet = mon_depickler_complet.load()
                
                i = 0.1
                while i <= 1.0 :
                    with open("composantes_connexes_"+type_comp+ "_"+str(i)+".pickle", 'rb') as fichier_comp:
                        mon_depickler_comp = pickle.Unpickler(fichier_comp)
                        composantes_connexes = mon_depickler_comp.load()
                        
                        compteur = 1
                        for composante in composantes_connexes :
                            
                            if len(composante) < 10 and len(composante) > 2 :
                                graphe_comp = nx.Graph()
                                graphe_comp = graphe_complet.subgraph(composante)
                                nx.set_node_attributes(graphe_comp, (33,33), "coordonnees")
                                pos = nx.circular_layout(graphe_comp)
                                
                                node_labels=dict([(u, (d["nom"]))for u,d in graphe_comp.nodes(data=True)])
        
                                for u,v,d in graphe_comp.edges(data=True) :
                                    
                                    if (graphe_comp.nodes[u]["nom"], graphe_comp.nodes[v]["nom"]) in dico_sim.keys() :
                                        graphe_comp.edges[u,v]["poids"] = dico_sim[(graphe_comp.nodes[u]["nom"], graphe_comp.nodes[v]["nom"])][0]
                                    else :
                                        graphe_comp.edges[u,v]["poids"] = dico_sim[(graphe_comp.nodes[v]["nom"], graphe_comp.nodes[u]["nom"])][0]
                                        
                                    
                                edge_labels = dict([((u,v), (round(d["poids"],2)))for u,v,d in graphe_comp.edges(data=True)])
                                
                                red_edges = []
                                
                                for u,v,d in graphe_comp.edges(data=True) :
                                    if d["poids"] >= i :
                                        red_edges.append((u,v))
                                
                                edge_colors = ['red' if edge in red_edges else 'black' for edge in graphe_comp.edges()]
                                densite = len(red_edges)/((len(composante)*(len(composante)-1))/2)
                                
                                plt.figure(figsize =(9,7))
                                plt.title(depart_sim)
                                #plt.title("poids > "+str(round(i,1)) + " densite : "+ str(round(densite,2)))
                                plt.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.9)
                                
                                nx.draw_networkx_nodes(graphe_comp, pos)
                                nx.draw_networkx_labels(graphe_comp, pos, labels = node_labels, font_size=8)
                                nx.draw_networkx_edges(graphe_comp, pos, edge_color=edge_colors)
                                nx.draw_networkx_edge_labels(graphe_comp, pos, edge_labels = edge_labels, label_pos=0.3)
                                plt.axis('off')
                                
                                
                                #plt.show()
                                plt.savefig("composantes_connexes_"+depart_sim+"_"+typ_sim+"/comp_"+type_comp+"_"+str(round(i,1))+"_"+str(compteur)+".png") # save as png
                                plt.close()
                                compteur+=1
                            
                    i = i+0.1
    else :
        with open("sim_"+depart_sim+"_"+typ_sim+"par_chaine.pickle", 'rb') as fichier_sim :
            mon_depickler = pickle.Unpickler(fichier_sim)
            dico_sim = mon_depickler.load()
            print(dico_sim.keys())
            
            with open("graphe_complet_pondere_sim.pickle", 'rb') as fichier_graphe_complet :
                mon_depickler_complet = pickle.Unpickler(fichier_graphe_complet)
                graphe_complet = mon_depickler_complet.load()
                
                i = 0.1
                while i <= 1.0 :
                    with open("composantes_connexes_"+type_comp+"_"+str(i)+".pickle", 'rb') as fichier_comp:
                        mon_depickler_comp = pickle.Unpickler(fichier_comp)
                        composantes_connexes = mon_depickler_comp.load()
                        
                        compteur = 1
                        for composante in composantes_connexes :
                            
                            if len(composante) < 10 and len(composante) > 2 :
                                graphe_comp = nx.Graph()
                                graphe_comp = graphe_complet.subgraph(composante)
                                nx.set_node_attributes(graphe_comp, (33,33), "coordonnees")
                                pos = nx.circular_layout(graphe_comp)
                                
                                node_labels=dict([(u, (d["nom"]))for u,d in graphe_comp.nodes(data=True)])
        
                                for u,v,d in graphe_comp.edges(data=True) :
                                    
                                    
                                    if (graphe_comp.nodes[u]["nom"], graphe_comp.nodes[v]["nom"]) in dico_sim.keys() :
                                        for j in range(4) :
                                            print(dico_sim[(graphe_comp.nodes[u]["nom"], graphe_comp.nodes[v]["nom"])][j])
                                        graphe_comp.edges[u,v]["poids"] = (dico_sim[(graphe_comp.nodes[u]["nom"], graphe_comp.nodes[v]["nom"])][0][0] + dico_sim[(graphe_comp.nodes[u]["nom"], graphe_comp.nodes[v]["nom"])][1][0] + dico_sim[(graphe_comp.nodes[u]["nom"], graphe_comp.nodes[v]["nom"])][2][0] + dico_sim[(graphe_comp.nodes[u]["nom"], graphe_comp.nodes[v]["nom"])][3][0])/4
                                    else :
                                        graphe_comp.edges[u,v]["poids"] = (dico_sim[(graphe_comp.nodes[v]["nom"], graphe_comp.nodes[u]["nom"])][0][0] + dico_sim[(graphe_comp.nodes[v]["nom"], graphe_comp.nodes[u]["nom"])][1][0] + dico_sim[(graphe_comp.nodes[v]["nom"], graphe_comp.nodes[u]["nom"])][2][0] + dico_sim[(graphe_comp.nodes[v]["nom"], graphe_comp.nodes[u]["nom"])][3][0])/4
                                        
                                    
                                edge_labels = dict([((u,v), (round(d["poids"],2)))for u,v,d in graphe_comp.edges(data=True)])
                                
                                red_edges = []
                                
                                for u,v,d in graphe_comp.edges(data=True) :
                                    if d["poids"] >= i :
                                        red_edges.append((u,v))
                                
                                edge_colors = ['red' if edge in red_edges else 'black' for edge in graphe_comp.edges()]
                                densite = len(red_edges)/((len(composante)*(len(composante)-1))/2)
                                
                                plt.figure(figsize =(9,7))
                                plt.title(depart_sim)
                                #plt.title("poids > "+str(round(i,1)) + " densite : "+ str(round(densite,2)))
                                plt.subplots_adjust(left=0.05, bottom=0.1, right=0.95, top=0.9)
                                
                                nx.draw_networkx_nodes(graphe_comp, pos)
                                nx.draw_networkx_labels(graphe_comp, pos, labels = node_labels, font_size=8)
                                nx.draw_networkx_edges(graphe_comp, pos, edge_color=edge_colors)
                                nx.draw_networkx_edge_labels(graphe_comp, pos, edge_labels = edge_labels, label_pos=0.3)
                                plt.axis('off')
                                
                                
                                #plt.show()
                                plt.savefig("composantes_connexes_"+depart_sim+"_"+typ_sim+"par_chaine/comp_"+type_comp+"_"+str(round(i,1))+"_"+str(compteur)+".png") # save as png
                                plt.close()
                                compteur+=1
                            
                    i = i+0.1
    
def choix_sim_stockee(choix):
        with open("graphe_complet_pondere_sim.pickle", 'rb') as fichier_graphe_complet :
            mon_depickler_complet = pickle.Unpickler(fichier_graphe_complet)
            graphe_complet = mon_depickler_complet.load()
            
            for u,v in graphe_complet.edges() :
                elt1 = graphe_complet.nodes[u]["nom"]
                elt2 = graphe_complet.nodes[v]["nom"]
                if "4V9F_0_25_4" not in elt1 and "4V9F_0_25_4" not in elt2 :
                    print(elt1)
                    print(elt2)
                    with open("graphes_extension/fichier_"+elt1+".pickle", 'rb') as fichier_graphe1 :
                        mon_depickler_graphe1 = pickle.Unpickler(fichier_graphe1)
                        graphe1 = mon_depickler_graphe1.load()
                        with open("graphes_extension/fichier_"+elt2+".pickle", 'rb') as fichier_graphe2 :
                            mon_depickler_graphe2 = pickle.Unpickler(fichier_graphe2)
                            graphe2 = mon_depickler_graphe2.load()
                            
                            with open("dico_graphe_epure_en_tout_test.pickle", 'rb') as fichier_commun :
                                mon_depickler_commun = pickle.Unpickler(fichier_commun)
                                dico_graphe = mon_depickler_commun.load()
                                
                                if choix == "non_cov_sans_motif" :
                                    if ("fichier_"+elt1, "fichier_"+elt2) in dico_graphe.keys() :
                                        sim = calcul_sim_non_cov_sans_motif(graphe1, graphe2, dico_graphe[("fichier_"+elt1, "fichier_"+elt2)])
                                    else :
                                        sim = calcul_sim_non_cov_sans_motif(graphe2, graphe1, dico_graphe[("fichier_"+elt2, "fichier_"+elt1)])
                                else :
                                    if ("fichier_"+elt1, "fichier_"+elt2) in dico_graphe.keys() :
                                        sim = calcul_sim_avec_poids(graphe1, graphe2, dico_graphe[("fichier_"+elt1, "fichier_"+elt2)])
                                    else :
                                        sim = calcul_sim_avec_poids(graphe2, graphe1, dico_graphe[("fichier_"+elt2, "fichier_"+elt1)])
                                        
                                graphe_complet.edges[u,v]["poids"] = sim
                
                            
        with open("graphe_complet_pondere_sim.pickle", 'wb') as fichier_graphe_complet_refait :
            mon_pickler_complet = pickle.Pickler(fichier_graphe_complet_refait)
            mon_pickler_complet.dump(graphe_complet)                    
    

def calcul_sim_globale_par_groupe(composantes_connexes, graphe_complet_pondere):
    with open("dico_graphe_epure_en_tout.pickle", 'rb') as fichier_graphe :
        mon_depickler = pickle.Unpickler(fichier_graphe)
        dico_graphe = mon_depickler.load()
    
        for composante in composantes_connexes :
            if len(composante) < 10 and len(composante) > 2 :
                graphe_comp = graphe_complet_pondere.subgraph(composante)
                
                max_nombre_arc = -1
                max_nombre_arete = -1
                max_nombre_sommet = -1
                for noeud, data in graphe_comp.nodes(data=True) :
                    with open("graphes_extension/"+data["nom"]+".pickle", 'rb') as fichier :
                        mon_depickler = pickle.Unpickler(fichier)
                        graphe = mon_depickler.load()
                        
                        nombre_arc, nombre_arete = nombre_arc_arete_graphe(graphe)
                        if nombre_arc < max_nombre_arc and nombre_arete < max_nombre_arete and max_nombre_sommet < graphe.number_of_nodes() :
                            max_nombre_arc = nombre_arc
                            max_nombre_arete = nombre_arete
                            max_nombre_sommet = graphe.number_of_nodes()
                
                aretes_idem = []
                print(graphe_comp.edges())            
                for u,v in graphe_comp.edges() :
                    nom_1 = graphe.nodes[u]["nom"]
                    nom_2 = graphe.nodes[v]["nom"]
                    if (nom_1, nom_2) in dico_graphe.keys() :
                        cle_1 = (nom_1, nom_2)
                    else :
                        cle_1 = (nom_2, nom_1)
                        
                    for w,z in graphe_comp.edges() :
                        nom_3 = graphe.nodes[w]["nom"]
                        nom_4 = graphe.nodes[z]["nom"]
                        if (nom_3, nom_4) in dico_graphe.keys() :
                            cle_2 = (nom_3, nom_4)
                        else :
                            cle_2 = (nom_4, nom_3) 
                            
                        if cle_1 != cle_2 :
                            for e1,e2,data_1 in dico_graphe[cle_1].edges(data=True) :
                                print("ramousnif")
                            
                        
                        
                        
                    
liste = ['5J7L_DA_191_3', '5J7L_DA_191_4', '5FDU_1A_301_1', '5J7L_DA_301_2', '5DM6_X_334_1', '5FDU_1A_334_2', '4V9F_0_335_1', '5J7L_DA_335_2', '3JCS_1_137_4', '4V88_A5_290_1', '4V88_A6_314_2', '5J7L_DA_218_3', '4V9F_0_251_2', '1FJG_A_62_8', '5J7L_DA_137_1', '4V9F_0_118_1', '4V9F_0_62_2', '5J7L_DA_271_2', '4V9F_0_224_1', '5DM6_X_197_1', '3GX5_A_138_6', '1FJG_A_317_2', '5J5B_BA_317_1', '1FJG_A_326_1', '5DM6_X_137_3', '5J5B_BA_314_1', '4V9F_0_134_6', '4V9F_0_328_1', '4V9F_0_197_2', '4V9F_0_62_16', '5J7L_DA_282_2', '4V88_A5_137_2', '5FDU_1A_224_3', '5J7L_DA_326_2']

if __name__ == '__main__':

#     with open("sim_extensions_non_covpar_chaine.pickle", 'rb') as fichier_graphe_complet_plus :
#         mon_pickler_complet = pickle.Unpickler(fichier_graphe_complet_plus)
#         dico_sim_par_chaine = mon_pickler_complet.load()
#         print(len(dico_sim_par_chaine.keys()))
# #         print(dico_sim_par_chaine.keys())
#         print(dico_sim_par_chaine[('fichier_1FJG_A_109_6', 'fichier_4V9F_0_30_23')])
#         for cle in dico_sim_par_chaine.keys() :
#             for i in range(4) :
#                 if dico_sim_par_chaine[cle][i][0] < 0.0 or dico_sim_par_chaine[cle][i][0] > 1.0 :
#                         print(cle)
# #                         print(i)
#                         print(dico_sim_par_chaine[cle])
#          
#         with open("grands_graphes.pickle", 'rb') as fichier_graphes :
#             mon_depickler_graphes = pickle.Unpickler(fichier_graphes)
#             graphes = mon_depickler_graphes.load()       
#             print(graphes[('4V9F','0',48,26)].nodes.data())         
#                         
#     with open("graphe_complet_pondere_sim.pickle", 'rb') as fichier_graphe_complet :
#         mon_depickler_complet = pickle.Unpickler(fichier_graphe_complet)
#         graphe_complet = mon_depickler_complet.load()
#         for x,data in graphe_complet.nodes(data=True) :
#             if data["nom"] == '4V9F_0_48_26' :
#                 u = x
#             if data["nom"] == '5J7L_DA_48_30' :
#                 v = x
#          
#         chaines_1, chaines_2, chaines_commun = recherche_chaines_par_morceau(u,v, graphe_complet, "graphe_global")
#         print(u)
#         print(v)
#         print(chaines_commun) 
#         with open("grands_graphes.pickle", 'rb') as fichier_graphes :
#             mon_depickler_graphes = pickle.Unpickler(fichier_graphes)
#             graphes = mon_depickler_graphes.load()
#             with open("fichier_comp_grands_graphes_V2.pickle", 'rb') as fichier_commun :
#                 mon_depickler_commun = pickle.Unpickler(fichier_commun)
#                 dico_graphe = mon_depickler_commun.load()
#                  
#                 elt1 = ('4V9F', '0', 48, 26)
#                 elt2 = ('5J7L', 'DA', 48, 30)
#                  
#                 if (elt1, elt2) in dico_graphe.keys() :
#                     cle = (elt1, elt2)
#                 else :
#                     cle = (elt2, elt1)
#                 graphe_commun = dico_graphe[cle]
#                 tab_sim = []
#                 for j in range(4) :
#                     print(j)
#                     sim = calcul_sim_non_cov_sans_motif_par_chaine(graphes[cle[0]], graphes[cle[1]], graphe_commun, chaines_1, chaines_2, chaines_commun, j)
#                     print(sim)
        
          
#         with open("graphe_complet_pondere_sim.pickle", 'rb') as fichier_graphe_complet :
#             mon_depickler_complet = pickle.Unpickler(fichier_graphe_complet)
#             graphe_complet = mon_depickler_complet.load()
#             print(graphe_complet.nodes.data())
#             for u,v in graphe_complet.edges() :
#                 if (graphe_complet.nodes[u]["nom"] == '5FJC_A_138_1' and graphe_complet.nodes[v]["nom"] == '5DM6_X_227_2') or (graphe_complet.nodes[v]["nom"] == '5FJC_A_138_1' and graphe_complet.nodes[u]["nom"] == '5DM6_X_227_2'):
#                     chaines_1, chaines_2, chaines_commun = recherche_chaines_par_morceau(u,v, graphe_complet, "graphe_global")
#                     print(chaines_1)
#                     print(chaines_2)
#                     print(chaines_commun)

#     with open("grands_graphes.pickle", 'rb') as fichier :
#         mon_depickler = pickle.Unpickler(fichier)
#         dico_graphes = mon_depickler.load()
#         print(dico_graphes[('5FJC', 'A',138,1)].edges.data())
        
#           
#         with open("fichiers_pickle/a-minor_test2.pickle", 'rb') as fichier_pickle :
#             mon_depickler_aminor = pickle.Unpickler(fichier_pickle)
#             tab_aminor = mon_depickler_aminor.load()
#             
#             for occ in tab_aminor :
#                 est_la = False
#                 for elt in liste :
#                     if occ["num_PDB"]+"_"+ occ["num_ch"]+"_"+ str(occ["num_motif"])+"_"+ str(occ["num_occ"]) == elt :
#                         est_la = True
#                         
#                 if est_la == False :
#                 
#                     cle = (occ["num_PDB"], occ["num_ch"], occ["num_motif"], occ['num_occ'])
#                     print(cle)
#                     ajout_chaines_grands_graphes(dico_graphes[cle], occ["a_minor"])
#                     print(dico_graphes[cle].nodes.data())
#                     
#     with open("grands_graphes.pickle", 'wb') as fichier_ec :
#         mon_pickler = pickle.Pickler(fichier_ec)
#         mon_pickler.dump(dico_graphes)
                    
            
    #choix_sim_stockee("par_poids_sans_motif")
    #calcul_sim_morceau("non_cov", "extensions")
    
    draw_composantes("non_cov", "graphe_global", type_comp="graphe_global_non_cov")
#     
#     
#     with open("graphe_complet_pondere_sim.pickle", 'rb') as fichier_graphe_complet :
#         mon_depickler_complet = pickle.Unpickler(fichier_graphe_complet)
#         graphe_complet = mon_depickler_complet.load()
#         
#         tab_proportion = [0,0,0,0]
#         nb_aretes = 0
#         
#         i = 0.1
#         #i = 0.4
#         graphes_deja_faits = []
#         while i <= 1.0 :
#             with open("composantes_connexes_"+str(i)+".pickle", 'rb') as fichier_comp:
#                 mon_depickler_comp = pickle.Unpickler(fichier_comp)
#                 composantes_connexes = mon_depickler_comp.load()
#                 
#                 for composante in composantes_connexes :
#                     if len(composante) < 10 and len(composante) > 2 :
#                         graphe_comp = graphe_complet.subgraph(composante)
#                         for u,v,t in graphe_comp.edges(data="poids") :
#                             if (graphe_comp.nodes[u]["nom"], graphe_comp.nodes[v]["nom"]) not in graphes_deja_faits and (graphe_comp.nodes[v]["nom"], graphe_comp.nodes[u]["nom"]) not in graphes_deja_faits :
#                                 if t < i :
#                                     for j in range(4) :
#                                         if graphe_complet.edges[u,v]["sim_par_chaine"][j] > i :
#                                             tab_proportion[j] += 1
#                                     nb_aretes += 1
#                                 graphes_deja_faits.append((graphe_comp.nodes[u]["nom"], graphe_comp.nodes[v]["nom"]))
#         
#             i = i + 0.1
#         for j in range(4) :
#             tab_proportion[j] = tab_proportion[j] / nb_aretes   
#         print(tab_proportion)
#         for i in range(4) :
#             tab_proportion[i] = tab_proportion[i] / nb_aretes
      
      
        
                        
                    
        
                            
                        