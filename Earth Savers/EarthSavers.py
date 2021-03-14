import pygame
import time
import random
import sys

pygame.init ()

CAPTION = "Earth Savers"
ICON = pygame.transform.scale(pygame.image.load('./Assets/icons/GREAT.png'), (50, 50))
width = 1200
height = 900

screen = pygame.display.set_mode((width, height))
pygame.display.set_icon(ICON)
pygame.display.set_caption(CAPTION)

clock = pygame.time.Clock()
click = False

counter = 0

def main_menu():
    global counter, click
    main_font = pygame.font.SysFont("MV Boli", 45)
    music = pygame.mixer.music.load('./music/Chill.mp3')
    pygame.mixer.music.play(-1)

    main_menuIMG = pygame.image.load("./Assets/backgrounds/main_menu.png")
    
    while True:

        screen.blit(main_menuIMG, (0,0))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(200, 700, 200, 50)
        button_2 = pygame.Rect(800, 700, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                counter = normal()
                main()
        if button_2.collidepoint((mx, my)):
            if click:
                difficulty()
        pygame.draw.rect(screen, (150, 150, 150), button_1)
        pygame.draw.rect(screen, (150, 150, 150), button_2)
        screen.blit(main_font.render("Play",1 , (255,255,255)), (230,690))
        screen.blit(main_font.render("Difficulty",1 , (255,255,255)), (805,690))
        
        

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)



def difficulty():
    global counter, click
    
    main_menuIMG = pygame.image.load("./Assets/backgrounds/main_menu.png")
    main_font = pygame.font.SysFont("MV Boli", 45)
    
    running = True
    while running:
        
        screen.blit(main_menuIMG, (0,0))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(200, 700, 200, 50)
        button_2 = pygame.Rect(510, 700, 200, 50)
        button_3 = pygame.Rect(800, 700, 200, 50)
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
                    
                
        if button_1.collidepoint((mx, my)):
            if click:
                counter = easy()
                main()
        if button_2.collidepoint((mx, my)):
            if click:
                counter = normal()
                main()
        if button_3.collidepoint((mx, my)):
            if click:
                counter = hard()
                main()

        pygame.draw.rect(screen, (150, 150, 150), button_1)
        pygame.draw.rect(screen, (150, 150, 150), button_2)
        pygame.draw.rect(screen, (150, 150, 150), button_3)
        
        screen.blit(main_font.render("Easy",1 , (255,255,255)), (240, 690))
        screen.blit(main_font.render("Normal",1 , (255,255,255)), (520, 690))
        screen.blit(main_font.render("Hard",1 , (255,255,255)), (840, 690))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()
        clock.tick(60)

        
         
        
def easy():
    return 4


def normal():
    return 6


def hard():
    return 8        
        
        
        

class thing:
    def __init__(self, x, y, Bin, ID):
        self.x = x
        self.y = y
        self.Bin = Bin
        self.ID = ID
        
        


        
        
        
        
def main():
    
    TrashSpeed = 5
    ProgressSpeed = 0.1
    lastX = 0
    
    Glasses = 0
    GlassBottles = 0
    Boxes = 0 
    Newspapers = 0
    Cans = 0
    PlasticBags = 0
    
    music = pygame.mixer.music.load('./music/ingame_music.mp3')
    pygame.mixer.music.play(-1)
    
    BG = pygame.image.load("./Assets/backgrounds/background100%.png")
    
    trash = [0]*10
    for i in range (0, 10):
        trash[i] = thing((1200+(i*250)), 780, random.randint(1, 3), random.randint(1, 2))
        
    main_font = pygame.font.SysFont("MV Boli", 45)
    
    
    END = pygame.image.load("./Assets/backgrounds/End_screen.png")
    ENDX = 1300
    ENDY = 0
    
    GlassBinIMG = pygame.transform.scale(pygame.image.load("./Assets/bins/GlassBin.png"), (210, 289))
    
    PaperBinIMG = pygame.transform.scale(pygame.image.load("./Assets/bins/PaperBin.png"), (210, 289))
    
    PlasticMetalBinIMG = pygame.transform.scale(pygame.image.load("./Assets/bins/PlasticMetalBin.png"), (210, 289))
    
    
    GreatIMG = pygame.image.load("./Assets/icons/GREAT.png")
    TerribleIMG = pygame.image.load("./Assets/icons/TERRIBLE.png")
    
    
    GlassBottleIMG = pygame.image.load("./Assets/trash/glass_bottle.png")
    BoxIMG = pygame.image.load("./Assets/trash/box.png")
    BagIMG = pygame.transform.scale(pygame.image.load("./Assets/trash/plastic_bag.png"), (90, 90))
    CanIMG = pygame.transform.scale(pygame.image.load("./Assets/trash/can.png"), (90, 90))
    NewspaperIMG = pygame.image.load("./Assets/trash/newspaper.png")
    GlassIMG = pygame.image.load("./Assets/trash/glass.png")
    points = 0
    progress = 100
    BarColor = (33, 194, 27)

    def drawing():

        
        
        screen.blit(BG, (0,0))
        screen.blit(GlassBinIMG, (220,470))
        screen.blit(PaperBinIMG, (480,470))
        screen.blit(PlasticMetalBinIMG, (740,470))
        pygame.draw.rect(screen, BarColor, [80, 30, progress*3, 30])
        pygame.draw.rect(screen, (0,0,0), [80, 30, 300, 30], 3)
        Score_display = main_font.render(f"Player score : {points}",1 , (0,0,0))
        End_Score_display = main_font.render(f"PLAYER SCORE : {points}",1 , (0,0,0))
        screen.blit(Score_display, (700,20))
        
        
        
        for i in range(0, 10):
            if(trash[i].Bin == 1):
                if(trash[i].ID == 1):
                    screen.blit(GlassBottleIMG,(trash[i].x, trash[i].y))
                if(trash[i].ID == 2):
                    screen.blit(GlassIMG,(trash[i].x, trash[i].y))
                    
            if(trash[i].Bin == 2):
                if(trash[i].ID == 1):
                    screen.blit(BoxIMG,(trash[i].x, trash[i].y))
                elif(trash[i].ID == 2):
                    screen.blit(NewspaperIMG,(trash[i].x, trash[i].y))
            if(trash[i].Bin == 3):
                if(trash[i].ID == 1):
                    screen.blit(BagIMG,(trash[i].x, trash[i].y))
                elif(trash[i].ID == 2):
                    screen.blit(CanIMG,(trash[i].x, trash[i].y))
                
                
                
        pygame.draw.rect(screen, (0,0,0), [180, 770, 200, 100], 5)
        pygame.draw.rect(screen, (0,0,0), [0, 770, 1200, 100], 2)           
        screen.blit(GreatIMG, (380, 15))
        screen.blit(TerribleIMG, (30, 15))
        screen.blit(END, (ENDX, ENDY))
        
        if(ENDX == 0 and ENDY == 0):
            screen.blit(End_Score_display, (300,200))
            screen.blit(main_font.render(f"Glass bottles missed: {GlassBottles}",1 , (0,0,0)), (300,300))
            screen.blit(main_font.render(f"Glasses missed: {Glasses}",1 , (0,0,0)), (300,400))
            screen.blit(main_font.render(f"Boxes missed: {Boxes}",1 , (0,0,0)), (300,500))
            screen.blit(main_font.render(f"Newspapers missed: {Newspapers}",1 , (0,0,0)), (300,600))
            screen.blit(main_font.render(f"Cans missed: {Cans}",1 , (0,0,0)), (300,700))
            screen.blit(main_font.render(f"Plastic bag missed: {PlasticBags}",1 , (0,0,0)), (300,800))
            
            
            for i in range(0, 10):
                trash[i].x = 1300
            print(min(trash[0].x, trash[1].x, trash[2].x, trash[3].x, trash[4].x, trash[5].x, trash[6].x, trash[7].x, trash[8].x, trash[9].x))
            
        
        
        pygame.display.update()
    
    running = 1
    while (running == 1):
        
        
        progress -= ProgressSpeed
        drawing()
        
        
        lastX = max(trash[0].x, trash[1].x, trash[2].x, trash[3].x, trash[4].x, trash[5].x, trash[6].x, trash[7].x, trash[8].x, trash[9].x)
        
        for i in range (0, 10):
            trash[i].x = trash[i].x - TrashSpeed
            if trash[i].x <= 0:
                if(trash[i].Bin == 1):
                    if(trash[i].ID == 1):
                        GlassBottles += 1
                    if(trash[i].ID == 2):
                        Glasses += 1
                if(trash[i].Bin == 2):
                    if(trash[i].ID == 1):
                        Boxes += 1
                    elif(trash[i].ID == 2):
                        Newspapers += 1
                if(trash[i].Bin == 3):
                    if(trash[i].ID == 1):
                        PlasticBags += 1
                    elif(trash[i].ID == 2):
                        Cans += 1
                trash[i].x = 2500
                trash[i].Bin = random.randint(1,3)
                progress -= punish
        
        if progress < 10 :
            BG = pygame.image.load("./Assets/backgrounds/background10%.png")
        if progress < 20 and progress > 10:
            BG = pygame.image.load("./Assets/backgrounds/background20%.png")
        if progress < 30 and progress > 20:
            BG = pygame.image.load("./Assets/backgrounds/background30%.png")
        if progress < 40 and progress > 30:
            BG = pygame.image.load("./Assets/backgrounds/background40%.png")
        if progress < 50 and progress > 40:
            BG = pygame.image.load("./Assets/backgrounds/background50%.png")
        if progress < 60 and progress > 50:
            BG = pygame.image.load("./Assets/backgrounds/background60%.png")
        if progress < 70 and progress > 60:
            BG = pygame.image.load("./Assets/backgrounds/background70%.png")
        if progress < 100 and progress > 70:
            BG = pygame.image.load("./Assets/backgrounds/background100%.png")
        
        if progress > 100:
            progress = 100
        if progress <= 0 :
            ENDX = 0
            ENDY = 0
        
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
                
            
        keys = pygame.key.get_pressed()
             
        punish = counter
        
        for i in range(0, 10):
            if (trash[i].x > 180 and trash[i].x < 380):
                if keys[pygame.K_1]:
                    if (trash[i].Bin == 1):
                        trash[i].x = lastX + 480
                        progress += 6
                        points += 10
                        
                if keys[pygame.K_2]:
                    if (trash[i].Bin == 2):
                        trash[i].x = lastX + 480
                        progress += 6
                        points += 10
                        
                if keys[pygame.K_3]:
                    if (trash[i].Bin == 3):
                        trash[i].x = lastX + 480
                        progress += 6
                        points += 10
                        
        for i in range(0, 10):
            if (trash[i].x <= -70):
                progress -= punish * 2
                trash[i].x = 2500
                trash[i].Bin = random.randint(1,3)
                trash[i].ID = random.randint(1,2)
                        
            if keys[pygame.K_ESCAPE]:
                ProgressSpeed = 0
                TrashSpeed = 0

            else:
                ProgressSpeed = 0.1
                TrashSpeed = 5
        clock.tick(60)

main_menu()
