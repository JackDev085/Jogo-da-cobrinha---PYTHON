#Importações necessárias para criar o jogo com pygame
import pygame
from pygame.locals import *
from sys import exit

#Iniciando o construtor para construção do jogo
pygame.init()

largura = 640
altura = 480
x=largura/2
y=altura/2
#criando a tela de exibição do jogo parametrizado por largura e altura
tela = pygame.display.set_mode((largura,altura))
#Renomeando o nome da janela que exibirá o jogo
pygame.display.set_caption('Jogo')
#Adiciondo um "Relógio" que vai ser usado como
#tempo do jogo
relogio = pygame.time.Clock()


#Loop principal do jogo para que ele possa continuar
while True:
    #Adiciona o tempo de velocidade do jogo
    relogio.tick(30)
    #Preenche toda a tela com a cor especificada
    tela.fill((0,0,0))
    #Para cada evento que acontecer no jogo
    for event in pygame.event.get():
        #Se o evento for sair do jogo ele irá fechar
        if event.type == QUIT:
            pygame.quit()
            exit()
            """
            #Movimentações de objetos
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20
                """
    #Movimentando o objeto de forma constante
    #utilizando as teclas
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    # Criando um retângulo no jogo
    # Tela / Cor do objeto / posição do objeto + especificações
    pygame.draw.rect(tela,(255,0,0),(x,y,40,50))

            #Criando um circulo no jogo
    """
               # Tela / Cor do objeto / posição do objeto + raio
    pygame.draw.circle(tela,(0,0,255),(300,260),40)
            #Desenhando uma linha na tela do jogo
                    #Tela / cor da linha / Começo da linha / Final da linha / tamanho da linha
    pygame.draw.line(tela, (255,255,0),(390,0),(390,600),6)
    #Atualizando o display após o término de todos os eventos
    """
    pygame.display.update()


