from random import randint

#loop que possibilita ao usuário continuar a jogar
continuar_jogando = "S"
while continuar_jogando != 'N':
    #matriz contendo três listas com varias palavras, tais listas representas níveis de dificuldade
    lista_palavras = [['amarelo', 'amiga', 'amor', 'ave', 'aviao', 'avo', 'balao', 'bebe', 'bolo', 'branco', 'cama', 'caneca',
          'celular', 'clube',
          'copo', 'doce', 'elefante', 'escola', 'estojo', 'faca', 'foto', 'garfo', 'geleia', 'girafa', 'janela',
          'limonada', 'mae',
          'meia', 'noite', 'oculos', 'onibus', 'ovo', 'pai', 'pao', 'parque', 'passarinho', 'peixe', 'pijama', 'rato',
          'umbigo'],
         ['afobado', 'amendoim', 'banheiro', 'caatinga', 'cachorro', 'campeonato', 'capricornio','catapora', 'corrupcao', 'crepusculo', 'empenhado', 'esparadrapo', 'forca', 'galaxia', 'historia', 'magenta',
          'manjericao', 'menta',
          'moeda', 'oracao', 'pacoca', 'palavra', 'pedreiro', 'pneumonia', 'pulmao', 'rotatoria', 'serenata',
          'transeunte', 'trilogia', 'xicara'],
         ['acender', 'afilhado', 'ardiloso', 'aspero', 'assombracao', 'asterisco', 'basquete', 'caminho', 'champanhe',
          'chiclete', 'chuveiro',
          'coelho', 'contexto', 'convivencia', 'coracao', 'desalmado', 'eloquente', 'esfirra', 'esquerdo', 'excecao',
          'fugaz', 'gororoba',
          'heterossexual', 'horrorizado', 'impacto', 'independencia', 'modernidade', 'oftalmologista',
          'otorrinolaringologista', 'paralelepipedo',
          'pororoca', 'prognosticio', 'quarentena', 'quimera', 'refeicao', 'reportagem', 'sino', 'taciturno', 'tenue',
          'visceral']]
    print('\033[036m-='*20)
    print('             JOGO DA FORCA')
    print('-=' * 20)

    print('[1] Fácil \n[2] Médio\n[3] Difícil')
    # Entrada para definir a dificuldade 
    modo = input('Escolha o modo de jogo: ')
    #loop de validação
    while modo.isdigit() == False or int(modo) not in [1,2,3]:
        modo = input('Escolha o modo de jogo: ')
    print('-=' * 20)
    modo = int(modo)
    palavra = lista_palavras[modo - 1][randint(0, len(lista_palavras[modo - 1]))]
    usadas = ''
    tracos_palavra = '*' * len(palavra)

    #bloco de condicionais para definir quantas chances/vidas o usuário terá
    if modo == 1:
        vidas = 7
    elif modo == 2:
        vidas = 5
    elif modo == 3: 
        vidas = 3

    # loop principal do jogo
    fim_loop = 0
    while fim_loop != -1:
        print('Vidas : {}'.format(vidas))
        print('Letras usadas: {}.'.format(usadas))
        print(tracos_palavra)
        palpite = input("Escolha uma letra ou chute a palavra: ")
        nao_encontrou = 0

        # loop para verificar se a letra está contida em algum lugar na palavra
        for i in range(len(palavra)):
            # caso a letra esteja contida na palavra essa condicional irá fazer a troca da variável tracos_palavra para mostra a posção que ela se encontra na palavra, a fim de facilitar o jogo 
            if palpite == palavra[i]:
                t1 = tracos_palavra[0:i]
                t2 = tracos_palavra[i + 1:len(tracos_palavra)]
                tracos_palavra = t1 + palpite + t2
            else:
                nao_encontrou += 1

        # Aqui eu adiciono caractere ou palavra já chutada pelo usuário
        usadas += ' ' + palpite

        # trecho que subtrai as vidas/chances que o usuário ainda possui
        if nao_encontrou == len(palavra) and palpite != palavra:
            vidas -= 1

        # Este trecho abaixo analisa se o jogo chegou ao fim para que o mesmo encerre o loop
        if (vidas == 0 or tracos_palavra == palavra) or vidas != 0 and palpite == palavra:
            print('-=' * 20)
            print('A palavra era\033[m \033[033m{}!\033[m'.format(palavra))
            fim_loop = -1
        
    # observe que este trecho está fora do loop do jogo, sendo que ele vai verificar se o jogador venceu ou perdeu a partida
    if vidas == 0:
        print('\033[031mGame Over!\033[m \033[036mTente novamente.')
    else:
        print('\033[032mParabéns você venceu!!\033[m \033[036mTente um nível mais dificil!')
    print('-=' * 20,end="")
    print("\033[m",end="")

    # Aqui eu pergunto se o usuário deseja jogar novamente ou se deseja parar, além de fazer a validação das entradas
    print("\033[036m")
    continuar_jogando = input('\nJogar novamente[S]/[N]? ').upper()
    while continuar_jogando.isdigit == True or continuar_jogando not in 'nNsS':
        continuar_jogando = input('\nJogar novamente[S]/[N]? ').upper()
    print("\033[m")