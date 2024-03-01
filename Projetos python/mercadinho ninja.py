
import random
import pygame

# Inicialização do pygame
pygame.init()

# Configurações da tela
largura_tela = 400
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Flappy Bird")

# Cores
branco = (255, 255, 255)
azul = (0, 0, 255)

# Variáveis do pássaro
bird_x = 50
bird_y = altura_tela // 2
bird_velocidade = 0
bird_gravidade = 0.5
bird_altura = 20
bird_largura = 20

# Variáveis dos obstáculos
obstaculo_x = largura_tela
obstaculo_largura = 50
obstaculo_espaco = 150
obstaculo_altura = random.randint(100, altura_tela - 100)
obstaculo_velocidade = 3

# Pontuação
pontos = 0
fonte = pygame.font.SysFont(None, 36)

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                bird_velocidade = -10

    # Atualizações de posição
    bird_velocidade += bird_gravidade
    bird_y += bird_velocidade
    obstaculo_x -= obstaculo_velocidade

    # Verifica colisão com o solo
    if bird_y > altura_tela - 20:
        rodando = False

    # Verifica colisão com os obstáculos
    if obstaculo_x < bird_x < obstaculo_x + obstaculo_largura:
        if bird_y < obstaculo_altura or bird_y > obstaculo_altura + obstaculo_espaco:
            rodando = False
        else:
            pontos += 1

    # Verifica se o obstáculo passou do pássaro
    if obstaculo_x < -obstaculo_largura:
        obstaculo_x = largura_tela
        obstaculo_altura = random.randint(100, altura_tela - 100)
        pontos += 1

    # Limpa a tela
    tela.fill(branco)

    # Desenha o pássaro
    pygame.draw.rect(tela, azul, (bird_x, bird_y, bird_largura, bird_altura))

    # Desenha os obstáculos
    pygame.draw.rect(tela, azul, (obstaculo_x, 0, obstaculo_largura, obstaculo_altura))
    pygame.draw.rect(tela, azul, (obstaculo_x, obstaculo_altura + obstaculo_espaco, obstaculo_largura, altura_tela))

    # Desenha a pontuação
    texto = fonte.render(f"Pontos: {pontos}", True, (0, 0, 0))
    tela.blit(texto, (10, 10))

    # Atualiza a tela
    pygame.display.update()

# Encerra o pygame
pygame.quit()