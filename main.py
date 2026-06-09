import pygame
import random
import json
import sys
import pyttsx3
import threading
from recursos.funcoes import inicializarBancoDeDados, limpar_tela, escreverDados, maior_pontuador
from recursos.trabalho import verificar_conquistas


limpar_tela()
inicializarBancoDeDados()
nome_maior, maior_pontos, dataJogada = maior_pontuador()
pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()
somDeEntrada = pygame.mixer.Sound("base/SomDeInicio.wav")
pygame.mixer.music.load("base/MusicaDaTelaRodando.mp3")

def falar(texto):
    def _falar():
        engine = pyttsx3.init()
        engine.say(texto)
        engine.runAndWait()
    threading.Thread(target=_falar, daemon=True).start()

falar("Bem vindo ao Highway Dodgers. Digite o seu nome")
print("Bem vindo, digite o seu nome")
while True:
    nome = input("Informe o Nome do Competidor:")
    if len(nome) > 0 and nome.replace(" ", "").isalnum():
        break
    else:
        print("Nome Inválido! Use apenas letras e números.")

       
tamanho = (1000,700)
pygame.display.set_caption("RacerBoom")
icone  = pygame.image.load("base/icone.png")
pygame.display.set_icon(icone)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho ) 
branco = (255, 255, 255)
preto = (0, 0, 0)

fundo = pygame.image.load("base/beckground.png")
fundoDead = pygame.image.load("base/backgroundDead.png")
fundoStart = pygame.image.load("base/backgroundStart.png")
sol_imagem = pygame.image.load("base/sol.png")

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
    
    pausado = False
    fundoMov1 = 0
    fundoMov2 = -2108
    velocidadeFundo = 1
    posicaoXSkyline = 425
    posicaoYSkyline = 475
    movimentoXSkyline  = 0
    movimentoYSkyline  = 0
    velocidadeMovSkyline = 5
    posicaoXCaminhao = random.choice([315, 370, 425, 480, 535])
    posicaoYCaminhao = -100
    velocidadeCaminhao = 5
    pontos = 0
    pygame.mixer.Sound.play(missileSound)
    pygame.mixer.music.play(-1)
    dificuldade = 20

    tamanho_sol = 100              
    velocidadePulso = 0.5
    
    conquista_texto = ""
    conquista_timer = 0
    fonte_conquista = pygame.font.SysFont("comicsans", 22, bold=True)

    # nuvem decorativa
    nuvem_x = random.randint(0, 800)
    nuvem_y = random.randint(20, 120)
    nuvem_vel = random.uniform(0.5, 2.0)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif evento.key == pygame.K_SPACE:
                    if pausado == True:
                        pausado = False
                        pygame.mixer.music.unpause()
                    elif pausado == False:
                        pausado = True
                        pygame.mixer.music.pause()

            if pausado == False:
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
                    movimentoXSkyline = velocidadeMovSkyline
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
                    movimentoXSkyline = -velocidadeMovSkyline
                elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
                    movimentoXSkyline = 0
                elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
                    movimentoXSkyline = 0
                
        if pausado == False:
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
                velocidadeFundo = velocidadeFundo + 1
                
                conquista = verificar_conquistas(pontos, nome)
                if conquista != "":
                    print("NOVA CONQUISTA: " + conquista)
                    conquista_texto = " " + conquista
                    conquista_timer = 180  # 3 segundos a 60fps
                                
            fundoMov1 = fundoMov1 + velocidadeFundo
            fundoMov2 = fundoMov2 + velocidadeFundo

            if fundoMov1 >= 2108:
                fundoMov1 = fundoMov2 - 2108
            if fundoMov2 >= 2108:
                fundoMov2 = fundoMov1 - 2108

            tamanho_sol = tamanho_sol + velocidadePulso
            
            if tamanho_sol > 100:
                velocidadePulso = -0.5
            elif tamanho_sol < 90:
                velocidadePulso = 0.5

            # movimento da nuvem
            nuvem_x -= nuvem_vel
            if nuvem_x < -200:
                nuvem_x = random.randint(1000, 1200)
                nuvem_y = random.randint(20, 120)
                nuvem_vel = random.uniform(0.5, 2.0)

            pixelsSkylineX = list(range(posicaoXSkyline, posicaoXSkyline + 60))
            pixelsSkylineY = list(range(posicaoYSkyline, posicaoYSkyline + 100))
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

        tela.fill(branco)
        tela.blit(fundo, (0, fundoMov1))
        tela.blit(fundo, (0, fundoMov2))
        
        sol_redimensionado = pygame.transform.scale(sol_imagem, (int(tamanho_sol), int(tamanho_sol)))
        rect_sol = sol_redimensionado.get_rect(center=(80, 80))
        tela.blit(sol_redimensionado, rect_sol)

        # desenha nuvem decorativa
        cor_nuvem = (220, 220, 220)
        pygame.draw.ellipse(tela, cor_nuvem, (int(nuvem_x),      int(nuvem_y),      80, 40))
        pygame.draw.ellipse(tela, cor_nuvem, (int(nuvem_x) + 20, int(nuvem_y) - 20, 60, 40))
        pygame.draw.ellipse(tela, cor_nuvem, (int(nuvem_x) + 50, int(nuvem_y) - 10, 70, 35))
        
        tela.blit(Skyline, (posicaoXSkyline, posicaoYSkyline))
        tela.blit(Caminhao, (posicaoXCaminhao, posicaoYCaminhao))

        texto = fonteMenu.render("Pontos: " + str(pontos), True, branco)
        tela.blit(texto, (700, 15))

        fonte_coord = pygame.font.SysFont("Arial", 25)
        texto_posicao = fonte_coord.render(f"X: {posicaoXSkyline} | Y: {posicaoYSkyline}", True, (255, 255, 255))
        tela.blit(texto_posicao, (10, 10))
        
        if pausado == True:
            texto_pause = fonteMenu.render("Game pausado", True, branco)
            tela.blit(texto_pause, (450, 300))

        if conquista_timer > 0:
            conquista_timer -= 1
            surf = fonte_conquista.render(conquista_texto, True, (255, 215, 0))
            bg = pygame.Surface((surf.get_width() + 20, surf.get_height() + 10), pygame.SRCALPHA)
            bg.fill((0, 0, 0, 160))
            tela.blit(bg, (tela.get_width() // 2 - bg.get_width() // 2, 10))
            tela.blit(surf, (tela.get_width() // 2 - surf.get_width() // 2, 15))
        
        pygame.display.update()
        relogio.tick(60)


def dead():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    larguraButtonStart = 150
    alturaButtonStart  = 40
    larguraButtonQuit = 150
    comandos  = 40
    
    estado = "dead"
    larguraVoltar = 150
    alturaVoltar = 40
    lista_ranking = []

    # inicializa os rects para evitar NameError na primeira iteração
    startButton  = pygame.Rect(10, 10, larguraButtonStart, alturaButtonStart)
    quitButton   = pygame.Rect(10, 60, larguraButtonQuit, comandos)
    voltarButton = pygame.Rect(275, 650, larguraVoltar, alturaVoltar)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            
            if estado == "dead":
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if startButton.collidepoint(evento.pos):
                        larguraButtonStart = 140
                        alturaButtonStart  = 35
                    if quitButton.collidepoint(evento.pos):
                        larguraButtonQuit = 140
                        comandos  = 35

                elif evento.type == pygame.MOUSEBUTTONUP:
                    if startButton.collidepoint(evento.pos):
                        larguraButtonStart = 150
                        alturaButtonStart  = 40
                        jogar()
                    
                    if quitButton.collidepoint(evento.pos):
                        larguraButtonQuit = 150
                        comandos = 40
                        
                        try:
                            banco = open("log.dat", "r")
                            dados = banco.read()
                            banco.close()
                            dadosDict = json.loads(dados) if dados != "" else {}
                        except:
                            dadosDict = {}
                        
                        lista_ranking = sorted(dadosDict.items(), key=lambda x: x[1][0], reverse=True)[:5]
                        estado = "ranking"

            elif estado == "ranking":
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if voltarButton.collidepoint(evento.pos):
                        larguraVoltar = 140
                        alturaVoltar = 35
                        
                elif evento.type == pygame.MOUSEBUTTONUP:
                    if voltarButton.collidepoint(evento.pos):
                        larguraVoltar = 150
                        alturaVoltar = 40
                        estado = "dead"
            
        if estado == "dead":
            tela.fill(branco)
            tela.blit(fundoDead, (0,0))
            
            startButton = pygame.draw.rect(tela, branco, (10, 10, larguraButtonStart, alturaButtonStart), border_radius=15)
            startTexto = fonteMenu.render("Tentar de novo?", True, preto)
            tela.blit(startTexto, startTexto.get_rect(center=startButton.center))
            
            quitButton = pygame.draw.rect(tela, branco, (10, 60, larguraButtonQuit, comandos), border_radius=15)
            quitTexto = fonteMenu.render("Recordes", True, preto)
            tela.blit(quitTexto, quitTexto.get_rect(center=quitButton.center))

        elif estado == "ranking":
            tela.fill(preto)
            
            titulo = fonteMenu.render("TOP 5 MAIORES PONTUADORES", True, branco)
            tela.blit(titulo, (180, 100))
            
            pos_y = 200
            for i, (nome, info) in enumerate(lista_ranking):
                texto_jogador = f"{i+1}. {nome} - {info[0]} pts ({info[1]})"
                item_ranking = fonteMenu.render(texto_jogador, True, branco)
                tela.blit(item_ranking, (150, pos_y))
                pos_y += 50
            
            voltarButton = pygame.draw.rect(tela, branco, (275, 650, larguraVoltar, alturaVoltar), border_radius=15)
            voltarTexto = fonteMenu.render("Voltar", True, preto)
            tela.blit(voltarTexto, voltarTexto.get_rect(center=voltarButton.center))

        pygame.display.update()
        relogio.tick(60)



def start():
    somDeEntrada.play()
    larguraButtonStart = 150
    alturaButtonStart  = 40
    larguraButtonQuit = 150
    comandos = 40
    
    estado = "menu" 
    larguraVoltar = 150
    alturaVoltar = 40

    # inicializa os rects para evitar NameError na primeira iteração
    startButton = pygame.Rect(330, 550, larguraButtonStart, alturaButtonStart)
    quitButton  = pygame.Rect(550, 550, larguraButtonQuit, comandos)
    voltarButton = pygame.Rect(275, 650, larguraVoltar, alturaVoltar)

    while True:
        for evento in pygame.event.get():
            print(evento)  # DEBUG - remover depois
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if estado == "menu":
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if startButton.collidepoint(evento.pos):
                        larguraButtonStart = 140
                        alturaButtonStart  = 35
                    if quitButton.collidepoint(evento.pos):
                        larguraButtonQuit = 140
                        comandos = 35
                        pygame.mixer.music.stop()

                elif evento.type == pygame.MOUSEBUTTONUP:
                    if startButton.collidepoint(evento.pos):
                        larguraButtonStart = 150
                        alturaButtonStart  = 40
                        jogar()
                    
                    if quitButton.collidepoint(evento.pos):
                        larguraButtonQuit = 150
                        comandos = 40
                        estado = "comandos"

            elif estado == "comandos":
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if voltarButton.collidepoint(evento.pos):
                        larguraVoltar = 140
                        alturaVoltar = 35
                        
                elif evento.type == pygame.MOUSEBUTTONUP:
                    if voltarButton.collidepoint(evento.pos):
                        larguraVoltar = 150
                        alturaVoltar = 40
                        estado = "menu"

        if estado == "menu":
            tela.fill(branco)
            tela.blit(fundoStart, (0,0))
            
            startButton = pygame.draw.rect(tela, branco, (330, 550, larguraButtonStart, alturaButtonStart), border_radius=15)
            startTexto = fonteMenu.render("Iniciar Game", True, preto)
            tela.blit(startTexto, startTexto.get_rect(center=startButton.center))
            
            quitButton = pygame.draw.rect(tela, branco, (550, 550, larguraButtonQuit, comandos), border_radius=15)
            quitTexto = fonteMenu.render("Comandos", True, preto)
            tela.blit(quitTexto, quitTexto.get_rect(center=quitButton.center))
            
            texto = fonteMenu.render(f"The Best - {nome_maior} - {maior_pontos} - {dataJogada} ", True, branco)
            tela.blit(texto, (480, 15))
            
        elif estado == "comandos":
            tela.fill(preto)
            
            titulo = fonteMenu.render("COMANDOS DO JOGO", True, branco)
            txt_esquerda = fonteMenu.render("Seta Esquerda (<-) : Move para Esquerda", True, branco)
            txt_direita = fonteMenu.render("Seta Direita (->) : Move para Direita", True, branco)
            txt_pausa = fonteMenu.render("Espaço : Pausa o Jogo", True, branco)
            
            tela.blit(titulo, (200, 150))
            tela.blit(txt_esquerda, (120, 300))
            tela.blit(txt_direita, (120, 370))
            tela.blit(txt_pausa, (120, 440))
            
            voltarButton = pygame.draw.rect(tela, branco, (275, 650, larguraVoltar, alturaVoltar), border_radius=15)
            voltarTexto = fonteMenu.render("Voltar", True, preto)
            tela.blit(voltarTexto, voltarTexto.get_rect(center=voltarButton.center))

        pygame.display.update()
        relogio.tick(60)

start()
