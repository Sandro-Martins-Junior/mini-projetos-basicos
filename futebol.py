import random
from collections import defaultdict

# Lista de jogadores com habilidades, posições e disponibilidade (nome, habilidade, posição, disponibilidade)
jogadores = [
    ("Celso", 85, "Goleiro", False), ("jose", 80 , "Goleiro", True), ("Barnei", 80, "Defensor", True), ("Fabinho", 85, "Defensor", False),
    ("Juninho", 88, "Meio-campo", True), ("Sandro", 80, "Atacante", True), ("Testa", 90, "Goleiro", True),
    ("Caue", 85, "Defensor", False), ("Fabiano", 85, "Meio-campo", False), ("Tabajara", 84, "Atacante", True),
    ("Rudi", 90, "Defensor", True), ("Ralf", 80, "Atacante", False), ("Diogo", 85, "Meio-campo", True),
    ("Ferreirinha", 78, "Defensor", True), ("Joao Vitor", 82, "Meio-campo", False),
    ("Xitao", 89, "Atacante", False),
    ("Daniel", 86, "Atacante", False), ("Marcelo", 90, "Meio-campo", False) , ("Val", 83 ,"Atacante", True),
    ("murilo", 87, "Atacante",  True),("Everton", 88, "Meio-campo", True), ("toco", 80 , "Defensor", True),
    ("leo", 85,"Meio-campo", True)
    ]

# Filtra os jogadores disponíveis
jogadores_disponiveis = [jogador for jogador in jogadores if jogador[3]]

# Separa os jogadores por posição
posicoes = defaultdict(list)
for jogador in jogadores_disponiveis:
    posicoes[jogador[2]].append(jogador)

# Função para dividir jogadores de uma posição em times equilibrados
def dividir_por_posicao(jogadores):
    jogadores.sort(key=lambda x: x[1], reverse=True)  # Ordena por habilidade
    Laranja, Azul = [], []
    soma_time1, soma_time2 = 0, 0

    for jogador in jogadores:
        if soma_time1 <= soma_time2:
            Laranja.append(jogador)
            soma_time1 += jogador[1]
        else:
            Azul.append(jogador)
            soma_time2 += jogador[1]

    return Laranja, Azul

# Cria os times
Laranja, Azul = [], []
soma_habilidade_time1 , soma_habilidade_time2 = 0,0

# Divide os jogadores de cada posição nos dois times
for posicao, jogadores_posicao in posicoes.items():
    random.shuffle(jogadores_posicao)  # Embaralha os jogadores dentro da posição
    t1, t2 = dividir_por_posicao(jogadores_posicao)
    Laranja.extend(t1)
    Azul.extend(t2)
    soma_habilidade_time1 += sum(j[1] for j in t1)
    soma_habilidade_time2 += sum(j[1] for j in t2)


# Exibe os times formados
print("Time Laranja:", [(jogador[0], jogador[1], jogador[2]) for jogador in Laranja])
print(soma_habilidade_time1)
print("Time Azul:", [(jogador[0], jogador[1], jogador[2]) for jogador in Azul])
print(soma_habilidade_time2)




