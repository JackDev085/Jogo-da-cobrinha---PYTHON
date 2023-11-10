#Importações necessárias para criar o jogo com pygame
import pygame
from pygame.locals import *
from sys import exit
from random import randint

#Iniciando o construtor para construção do jogo
pygame.init()
#Adicionando o valor do volume para a música de fundo
pygame.mixer.music.set_volume(0.1)
#Atribuindo a variável musica_fundo uma música de fundo
musica_fundo = pygame.mixer.music.load('musica.mp3')

pygame.mixer.music.play(-1)
#Adicionando um barulho para som de colisão
barulho_colisao = pygame.mixer.Sound('sm64_coin.wav')

barulho_colisao.set_volume(0.05)
largura = 640
altura = 480
x_cobra=int(largura/2)
y_cobra=int((altura/2))

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(40,600)
y_maca = randint(50,430)
x_cobra
pontos = 0

fonte = pygame.font.SysFont('times new roman', 40,True,True)
#criando a tela de exibição do jogo parametrizado por largura e altura
tela = pygame.display.set_mode((largura,altura))
#Renomeando o nome da janela que exibirá o jogo
pygame.display.set_caption('Jogo')
#Adiciondo um "Relógio" que vai ser usado como
#tempo do jogo
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5
def aumenta_cobra(lista_cobra):
    for xey in lista_cobra:

        pygame.draw.rect(tela, (0,255,0), (xey[0],xey[1],20,20))
#Loop principal do jogo para que ele possa continuar
while True:
    #Adiciona o tempo de velocidade do jogo
    relogio.tick(30)
    #Preenche toda a tela com a cor especificada
    tela.fill((255,255,255))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
    #Para cada evento que acontecer no jogo
    for event in pygame.event.get():
        #Se o evento for sair do jogo ele irá fechar
        if event.type == QUIT:
            pygame.quit()
            exit()
            #Movimentações de objetos
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle =  0
            if event.key == K_d:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade

    x_cobra = x_cobra+x_controle
    y_cobra = y_cobra+y_controle

    # Criando um retângulo no jogo
    # Tela / Cor do objeto / posição do objeto + especificações
    cobra = pygame.draw.rect(tela,(0,255,0),(x_cobra,y_cobra,20,20))
    #Criando um novo retângulo
    comida = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))

    #Adicionando um evento de colisão
    if cobra.colliderect(comida):
        x_maca = randint(40,600)
        y_maca = randint(50,430)
        #Incrementando os pontos quando houver colisão
        pontos = pontos + 1
        #Toda vez que ouver uma colisão será tocado o  som que estiver atribuido a barulho_colisao
        barulho_colisao.play()
        comprimento_inicial = comprimento_inicial + 1
    #Criando um circulo no jogo

    lista_cabeca=[]
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)
    """

               # Tela / Cor do objeto / posição do objeto + raio
    pygame.draw.circle(tela,(0,0,255),(300,260),40)
            #Desenhando uma linha na tela do jogo
                    #Tela / cor da linha / Começo da linha / Final da linha / tamanho da linha
    pygame.draw.line(tela, (255,255,0),(390,0),(390,600),6)
    #Atualizando o display após o término de todos os eventos
    """
    #Exibindo o texto formatado na cordenada desejada
    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()


