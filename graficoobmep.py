import pygame
pygame.init()
#paleta de cores
cores = {'vermelho_escuro': (120, 0, 0), 
         'vermelho_claro': (241, 106, 115), 
         'bege': (253, 240, 213), 
         'azul_escuro': (0, 48, 73), 
         'azul_claro': (142, 181, 205)}

#fonte
fonte = pygame.font.SysFont('Arial', 20)
fonte_bold = pygame.font.SysFont('Arial', 20, bold = True)
fonte_small = pygame.font.SysFont('Arial', 15)
fonte_titulo = pygame.font.SysFont('Arial', 30, bold = True)
caixa_selecao_ativa = False

def desenhar_indice():
    pygame.draw.rect(janela, cores['vermelho_escuro'], pygame.Rect(0, 0, x_indice, janela.get_height()))
#escrever indice T_T
    if pagina == 'inicio':
        indice_texto = fonte_bold.render("Inicio", True, cores['vermelho_claro'])
    else: indice_texto = fonte.render("Inicio", True, cores['vermelho_claro'])
    indice_texto_rect = indice_texto.get_rect()
    indice_texto_rect.center = (janela.get_width()/13, janela.get_height()/15)
    janela.blit(indice_texto, indice_texto_rect)

#criar botao grafico 1
    if pagina == 'grafico 1':
        grafico1_texto = fonte_bold.render("Grafico1", True, cores['vermelho_claro'])
    else: grafico1_texto = fonte.render("Grafico1", True, cores['vermelho_claro'])
    grafico1_texto_rect = grafico1_texto.get_rect()
    grafico1_texto_rect.center = (janela.get_width()/13, janela.get_height()/9)
    janela.blit(grafico1_texto, grafico1_texto_rect)

#criar botao grafico 2
    if pagina == 'grafico 2':
        grafico2_texto = fonte_bold.render("Grafico2", True, cores['vermelho_claro'])
    else: grafico2_texto = fonte.render("Grafico2", True, cores['vermelho_claro'])
    grafico2_texto_rect = grafico2_texto.get_rect()
    grafico2_texto_rect.center = (janela.get_width()/13, janela.get_height()/6.5)
    janela.blit(grafico2_texto, grafico2_texto_rect)

#criar botao criar
    if pagina == 'adicionar':
        criar_texto = fonte_bold.render("Adicionar", True, cores['vermelho_claro'])
    else: criar_texto = fonte.render("Adicionar", True, cores['vermelho_claro'])
    criar_texto_rect = criar_texto.get_rect()
    criar_texto_rect.center = (janela.get_width()/13, janela.get_height()/5.1)
    janela.blit(criar_texto, criar_texto_rect)

def desenhar_graficos(qual):
    if qual == 'grafico_1':
        arquivo = open('grafico1.txt', 'r')
    elif qual == 'grafico_2':
        arquivo = open('grafico2.txt', 'r')
    dados_brutos = arquivo.readlines()
    dados = []
    #armazena os dados em uma lista de tuplas(acertos, total, data)
    for linha in range(len(dados_brutos)):
        dado = str(dados_brutos[linha]).strip(' \n').split(',')# strip() remove espaços em branco extras, como quebras de linha 
        dados.append((int(dado[0]), int(dado[1]), str(dado[2]).strip()))
    arquivo.close()

    segmentos_y = janela.get_height()/dados[0][1]
    #desenhar grade atrás
    #linhas
    for i in range(dados[0][1]):
        pygame.draw.line(janela, cores['bege'],(x_indice, janela.get_height()-segmentos_y * i), (janela.get_width(), janela.get_height()- segmentos_y * i), 1)
        grade_nums = fonte_small.render(str(i), True, cores['bege'])
        grade_nums_rect = grade_nums.get_rect()
        grade_nums_rect.center = (x_indice + 10, janela.get_height()-segmentos_y * i+10)
        janela.blit(grade_nums, grade_nums_rect)
    
    #desenha  o grafico
    quantidade_pontos = len(dados)-1
    area_grafico = janela.get_width() - x_indice
    for segmento in range(quantidade_pontos):
        ponto_inicial = x_indice+area_grafico/quantidade_pontos * segmento, janela.get_height() - (segmentos_y * dados[segmento][0])
        ponto_final = x_indice+area_grafico/quantidade_pontos * (segmento+1), janela.get_height() - (segmentos_y * dados[segmento+1][0])
        pygame.draw.line(janela, cores['vermelho_escuro'], ponto_inicial, ponto_final, 2)

def tela_adicionar():
    #Título
    adicionar_texto = fonte_titulo.render("Adicionar dados", True, cores['azul_claro'])
    adicionar_texto_rect = adicionar_texto.get_rect()
    adicionar_texto_rect.center = (janela.get_width()/3.2, janela.get_height()/16)
    janela.blit(adicionar_texto, adicionar_texto_rect)



    #caixa grafico
    if caixa_selecao_ativa == True:
        cor_caixa_selecao = cores['vermelho_claro']
        #opc caixa 1
        pygame.draw.rect(janela, cores['vermelho_escuro'], pygame.Rect(janela.get_width()/4.5, janela.get_height()/9 + janela.get_height()/20, janela.get_width()/8, janela.get_height()/20))
        grafico_opc1_texto = fonte.render("Grafico 1", True, cores['vermelho_claro'])
        grafico_opc1_texto_rect = grafico_opc1_texto.get_rect()
        grafico_opc1_texto_rect.center = (janela.get_width()/3.5, janela.get_height()/7.6 + janela.get_height()/20)
        janela.blit(grafico_opc1_texto, grafico_opc1_texto_rect)

        #opc caixa 2
        pygame.draw.rect(janela, cores['vermelho_escuro'], pygame.Rect(janela.get_width()/4.5, janela.get_height()/9 + (janela.get_height()/20)*2, janela.get_width()/8, janela.get_height()/20))
        grafico_opc2_texto = fonte.render("Grafico 2", True, cores['vermelho_claro'])
        grafico_opc2_texto_rect = grafico_opc2_texto.get_rect()
        grafico_opc2_texto_rect.center = (janela.get_width()/3.5, janela.get_height()/7.6 + (janela.get_height()/20)*2)
        janela.blit(grafico_opc2_texto, grafico_opc2_texto_rect)
    else: cor_caixa_selecao = cores['vermelho_escuro']
    if opc_grafico == 1:
        texto_caixa_s = 'Grafico 1'
    if opc_grafico == 2:
        texto_caixa_s = 'Grafico 2'
    else: texto_caixa_s = 'Grafico  \/'

    pygame.draw.rect(janela, cor_caixa_selecao, pygame.Rect(janela.get_width()/4.5, janela.get_height()/9, janela.get_width()/8, janela.get_height()/20))
    grafico_texto = fonte.render(texto_caixa_s, True, cores['azul_claro'])
    grafico_texto_rect = grafico_texto.get_rect()
    grafico_texto_rect.center = (janela.get_width()/3.5, janela.get_height()/7.6)
    janela.blit(grafico_texto, grafico_texto_rect)

    #caixa input acertos
    input_acertos_titulo = fonte.render("Acertos", True, cores['azul_claro'])
    input_acertos_titulo_rect = input_acertos_titulo.get_rect()
    input_acertos_titulo_rect.center = (janela.get_width()/3.5, janela.get_height()/5.6 + janela.get_height()/20)
    janela.blit(input_acertos_titulo, input_acertos_titulo_rect)

    #caixa input total de acertos

    #botão enviar

#def tela_lista(qual):


#configurações da janela principal
altura_janela = 700
largura_janela = 900
janela = pygame.display.set_mode((largura_janela, altura_janela), pygame.RESIZABLE)
pygame.display.set_caption('Progresso!!!')
janela.fill(cores['azul_claro'])
x_indice = janela.get_width()/ 6

#Qual pagina mostrar(inicio, grafico 1, grafico 2, adicionar)
pagina = 'inicio'

desenhar_indice()

#Loop principal
run = True
while run:
    pygame.time.delay(60)
    x_indice = janela.get_width()/ 6
    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pagina != 'adicionar':
                caixa_selecao_ativa = False
                opc_grafico = 0
            #clicar no botao indice
            if mouse_y > (janela.get_height()/15 - 10) and mouse_y < (janela.get_height()/15 + 10) and mouse_x <= janela.get_width()/6:
                pagina = 'inicio'
            #clicar no botao grafico 1
            if mouse_y > (janela.get_height()/9 - 10) and mouse_y < (janela.get_height()/9 + 10) and mouse_x <= janela.get_width()/6:
                pagina = 'grafico 1'
            #clicar no botao grafico 2
            if mouse_y > (janela.get_height()/6.5 - 10) and mouse_y < (janela.get_height()/6.5 + 10) and mouse_x <= janela.get_width()/6:
                pagina = 'grafico 2'
            if mouse_y > (janela.get_height()/5.1 - 10) and mouse_y < (janela.get_height()/5.1 + 10) and mouse_x <= janela.get_width()/6:
                if pagina != 'adicionar':
                    input_acertos = ''
                pagina = 'adicionar'
            if pagina == 'adicionar':
                #colisão caixa seleção gráfico
                if (janela.get_width()/4.5 + janela.get_width()/8) > mouse_x > (janela.get_width()/4.5) and (janela.get_height()/9 + janela.get_height()/20) > mouse_y > (janela.get_height()/9):
                    caixa_selecao_ativa = True
            if caixa_selecao_ativa == True:
                if (janela.get_width()/4.5 + janela.get_width()/8) > mouse_x > (janela.get_width()/4.5) and (janela.get_height()/9 + (janela.get_height()/20)*2) > mouse_y > (janela.get_height()/9 + janela.get_height()/20):
                    opc_grafico = 1
                    caixa_selecao_ativa = False

                elif  (janela.get_width()/4.5 + janela.get_width()/8) > mouse_x > (janela.get_width()/4.5) and (janela.get_height()/9 + (janela.get_height()/20)*3) > mouse_y > (janela.get_height()/9 + (janela.get_height()/20)*2):
                    print('opc 2')
                    opc_grafico = 2
                    caixa_selecao_ativa = False

                elif not (janela.get_width()/4.5 + janela.get_width()/8) > mouse_x > (janela.get_width()/4.5) and not (janela.get_height()/9 + janela.get_height()/20) > mouse_y > (janela.get_height()/9):
                    caixa_selecao_ativa = False

    #ver que pagina ta e entrar na certa
    if pagina == 'adicionar':
        janela.fill(cores['azul_escuro'])
        tela_adicionar()
    elif pagina == 'inicio':
        janela.fill(cores['azul_claro'])
    elif pagina == 'grafico 1':
        janela.fill(cores['azul_claro'])
        desenhar_graficos('grafico_1')
    elif pagina == 'grafico 2':
        janela.fill(cores['azul_claro'])
        desenhar_graficos('grafico_2')
    desenhar_indice()


    pygame.display.update()

pygame.quit()
