import pygame
import pygame_gui
import sys
import random
from quadrado import Quadrado


class Jogo:
    def __init__(self):
        self.largura_tela = 800
        self.altura_tela = 600
        self.tela = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        pygame.display.set_caption("Jogo do Quadrado")
        self.clock = pygame.time.Clock()
        self.fonte = pygame.font.Font(None, 36)

        self.tempo_limite = 30_000  # Tempo limite em segundos
        self.inicio = pygame.time.get_ticks()
        self.pontuação = 0 
        self.rodando = True

        self.quadrado = Quadrado(self.largura_tela, self.altura_tela, (255, 0, 0))
        self.gerenciador_ui = pygame_gui.UIManager((self.largura_tela, self.altura_tela))
    
    def mostrar_texto(self, texto, x, y):
        texto_renderizado = self.fonte.render(texto, True, (255, 255, 255))
        self.tela.blit(texto_renderizado, (x, y))
    
    def carregar_recorde(self):
        try:
            with open("recorde.txt", "r") as arquivo:
                return int(arquivo.read().strip())
        except (FileNotFoundError, ValueError):
            return 0  # Retorna 0 se o arquivo não existir ou estiver vazio

    def salvar_recorde(self, novo_recorde):
        with open("recorde.txt", "w") as arquivo:
            arquivo.write(str(novo_recorde))

        
    def executar(self):
        recorde = self.carregar_recorde()
        botao_reiniciar = None

        while self.rodando:
            self.tela.fill((0, 0, 0))
            tempo_atual = pygame.time.get_ticks()
            tempo_restante = (self.tempo_limite - (tempo_atual - self.inicio)) //1000
            
            if tempo_restante <= 0:
                self.rodando = False
                if self.pontuação > recorde:
                    self.salvar_recorde(self.pontuação) # Salva o novo recorde se for maior
                self.mostrar_texto("Tempo esgotado!", 300, 250)
                self.mostrar_texto(f"Pontuação final: {self.pontuação}", 300, 300)
                self.mostrar_texto(f"Recorde: {recorde}", 300, 350)
                
                # Cria o botão de reinício
                if botao_reiniciar is None:
                    botao_reiniciar = pygame_gui.elements.UIButton(
                        relative_rect=pygame.Rect((self.largura_tela // 2 - 75, 350), (150, 50)),
                        text="Recomeçar",
                        manager=self.gerenciador_ui  # Use o gerenciador de UI inicializado no __init__
                    )
                pygame.display.flip()

                while not self.rodando:
                    tempo_delta = self.clock.tick(60) / 1000.0
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == pygame.USEREVENT:
                            if event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == botao_reiniciar:
                                if event.ui_element == botao_reiniciar:
                                    self.rodando = True
                        
                        self.gerenciador_ui.process_events(event)
                    
                    self.gerenciador_ui.update(tempo_delta)
                    self.gerenciador_ui.draw_ui(self.tela)
                    pygame.display.flip()

                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.rodando = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.quadrado.foi_clicado(event.pos):
                        self.pontuação += 1
                        self.quadrado.mover()
                        self.quadrado.cor = (
                            random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255),
                        )
                         # Diminui o tamanho do quadrado a cada 5 pontos
                        if self.pontuação % 5 == 0:
                            self.quadrado.tamanho = max(10, self.quadrado.tamanho - 10)

            self.quadrado.desenhar(self.tela)
            self.mostrar_texto(f"Pontuação: {self.pontuação}", 10, 10) # Mostra a pontuação atual
            self.mostrar_texto(f"Tempo restante: {tempo_restante}", 10, 50) # Mostra o tempo restante
            self.mostrar_texto(f"Pontuação: {self.pontuação}", 10, 90) # Mostra a pontuação atual
            self.mostrar_texto(f"Recorde: {recorde}", 10, 130)  # Mostra o recorde durante o jogo 

            if tempo_restante <= 0:
                # Exibe mensagem de fim de jogo
                fim = self.fonte.render("FIM DE JOGO", True, (255, 0, 0))
                pontuacao_final = self.fonte.render(f"Pontuação: {self.pontuação}", True, (255, 255, 255))
                recorde_final = self.fonte.render(f"Recorde: {recorde}", True, (255, 255, 255))

                # Calcula as posições para centralizadas
                fim_x = (self.largura_tela - fim.get_width()) // 2
                pontuacao_x = (self.largura_tela - pontuacao_final.get_width()) // 2
                recorde_x = (self.largura_tela - recorde_final.get_width()) // 2

                # Exibe os textos centralizados
                self.tela.blit(fim, (fim_x, 200))
                self.tela.blit(pontuacao_final, (pontuacao_x, 250))
                self.tela.blit(recorde_final, (recorde_x, 300))

                pygame.display.update()
                pygame.type.wait(3000)
                self.rodando = False

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()   