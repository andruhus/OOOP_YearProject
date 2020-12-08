from Image_to_list_loader import GameOverPict
from ImagePlacingFunc import *
from GameLogicFunc import *
from random import randrange
import pygame


class Game:

    def DrawMatrix(self, a, win):
        for i in range(0, 4):
            for j in range(0, 4):
                DrawCell(a[i][j], i, j, win)
        DrawBackground(win)
        pygame.display.update()

    def __init__(self, win, mode, music, file=None):
        self.mainlist = []
        self.prevlist = []
        self.win = win
        if file == None:
            for i in range(0, 4):
                b = [0, 0, 0, 0]
                self.mainlist.append(b)
            for i in range(0, 4):
                b = [0, 0, 0, 0]
                self.prevlist.append(b)
        else:
            with open(file, "r") as file:
                for i in range(0, 4):
                    line = file.readline()
                    temp_int = ""
                    j = 0
                    b = [0, 0, 0, 0]
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
        self.DrawMatrix(self.mainlist, self.win)

    def PlacingRand(self):
        a = []
        for x in range(0, 4):
            for y in range(0, 4):
                if self.mainlist[x][y] == 0:
                    a.append(CoordIntoNumber(x, y))
        if len(a) > 0:
            pl = randrange(0, len(a), 1)
            x, y = NumberIntoCoord(a[pl])
            self.mainlist[x][y] = 1

    def CHECK_nextMove(self):
        t = self.mainlist
        move_checker = CHECK_TABLES(UpComm(t), self.mainlist) or CHECK_TABLES(DownComm(t),
                                                                              self.mainlist) or CHECK_TABLES(
            LeftComm(t), self.mainlist) or CHECK_TABLES(RightComm(t), self.mainlist)

        for q in self.mainlist:
            for e in q:
                if e == 0:
                    return True

        return move_checker
        # return False

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
        self.win.blit(GameOverPict[index_of_GamOv], (0, 0))
        pygame.display.update()
        In_Game_Over = True
        while In_Game_Over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.runmenu = False
                    In_Game_Over = False
                if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
                    In_Game_Over = False

    def Next_Move(self, key):
        self.run = self.CHECK_nextMove() and self.run
        if self.run:
            if key == "a" and CHECK_TABLES(UpComm(self.mainlist), self.mainlist):
                for i in range(0, 4):
                    for j in range(0, 4):
                        self.prevlist[i][j] = self.mainlist[i][j]
                self.mainlist = UpComm(self.mainlist)
                for i in range(0, self.mode + 1):
                    self.PlacingRand()

            elif key == "w" and CHECK_TABLES(LeftComm(self.mainlist), self.mainlist):
                for i in range(0, 4):
                    for j in range(0, 4):
                        self.prevlist[i][j] = self.mainlist[i][j]
                self.mainlist = LeftComm(self.mainlist)
                for i in range(0, self.mode + 1):
                    self.PlacingRand()

            elif key == "d" and CHECK_TABLES(DownComm(self.mainlist), self.mainlist):
                for i in range(0, 4):
                    for j in range(0, 4):
                        self.prevlist[i][j] = self.mainlist[i][j]
                self.mainlist = DownComm(self.mainlist)
                for i in range(0, self.mode + 1):
                    self.PlacingRand()

            elif key == "s" and CHECK_TABLES(RightComm(self.mainlist), self.mainlist):
                for i in range(0, 4):
                    for j in range(0, 4):
                        self.prevlist[i][j] = self.mainlist[i][j]
                self.mainlist = RightComm(self.mainlist)
                for i in range(0, self.mode + 1):
                    self.PlacingRand()

            elif key == "b":
                for i in range(0, 4):
                    for j in range(0, 4):
                        self.mainlist[i][j] = self.prevlist[i][j]

            elif key == "e":
                self.run = False

            else:
                pass

            self.DrawMatrix(self.mainlist, self.win)
        else:
            self.GameOver()

    def SaveGame(self):
        with open("save.txt", "w") as f:
            for t in self.mainlist:
                for y in t:
                    f.write(str(y) + " ")
                f.write("\n")

    def Stop_Music(self):
        if self.music > 0:
            pygame.mixer.music.stop()

    def Play(self):
        if self.music > 0:
            path_to_music = "Music/"
            pygame.mixer.music.load(path_to_music + str(self.music) + ".mp3")
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



