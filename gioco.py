import pygame
import random
uccellox, uccelloy, uccello_vel, punteggio = 0,0,0,0
basex = 0
tubi = None
class Tubi_c:
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75, 150)
        self.attraversato = False

    def avanza_disegna(self):
        self.x -= vel_avanzamento
        schermo.blit(tubo_giu, (self.x, self.y + 190)) #tentativi (da rivedere)
        schermo.blit(tubo_su, (self.x, self.y - 210))

    def collisione(self, bird, uccellox, uccelloy):
        margine = 6
        uccello_lato_dx = uccellox + bird.get_width() - margine
        uccello_lato_sx = uccellox + margine
        tubo_lato_dx = self.x + tubo_giu.get_width()
        tubo_lato_sx = self.x + margine
        uccello_lato_su = uccelloy + margine
        uccello_lato_giu = uccelloy + bird.get_height() - margine
        tubo_lato_su = self.y + 100
        tubo_lato_giu = self.y + 200
        if uccello_lato_dx > tubo_lato_sx and uccello_lato_sx < tubo_lato_dx:
            if uccello_lato_su < tubo_lato_su or uccello_lato_giu > tubo_lato_giu:
                perso()

def init():
    #global uccellox, uccelloy, uccello_vel, punteggio
    #global basex
    global tubi
    tubi = []
    tubi.append(Tubi_c())
    basex = 0
    uccellox, uccelloy = 60, 150
    uccello_vel = 0
    punteggio = 0

def disegna_ogg(schermo, sfondo, bird, base):
    schermo.blit(sfondo, (0, 0))
    for i in tubi:
        i.avanza_disegna()
    schermo.blit(bird, (uccellox, uccelloy))
    schermo.blit(base, (basex, 400))

    font = pygame.font.Font(None, 30)
    testo_punteggio = font.render(f"Punteggio: {punteggio}", True, (255, 255, 255))
    schermo.blit(testo_punteggio, (10, 10))

def aggiorna(fps):
    pygame.display.update()
    pygame.time.Clock().tick(fps)

def perso():
    global punteggio
    schermo.blit(gameover, (50, 180))
    aggiorna(fps)
    ricomincia = False
    while not ricomincia:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                init()
                ricomincia = True
            if event.type == pygame.QUIT:
                pygame.quit()

pygame.init()
sfondo = pygame.image.load('gioco_py/sfondo.png')
bird = pygame.image.load('gioco_py/uccello.png')
base = pygame.image.load('gioco_py/base.png')
gameover = pygame.image.load('gioco_py/gameover.png')
tubo_giu = pygame.image.load('gioco_py/tubo.png')
tubo_su = pygame.transform.flip(tubo_giu, False, True)

schermo = pygame.display.set_mode((300, 500))
fps = 50
vel_avanzamento = 3
init()

while True:
    basex -= vel_avanzamento
    if basex < -40:
        basex = 0

    uccello_vel += 0.4
    uccelloy += uccello_vel

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            uccello_vel = -7

    if tubi[-1].x < 150 and not tubi[-1].attraversato:
        tubi[-1].attraversato = True
        punteggio += 1
        tubi.append(Tubi_c()) 

    for i in tubi:
        i.collisione(bird, uccellox, uccelloy)

    if uccelloy > 380:
        perso()

    disegna_ogg(schermo, sfondo, bird, base)
    aggiorna(fps)
