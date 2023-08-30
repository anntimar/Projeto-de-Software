import pygame
import sys
import subprocess

# Inicialize o Pygame
pygame.init()

# Configurações da janela
largura, altura = 800, 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Terminal Pygame")

# Configurações de cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Crie uma fonte para o texto
fonte = pygame.font.Font(None, 36)

# Variáveis para entrada e saída de texto
entrada_texto = ""
saida_texto = []


# Função para escrever texto na janela
def escrever_texto(texto, posicao):
    texto_surface = fonte.render(texto, True, preto)
    janela.blit(texto_surface, posicao)


# Loop principal
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                # Quando o usuário pressiona Enter, execute o comando
                comando = entrada_texto.strip()
                saida_texto.append(f">> {comando}")
                try:
                    # Execute o comando e capture a saída
                    resultado = subprocess.check_output(
                        comando, shell=True, stderr=subprocess.STDOUT, text=True
                    )
                    saida_texto.extend(resultado.splitlines())
                except subprocess.CalledProcessError as e:
                    saida_texto.append(str(e))

                entrada_texto = ""
            elif evento.key == pygame.K_BACKSPACE:
                entrada_texto = entrada_texto[:-1]
            else:
                entrada_texto += evento.unicode

    # Limpe a janela
    janela.fill(branco)

    # Desenhe a entrada de texto
    escrever_texto(">> " + entrada_texto, (10, altura - 40))

    # Desenhe a saída de texto
    for i, linha in enumerate(reversed(saida_texto)):
        escrever_texto(linha, (10, altura - (i + 2) * 40))

    pygame.display.flip()

# Saia do Pygame
pygame.quit()
sys.exit()
