from FuncforCell import *
from random import randrange
import pygame

CellImages = [pygame.image.load("Слайд1.JPG"),pygame.image.load("Слайд2.JPG"),pygame.image.load("Слайд3.JPG"),pygame.image.load("Слайд4.JPG"),pygame.image.load("Слайд5.JPG"),pygame.image.load("Слайд6.JPG"),pygame.image.load("Слайд7.JPG"),pygame.image.load("Слайд8.JPG"),pygame.image.load("Слайд9.JPG"),pygame.image.load("Слайд10.JPG"),pygame.image.load("Слайд11.JPG"),pygame.image.load("Слайд12.JPG"),pygame.image.load("Слайд13.JPG"),pygame.image.load("Слайд14.JPG"),pygame.image.load("Слайд15.JPG"),pygame.image.load("Слайд16.JPG")]
for i in range(0,16):
    CellImages[i] = pygame.transform.scale(CellImages[i],(Size,Size))

GameOverPict = []
for i in range(0,9):
    GameOverPict.append(pygame.image.load("GO" + str(i + 1) + ".JPG"))
for i in range(0,9):
    GameOverPict[i] = pygame.transform.scale(GameOverPict[i],(500,500))

def DrawCell(a,b,c,win):
    x,y = Coordinate(b,c)
    if a > 0 and a < 17:
        win.blit(CellImages[a - 1], (x,y))
    else:
        pygame.draw.rect(win, (255,255,255), (x,y,Size,Size))
     
def DrawBackground(win):
    pygame.draw.rect(win, (0,0,0), (250,250 - 2 * Size,3,4 * Size))
    pygame.draw.rect(win, (0,0,0), (250 - Size,250 - 2 * Size,3,4 * Size))
    pygame.draw.rect(win, (0,0,0), (250 + Size,250 - 2 * Size,3,4 * Size))
    pygame.draw.rect(win, (0,0,0), (250 - 2 * Size,250,4 * Size,3))
    pygame.draw.rect(win, (0,0,0), (250 - 2 * Size,250 - Size,4 * Size,3))
    pygame.draw.rect(win, (0,0,0), (250 - 2 * Size,250 + Size,4 * Size,3))





def CoordIntoNumber(x,y):
    return x * 4 + y + 1

def NumberIntoCoord(x):
    x -= 1
    a = x // 4
    b = x % 4
    return a,b




def Presser(list):
    b = [0,0,0,0]
    temp_ind = 0
    for k in list:
        if k != 0:
            if b[temp_ind] == 0:
                b[temp_ind] = k
            else:
                if b[temp_ind] == k:
                    b[temp_ind] += 1
                else:
                    b[temp_ind + 1] = k
                temp_ind += 1
    return b

def LeftComm(ac):
    a = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(0,4):
        for j in range(0,4):
            a[i][j] = ac[i][j]
    for i in range(0,4):
        a[i] = Presser(a[i])
    return a

def RightComm(ac):
    a = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(0,4):
        for j in range(0,4):
            a[i][j] = ac[i][j]
    for i in range(0,4):
        b = [0,0,0,0]
        for j in range(0,4):
            b[3 - j] = a[i][j]
        b = Presser(b)
        for j in range(0,4):
            a[i][j] = b[3 - j]
    return a

def DownComm(ac):
    a = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(0,4):
        for j in range(0,4):
            a[i][j] = ac[i][j]
    for j in range(0,4):
        b = [0,0,0,0]
        for i in range(0,4):
            b[3 - i] = a[i][j]
        b = Presser(b)
        for i in range(0,4):
            a[i][j] = b[3 - i]
    return a

def UpComm(ac):
    a = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(0,4):
        for j in range(0,4):
            a[i][j] = ac[i][j]
    for j in range(0,4):
        b = [0,0,0,0]
        for i in range(0,4):
            b[i] = a[i][j]
        b = Presser(b)
        for i in range(0,4):
            a[i][j] = b[i]
        
    return a



def CHECK_TABLES(a,b):
    for i in range(0,4):
        for j in range(0,4):
            if a[i][j] != b[i][j]:
                return True
    return False




class Game:

    def DrawMatrix(self,a,win):
        for i in range(0,4):
            for j in range(0,4):
                DrawCell(a[i][j],i,j,win)
        DrawBackground(win)
        pygame.display.update()


    def __init__(self,win,mode,music,file=None):
        self.mainlist = []
        self.prevlist = []
        self.win = win
        if file == None:
            for i in range(0,4):
                b = [0,0,0,0]
                self.mainlist.append(b)
            for i in range(0,4):
                b = [0,0,0,0]
                self.prevlist.append(b)
        else:
            with open(file,"r") as file:
                for i in range(0,4):
                    line = file.readline()
                    temp_int = ""
                    j = 0
                    b = [0,0,0,0]
                    for k in line:
                        if k == " ":
                            b[j] = int(temp_int)
                            j += 1
                            temp_int = ""
                        else:
                            temp_int += k
                    self.mainlist.append(b)
                    self.prevlist.append(b)
        self.run = True
        self.runmenu = True
        self.mode = mode
        self.music = music
        self.DrawMatrix(self.mainlist,self.win)

    
    


    def PlacingRand(self):
            a = []
            for x in range(0,4):
                for y in range(0,4):
                    if self.mainlist[x][y] == 0:
                        a.append(CoordIntoNumber(x,y))
            if len(a) > 0:
                pl = randrange(0,len(a),1)
                x,y = NumberIntoCoord(a[pl])
                self.mainlist[x][y] = 1




    def CHECK_nextMove(self):
        t = self.mainlist
        move_checker = CHECK_TABLES(UpComm(t),self.mainlist) or CHECK_TABLES(DownComm(t),self.mainlist) or CHECK_TABLES(LeftComm(t),self.mainlist) or CHECK_TABLES(RightComm(t),self.mainlist)
         

        for q in self.mainlist:
            for e in q:
                if e == 0:
                    return True

        return move_checker
        #return False
   
    def Get_Result_Game_Over(self):
        result = 0
        destination = 2048 * (self.mode + 1)
        for i in self.mainlist:
            for j in i:
                if j > destination:
                    return 2
                if j == destination:
                    result = 1
        return result

    def GameOver(self):
        result = self.Get_Result_Game_Over()
        index_of_GamOv = 3 * self.mode + result
        self.win.blit(GameOverPict[index_of_GamOv],(0,0))
        pygame.display.update()
        In_Game_Over = True
        while In_Game_Over:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.runmenu = False
                        In_Game_Over = False
                    if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
                        In_Game_Over = False

    def Next_Move(self,key):
        self.run = self.CHECK_nextMove() and self.run
        if self.run:
            if key == "a" and CHECK_TABLES(UpComm(self.mainlist),self.mainlist):
                for i in range(0,4):
                    for j in range(0,4):
                        self.prevlist[i][j] = self.mainlist[i][j]
                self.mainlist = UpComm(self.mainlist)
                for i in range(0,self.mode + 1):
                    self.PlacingRand()

            elif key == "w" and CHECK_TABLES(LeftComm(self.mainlist),self.mainlist):
                for i in range(0,4):
                    for j in range(0,4):
                        self.prevlist[i][j] = self.mainlist[i][j]
                self.mainlist = LeftComm(self.mainlist)
                for i in range(0,self.mode + 1):
                    self.PlacingRand()
                
            elif key == "d" and CHECK_TABLES(DownComm(self.mainlist),self.mainlist):
                for i in range(0,4):
                    for j in range(0,4):
                        self.prevlist[i][j] = self.mainlist[i][j]
                self.mainlist = DownComm(self.mainlist)
                for i in range(0,self.mode + 1):
                    self.PlacingRand()
                
            elif key == "s" and CHECK_TABLES(RightComm(self.mainlist),self.mainlist):
                for i in range(0,4):
                    for j in range(0,4):
                        self.prevlist[i][j] = self.mainlist[i][j]
                self.mainlist = RightComm(self.mainlist)
                for i in range(0,self.mode + 1):
                    self.PlacingRand()
                
            elif key == "b":
                for i in range(0,4):
                    for j in range(0,4):
                        self.mainlist[i][j] = self.prevlist[i][j]

            elif key == "e":
                self.run = False

            else:
                pass

            
                
            self.DrawMatrix(self.mainlist,self.win)
        else:
            self.GameOver()
            
    def SaveGame(self):
        with open("save.txt","w") as f:
            for t in self.mainlist:
                for y in t:
                    f.write(str(y) + " ")
                f.write("\n")

    def Stop_Music(self):
        if self.music > 0:
            pygame.mixer.music.stop()

    def Play(self):
        if self.music > 0:
            pygame.mixer.music.load(str(self.music) + ".mp3")
            pygame.mixer.music.play()
        while self.run:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    self.SaveGame()
                    self.Stop_Music()
                    return False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.Next_Move("w")
                    elif event.key == pygame.K_a:
                        self.Next_Move("a")
                    elif event.key == pygame.K_s:
                        self.Next_Move("s")
                    elif event.key == pygame.K_d:
                        self.Next_Move("d")
                    elif event.key == pygame.K_BACKSPACE:
                        self.Next_Move("b")
                    elif event.key == pygame.K_ESCAPE:
                        self.Next_Move("e")
                        self.SaveGame()
                        self.Stop_Music()
                        return True
                    else:
                        pass
        self.Stop_Music()
        return self.runmenu
        


    