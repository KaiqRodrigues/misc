
import pygame
import numpy as np

pygame.init()

largura = 1000
altura = 900
celula = 20
simulando = False
coluna_num = largura // celula
linha_num = altura // celula

tela =pygame.display.set_mode((largura, altura))
tempo = pygame.time.Clock()
running = True
nova_grade = []
vivos = []
seres = []
qtde_viz = 0 
grade = np.zeros((linha_num, coluna_num), dtype=int)

vizinhos= (
    (-1,-1),
    (-1,0),
    (-1,1),
    (0,-1),
    (0,1),
    (1,-1),
    (1,0),
    (1,1)
)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                simulando = not simulando

        if event.type == pygame.MOUSEBUTTONDOWN and not simulando:
            x,y = pygame.mouse.get_pos()
            coluna = x // celula   #54 // 20 = 2  coluna 2
            linha = y //celula
            
            grade[linha, coluna] = 1 - grade[linha, coluna]


    if simulando:
        grade_aux = grade.copy()
        vivos = []
        for linha in range(linha_num):
            for coluna in range(coluna_num):
                seres.append([linha, coluna])

        for pessoa in seres:
            qtde_viz = 0
            for viz in vizinhos:
                pos_viz_x = pessoa[0] + viz[0] 
                pos_viz_y = pessoa[1] + viz[1]
                if (pos_viz_x < 0 or pos_viz_x >= linha_num) or (pos_viz_y < 0 or pos_viz_y >= coluna_num):
                    pass
                else:
                    if grade[pos_viz_x, pos_viz_y] == 1:
                        qtde_viz = qtde_viz +1
        

            if 3 < qtde_viz or qtde_viz < 2:
                grade_aux[pessoa[0], pessoa[1]] = 0
            if qtde_viz == 3:
                grade_aux[pessoa[0], pessoa[1]] = 1
            else: pass



        grade = grade_aux

        #REGRAS
        """
        1 vizinho = morre
        4 vizinhos ou mais= morre
        3 vizinhos exatos = nasce

        """


    tela.fill("black")

    for linha in range(linha_num):
        for coluna in range(coluna_num):

            if grade[linha, coluna] ==1:
                pygame.draw.rect(
                    tela,
                    "white",(
                    coluna*celula, 
                    linha *celula, 
                    celula,celula)
                )
                

            elif grade[linha, coluna] ==0:
                pygame.draw.rect(
                    tela,
                    "black",(
                    coluna*celula, 
                    linha *celula,
                    celula, #largura da cor
                    celula) #altura da cor
                )    


    pygame.display.flip()

    tempo.tick(30)

pygame.quit()
