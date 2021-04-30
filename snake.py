import pygame
import random
 
pygame.init()
 
#valores iniciais 
x = 300
y = 300
 
d = 10
comida_radius = 5 # pq 5 e não 10? 5 é o raio do centro do circulo até sua extremidade. 
 
lista_cobra = [[x, y]]
 
dx = 0
dy = 0
 
x_comida = round(random.randrange(0, 600 -d) / 20) * 20
y_comida = round(random.randrange(0, 600 -d) / 20) * 20
 
#cores
azul = (50, 100, 213)
vermelho = (255,0,0)
preto = (0,0,0)
verde = (50,205,50)
branco = (255, 255, 255)
 
dimensoes = (600, 600)
 
tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption('Snake da Kenzie')
 
# pontuação 
minhafonte = pygame.font.SysFont("monospace", 16)
 
tela.fill(azul)
 
clock = pygame.time.Clock()
 
def desenha_cobra(lista_cobra):
    tela.fill(azul)
    scoretext = minhafonte.render("Total de pontos: " + str(len(lista_cobra)), 1, branco)
    tela.blit(scoretext, (5, 5))
 
    q_vermelho = True # Foi adicionado para que nossa cobra agora seja listada de vermelho e preto, como uma coral haha. a cada loop dentro do for, o quadrado seguinte recebe a cor contraria do anterior.
    for unidade in lista_cobra:
        if(q_vermelho):
            pygame.draw.rect(tela, vermelho, [unidade[0],unidade[1], d, d])
            q_vermelho = False # esse foi um quadrado vermelho, então o proximo n pode ser vermelho.
        else:
            pygame.draw.rect(tela, preto, [unidade[0],unidade[1], d, d])
            q_vermelho = True # esse foi um quadrado preto, então o proximo n pode ser preto.
 
def mover_cobra(dx, dy, lista_cobra):
    stop = False
 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = +d
                dy = 0
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = +d
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_ESCAPE:
                print('quit')
                stop = True
 
    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy
 
    lista_cobra.append([x_novo, y_novo])
 
    del lista_cobra[0]
 
    return stop, dx, dy, lista_cobra
 
def verifica_comida(dx, dy, x_comida, y_comida, lista_cobra):
    head = lista_cobra[-1]
    x_novo = head[0] + dx
    y_novo = head[1] + dy
 
    if head[0] == x_comida and head[1] == y_comida:
        lista_cobra.append([x_novo, y_novo])
 
        #como a comida foi achada podemos setar novos valores de endereço para ela, e esses valores são usados para desenhar e já são enviados com o return para os valores "globais" de posição desta.
        x_comida = round(random.randrange(0, 600 -d) / 20) * 20 
        y_comida = round(random.randrange(0, 600 -d) / 20) * 20
 
    #caso queira que a comida seja redonda descomente a linha 85 e comente a 86
    #pygame.draw.circle(tela, verde, [x_comida, y_comida], comida_radius)
    pygame.draw.rect(tela, verde, [x_comida, y_comida, d, d])
 
    return x_comida, y_comida, lista_cobra
 
stop = False
while not stop:
    pygame.display.update()
    stop, dx, dy, lista_cobra = mover_cobra(dx, dy, lista_cobra) #mover a cobra antes de desenhar melhorou ligeraimente a jogabilidade. 
    desenha_cobra(lista_cobra)
    x_comida, y_comida, lista_cobra = verifica_comida(dx, dy, x_comida, y_comida, lista_cobra)
    print(lista_cobra)
    clock.tick(10)