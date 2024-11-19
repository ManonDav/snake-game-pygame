import pygame
import random


L_CARRE = 10 # Largeur d’un carre du serpent.
VITESSE = 10 # Vitesse de deplacement du serpent (doit etre egale a L_CARRE).

def snake_init(niveau,coord,longueur,vitesse_agr):
    """
        dico des éléments de niveau, tuple(int,int),int,int => rien
        Initialise le serpent
    """
    serpent={}
    serpent["niv"]=niveau
    serpent["vit_agr"]=vitesse_agr
    serpent["depl_x"]=VITESSE
    serpent["depl_y"]=0
    serpent["direction"]="droite"
    x=coord[0]
    y=coord[1]
    serpent["corps"]=[[x,y]]
    for i in range(1,longueur):
        serpent["corps"].append([x-(i*L_CARRE),y])
    serpent["larg"]=L_CARRE
    
    return serpent

def snake_dessine(serpent):
    """
        dico des éléments de serpent => rien
        Dessine le serpent
    """
    for i in range(len(serpent["corps"])):
        pygame.draw.rect(serpent["niv"]["surf"], (0,195,0), (serpent["corps"][i][0],serpent["corps"][i][1],L_CARRE,L_CARRE))
    
# def snake_update_pos(serpent):
#     if serpent["direction"]=="droite":
#         serpent["corps"][0][0]+=serpent["depl_x"]
#         i=1
#         while serpent["corps"][i-1][1]==serpent["corps"][i][1]:
#             serpent["corps"][i][0]+=serpent["depl_x"]
#             i+=1
#             if i == len(serpent["corps"]):
#                 break
#         for j in range(i,len(serpent["corps"])):
#             serpent["corps"][j][1]+=serpent["depl_y"]
#             
#     if serpent["direction"]=="gauche":
#         serpent["corps"][0][0]+=serpent["depl_x"]
#         i=1
#         while serpent["corps"][i-1][1]==serpent["corps"][i][1]:
#             serpent["corps"][i][0]+=serpent["depl_x"]
#             i+=1
#             if i == len(serpent["corps"]):
#                 break
#         for i in range(i,len(serpent["corps"])):
#             serpent["corps"][i][1]+=serpent["depl_y"]
#             
#     if serpent["direction"]=="haut":
#         serpent["corps"][0][1]+=serpent["depl_y"]
#         i=1
#         while serpent["corps"][i-1][0]==serpent["corps"][i][0]:
#             serpent["corps"][i][1]+=serpent["depl_y"]
#             i+=1
#             if i == len(serpent["corps"]):
#                 break
#         for i in range(i,len(serpent["corps"])):
#             serpent["corps"][i][0]+=serpent["depl_x"]
#             
#     if serpent["direction"]=="bas":
#         serpent["corps"][0][1]+=serpent["depl_y"]
#         i=1
#         while serpent["corps"][i-1][0]==serpent["corps"][i][0]:
#             serpent["corps"][i][1]+=serpent["depl_y"]
#             i+=1
#             if i == len(serpent["corps"]):
#                 break
#         for i in range(i,len(serpent["corps"])):
#             serpent["corps"][i][0]+=serpent["depl_x"]     
#                 
#     print(serpent["corps"])
    
def snake_update_pos(serpent):
    """
        dico des éléments de serpent => rien
        Met à jour la position du serpent
    """
    if serpent["direction"]=="droite" or serpent["direction"]=="gauche":
        liste_x=[]
        liste_y=[]
        for i in range(len(serpent["corps"])):
            liste_x.append(serpent["corps"][i][0])
            liste_y.append(serpent["corps"][i][1])
        serpent["corps"][0][0]+=serpent["depl_x"]
        for i in range(len(serpent["corps"])-1):
            serpent["corps"][i+1][0]=liste_x[i]
            serpent["corps"][i+1][1]=liste_y[i]

            
    if serpent["direction"]=="haut" or serpent["direction"]=="bas":
        liste_x=[]
        liste_y=[]
        for i in range(len(serpent["corps"])):
            liste_x.append(serpent["corps"][i][0])
            liste_y.append(serpent["corps"][i][1])
        serpent["corps"][0][1]+=serpent["depl_y"]
        for i in range(len(serpent["corps"])-1):
            serpent["corps"][i+1][0]=liste_x[i]
            serpent["corps"][i+1][1]=liste_y[i]


def snake_heurte_mur(serpent):
    """
        dico des éléments de serpent => bool
        Vérifie si la tête du serpent ne rencontre pas un des bords de la fenêtre
    """
#     if serpent["corps"][0][0]==serpent["niv"]["rect_jeu"][2] or serpent["corps"][0][0]==serpent["niv"]["rect_jeu"][0]:
#         return True
#     if serpent["corps"][0][1]==serpent["niv"]["rect_jeu"][3] or serpent["corps"][0][1]==serpent["niv"]["rect_jeu"][1]:
#         return True
    return serpent["corps"][0][0]==serpent["niv"]["rect_jeu"][2] or serpent["corps"][0][0]==serpent["niv"]["rect_jeu"][0] or serpent["corps"][0][1]==serpent["niv"]["rect_jeu"][3] or serpent["corps"][0][1]==serpent["niv"]["rect_jeu"][1]

def snake_mort_queue(serpent):
    """
        dico des éléments de serpent => bool
        Vérifie si la tête du serpent ne rencontrent pas une autre partie de son corps
    """
    for i in range(1,len(serpent["corps"])):
        if serpent["corps"][0]==serpent["corps"][i]:
            return True
        
def snake_mange(serpent,fruit):
    """
        dico des éléments de serpent, dico des éléments de fruit => bool
        Si le serpent mange la pomme, une nouvelle pomme apparaît
    """
    if serpent["corps"][0]==fruit["pos"]:
        x=random.randrange(0,600,L_CARRE)
        y=random.randrange(0,370,L_CARRE)
        fruit["pos"]=[x,y]
        return True

def snake_grandit(serpent):
    """
        dico des éléments de serpent => rien
        Agrandit le serpent quand il mange une pomme
    """
    for _ in range(serpent["vit_agr"]):
        x,y=serpent["corps"][-1]
        x2,y2=serpent["corps"][-2]
        
        if x==x2 and serpent["direction"]=="haut":
            serpent["corps"].append([x,y+L_CARRE])
            
        if x==x2 and serpent["direction"]=="bas":
            serpent["corps"].append([x,y-L_CARRE])
            
        if y==y2 and serpent["direction"]=="droite":
            serpent["corps"].append([x-L_CARRE,y])
            
        if y==y2 and serpent["direction"]=="gauche":
            serpent["corps"].append([x+L_CARRE,y])






