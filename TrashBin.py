import pygame
import time
import random
pygame.init ()


CAPTION = "FunBin"
ICON = pygame.transform.scale(pygame.image.load('Logo3.png'), (50, 50))


width = 1200
height = 900


screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(ICON)
pygame.display.set_caption(CAPTION)


clock = pygame.time.Clock()


class thing:
    def __init__(self, x, y, Bin):
        self.x = x
        self.y = y
        self.Bin = Bin

def main():
    
    BG = pygame.image.load("background100%.png")
    
    trash = [0]*10
    
    for i in range (0, 10):
        trash[i] = thing((1200+(i*250)), 780, random.randint(1, 3))
    BarColor = (33, 194, 27)
    
    
    main_font = pygame.font.SysFont("MV Boli", 45)
    GlassBinIMG = pygame.image.load("GlassBin.png")
    PaperBinIMG = pygame.image.load("PaperBin.png")
    PlasticMetalBinIMG = pygame.image.load("PlasticMetalBin.png")
    GreatIMG = pygame.image.load("GREAT.png")
    TerribleIMG = pygame.image.load("TERRIBLE.png")
    progress = 100
    
    
    
    timer = 0


    
    
    
    def drawing():
        screen.blit(BG, (0,0))
        screen.blit(GlassBinIMG, (220,470))
        screen.blit(PaperBinIMG, (480,470))
        screen.blit(PlasticMetalBinIMG, (740,470))
        pygame.draw.rect(screen, BarColor, [80, 30, progress*3, 30])
        pygame.draw.rect(screen, (0,0,0), [80, 30, 300, 30], 3)
        
        
        for i in range(0, 10):
            if(trash[i].Bin == 1):
                pygame.draw.rect(screen, (0,255,0), [trash[i].x, trash[i].y, 80, 80])
            if(trash[i].Bin == 2):
                pygame.draw.rect(screen, (0,0,255), [trash[i].x, trash[i].y, 80, 80])
            if(trash[i].Bin == 3):
                pygame.draw.rect(screen, (255,255,0), [trash[i].x, trash[i].y, 80, 80])
            if(trash[i].Bin == 4):
                pygame.draw.rect(screen, (0,0,0), [trash[i].x, trash[i].y, 80, 80])
                
                
        pygame.draw.rect(screen, (0,0,0), [180, 770, 200, 100], 5)
        pygame.draw.rect(screen, (0,0,0), [0, 770, 1200, 100], 2)           
        screen.blit(GreatIMG, (380, 15))
        screen.blit(TerribleIMG, (30, 15))
        pygame.display.update()
    
    
    
    
    running = 1
    while (running == 1):


        
        for i in range (0, 10):
            trash[i].x = trash[i].x - 5  
            if trash[i].x <= -80:
                trash[i].x = 2500
                trash[i].Bin = random.randint(1,3)
        
        if progress < 30 :
            BG = pygame.image.load("background30%.png")
        
        if progress < 50 and progress > 30:
            BG = pygame.image.load("background50%.png")
                
        if progress < 75 and progress > 50:
            BG = pygame.image.load("background75%.png")
        
        if progress > 75:
            BG = pygame.image.load("background100%.png")
        
        if progress > 100:
            progress = 100
        
        drawing()
        progress = progress -0.1
                
            
        
        
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
                
            
        keys = pygame.key.get_pressed()
        for i in range(0, 10):
            if(trash[i].x > 180 and trash[i].x < 380):
                if keys[pygame.K_1]:
                    if(trash[i].Bin == 1):
                        trash[i].x = max(trash[0].x, trash[1].x, trash[2].x, trash[3].x, trash[4].x, trash[5].x, trash[6].x, trash[7].x, trash[8].x, trash[9].x) + 480
                        progress += 6
                if keys[pygame.K_2]:
                    if(trash[i].Bin == 2):
                        trash[i].x = max(trash[0].x, trash[1].x, trash[2].x, trash[3].x, trash[4].x, trash[5].x, trash[6].x, trash[7].x, trash[8].x, trash[9].x) + 480
                        progress += 6
                if keys[pygame.K_3]:
                    if(trash[i].Bin == 3):
                        trash[i].x = max(trash[0].x, trash[1].x, trash[2].x, trash[3].x, trash[4].x, trash[5].x, trash[6].x, trash[7].x, trash[8].x, trash[9].x) + 480
                        progress += 6
                if keys[pygame.K_4]:
                    running = 2
                        
                    
        clock.tick(60)
    else:
        print(str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2))
main()