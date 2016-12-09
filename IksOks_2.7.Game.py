import pygame
import random

pygame.init()

display_width = 500
display_height = 500

black = (0,0,0)
white = (255,255,255)

yellow = (100,142,253)
pink = (146,250,180)

bright_yellow = (49,105,253)
bright_pink = (62,247,122)

narandzasta = (237,159,107)
tamno_narandzasta = (230,121,49)

zelena = (230,226,117)
tamno_zelena = (235,231,61)

crvena = (243,109,116)
tamno_crvena = (239,56,66)

prazno = " "
figura = ""
igraj = ""

txt = []

for i in range (9):
    txt += " "

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Iks Oks Game')


def things(thingx, thingy, thingw, thingh,debljina_linije, color):
    pygame.draw.line(gameDisplay, color, [thingx, thingy],[thingw, thingh],debljina_linije)

def X_O(txt):
    font = pygame.font.SysFont("comicsansms", 100)
    text = font.render(txt, True, black)

def pozicija(txt,x,y):
    font = pygame.font.SysFont("comicsansms", 100)
    text = font.render(txt, True, black)
    gameDisplay.blit(text,(x,y))


def pobednik():
    s = 0
    
    pobeda = ((0,1,2),
              (3,4,5),
              (6,7,8),
              (0,3,6),
              (1,4,7),
              (2,5,8),
              (0,4,8),
              (2,4,6))
    for i in pobeda:
        for j in i:
            if txt[j] == figura:
                s += 1
                if s == 3:
                    pobednik = figura
                    return pobednik
            
        s = 0
    if prazno not in txt:
        pobednik = "Nereseno"
        return pobednik
    else:
        return None

def dozvoljeni_potezi():
    global prazno
    dozvoljeni_potez = []
    for i in range(9):
        if txt[i] == prazno:
            dozvoljeni_potez.append(i)
    print("\nDozvoljeni potezi: ", dozvoljeni_potez)

    return dozvoljeni_potez

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
  

def button(msg,x,y,w,h,ic,ac,action=None,a="",b=""):
    global figura, igraj

    figura = a
    igraj = b

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)
    

def quitgame():
    pygame.quit()
    quit()

def kraj_igre(a):

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)       
        largeText = pygame.font.SysFont("comicsansms",70)
        TextSurf, TextRect = text_objects(a, largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("PLAY 1",20,400,100,50,yellow,bright_yellow,game_loop,"X", "Igraj")
        button("PLAY 2",140,400,100,50,narandzasta,tamno_narandzasta,game_loop,"O","Igraj")
        button("PLAY 3",260,400,100,50,zelena,tamno_zelena,game_loop,"X")
        button("Quit",380,400,100,50,pink,bright_pink,quitgame)
        button("Uputstvo za igru",150,50,200,50,crvena,tamno_crvena,uputstvo)
        
        pygame.display.update()


def racunar_igra(figura):
    s = 0
    a = 0
    kopija = txt[:]
    prob = None
    
    najbolji_potezi = (4,0,2,6,8,1,3,5,7)
    pobeda = ((0,1,2),
              (3,4,5),
              (6,7,8),
              (0,3,6),
              (1,4,7),
              (2,5,8),
              (0,4,8),
              (2,4,6))

    
    dozvoljeni_potez = dozvoljeni_potezi()

    # ako ima polje da rac pobedi da stavi tu
    for c in dozvoljeni_potez:
        kopija[c] = figura
        
        for i in pobeda:
            for j in i:
                if kopija[j] == figura:
                    s += 1
                    if s == 3:
                        pob = figura
                        if figura == pob:
                            txt[c] = figura
                            return c
                             
            s = 0
        kopija[c] = prazno 

    
    # ako ima polje da covek pobedi da ga blokira
    figura = zamena(figura)
    for b in dozvoljeni_potez:
        kopija[b] = figura
        
        for i in pobeda:
            for j in i:
                if kopija[j] == figura:
                    s += 1
                    if s == 3:
                        pob = figura
                        if figura == pob:
                            figura = zamena(figura)
                            txt[b] = figura
                            return b
            
            s = 0
        kopija[b] = prazno

    # ako ne postoji nijedno od predhodna dva polja,
    # da stavi u polje iz liste najboljih polja
    for f in najbolji_potezi:
        if f in dozvoljeni_potez:
            txt[f] = figura
            return f

def zamena(figura):
    if figura == "X":
        figura = "O"
    elif figura == "O":
        figura = "X"

    return figura
        
def uputstvo():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)

        things(200, 100, 200, 400, 5, black)
        things(300, 100, 300, 400, 5, black)
        things(100, 200, 400, 200, 5, black)
        things(100, 300, 400, 300, 5, black)

        p1 = pozicija("1",115,80)
        p2 = pozicija("2",215,80)
        p3 = pozicija("3",315,80)
        p4 = pozicija("4",115,180)
        p5 = pozicija("5",215,180)
        p6 = pozicija("6",315,180)
        p7 = pozicija("7",115,280)
        p8 = pozicija("8",215,280)
        p9 = pozicija("9",315,280)
        

        button("PLAY 1",20,430,100,50,yellow,bright_yellow,game_loop,"X", "Igraj")
        button("PLAY 2",140,430,100,50,narandzasta,tamno_narandzasta,game_loop,"O", "Igraj")
        button("PLAY 3",260,430,100,50,zelena,tamno_zelena,game_loop,"X")
        button("Quit",380,430,100,50,pink,bright_pink,quitgame)
        button("Nazad!",150,20,200,50,crvena,tamno_crvena,game_intro)
        
        pygame.display.update()

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",70)
        TextSurf, TextRect = text_objects("Iks Oks Game", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("PLAY 1",20,400,100,50,yellow,bright_yellow,game_loop,"X", "Igraj")
        button("PLAY 2",140,400,100,50,narandzasta,tamno_narandzasta,game_loop,"O", "Igraj")
        button("PLAY 3",260,400,100,50,zelena,tamno_zelena,game_loop,"X")
        button("Quit",380,400,100,50,pink,bright_pink,quitgame)
        button("Uputstvo za igru",150,50,200,50,crvena,tamno_crvena,uputstvo)
        
        pygame.display.update()

def igra(broj):
    global figura, txt

    txt[broj] = figura
    if pobednik() == figura:
        a = figura + " je pobedio"
        kraj_igre(a)
    figura = zamena(figura)
    
    
def game_loop():

    global txt, figura

    for i in range (9):
        txt[i] = " "


    if figura == "O":
        broj = random.randrange(0,8)
        txt[broj] = figura
        figura = zamena(figura)
    

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_1:
                    if txt[0] == prazno:
                        broj = 0
                    else:
                        continue
                elif event.key == pygame.K_2:
                    if txt[1] == prazno:
                        broj = 1
                    else:
                        continue
                elif event.key == pygame.K_3:
                    if txt[2] == prazno:
                        broj = 2
                    else:
                        continue
                elif event.key == pygame.K_4:
                    if txt[3] == prazno:
                        broj = 3
                    else:
                        continue
                elif event.key == pygame.K_5:
                    if txt[4] == prazno:
                        broj = 4
                    else:
                        continue
                elif event.key == pygame.K_6:
                    if txt[5] == prazno:
                        broj = 5
                    else:
                        continue
                elif event.key == pygame.K_7:
                    if txt[6] == prazno:
                        broj = 6
                    else:
                        continue
                elif event.key == pygame.K_8:
                    if txt[7] == prazno:
                        broj = 7
                    else:
                        continue
                elif event.key == pygame.K_9:
                    if txt[8] == prazno:
                        broj = 8
                    else:
                        continue

                else:
                    continue

                igra(broj)

                if igraj == "Igraj":
                    broj = racunar_igra(figura)
                    if broj != None:
                        igra(broj)

                if prazno not in txt:
                    a = "Nereseno!"
                    kraj_igre(a)
            
                

        gameDisplay.fill(white)

        things(200, 100, 200, 400, 5, black)
        things(300, 100, 300, 400, 5, black)
        things(100, 200, 400, 200, 5, black)
        things(100, 300, 400, 300, 5, black)
    
        
        p1 = pozicija(txt[0],115,80)
        p2 = pozicija(txt[1],215,80)
        p3 = pozicija(txt[2],315,80)
        p4 = pozicija(txt[3],115,180)
        p5 = pozicija(txt[4],215,180)
        p6 = pozicija(txt[5],315,180)
        p7 = pozicija(txt[6],115,280)
        p8 = pozicija(txt[7],215,280)
        p9 = pozicija(txt[8],315,280)

        
        pygame.display.update()




    

game_intro()
game_loop()
pygame.quit()
quit()
