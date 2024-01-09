import pygame
import random

class tubi_c:
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75,150) #genero casuale la pos verticale   
    def avanza_disegna(self):
        self.x -= vel_avanzamento
        schermo.blit(tubo_giu, (self.x, self.y+210))
        schermo.blit(tubo_su, (self.x,self.y-210))
    def collisione(self,bird, uccellox, uccelloy):
      #devo calcolare i confini dei tubi
      margine = 5
      uccello_lato_dx = uccellox+bird.get_width()-margine
      uccello_lato_sx = uccellox+margine
      tubo_lato_dx = self.x+tubo_giu.get_width()
      tubo_lato_sx = self.x + margine
      uccello_lato_su = uccelloy + margine
      uccello_lato_giu = uccelloy+bird.get_height()-margine
      tubo_lato_su = self.y+110
      tubo_lato_giu= self.y+210
      if uccello_lato_dx > tubo_lato_sx and uccello_lato_sx < tubo_lato_dx:
          if uccello_lato_su < tubo_lato_su or uccello_lato_giu > tubo_lato_giu:
            perso(schermo,gameover,fps)

def init():
    global uccellox, uccelloy, uccello_vel
    global basex
    global tubi
    tubi = []
    tubi.append(tubi_c())
    basex = 0
    uccellox, uccelloy = 60, 150
    uccello_vel = 0
    
def disegna_ogg(schermo,sfondo,bird,base):
    schermo.blit(sfondo, (0,0))
    for i in tubi:
        i.avanza_disegna()
    schermo.blit(bird,(uccellox,uccelloy))
    schermo.blit(base, (basex,400))

def aggiorna(fps):
    pygame.display.update()
    pygame.time.Clock().tick(fps) #gli dico con quanti fps aggiornare

def perso(schermo,gameover,fps):
    schermo.blit(gameover, (50,180))
    aggiorna(fps)
    ricomincia = False
    while not ricomincia:
        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE): # se premo lo spazio ricomincio altrimenti nulla
                init()
                ricomincia = True #rinizio il gioco
            if event.type == pygame.QUIT:
                pygame.quit()

    
pygame.init()
sfondo = pygame.image.load('gioco_py/sfondo.png')
bird = pygame.image.load('gioco_py/uccello.png')
base = pygame.image.load('gioco_py/base.png')
gameover = pygame.image.load('gioco_py/gameover.png')
tubo_giu = pygame.image.load('gioco_py/tubo.png')
tubo_su = pygame.transform.flip(tubo_giu, False, True) #1 campo immagine da cambiare, 2 flip orizzontale, 3 flip verticale

schermo = pygame.display.set_mode((288, 512)) #dimensione cellulare
fps = 50
vel_avanzamento = 3
init()

while True: #il gioco va all'infinito
    basex -= vel_avanzamento #sposto la base a sinistra
    if basex < -40: #test
        basex = 0 # se basex < -40 lo riporto a 0 cosi si ripete nello schermo
    
    uccello_vel += 0.4
    uccelloy += uccello_vel #gravita
    
    for event in pygame.event.get(): #legge eventi come clic mouse o tasti premuti 
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_UP): #controlla se premo freccia in su (k_up)
            uccello_vel = -7 #smette di scendere e sale
        if event.type == pygame.QUIT: #se clicco sulla x chiudo il gioco
            pygame.quit() 
    if tubi[-1].x < 150: #se la pos x dell'ultimo tubo in lista è minore di 150 ne creo un'altro
        tubi.append(tubi_c())
    for i in tubi:
        i.collisione(bird,uccellox,uccelloy)
    if uccelloy > 380: # se tocco il pavimento perdo
        perso(schermo,gameover,fps)
    
    
    disegna_ogg(schermo,sfondo,bird,base)
    aggiorna(fps) #aggiorno lo schermo
    