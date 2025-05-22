import random 
import pygame

class Button():
    def __init__(self,x,y,width,pos,heigth):
        self.x =  x
        self.y =  y
        self.width = width
        self.heigth = heigth
        self.pos = pos

    def clicked(self,pos):
        self.pos = pygame.mouse.get_pos()
        if self.pos[0] > self.x and self.pos[0] <self.x + self.width:
           if self.pos[1] > self.y and self.pos[0] <self.y + self.heigth:
               return True

        return False
    
class RpsGame():
    def __init__(self):
        pygame.init()
        self.screen = pygame.diplay.set_mode((960,640))  
        pygame.display.set_caption("Rps Smasher") 
        self.bg = pygame.image.load("background.jpg")
        self.r_btn = pygame.image.load("r_button.png").convert_alpha()
        self.p_btn = pygame.image.load("p_button.png").convert_alpha()
        self.s_btn = pygame.image.load("s_button.png").convert_alpha()

        self.choose_rock  =  pygame.image.load("rock.png").convert_alpha()  
        self.choose_paper  =  pygame.image.load("paper.png").convert_alpha()  
        self.choose_scissor =  pygame.image.load("scissor.png").convert_alpha()  
         
        
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.r_btn, (20, 500))
        self.screen.blit(self.p_btn, (330, 500))
        self.screen.blit(self.s_btn, (20, 500))

        self.rock_btn = Button(30, 520, (30, 520), 300, 140)
        self.paper_btn = Button(330, 520, (330, 520), 300, 140)
        self.scissor_btn = Button(640, 520, (640, 520), 300, 140)



