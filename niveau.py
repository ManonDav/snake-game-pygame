import pygame

def niveau_init(surface):
    """
        surface de dessin => rien
        Initialise le niveau
    """
    niveau={}
    niveau["surf"]=surface
    niveau["score"]=0
    niveau["max_score"]=10000
    niveau["rect_score"]=(0,370,600,30)
    niveau["rect_jeu"]=(0,0,600,370)
    
    return niveau
    
def niveau_dessine(niveau):
    """
        dico des éléments de niveau => rien
        Dessine le niveau
    """
    pygame.draw.rect(niveau["surf"], (255,255,255), niveau["rect_score"])
    pygame.draw.rect(niveau["surf"], (0,0,0), niveau["rect_jeu"])
    
    police=pygame.font.SysFont("arial",15)
    image_score=police.render("Score = "+ str(niveau["score"]),1,(200,55,255))
    niveau["surf"].blit(image_score,(275,378))
    