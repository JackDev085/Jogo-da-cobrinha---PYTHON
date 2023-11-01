#Importações necessárias para criar o jogo com pygame
import pygame
from pygame.locals import *
from sys import exit

#Iniciando o construtor para construção do jogo
pygame.init()

largura = 640
altura = 480
#criando a tela de exibição do jogo parametrizado por largura e altura
tela = pygame.display.set_mode((largura,altura))
#Renomeando o nome da janela que exibirá o jogo
pygame.display.set_caption('Jogo')

#Loop principal do jogo para que ele possa continuar
while True:
    #Para cada evento que acontecer no jogo
    for event in pygame.event.get():
        #Se o evento for sair do jogo ele irá fechar
        if event.type == QUIT:
            pygame.quit()
            exit()
            #Criando um retângulo no jogo
                    #Tela / Cor do objeto / posição do objeto + especificações
    pygame.draw.rect(tela,(255,0,0),(200,300,40,50))
            #Criando um circulo no jogo
                    # Tela / Cor do objeto / posição do objeto + raio
    pygame.draw.circle(tela,(0,0,255),(300,260),40)
            #Desenhando uma linha na tela do jogo
                    #Tela / cor da linha / Começo da linha / Final da linha / tamanho da linha
    pygame.draw.line(tela, (255,255,0),(390,0),(390,600),6)
    #Atualizando o display após o término de todos os eventos
    pygame.display.update()


