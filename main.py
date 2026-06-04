import pygame
import random
from recursos.funcoes import inicializarBancoDeDados, limpar_tela, escreverDados, maior_pontuador

limpar_tela()
inicializarBancoDeDados()
nome_maior, maior_pontos, dataJogada = maior_pontuador()
pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()
somDeEntrada = pygame.mixer.Sound("base/SomDeInicio.wav")
pygame.mixer.music.load("base/MusicaDaTelaRodando.mp3")
while True:
    nome = input("Informe o Nome do Competidor:")
    if len(nome) > 0: 
        break
    else:
        print("Nome Inválido!")

       
tamanho = (1000,700)
pygame.display.set_caption("RacerBoom")
icone  = pygame.image.load("base/icone.png")
pygame.display.set_icon(icone)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho ) 
branco = (255, 255, 255)
preto = (0, 0, 0)

fundo = pygame.image.load("base/beckground.png")
fundoDead = pygame.image.load("base/backgroundDead.jpg")
fundoStart = pygame.image.load("base/backgroundStart.jpg")

Skyline = pygame.image.load("base/CarroSKYLine.png")
Skyline = pygame.transform.scale(Skyline, (150,90))
Caminhao = pygame.image.load("base/Caminhao.png")
Caminhao = pygame.transform.scale(Caminhao, (150,150))
missileSound = pygame.mixer.Sound("base/missile.wav")
explosaoSound = pygame.mixer.Sound("base/explosao.wav")
fonteMenu = pygame.font.SysFont("comicsans",18)

def jogar():
    somDeEntrada.stop()
    pygame.mixer.music.play()
    
    fundoMov1 = 0
    fundoMov2 = -2108
    posicaoXSkyline = 425
    posicaoYSkyline = 475
    movimentoXSkyline  = 0
    movimentoYSkyline  = 0
    velocidadeMovSkyline = 5
    posicaoXCaminhao = random.choice([315, 370, 425, 480, 535])
    posicaoYCaminhao = -100
    velocidadeCaminhao = 2
    pontos = 0
    pygame.mixer.Sound.play(missileSound)
    pygame.mixer.music.play(-1)
    dificuldade = 20
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
                movimentoXSkyline = 0
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
                movimentoXSkyline = velocidadeMovSkyline
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
                movimentoXSkyline = -velocidadeMovSkyline
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
                movimentoXSkyline = 0
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
                movimentoXSkyline = 0
                
        
        posicaoXSkyline = posicaoXSkyline + movimentoXSkyline          
        posicaoYSkyline = posicaoYSkyline + movimentoYSkyline            
        if posicaoXSkyline < 315:
            posicaoXSkyline = 315
        elif posicaoXSkyline > 535:
            posicaoXSkyline = 535
        if posicaoYSkyline < 0 :
            posicaoYSkyline = 0
        elif posicaoYSkyline > 550:
            posicaoYSkyline = 550
            
            
        posicaoYCaminhao = posicaoYCaminhao + velocidadeCaminhao
        if posicaoYCaminhao > 800:
            pygame.mixer.Sound.play(missileSound)
            posicaoYCaminhao = -100
            posicaoXCaminhao = random.choice([315, 370, 425, 480, 535])
            pontos = pontos + 1
            velocidadeCaminhao = velocidadeCaminhao + 1
                            
        tela.fill(branco)
        tela.blit(fundo, (0, fundoMov1))
        tela.blit(fundo, (0, fundoMov2))
        fundoMov1 += 1
        fundoMov2 += 1

        if fundoMov1 >= 2108:
            fundoMov1 = -2108
        if fundoMov2 >= 2108:
            fundoMov2 = -2108

        tela.blit(Skyline, (posicaoXSkyline, posicaoYSkyline))
        tela.blit(Caminhao, (posicaoXCaminhao, posicaoYCaminhao))

        texto = fonteMenu.render("Pontos: " + str(pontos), True, branco)
        tela.blit(texto, (700, 15))

        fonte_coord = pygame.font.SysFont("Arial", 25)
        texto_posicao = fonte_coord.render(f"X: {posicaoXSkyline} | Y: {posicaoYSkyline}", True, (255, 255, 255))
        tela.blit(texto_posicao, (10, 10))
            
        pixelsSkylineX = list(range(posicaoXSkyline, posicaoXSkyline + 116))
        pixelsSkylineY = list(range(posicaoYSkyline, posicaoYSkyline + 60))
        pixelsCaminhaoX = list(range(posicaoXCaminhao, posicaoXCaminhao + 60))
        pixelsCaminhaoY = list(range(posicaoYCaminhao, posicaoYCaminhao + 137))

        if len(list(set(pixelsCaminhaoY).intersection(set(pixelsSkylineY)))) > dificuldade:
            if len(list(set(pixelsCaminhaoX).intersection(set(pixelsSkylineX)))) > dificuldade:
                escreverDados(nome, pontos)
                dead()
                
            else:
                print("Ainda Vivo, mas por pouco!")
        else:
            print("Ainda Vivo")
        
        
        pygame.display.update()
        relogio.tick(60)

def dead():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    larguraButtonStart = 150
    alturaButtonStart  = 40
    larguraButtonQuit = 150
    alturaButtonQuit  = 40
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 140
                    alturaButtonStart  = 35
                if quitButton.collidepoint(evento.pos):
                    larguraButtonQuit = 140
                    alturaButtonQuit  = 35

                
            elif evento.type == pygame.MOUSEBUTTONUP:
                # Verifica se o clique foi dentro do retângulo
                if startButton.collidepoint(evento.pos):
                    #pygame.mixer.music.play(-1)
                    larguraButtonStart = 150
                    alturaButtonStart  = 40
                    jogar()
                if quitButton.collidepoint(evento.pos):
                    #pygame.mixer.music.play(-1)
                    larguraButtonQuit = 150
                    alturaButtonQuit  = 40
                    quit()
            
        tela.fill(branco)
        tela.blit(fundoDead, (0,0))
        startButton = pygame.draw.rect(tela, branco, (10,10, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteMenu.render("Iniciar Game", True, preto)
        tela.blit(startTexto, (25,12))
        
        quitButton = pygame.draw.rect(tela, branco, (10,60, larguraButtonQuit, alturaButtonQuit), border_radius=15)
        quitTexto = fonteMenu.render("Sair do Game", True, preto)
        tela.blit(quitTexto, (25,62))


        pygame.display.update()
        relogio.tick(60)



def start():
    somDeEntrada.play()
    larguraButtonStart = 150
    alturaButtonStart  = 40
    larguraButtonQuit = 150
    alturaButtonQuit  = 40
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 140
                    alturaButtonStart  = 35
                if quitButton.collidepoint(evento.pos):
                    larguraButtonQuit = 140
                    alturaButtonQuit  = 35
                    pygame.mixer.music.stop()

                
            elif evento.type == pygame.MOUSEBUTTONUP:
                # Verifica se o clique foi dentro do retângulo
                if startButton.collidepoint(evento.pos):
                    #pygame.mixer.music.play(-1)
                    larguraButtonStart = 150
                    alturaButtonStart  = 40
                    jogar()
                if quitButton.collidepoint(evento.pos):
                    #pygame.mixer.music.play(-1)
                    larguraButtonQuit = 150
                    alturaButtonQuit  = 40
                    quit()
            
        tela.fill(branco)
        tela.blit(fundoStart, (0,0))
        startButton = pygame.draw.rect(tela, branco, (10,10, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteMenu.render("Iniciar Game", True, preto)
        tela.blit(startTexto, (25,12))
        
        quitButton = pygame.draw.rect(tela, branco, (10,60, larguraButtonQuit, alturaButtonQuit), border_radius=15)
        quitTexto = fonteMenu.render("Sair do Game", True, preto)
        tela.blit(quitTexto, (25,62))
        texto = fonteMenu.render(f"The Best - {nome_maior} - {maior_pontos} - { dataJogada} ", True, branco)
        tela.blit(texto, (480,15))
        

        pygame.display.update()
        relogio.tick(60)
           
start()