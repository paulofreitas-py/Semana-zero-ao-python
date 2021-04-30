import pygame
import randomazul = (50, 100, 213)
laranja = (205, 102, 0)
verde = (0, 255, 0)dimensoes = (600, 600)### VALORES INICIAIS ###x = 300
y = 300d = 20lista_cobra = [[x, y]]dx = 0
dy = 0x_comida = round(random.randrange(0, 600 - d) / 20) * 20
y_comida = round(random.randrange(0, 600 - d) / 20) * 20tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption('Snake da Kenzie')tela.fill(azul)clock = pygame.time.Clock()def desenha_cobra(lista_cobra):
    tela.fill(azul)
    for unidade in lista_cobra:
        pygame.draw.rect(tela, laranja, [unidade[0], unidade[1], d, d])def mover_cobra(dx, dy, lista_cobra):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy    lista_cobra.append([x_novo, y_novo])    del lista_cobra[0]    return dx, dy, lista_cobradef verifica_comida(dx, dy, x_comida, y_comida, lista_cobra):    head = lista_cobra[-1]    x_novo = head[0] + dx
    y_novo = head[1] + dy    if head[0] == x_comida and head[1] == y_comida:
        lista_cobra.append([x_novo, y_novo])    pygame.draw.rect(tela, verde, [x_comida, y_comida, d, d])    return x_comida, y_comida, lista_cobrawhile True:
    pygame.display.update()
    desenha_cobra(lista_cobra)
    dx, dy, lista_cobra = mover_cobra(dx, dy, lista_cobra)
    x_comida, y_comida, lista_cobra = verifica_comida(
        dx, dy, x_comida, y_comida, lista_cobra)
    print(lista_cobra)    clock.tick(20)
