# -*- coding: utf-8 -*

# Importando as bibliotecas necessárias.
import pygame
import random
import time
from os import path
from config import INIT, QUIT, LEVEL2, LEVEL3
from cenario2 import cenario2
from cenario3 import cenario3

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

# Dados gerais do jogo.
WIDTH = 480 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
UP= 0
DOWN=1
LEFT=2
RIGHT=3

DIRECTION=0



# Classe Jogador que representa a nave
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        
        player_img = pygame.image.load(path.join(img_dir, "link_up.png")).convert()
        self.image = player_img
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (50, 38))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2
        
        # Velocidade da nave
        self.speedx = 0
        self.speedy = 0
        
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = 0
    
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
                    
# Classe Mob que representa os meteoros
class Mob(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        mob_img = pygame.image.load(path.join(img_dir, "Goblin.gif")).convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(mob_img, (50, 38))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        #self.rect.x = random.randrange(WIDTH - self.rect.width)
        # Sorteia um lugar inicial em y
        #self.rect.y = random.randrange(-100, -40)
        rand= random.randint(0,3)
        
        if rand == 0:
            self.rect.x = random.randrange(0, 480)  #altura   
            self.rect.y = random.randrange(-100, -40)         
            self.speedx = random.randrange(-2, 2)             
            self.speedy = random.randrange(2, 9)
        elif rand == 1:
            self.rect.x = random.randrange(-100, -40)
            self.rect.y = random.randrange(0, 600)  #lado
            self.speedx = random.randrange(2, 9)
            self.speedy = random.randrange(-3, 3)
        elif rand == 2:
            self.rect.x = random.randrange(0, 480)  #altura
            self.rect.y = random.randrange(650, 700)
            self.speedx = random.randrange(-3, 3)
            self.speedy = random.randrange(-9, -2)
        elif rand == 3:
            self.rect.x = random.randrange(490, 500)
            self.rect.y = random.randrange(0, 600)  #lado
            self.speedx = random.randrange(-9, -2)
            self.speedy = random.randrange(-3, 3)
        
        # Sorteia uma velocidade inicial
        #self.speedx = random.randrange(1, 3)
        #self.speedy = random.randrange(1, 7)
        
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Se o meteoro passar do final da tela, volta para cima
        #if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
        
        """
        
        if rand == 0:
            self.rect.x = random.randrange(0, 480)  #altura   
            self.rect.y = random.randrange(-100, -40)         
            self.speedx = random.randrange(-2, 2)             
            self.speedy = random.randrange(2, 9)
        elif rand == 1:
            self.rect.x = random.randrange(-100, -40)
            self.rect.y = random.randrange(0, 600)  #lado
            self.speedx = random.randrange(2, 9)
            self.speedy = random.randrange(-3, 3)
        elif rand == 2:
            self.rect.x = random.randrange(0, 480)  #altura
            self.rect.y = random.randrange(650, 700)
            self.speedx = random.randrange(-3, 3)
            self.speedy = random.randrange(-9, -2)
        elif rand == 3:
            self.rect.x = random.randrange(490, 500)
            self.rect.y = random.randrange(0, 600)  #lado
            self.speedx = random.randrange(-9, -2)
            self.speedy = random.randrange(-3, 3)
            
        """

# Classe Bullet que representa os tiros
        
class Bullet(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, x, y,direction):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.direction = direction
        # Carregando a imagem de fundo.
        if self.direction == 0:
            bullet_img = pygame.image.load(path.join(img_dir, "arrow.png")).convert()
            self.image = pygame.transform.scale(bullet_img, (30, 54))
        elif self.direction == 1:
            bullet_img = pygame.image.load(path.join(img_dir, "arrow.down.png")).convert()
            self.image = pygame.transform.scale(bullet_img, (30, 54))
        elif self.direction == 2:
            bullet_img = pygame.image.load(path.join(img_dir, "arrow.left.png")).convert()
            self.image = pygame.transform.scale(bullet_img, (30, 54))
        elif self.direction == 3:
            bullet_img = pygame.image.load(path.join(img_dir, "arrow.right.png")).convert()
            self.image = pygame.transform.scale(bullet_img, (30, 54))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 0
        self.speedx = 0
        
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        
        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()
            
            
pontos = 0            
     
def cenario1(screen,direction_t):
    direction = direction_t
    
# Inicialização do Pygame.
    fonte = pygame.font.SysFont('comicsans', 40, True)
    
    # Tamanho da tela.
    
    
    pontos = 0
    
    
    # Nome do jogo
    
    
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    
    # Carrega o fundo do jogo
    background = pygame.image.load(path.join(img_dir, 'kokiriii.png')).convert()
    background_rect = background.get_rect()
    
    # Carrega os sons do jogo
    pygame.mixer.music.load(path.join(snd_dir, 'kokiri.mp3')) 
    pygame.mixer.music.set_volume(0.4)
    boom_sound = pygame.mixer.Sound(path.join(snd_dir, 'linkdie.wav'))
    destroy_sound = pygame.mixer.Sound(path.join(snd_dir, 'hit.wav'))
    pew_sound = pygame.mixer.Sound(path.join(snd_dir, 'arrowhits.wav'))
    
    # Cria uma nave. O construtor será chamado automaticamente.
    player = Player()
    
    # Cria um grupo de todos os sprites e adiciona a nave.
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    
    # Cria um grupo só dos meteoros
    mobs = pygame.sprite.Group()
    
    # Cria um grupo para tiros
    bullets = pygame.sprite.Group()
    
    # Cria 8 meteoros e adiciona no grupo meteoros
    for i in range(2):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    
    # Comando para evitar travamentos.
    
    # Loop principal.
    pygame.mixer.music.play(loops=-1)
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                running = False
            
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    direction = 2
                    player.speedx = -8
                    player_img = pygame.image.load(path.join(img_dir, "link_left.png")).convert()
                    player.image = player_img
                    player.image = pygame.transform.scale(player_img, (50, 38))
                    player.image.set_colorkey(BLACK)
                if event.key == pygame.K_RIGHT:
                    direction= 3
                    player.speedx = 8
                    player_img = pygame.image.load(path.join(img_dir, "link_right.png")).convert()
                    player.image = player_img
                    player.image = pygame.transform.scale(player_img, (50, 38))
                    player.image.set_colorkey(BLACK)

                # Se for um espaço atira!
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.centerx, player.rect.top, direction)
                    if direction==0:
                        bullet.speedy=-10
                    if direction==1:
                        bullet.speedy=10
                    if direction==2:
                        bullet.speedx= -10
                    if direction==3:
                        bullet.speedx= 10
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    pew_sound.play()
                    

                if event.key == pygame.K_UP:
                    direction= 0
                    player.speedy = -8
                    player_img = pygame.image.load(path.join(img_dir, "link_up.png")).convert()
                    player.image = player_img
                    player.image = pygame.transform.scale(player_img, (50, 38))
                    player.image.set_colorkey(BLACK)
                if event.key == pygame.K_DOWN:
                    direction=1
                    player.speedy = 8
                    player_img = pygame.image.load(path.join(img_dir, "link_down.png")).convert()
                    player.image = player_img
                    player.image = pygame.transform.scale(player_img, (50, 38))
                    player.image.set_colorkey(BLACK)

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                if event.key == pygame.K_UP:
                    player.speedy = 0
                if event.key == pygame.K_DOWN:
                    player.speedy = 0
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
        
        # Verifica se houve colisão entre tiro e meteoro
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits: # Pode haver mais de um
            # O meteoro e destruido e precisa ser recriado
            destroy_sound.play()
            pontos += 100
            
        
        # Verifica se houve colisão entre nave e meteoro
        hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
        if hits:
            # Toca o som da colisão
            boom_sound.play()
            time.sleep(1) # Precisa esperar senão fecha
            state = QUIT
            running = False
            
        if pontos >= 1000:
            state = LEVEL2
            running = False
            
        elif pontos >= 3000:
            state= LEVEL3
            running=False
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        rend_fonte= fonte.render('Pontuação: '+ str(pontos), 1, WHITE)
        retang= rend_fonte.get_rect()
        screen.blit(rend_fonte, retang)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
        tempo = 0
        
        milli = clock.tick()
        seconds= milli*1000
        tempo += seconds
        
        if tempo % 17 == 0:
            m = Mob() 
            all_sprites.add(m)
            mobs.add(m)
                           
    return state

pygame.init()
pygame.mixer.init()    
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The adventures of Link")   
try:
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = cenario1(screen, DIRECTION)
        if state == LEVEL2:
            state = cenario2(screen,DIRECTION)
        if state == LEVEL3:
            state = cenario3(screen,DIRECTION)
        else:
            state = QUIT
finally:
    pygame.quit()
