import pygame
from niveau import *
from serpent import *
from fruit import *

L_CARRE = 10 # Largeur d’un carre du serpent.
VITESSE = 10 # Vitesse de deplacement du serpent (doit etre egale a L_CARRE).

def main():
    """Fonction principale du programme"""

    pygame.init()
    horloge = pygame.time.Clock()
    surface = pygame.display.set_mode((600,400))
    pygame.display.set_caption("SNAKE")
    continuer = True
    ouverture(surface)
    pygame.time.wait(5000)
    niveau=niveau_init(surface)
    snake=snake_init(niveau,(100,200),4,2)
    fruit=fruit_init(niveau)
    while continuer :
        # Gérer les événements
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                continuer = False
                
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    snake["depl_x"]=VITESSE*-1
                    snake["direction"]="gauche"
                elif event.key==pygame.K_RIGHT:
                    snake["depl_x"]=VITESSE
                    snake["direction"]="droite"
                elif event.key==pygame.K_UP:
                    snake["depl_y"]=VITESSE*-1
                    snake["direction"]="haut"
                elif event.key==pygame.K_DOWN:
                    snake["depl_y"]=VITESSE
                    snake["direction"]="bas"
        
        niveau_dessine(niveau)
        snake_update_pos(snake)
        snake_dessine(snake)
        fruit_dessine(fruit)
        
        if snake_heurte_mur(snake):
            print("Vous êtes mort")
            break
        if snake_mort_queue(snake):
            print("Vous êtes mort")
            break
        if snake_mange(snake,fruit):
            niveau["score"]+=1
            snake_grandit(snake)
        if niveau["max_score"]==niveau["score"]:
            print("Vous avez gagné")
            break
        # Mettre à jour l'écran
        pygame.display.update()
        # Ajuster la vitesse de la boucle
        horloge.tick(15)
    pygame.quit()
    
def ouverture(surface):
    """
        surface de dessin => rien
        Dessine la page d'ouverture
    """
    police=pygame.font.SysFont("arial",35)
    image_texte=police.render("SNAKE",1,(255,255,255))
    surface.blit(image_texte,(260,100))
    
    police2=pygame.font.SysFont("arial",15)
    image_texte2=police2.render("by Manon Davion",1,(255,255,255))
    surface.blit(image_texte2,(325,130))
    
    image_instruction=police2.render("Flèches directionnelles pour diriger le serpent",1,(255,255,255))
    surface.blit(image_instruction,(150,200))
    
    image_instruction2=police2.render("Vous perdez si vous touchez les bords ou le corps de votre serpent",1,(255,255,255))
    image_instruction3=police2.render("Mangez le plus de pommes possibles !!",1,(255,255,255))
    surface.blit(image_instruction2,(150,225))
    surface.blit(image_instruction3,(150,250))
    
    image_version=police2.render("Version 1.1 ",1,(255,255,255))
    surface.blit(image_version,(520,350))
    
    image_date=police2.render("29/11/2022",1,(255,255,255))
    surface.blit(image_date,(520,375))
    pygame.display.flip()
    


    

if __name__ == "__main__":
    main()
    
    
    
    