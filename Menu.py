import pygame
from FuncforGame import Game,CellImages


MENU_IMAGES = [pygame.image.load("MenIm1.JPG"),pygame.image.load("MenIm2.JPG"),pygame.image.load("MenIm3.JPG"),pygame.image.load("MenIm4.JPG"),pygame.image.load("MenIm5.JPG")]
for i in range(0,5):
    MENU_IMAGES[i] = pygame.transform.scale(MENU_IMAGES[i],(500,500))
Instruction = [pygame.image.load("InstrIm1.JPG"),pygame.image.load("InstrIm2.JPG")]
for i in range(0,2):
    Instruction[i] = pygame.transform.scale(Instruction[i],(500,500))

Background = pygame.image.load("background.JPG")
Background = pygame.transform.scale(Background,(500,500))

Heads = []
for i in range(0,2):
    pict = pygame.image.load("head" + str(i+1) + ".JPG")
    Heads.append(pict)
for i in range(0,2):
    Heads[i] = pygame.transform.scale(Heads[i],(150,50))


Mode = []
for i in range(0,3):
    pict = pygame.image.load("mode" + str(i+1) + ".JPG")
    Mode.append(pict)
for i in range(0,3):
    Mode[i] = pygame.transform.scale(Mode[i],(400,50))



Music_Im = []
for i in range(0,5):
    pict = pygame.image.load("music" + str(i+1) + ".JPG")
    Music_Im.append(pict)
for i in range(0,5):
    Music_Im[i] = pygame.transform.scale(Music_Im[i],(400,50))


Mode_Highlighted = []
for i in range(0,3):
    pict = pygame.image.load("modegreen" + str(i+1) + ".JPG")
    Mode_Highlighted.append(pict)
for i in range(0,3):
    Mode_Highlighted[i] = pygame.transform.scale(Mode_Highlighted[i],(400,50))


Music_Im_Highlighted = []
for i in range(0,5):
    pict = pygame.image.load("musicgreen" + str(i+1) + ".JPG")
    Music_Im_Highlighted.append(pict)
for i in range(0,5):
    Music_Im_Highlighted[i] = pygame.transform.scale(Music_Im_Highlighted[i],(400,50))

class Menu:
    def __init__(self):
        self.win = pygame.display.set_mode((500,500))
        pygame.display.set_caption("2048")
        self.win.blit(MENU_IMAGES[0],(0,0))
        pygame.display.update()
        self.run = True
        self.music = 0
        self.mode = 0
        self.count = 0
        self.countkey = 0


    def NewGame(self):
        count = 0
        self.win.blit(Instruction[0],(0,0))
        pygame.display.update()
        while count < 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
                    if count == 0:
                        self.win.blit(Instruction[1],(0,0))
                        pygame.display.update()
                    if count == 1:
                        g = Game(self.win,self.mode,self.music)
                        g.PlacingRand()
                        g.DrawMatrix(g.mainlist,g.win)
                        self.run = g.Play()
                        self.win.blit(MENU_IMAGES[0],(0,0))
                        pygame.display.update()
                        
                        
                    count += 1

    def ResumeGame(self):
        g = Game(self.win,self.mode,self.music,"save.txt")
        g.PlacingRand()
        g.DrawMatrix(g.mainlist,g.win)
        self.run = g.Play()
        self.win.blit(MENU_IMAGES[0],(0,0))
        pygame.display.update()

    def Settings(self):
        Is_Setting_On = True
        keycount = 0
        def DrawSett():
            self.win.blit(Background,(0,0))
            self.win.blit(Heads[0],(50,50))
            pygame.draw.rect(self.win,(0,0,0),(50,98,400,2))
            self.win.blit(Music_Im[self.music],(50,100))
            self.win.blit(Heads[1],(50,250))
            pygame.draw.rect(self.win,(0,0,0),(50,298,400,2))
            self.win.blit(Mode[self.mode],(50,300))
            pygame.display.update()
        DrawSett()
        while Is_Setting_On:
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    Is_Setting_On = False
                if event.type == pygame.KEYUP:
                    
                    def ChangeSettKey(keycount):
                        keycount %= 8
                        DrawSett()
                        if keycount < 5:
                            pygame.draw.rect(self.win,(0,0,0),(50,140,400,2))
                            for i in range(0,5):
                                self.win.blit(Music_Im[i],(50,150 + i*50))
                        else:
                            pygame.draw.rect(self.win,(0,0,0),(50,340,400,2))
                            for i in range(0,3):
                                self.win.blit(Mode[i],(50,350 + i*50))
                        pygame.display.update()
                        if keycount < 5:
                            self.win.blit(Music_Im_Highlighted[keycount],(50,150 + keycount*50))
                            pygame.display.update()
                        else:
                            self.win.blit(Mode_Highlighted[keycount - 5],(50,350 + (keycount-5)*50))
                            pygame.display.update()
                        
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        keycount -= 1
                        ChangeSettKey(keycount)
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        keycount += 1
                        ChangeSettKey(keycount)
                    if event.key == pygame.K_ESCAPE:
                        Is_Setting_On = False
                    if event.key == pygame.K_RETURN:
                        if keycount < 5:
                            self.music = keycount
                        else:
                            self.mode = keycount - 5
                        DrawSett()

    def Exit(self):
        self.run = False

    def Start(self):
        while self.run:
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.countkey -= 1
                        self.countkey %= 4
                        self.win.blit(MENU_IMAGES[self.countkey + 1],(0,0))
                        pygame.display.update()

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.countkey += 1
                        self.countkey %= 4
                        self.win.blit(MENU_IMAGES[self.countkey + 1],(0,0))
                        pygame.display.update()

                    if event.key == pygame.K_RETURN:
                        if self.countkey == 0:
                            self.NewGame()
                        elif self.countkey == 1:
                            self.ResumeGame()
                        elif self.countkey == 2:
                            self.Settings()
                            self.win.blit(MENU_IMAGES[0],(0,0))
                            pygame.display.update()
                        elif self.countkey == 3:
                            self.Exit()
                        else:
                            pass
                    
                if event.type == pygame.MOUSEMOTION:
                   x,y = pygame.mouse.get_pos()
                   if x > 134 and x < 366:
                       if y > 194 and y < 256:
                            self.count = 0
                            self.win.blit(MENU_IMAGES[1],(0,0))
                            pygame.display.update()
                       elif y > 255 and y < 320:
                            self.count = 1
                            self.win.blit(MENU_IMAGES[2],(0,0))
                            pygame.display.update()
                       elif y > 319 and y < 385:
                            self.count = 2
                            self.win.blit(MENU_IMAGES[3],(0,0))
                            pygame.display.update()
                       elif y > 384 and y < 450:
                            self.count = 3
                            self.win.blit(MENU_IMAGES[4],(0,0))
                            pygame.display.update()
                       else:
                            self.count = 4
                            self.win.blit(MENU_IMAGES[0],(0,0))
                            pygame.display.update()
                   else:
                        self.count = 4
                        self.win.blit(MENU_IMAGES[0],(0,0))
                        pygame.display.update()
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.count == 0:
                        self.NewGame()
                    elif self.count == 1:
                        self.ResumeGame()
                    elif self.count == 2:
                        self.Settings()
                        self.win.blit(MENU_IMAGES[0],(0,0))
                        pygame.display.update()
                    elif self.count == 3:
                        self.Exit()
                    else:
                        pass
