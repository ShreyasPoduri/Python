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

        self.font = pygame.font.Font(("Splatch.ttf") , 90)
        self.text = self.font.render(f"", True ,(255, 255, 255) )

        self.pl_score = 0 
        self.pc_score = 0

        def player(self):
            if self.rock_btn.clicked(30):
               self.p_option = "rock"
               self.screen.blit(self.choose_rock, (120, 200))

            elif self.paper_btn.clicked(30):
               self.p_option = "paper"
               self.screen.blit(self.choose_paper, (120, 200))

            else: 
               self.scissor_btn.clicked(30)
               self.p_option = "acissor"
               self.screen.blit(self.choose_scissor, (120, 200))

            return self.p_option
        


        def pc_choice(self):
            self.pc_random_choice = ""

            option = ["rock", "paper" ,"scissor"]
            pc_choice = random.choice(list(option))

            if pc_choice == "paper":
                self.pc_random_choice = "paper"
                pc_choice = self.choose_paper

            elif pc_choice == "rock":
                self.pc_random_choice = "rock"
                pc_choice = self.choose_rock

            else:
                pc_choice == "scissors"
                self.pc_random_choice = "scissors"
                pc_choice = self.choose_scissor


            def pl_score_cache(self):

                    self.pl_score = 0
                    self.pc_score = 0

                    pl = self.p_option
                    pc = self.pc_random_choice

                    if pl == "rock" and pc == "paper" or pl == "paper" and pc == "scissor" or pl == "scissors" and pc == "rock":
                        self.pc_score +=1

                    elif pl == pc:
                        pass

                    else:
                        self.pl_score +=1

                    return self.pc_score
            
            def image_reset(self):
                self.screen.blit(self.text, (330, 0))
                self.text = self.font.render("", True, (0,0,0))
                self.screen.blit(self.bg, (0,0))
                self.screen.blit(self.r_btn, (20,500))
                self.screen.blit(self.p_btn, (330,500))
                self.screen.blit(self.c_btn, (640,500))

            def game_loop(self):
                run = True
                pygame.time.Clock()
                rps_game = RpsGame()

                while run:
                    pygame.display.update()
                    self.screen.blit(self.text, (330,0))

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                    
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.rock_button
                    


                






            



               




