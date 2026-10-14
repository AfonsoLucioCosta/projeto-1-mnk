# FUNÇÕES PRINCIPAIS DO PROJETO

from math import sqrt

# Projeto (2.1.1) 
def eh_tabuleiro(tab):
    """
    Verifica se o tabuleiro fornecido é válido.

    Um tabuleiro válido deve:
    1. ser um tuplo constituido por tuplos.
    2. Todos os tuplos devem ter o mesmo número de elementos.
    3. Todos os elementos inseridos tem de ser inteiros (-1, 0 ou 1).

    Retorna True se o tabuleiro for válido, False caso contrário.
    """
    # Validar m
    if not validate_tabuleiro(tab): # Validar tuplo
        return False
    # Validar n
    for x in tab: # x percorre o tuplo
        if not validate_tabuleiro(x): 
            return False
        if len(tab[0]) != len(x): # Verificar se todas as linhas tem o mesmo número de colunas
            return False
        for e in x:
            if not isinstance(e, int):# Verificar se todos os elementos do tuplo sao inteiros
                return False
            if e not in (-1,0,1):# Verificar se todos os elementos do tuplo sao -1, 0 ou 1
                return False
    return True


# Projeto (2.1.2)
def eh_posicao(pos):
    """
    Verifica se o argumento fornecido é uma posição válida.

    A função verifica se o argumento pos é um número inteiro positivo.

    Retorna True se o argumento for uma posição válida, False caso contrário.
    """
    if type(pos) == int and 0 < pos < 10001:# Verificar se o argumento fornecido é um número inteiro positivo
        return True
    return False


# Projeto (2.1.3)
def obtem_dimensao(tab):
    """
    Obtém a dimensão de um tabuleiro.

    A função obtém a dimensão de um tabuleiro fornecido como argumento,
    retornando um tuplo contendo o número de linhas e o número de colunas.

    Args:
        tab (tuple): O tabuleiro representado como um tuplo de tuplos.

    Returns:
        tuple: Um tuplo contendo o número de linhas e o número de colunas do tabuleiro.
    """

    m = len(tab) # Obter o número de linhas
    n = len(tab[0]) # Obter o número de colunas
    return (m, n)


# Projeto (2.1.4)
def obtem_valor(tab, pos):

    """
    Obtém o valor na posição especificada em um tabuleiro.

    A função obtém o valor na posição especificada por pos em um tabuleiro
    representado por tab, retornando o valor naquela posição.

    Args:
        tab (tuple): O tabuleiro representado como um tuplo de tuplos.
        pos (int): A posição no tabuleiro.

    Returns:
        int: O valor na posição especificada do tabuleiro.
    """
    tup_aux = ()
    for x in tab: # x percorre o tuplo
        tup_aux += x # Concatenar tuplos
    return tup_aux[pos-1] #retorna o valor na posição especificada


# Projeto (2.1.5)
def obtem_coluna(tab, pos):
    """
    Obtém as posições lineares de uma coluna específica de um tabuleiro.

    A função calcula todas as posições lineares de uma coluna no tabuleiro
    representado por `tab`, dado um número de posição `pos`. O índice da
    posição é feito a partir de 1. O tabuleiro é representado como um tuplo
    de tuplos, onde cada tuplo representa uma linha do tabuleiro.
    Esta função retorna um tuplo contendo as posições lineares da coluna
    especificada.

    Args:
        tab (tuple): O tabuleiro representado como um tuplo de tuplos.
        pos (int): A posição no tabuleiro.

    Returns:
        tuple: Um tuplo contendo as posições lineares da coluna especificada.
    """
    m = len(tab)
    n = len(tab[0])

    if pos > m * n or pos <= 0: # Verificar se a posição está dentro dos limites do tabuleiro
        return 

    coluna = pos % n # Obter o número da coluna
    if coluna == 0: # Verificar se o número da coluna é zero
        coluna = n # Mudar o número da coluna para o número de colunas
    
    tup = () 
    for i in range(m): # i percorre o tuplo
        x = i*n + coluna # Obter as posições lineares da coluna
        tup += (x,)  # Adicionar as posições lineares a tuplo
    
    return tup


# Projeto (2.1.6)
def obtem_linha(tab, pos):
    """
    Obtém as posições lineares de uma linha específica de um tabuleiro.

    A função calcula todas as posições lineares de uma linha no tabuleiro
    representado por `tab`, dado um número de posição `pos`. O índice da
    posição é feito a partir de 1. O tabuleiro é representado como um tuplo
    de tuplos, onde cada tuplo representa uma linha do tabuleiro.
    Esta função retorna um tuplo contendo as posições lineares da linha
    especificada.

    Args:
        tab (tuple): O tabuleiro representado como um tuplo de tuplos.
        pos (int): A posição no tabuleiro.

    Returns:
        tuple: Um tuplo contendo as posições lineares da linha especificada.
    """

    m = len(tab)
    n = len(tab[0])

    linha = (pos-1) // n # Obter o número da linha
    
    # Obter as posições lineares das linhas
    tup = ()
    for i in range(n):  # i percorre o tuplo
        x = linha * n + i + 1  # Obter as posições lineares da linha
        tup += (x,)  # Adicionar as posições lineares a tuplo
    
    return tup


# Projeto (2.1.7)
def obtem_diagonais(tab, pos):
     
    """
    Obtém as posições lineares das diagonais de um tabuleiro.

    A função calcula todas as posições lineares das diagonais do tabuleiro
    representado por `tab`, dado um número de posição `pos`. O índice da
    posição é feito a partir de 1. O tabuleiro é representado como um tuplo
    de tuplos, onde cada tuplo representa uma linha do tabuleiro.
    Esta função retorna um tuplo contendo as posições lineares das diagonais
    especificadas.

    Args:
        tab (tuple): O tabuleiro representado como um tuplo de tuplos.
        pos (int): A posição no tabuleiro.

    Returns:
        tuple: Um tuplo contendo as posições lineares das diagonais especificadas.
    """
    m, n = obtem_dimensao(tab)

    if pos > m * n or pos <= 0: # Verificar se a posição está dentro dos limites do tabuleiro
        return 

    linha_aux = (pos - 1) // n  # Obter o número da linha
    coluna_aux = (pos - 1) % n  # Obter o número da coluna 

    # Encontrar as posições da diagonal descendente
    diagonal = ()
    linha = linha_aux 
    coluna = coluna_aux

    while linha >= 0 and coluna >= 0:  # Subir na diagonal
        diagonal = (linha * n + coluna + 1,) + diagonal  # Adicionar as posições lineares a tuplo
        linha -= 1 
        coluna -= 1

    linha = linha_aux + 1 # Mudar o número da linha para o número de linhas
    coluna = coluna_aux + 1 # Mudar o número da coluna para o número de colunas

    while linha < m and coluna < n:  # Descer na diagonal
        diagonal += (linha * n + coluna + 1,)  # Adicionar as posições lineares a tuplo
        linha += 1
        coluna += 1

    # Encontrar as posições da antidiagonal
    antidiagonal = ()
    linha = linha_aux
    coluna = coluna_aux

    while linha >= 0 and coluna < n:  # Subir na antidiagonal
        antidiagonal =   antidiagonal + (linha * n + coluna + 1,) # Adicionar as posições lineares a tuplo
        linha -= 1
        coluna += 1
    linha = linha_aux + 1
    coluna = coluna_aux - 1
    while linha < m and coluna >= 0:  # Descer na antidiagonal
        antidiagonal = (linha * n + coluna + 1,) + antidiagonal # Adicionar as posições lineares a tuplo
        linha += 1
        coluna -= 1

    return (diagonal, antidiagonal) # Retornar diagonais em forma de tuplos


# Projeto (2.1.8)
def tabuleiro_para_str(tab):
    """
    Converte um tabuleiro em forma de string.

    A função tabuleiro_para_str converte um tabuleiro em forma de string,
    representando cada linha do tabuleiro com uma linha na string. Entre
    cada linha do tabuleiro, é adicionado um caractere de linha nova
    ("\n") e uma linha de separação que tem o mesmo comprimento da linha
    do tabuleiro. Entre cada coluna do tabuleiro, é adicionado um separador
    ("---").

    Args:
        tab (tuple): O tabuleiro representado como um tuplo de tuplos.

    Returns:
        str: A string representando o tabuleiro.
    """

    tabuleiro = ""
    for x in range(len(tab)):
        line = ""
        for y in range(len(tab[x])):
            if y == len(tab[x])-1: # Se chegarmos à última coluna
                line += f"{convert_to_char(tab[x][y])}" # Acaba com X/O/+, por ser a última coluna
                if not x == len(tab)-1: # Enquanto não chegarmos à última linha (a percorrer todas as linhas)
                    line += "\n"
                    line_break = line.replace("O", "|").replace("X", "|").replace("+", "|").replace("-", " ") 
                    line += line_break
                tabuleiro += line
                break
            line += f"{convert_to_char(tab[x][y])}---" # Enquanto estiver a percorrer as colunas
    return tabuleiro


# Projeto (2.2.1)
def eh_posicao_valida(tab, pos):

    '''
    Verifica se uma dada posição é válida em um tabuleiro.

    A função verifica se a posição `pos` é válida no tabuleiro `tab`.
    Uma posição é considerada válida se estiver contida no intervalo
    [1, m * n], onde m é o número de linhas e n é o número de colunas
    do tabuleiro.

    Args:
        tab (tuple): Um tabuleiro.
        pos (int): O número da posição a verificar.

    Returns:
        bool: True se a posição for válida, False caso contrário.

    Raises:
        ValueError: Se o tabuleiro ou a posição não forem válidos.
    '''
    if not eh_tabuleiro(tab) or not eh_posicao(pos):
        raise ValueError('eh_posicao_valida: argumentos invalidos')

    m, n = obtem_dimensao(tab)
    
    if 1 <= pos <= m * n: # Verificar se a posição está dentro dos limites do tabuleiro
        return True
    else:
        return False
    

# Projeto (2.2.2)
def eh_posicao_livre(tab, pos):
    '''
    Verifica se uma dada posição é livre em um tabuleiro.

    A função verifica se a posição `pos` é válida e se o valor
    associado a essa posição no tabuleiro `tab` é igual a 0. Isto
    é, se a posição estiver dentro dos limites do tabuleiro e se
    estiver livre.

    Args:
        tab (tuple): Um tabuleiro.
        pos (int): O número da posição a verificar.

    Returns:
        bool: True se a posição for livre, False caso contrário.

    Raises:
        ValueError: Se o tabuleiro ou posicao não forem válidos.
    '''
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab, pos):
        raise ValueError('eh_posicao_livre: argumentos invalidos')

    if eh_posicao_valida(tab, pos) == False or obtem_valor(tab, pos) != 0: # Verificar se a posição está dentro dos limites do tabuleiro e se o valor da posição é 0
        return False
    else:
        return True    


# Projeto (2.2.3)
def obtem_posicoes_livres(tab):
    '''
    Obtém as posições livres em um tabuleiro.

    A função percorre todas as posições do tabuleiro e verifica
    quais delas estão livres, ou seja, quais delas tem o valor
    igual a 0.

    Args:
        tab (tuple): O tabuleiro.

    Returns:
        tuple: Um tuplo com as posições livres do tabuleiro.

    Raises:
    ValueError: Se o tabuleiro não for válidos.
    '''
    
    if not eh_tabuleiro(tab):
        raise ValueError('obtem_posicoes_livres: argumento invalido')

    posicao_livres = devolve_tuplo_posicoes(tab, 0) #retorna o valor da posição = 0, na função a cima
    return posicao_livres


# Projeto (2.2.4)
def obtem_posicoes_jogador(tab, jog):

    """
    Obtém as posições ocupadas por um jogador específico em um tabuleiro.

    A função percorre o tabuleiro e retorna um tuplo contendo as 
    posições ocupadas pelo jogador especificado por `jog`. O jogador 
    pode ser representado pelos valores 1 ou -1.

    Args:
        tab (tuple): O tabuleiro representado como um tuplo de tuplos.
        jog (int): O jogador, que pode ser 1 ou -1.

    Returns:
        tuple: Um tuplo contendo as posições ocupadas pelo jogador no 
               tabuleiro.

    Raises:
        ValueError: Se o tabuleiro ou o jogador não forem válidos.
    """
    if not eh_tabuleiro(tab) or not eh_jogador(jog):     
        raise ValueError('obtem_posicoes_jogador: argumentos invalidos')

    posicoes_jogador = devolve_tuplo_posicoes(tab, jog)  #retorna o valor da posição = jog [1, -1], na função a cima
    return posicoes_jogador


# Projeto (2.2.5)
def obtem_posicoes_adjacentes(tab, pos):

    """
    Obtém as posições adjacentes de uma posição específica em um tabuleiro.

    A função percorre o tabuleiro e retorna um tuplo contendo as posições adjacentes
    (superior esquerda, cima, superior direita, esquerda, direita, inferior esquerda, baixo, inferior direita) 
    da posição especificada pelo argumento pos.

    Args:
        tab (tuple): O tabuleiro representado como um tuplo de tuplos.
        pos (int): A posição no tabuleiro.

    Returns:
        tuple: Um tuplo contendo as posições adjacentes da posição no tabuleiro.

    Raises:
        ValueError: Se o tabuleiro ou a posição não forem válidos.
    """

    if not eh_posicao(pos) or not eh_tabuleiro(tab) or not eh_posicao_valida(tab, pos):
        raise ValueError('obtem_posicoes_adjacentes: argumentos invalidos')
    
    linha, coluna = devolve_indice_posicao(tab, pos)
    posicoes_adjacentes = ()

    if linha > 0 and coluna > 0:  # superior esquerda
        posicoes_adjacentes += (pos - len(tab[0]) - 1,)
    if linha > 0:  # cima
        posicoes_adjacentes += (pos - len(tab[0]),)
    if linha > 0 and coluna < len(tab[0]) - 1:  # superior direita
        posicoes_adjacentes += (pos - len(tab[0]) + 1,)
    if coluna > 0:  # esquerda
        posicoes_adjacentes += (pos - 1,)
    if coluna < len(tab[0]) - 1:  # direita
        posicoes_adjacentes += (pos + 1,)
    if linha < len(tab) - 1 and coluna > 0:  # inferior esquerda
        posicoes_adjacentes += (pos + len(tab[0]) - 1,)
    if linha < len(tab) - 1:  # baixo
        posicoes_adjacentes += (pos + len(tab[0]),)
    if linha < len(tab) - 1 and coluna < len(tab[0]) - 1:  # inferior direita
        posicoes_adjacentes += (pos + len(tab[0]) + 1,)

    return posicoes_adjacentes 


# Projeto (2.2.6)
def ordena_posicoes_tabuleiro(tab, tup):
    '''
    Ordena as posições de um tabuleiro em ordem crescente de distância 
    em relação à posição central.

    A função ordena as posições do tabuleiro recebido como parâmetro em um tuplo
    por ordem crescente de distância em relação à posição central.

    Args:
        tab (tuple): O tabuleiro representado como um tuplo de tuplos.
        tup (tuple): O tuplo de posições a ser ordenado.

    Returns:
        tuple: O tuplo ordenado com as posições do tabuleiro em ordem crescente de distância em relação à posição central.

    Raises:
        ValueError: Se o tabuleiro ou o argumento tup forem inválidos.
    '''

    def encontra_menor(posicoes):

        menor = posicoes[0] # Seleciona o primeiro elemento do tuplo
        for pos in posicoes:
            if (pos[0] < menor[0]) or (pos[0] == menor[0] and pos[1] < menor[1]): # Verifica se o elemento atual é menor
                menor = pos # Atualiza o elemento menor
        return menor # Retorna o elemento menor

    if not eh_tabuleiro(tab) or not isinstance(tup, tuple): # Verificar se os argumentos sao validos (eh_tabuleiro e tup) 
        raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
    
    m, n = obtem_dimensao(tab) # Obter as dimensões do tabuleiro
    if len(tup) > m * n:
        raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')

    pos_central = posicao_central(m, n) # Obter a posição central
    linha_central, coluna_central = devolve_indice_posicao(tab, pos_central) # Obter as coordenadas da posição central
    
    posicoes_distancia = ()
    for pos in range(1, m * n + 1):
        linha_atual, coluna_atual = devolve_indice_posicao(tab, pos) # Obter as coordenadas da posição

        #distancia = max(abs(linha_atual - linha_central),abs(coluna_atual - coluna_central)) 
        #posicoes_distancia += ((distancia, pos),)  
        distancia = sqrt((linha_atual - linha_central) ** 2 + (coluna_atual - coluna_central) ** 2)
        posicoes_distancia += ((distancia, pos),)
        
    # Ordenar o tuplo usando a técnica de seleção
    posicoes_ordenadas_aux = ()
    while posicoes_distancia: 
        menor = encontra_menor(posicoes_distancia) # Encontra o menor elemento
        posicoes_ordenadas_aux += (menor[1],) # Adiciona o elemento ao tuplo ordenado
        # Remove o menor elemento do tuplo original
        posicoes_distancia = tuple(p for p in posicoes_distancia if p != menor) # Remove o menor elemento do tuplo

    posicoes_ordenadas = ()
    for pos in posicoes_ordenadas_aux:
        if pos in tup:
            posicoes_ordenadas += (pos,)

    return posicoes_ordenadas


# Projeto (2.2.7)
def marca_posicao(tab, pos, jog):

    '''
    Marca a posição de um tabuleiro com o valor de um jogador.

    A função marca_posicao marca a posição de um tabuleiro com o valor de um jogador.

    Args:
        tab (tuple): O tabuleiro representado como um tuplo de tuplos.
        pos (int): A posição a ser marcada no tabuleiro.
        jog (int): O valor do jogador (1 ou -1).

    Returns:
        tuple: O tabuleiro com a posição marcada.
    
    Raises:
        ValueError: Se o tabuleiro, a posição ou o jogador forem inválidos.
    '''
    if not eh_tabuleiro(tab)or not eh_posicao(pos) or not eh_posicao_valida(tab, pos) or not eh_jogador(jog) or not eh_posicao_livre(tab, pos):
        raise ValueError('marca_posicao: argumentos invalidos')
    
    linha, coluna = devolve_indice_posicao(tab, pos)
    
    tab_list = list(tab) # Cria uma cópia do tabuleiro
    line_list = list(tab_list[linha]) # Cria uma cópia da linha
    line_list[coluna] = jog # Marca a posição

    line_tup = tuple(line_list) # Transforma a função em um tuplo
    tab_list[linha] = line_tup  # Transforma a linha em um tuplo
    tab_tup = tuple(tab_list) # Transforma o tabuleiro em um tuplo

    return tab_tup 


# Projeto (2.2.8)
def verifica_k_linhas(tab, pos, jog, k):
   
    """
    Verifica se existem k peças consecutivas do jogador atual a partir de uma posição específica.
    
    A função verifica se, a partir de uma posição no tabuleiro, existem k peças consecutivas do jogador atual
    na horizontal, vertical, ou diagonal. Os argumentos devem ser válidos para a execução da função.
    
    Args:
        tab (tuple): O tabuleiro representado como um tuplo de tuplos.
        pos (int): A posição no tabuleiro.
        jog (int): O jogador atual, representado por 1 ou -1.
        k (int): O número de peças consecutivas necessárias para ganhar.
    
    Returns:
        bool: Retorna True se existirem k peças consecutivas do jogador atual a partir da posição específica,
              caso contrário retorna False.
    
    Raises:
        ValueError: Se o tabuleiro, a posição, o jogador, ou o argumento `k` forem inválidos.
    """
    # Verifica se os argumentos são válidos
    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab, pos) or not eh_jogador(jog) or not isinstance(k, int) or k <= 0:
        raise ValueError('verifica_k_linhas: argumentos invalidos')

    # Converte a posição em índices de linha e coluna
    num_linhas = len(tab)
    num_colunas = len(tab[0])
    pos_linha, pos_coluna = devolve_indice_posicao(tab, pos)
    
    if jog != tab[pos_linha][pos_coluna]:
        return False

    def contar_consecutivos(direcao_linha, direcao_coluna):
        count = 1  # Começa com 1 para incluir a posição atual
        # Verifica em uma direção (positiva)
        linha = pos_linha + direcao_linha
        coluna = pos_coluna + direcao_coluna
        while 0 <= linha < num_linhas and 0 <= coluna < num_colunas and tab[linha][coluna] == jog:
            count += 1
            linha += direcao_linha
            coluna += direcao_coluna

        return count

    # Verifica em todas as direções
    # Direção horizontal (0, 1) e (0, -1)
    total_horizontal = contar_consecutivos(0, 1) + contar_consecutivos(0, -1) - 1  # -1 para não contar a posição atual duas vezes
    if total_horizontal >= k:
        return True

    # Direção vertical (1, 0) e (-1, 0)
    total_vertical = contar_consecutivos(1, 0) + contar_consecutivos(-1, 0) - 1
    if total_vertical >= k:
        return True

    # Direção diagonal (1, 1) e (-1, -1)
    total_diagonal_descendente = contar_consecutivos(1, 1) + contar_consecutivos(-1, -1) - 1
    if total_diagonal_descendente >= k:
        return True

    # Direção diagonal (1, -1) e (-1, 1)
    total_diagonal_ascendente = contar_consecutivos(1, -1) + contar_consecutivos(-1, 1) - 1
    if total_diagonal_ascendente >= k:
        return True

    return False


# Projeto (2.3.1)
def eh_fim_jogo(tab, k):
    
    '''
    Verifica se o jogo terminou.

    A função determina se um jogo  num tabuleiro fornecido terminou, seja por um jogador ter
    completado uma sequência de `k` peças consecutivas ou por não haver mais posições livres
    no tabuleiro.

    Args:
        tab (tuple): O tabuleiro representado como um tuplo de tuplos.
        k (int): O número de peças consecutivas necessárias para ganhar.

    Returns:
        bool: Retorna True se o jogo terminou (um jogador ganhou ou não há posições livres),
              ou False caso contrário.

    Raises:
        ValueError: Se o tabuleiro ou o argumento `k` não forem válidos.
    '''

    # Verifica se os argumentos são válidos
    if not eh_tabuleiro(tab) or not isinstance(k, int) or k <= 0:
        raise ValueError('eh_fim_jogo: argumentos invalidos')
    
    # Verifica se existe uma linha de k ou mais consecutivos para algum jogador
    for pos in range(1, len(tab) * len(tab[0]) + 1):
        if verifica_k_linhas(tab, pos, 1, k) or verifica_k_linhas(tab, pos, -1, k):
            return True
    
    # Verifica se ainda existem posições livres
    for linha in tab:
        if 0 in linha:
            return False

    # Se não existem posições livres, o jogo termina em empate
    return True


# Projeto (2.3.2)
def escolhe_posicao_manual(tab):

    '''
    Solicita ao jogador para escolher uma posição livre no tabuleiro.

    Verifica se a posição escolhida pelo jogador é uma posição válida e livre no tabuleiro fornecido.
    Caso a posição não seja válida ou não esteja livre, o jogador será solicitado a escolher novamente.

    Args:
        tab (tuple): O tabuleiro representado como um tuplo de tuplos.

    Returns:
        int: A posição escolhida pelo jogador.

    Raises:
        ValueError: Se a posição escolhida não for válida ou não estiver livre no tabuleiro.
    '''

    if not eh_tabuleiro(tab):
        raise ValueError('escolhe_posicao_manual: argumento invalido') # Verifica se os argumentos são válidos
    
    pos = input("Turno do jogador. Escolha uma posicao livre: ") # Solicita ao jogador para escolher uma posição livre
    if pos.isdigit() == False: # Verifica se a posição escolhida pelo jogador é um número 
        raise ValueError('escolhe_posicao_manual: argumento invalido')# Verifica se a posição escolhida pelo jogador é uma posição válida
    if not eh_posicao(int(pos)) or not eh_posicao_valida(tab, int(pos)): # Verifica se a posição escolhida pelo jogador está livre no tabuleiro
        raise ValueError('escolhe_posicao_manual: argumento invalido') # Caso a posição não seja válida ou não esteja livre, o jogador será solicitado a escolher novamente

    while not eh_posicao_livre(tab, int(pos)): # Verifica se a posição escolhida pelo jogador está livre no tabuleiro
        pos = input("Turno do jogador. Escolha uma posicao livre: ") # Solicita ao jogador para escolher uma posição livre
        if pos.isdigit() == False: # Verifica se a posição escolhida pelo jogador é um número
            raise ValueError('escolhe_posicao_manual: argumento invalido') # Verifica se a posição escolhida pelo jogador é uma posição válida
        if not eh_posicao(int(pos)) or not eh_posicao_valida(tab, int(pos)): # Verifica se a posição escolhida pelo jogador está livre no tabuleiro
            raise ValueError('escolhe_posicao_manual: argumento invalido') # Caso a posição não seja válida ou não esteja livre, o jogador será solicitado a escolher novamente
            
    return int(pos) 
           

# Projeto (2.3.3)
def escolhe_posicao_auto(tab, jog, k, lvl):
    '''
    Escolhe automaticamente uma posição no tabuleiro para o jogador.

    A função escolhe automaticamente uma posição no tabuleiro para o jogador, com base no nível de
    dificuldade `lvl`. Se o nível for 'facil', a função escolhe uma posição adjacente a uma
    posição ocupada pelo jogador. Caso contrário, escolhe uma posição qualquer.

    Args:
        tab (tuple): O tabuleiro representado como um tuplo de tuplos.
        jog (int): O jogador que escolhe a posição (1 ou -1).
        k (int): O número de peças consecutivas necessárias para ganhar.
        lvl (str): O nível de dificuldade do jogo ('facil', 'medio' ou 'dificil').

    Returns:
        int: A posição escolhida pelo computador.

    Raises:
        ValueError: Se lvl, o tabuleiro, o jogador, ou o argumento k forem inválidos.
    '''
    if not eh_lvl(lvl) or not eh_tabuleiro(tab) or not eh_jogador(jog) or not isinstance(k, int) or k <= 0:
        raise ValueError('escolhe_posicao_auto: argumentos invalidos')

    if lvl == 'facil': 
        posicoes_jogador = obtem_posicoes_jogador(tab, jog) 

        possiveis_posicoes = ()
        for pos in posicoes_jogador:
            posicoes_adjacentes = obtem_posicoes_adjacentes(tab, pos) # Obtem as posicoes adjacentes
            for pos_adj in posicoes_adjacentes: # Verifica se as posicoes adjacentes estão livres
                if eh_posicao_livre(tab, pos_adj): # Se estiverem livres, adiciona-as
                    possiveis_posicoes += (pos_adj,) 
        
        if possiveis_posicoes == ():
            possiveis_posicoes = obtem_posicoes_livres(tab) # Se nenhuma das posicoes adjacentes estiver livre, escolhe uma livre

        pos_escolhida = possiveis_posicoes[0] # Escolhe a primeira posicao livre
        return pos_escolhida  
    
    if lvl == 'normal':
        L = k 
        while L > 0:
            for i in ordena_posicoes_tabuleiro(tab, obtem_posicoes_livres(tab)):
                novotab = marca_posicao(tab, 1, jog)
                if verifica_k_linhas(novotab, 1, jog, L) == True:
                    return i
                novotab = tab
            for i in ordena_posicoes_tabuleiro(tab, obtem_posicoes_livres(tab)):
                novotab = marca_posicao(tab, 1, -jog)
                if verifica_k_linhas(novotab, 1, -jog, L) == True:
                    return i
                novotab = tab
            L -= 1


                
    

# Projeto (2.3.4)
def jogo_mnk(cfg, jog, lvl):
    '''
    Executa um jogo de MNK entre um jogador e o computador.

    A função executa um jogo de MNK entre um jogador e o computador, com
    configuração `cfg` e nível de dificuldade `lvl`.

    Args:
        cfg (tuple): A configuração do jogo (m, n, k).
        jog (int): O jogador (1 para preto, -1 para branco).
        lvl (int): O nível de dificuldade do computador (entre 1 e 4).

    Returns:
        O resultado do jogo (1 se o jogador venceu, -1 se o computador
        venceu, 0 em caso de empate).
        

    Raises:
        ValueError: Se cfg, o tamanho de cfg, o jogador ou o nível forem inválidos.
    '''
    # Verifica se os argumentos são válidos
    if not isinstance(cfg, tuple) or len(cfg) != 3:
        raise ValueError('jogo_mnk: argumentos invalidos')
    
    m, n, k = cfg  # Desempacota a configuração
    if not (isinstance(m, int) and isinstance(n, int) and isinstance(k, int)):
        raise ValueError('jogo_mnk: argumentos invalidos')

    if not (2 <= m <= 100):
        raise ValueError('jogo_mnk: argumentos invalidos') # Verifica se m é um número entre 2 e 100
    
    if not (2 <= n <= 100):
        raise ValueError('jogo_mnk: argumentos invalidos') # Verifica se n é um número entre 2 e 100
    
    if k > n or k > m and k >= 1:
        raise ValueError('jogo_mnk: argumentos invalidos') # Verifica se k é um número entre 1 e min(m, n)
        
    tab = ((0,)*n,)*m # Cria um tabuleiro vazio
    eh_tabuleiro(tab)

    # Início do loop do jogo
    while True:

        tab_string = tabuleiro_para_str(tab) # Cria a string do tabuleiro
        print(tab_string) # Imprime o tabuleiro

        pos = escolhe_posicao_manual(tab) # Escolhe uma posicao livre
        if eh_posicao_valida(tab, pos): # Verifica se a posicao é valida
            if eh_posicao_livre(tab, pos): # Verifica se a posicao é livre
                tab = marca_posicao(tab, pos, jog) # Marca a posicao
                # if verifica_k_linhas == True:
                #     print(f"VITORIA\n{jog}")
                # else:
                #     print(f"EMPATE\n{0}")
        
        if obtem_posicoes_livres(tab) == (): # Verifica se há posicoes livres
            tab_string = tabuleiro_para_str(tab) # Cria a string do tabuleiro
            print(tab_string) # Imprime o tabuleiro
            print(f"EMPATE\n{0}") # Imprime EMPATE
            break # Encerra o loop
        elif eh_fim_jogo(tab, k): # Verifica se o jogo terminou
            tab_string = tabuleiro_para_str(tab) # Cria a string do tabuleiro
            print(tab_string) # Imprime o tabuleiro
            print(f"VITORIA\n{jog}") # Imprime VITORIA
            break # Encerra o loop
        
        pos_auto = escolhe_posicao_auto(tab, -jog, k, lvl)
        if eh_posicao_valida(tab, pos_auto):
            if eh_posicao_livre(tab, pos_auto):
                tab = marca_posicao(tab, pos_auto, -jog)
                # if verifica_k_linhas == True:
                #     print(f"DERROTA\n{-jog}")
                # else:
                #     print(f"EMPATE\n{0}")

        if obtem_posicoes_livres(tab) == ():
            tab_string = tabuleiro_para_str(tab)
            print(tab_string)
            print(f"EMPATE\n{0}")
            break
        elif eh_fim_jogo(tab, k):
            tab_string = tabuleiro_para_str(tab)
            print(tab_string)
            print(f"DERROTA\n{-jog}")
            break






# FUNÇÕES AUXILIARES

#(2.1.1)
def validate_tabuleiro(tup):
    '''
    É uma função auxiliar que verifica se o argumento fornecido é um tuplo e 
    se o argumento fornecido é um tuplo com entre 2 e 100 elementos.

    Retorna True se o argumento for um tuplo com entre 2 e 100 elementos, False caso contrário.

    Args:
        tup (tuple): O tuplo que deve ser validado.

    Returns:
        bool: True se o tuplo for um tuplo com entre 2 e 100 elementos, False caso contrário.
    '''
    if not isinstance(tup, tuple): # Verifica se é um tuplo
        return False 
    if not 2 <= len(tup) <= 100: # Verifica se o tuplo tem entre 2 e 100 elementos
        return False
    return True


# (2.1.8)
def convert_to_char(number):

    '''
    É uma função auxiliar que converte um número em um caractere.

    A função recebe um número inteiro como entrada e retorna o caractere que o representa.

    Se o número for 1, o caractere é 'X'.
    Se o número for 0, o caractere é '+'.
    Se o número for -1, o caractere é 'O'.

    Args:
        number (int): O número que deve ser convertido.

    Returns:    
        char (str): O caractere correspondente ao número fornecido.
    '''
    
    if number == 1: # Se o número for 1
        char = "X" # O char é 'X'
    elif number == 0: # Se o número for 0
        char = "+" # O char é '+'
    elif number == -1: # Se o número for -1
        char = "O" # O char é 'O'
    
    return char


#(2.2.3)
def devolve_tuplo_posicoes(tab, valor_pos):

    '''
    É uma função auxiliar que devolve um tuplo com as posições lineares de elementos específicos no tabuleiro.

    A função percorre o tabuleiro representado por `tab`, que é um tuplo de tuplos,
    e identifica as posições lineares onde o valor do elemento é igual a `valor_pos`.
    Cada posição linear é calculada começando a indexação em 1.

    Args:
        tab (tuple): O tabuleiro representado como um tuplo de tuplos.
        valor_pos (int): O valor dos elementos cuja posição linear deve ser devolvida.

    Returns:
        tuple: Um tuplo contendo as posições lineares dos elementos que correspondem a `valor_pos`.
    '''
    tup_posicoes = ()
    for x in range(len(tab)): # x percorre o tuplo 
        for i in range(len(tab[x])): #i percorre o tuplo
            pos = x * len(tab[x]) + i + 1  # Cálculo da posição (indexação começa em 1)
            if tab[x][i] == valor_pos:  # Se a posição estiver livre (valor 0)
                tup_posicoes += (pos,)  # Adicionar ao tuplo de posições livres
    return tup_posicoes


#(2.2.4)
def eh_jogador(jog):
    
    '''
    Verifica se o jogador é válido (1 ou -1).
    
    A função recebe um valor de jogador e verifica se ele é um dos valores válidos (1 ou -1).
    Retorna True se o jogador for válido e False caso contrário.

    Args:
        jog (int): O valor do jogador.

    Returns:
        bool: Retorna True se o jogador for válido e False caso contrário.
    '''
    # Verificar se o jogador é válido (1 ou -1)
    if jog not in [1, -1] or type(jog) != int:
        return False
    return True


#(2.2.5)
def devolve_indice_posicao(tab, pos):
     
    '''
    É uma função auxiliar que devolve o índice da posição no tabuleiro.

    A função percorre o tabuleiro representado por `tab`, que é um tuplo de tuplos,
    e encontra o índice da posição que corresponde ao número linear dado por `pos`.
    A indexação das posições começa em 1.

    Args:
        tab (tuple): O tabuleiro representado como um tuplo de tuplos.
        pos (int): O número linear da posição que deve ser encontrada.

    Returns:
        tuple: O índice da posição correspondente ao número linear dado por `pos`.
    '''
    for x in range(len(tab)): # x percorre o tuplo
        for i in range(len(tab[x])): #i percorre o tuplo
            pos_aux = x * len(tab[x]) + i + 1  # Cálculo da posição (indexação começa em 1)
            if pos_aux == pos:
                return (x, i)
            

#(2.3.3)
def eh_lvl(lvl):
    '''
    Esta função é uma função auxiliar que verifica se o nível de entrada é válido, podendo ser 'facil', 'normal' ou 'dificil'. 
    Retorna True se o nível for válido e False caso contrário.

    Args:
        lvl (str): O nível de dificuldade do jogo ('facil', 'normal' ou 'dificil').

    Returns:
        bool: Retorna True se o nível for necessário ou False caso contrário.
    '''
    if lvl not in ('facil', 'normal', 'dificil'): # Verifica se o nível é valido
        return False
    else:
        return True


#(2.2.6)
def posicao_central(nr_linhas, nr_colunas):
    '''
    É uma função auxiliar que devolve a posição linear central do tabuleiro.

    A função recebe o número de linhas e colunas do tabuleiro e calcula a posição linear central.

    Args:
        nr_linhas (int): O número de linhas do tabuleiro.
        nr_colunas (int): O número de colunas do tabuleiro.

    Returns:
        int: A posição linear central do tabuleiro.
    '''

    pos_linear = (nr_linhas // 2) * nr_colunas + (nr_colunas // 2) + 1 # Cálculo da posição cental (indexação começa em 1)
    return pos_linear



