import pygame

GameOverPict = []
path_n_comm_name = "Images/Game over/GO"
for i in range(0, 9):
    GameOverPict.append(pygame.image.load(path_n_comm_name + str(i + 1) + ".JPG"))
    GameOverPict[i] = pygame.transform.scale(GameOverPict[i], (500, 500))

Size = 125
CellImages = []
path_n_comm_name = "Images/Nubers/Слайд"
for i in range(0, 16):
    CellImages.append(pygame.image.load(path_n_comm_name + str(i+1)+ ".JPG"))
    CellImages[i] = pygame.transform.scale(CellImages[i], (Size, Size))

MENU_IMAGES = []
path_n_comm_name = "Images/Menu/MenIm"

for i in range(0, 5):
    MENU_IMAGES.append(pygame.image.load(path_n_comm_name + str(i + 1) + ".JPG"))
    MENU_IMAGES[i] = pygame.transform.scale(MENU_IMAGES[i], (500, 500))

Instruction = []
path_n_comm_name = "Images/Instruction/InstrIm"
for i in range(0, 2):
    Instruction.append(pygame.image.load(path_n_comm_name + str(i + 1) + ".JPG"))
    Instruction[i] = pygame.transform.scale(Instruction[i], (500, 500))

    
path_n_comm_name = "Images/background.JPG"
Background = pygame.image.load(path_n_comm_name)
Background = pygame.transform.scale(Background, (500, 500))

Heads = []
path_n_comm_name = "Images/Settings/head"
for i in range(0, 2):
    Heads.append(pygame.image.load(path_n_comm_name + str(i + 1) + ".JPG"))
    Heads[i] = pygame.transform.scale(Heads[i], (150, 50))

Mode = []
path_n_comm_name = "Images/Settings/mode"
for i in range(0, 3):
    Mode.append(pygame.image.load(path_n_comm_name + str(i + 1) + ".JPG"))
    Mode[i] = pygame.transform.scale(Mode[i], (400, 50))

Music_Im = []
path_n_comm_name = "Images/Settings/music"
for i in range(0, 5):
    Music_Im.append(pygame.image.load(path_n_comm_name + str(i + 1) + ".JPG"))
    Music_Im[i] = pygame.transform.scale(Music_Im[i], (400, 50))

Mode_Highlighted = []
path_n_comm_name = "Images/Settings/modegreen"
for i in range(0, 3):
    Mode_Highlighted.append(pygame.image.load(path_n_comm_name + str(i + 1) + ".JPG"))
    Mode_Highlighted[i] = pygame.transform.scale(Mode_Highlighted[i], (400, 50))

Music_Im_Highlighted = []
path_n_comm_name = "Images/Settings/musicgreen"
for i in range(0, 5):
    Music_Im_Highlighted.append(pygame.image.load(path_n_comm_name + str(i + 1) + ".JPG"))
    Music_Im_Highlighted[i] = pygame.transform.scale(Music_Im_Highlighted[i], (400, 50))