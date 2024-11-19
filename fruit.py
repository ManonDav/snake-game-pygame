import random
import pygame


L_CARRE = 10

def fruit_init(niveau):
    """
        dico des éléments de niveau => rien
        Initialisation du fruit
    """
    fruit={}
    fruit["niv"]=niveau
    x=random.randrange(0,600,L_CARRE)
    y=random.randrange(0,370,L_CARRE)
    fruit["pos"]=[x,y]
    fruit["larg"]=L_CARRE
    
    return fruit
    
def fruit_dessine(fruit):
    """
        dico des éléments de fruit => rien
        Dessine le fruit
    """
    pygame.draw.rect(fruit["niv"]["surf"],(195,0,0),(fruit["pos"][0],fruit["pos"][1],fruit["larg"], fruit["larg"]))
    
    

    
