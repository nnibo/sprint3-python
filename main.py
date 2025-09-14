# Copa Passa a Bola - Versão Terminal

# Listas de usuários
jogadoras = []
torcedoras = []

# Jogos, melhores momentos e destaques em arrays
jogos = ["Leonas FC x Guerreiras - 10/09 14h", "Estrelas x Panteras - 11/09 16h"]
melhores_momentos = [
    'Adriana pega a bola, dribla 3 jogadoras e faz um golaço',
    'Debinha cruza, e de cabeça Marta faz o gol',
    'Leticia defende uma bola em cima da linha'
]
destaques_torneio = [
    {"Nome": "Marta", "Estatistica": 20, "Posição": "Meia Atacante", "Troféu": "MVP"},
    {"Nome": "Marta", "Estatistica": 35, "Posição": "Atacante", "Troféu": "Artilheira"},
    {"Nome": "Marta", "Estatistica": 2, "Posição": "Zagueira", "Troféu": "Melhor Defensora"}
]

# Times e campeonatos
times = [{"Nome": "Corinthians", "Jogadoras": []}]
campeonatos = [
    {"Nome": "Copa PAB Teste", "Edição": 1, "Disponivel": False, "Times": []},
    {"Nome": "PAB Edição 2", "Edição": 2, "Disponivel": False, "Times": []},
    {"Nome": "PAB Edição 3", "Edição": 3, "Disponivel": True, "Times": []}
]

# Exemplo de loja de 2 tipos de usuarios
lista_produtos_jogadora = [{"Produto": "Chuteira Especial", "Preço": "200 pontos"}, {"Produto": "Treinamento no CT do Corinthians", "Preço": "300 pontos"}]
lista_produtos_torcedora = [{"Produto": "Camisa Oficial", "Preço": "R$150"}, {"Produto": ""}]


# =================
# Funções de Menu
# =================

def mostrar_menu_jogadora():
    print("""
    --- Menu Jogadora ---
    1 - Home
    2 - Chaveamento
    3 - Campeonatos
    4 - Mapa do Evento
    5 - Loja
    6 - Notícias
    0 - Logout
    """)

def mostrar_menu_torcedora():
    print("""
    --- Menu Torcedora ---
    1 - Home
    2 - Chaveamento
    3 - Mapa
    4 - Loja
    5 - Notícias
    0 - Logout
    """)

# ===================================
# Telas das jogadoras e torcedoras
# ===================================

# Home page com jogos, videos e noticias
def home_page():
    print("\n🏆 Copa Passa a Bola - Bem-vindo(a)!")
    print("Este torneio tem como objetivo dar visibilidade às jogadoras.")
    print("Veja abaixo informações e destaques!\n")

    # Mostrando os jogos
    print("📅 Jogos do dia:")
    for jogo in jogos:
        print("-", jogo)

    # Mostrando cada video
    print("\n🎥 Melhores Momentos:")
    for video in melhores_momentos:
        print("-", video)

    # Mostrando as melhores do torneio
    print("\n⭐ Destaques do Torneio:")
    for destaque in destaques_torneio:
        print(f"{destaque['Nome']} - {destaque['Troféu']} ({destaque['Estatistica']} estatísticas)")

# Gerando o chaveamento da copa
def chaveamento():
    print("\n📊 Chaveamento do Torneio:")
    if len(times) < 2:
        print("Não tem times suficientes para gerar o chaveamento")
    else:
        print(f"{times[0]['Nome']} x {times[1]['Nome']}")
# Mostrando as quadras e os jogos
def mapa_evento():
    print("\n🗺️ Mapa do Evento:")
    print("Quadra 1: Leonas FC x Guerreiras")
    print("Quadra 2: Estrelas x Panteras")

# Mostrando as noticias do futebol feminino
def noticias():
    print("\n📰 Notícias do Futebol Feminino:")
    print("- Seleção Sub-20 vence torneio internacional!")
    print("- Novo campeonato feminino lançado no interior de SP.")
    print("- Marta anuncia planos de aposentadoria após a Copa.")

# ==================================================
# FUNCIONALIDADES E TELAS EXCLUSIVAS DAS JOGADORAS
# ==================================================

def adicionar_jogadora_time():
    # pega sempre o último time criado, o que o usuario acabou de adicionar
    time = times[-1]
    adicionar_jogadora = int(input(f"Deseja adicionar jogadoras ao time {time['Nome']}? 1 - Sim | 2 - Não: "))
    if adicionar_jogadora == 1:
        nome_jogadora = input("Digite o nome da jogadora: ")
        jogadoras.append({"Nome": nome_jogadora, "Senha": None})
        time["Jogadoras"].append(nome_jogadora)
        print("Jogadora adicionada com sucesso")

# Função para ingressar em um campeonato
def campeonatos_menu():
    print("\n⚽ Campeonatos Disponíveis:")
    for campeonato in campeonatos:
        print(f"Edição {campeonato['Edição']} - {campeonato['Nome']} | Disponível: {campeonato['Disponivel']}")

    escolha = int(input("Digite a edição do campeonato que deseja ingressar: "))
    for campeonato in campeonatos: 
        # Validação para ver se a edição do campeonato é a mesma que o usuario escolheu e se o campeonato está disponivel para inscrição
        if campeonato["Edição"] == escolha and campeonato["Disponivel"]:
            if len(times) == 1:  
                nome_time = input("Digite o nome do seu time: ")
                novo_time = {"Nome": nome_time, "Jogadoras": []}
                times.append(novo_time)
                print("✅ Time criado e inscrito com sucesso!")

                adicionar_jogadora_time()
            return
    print("⚠️ Campeonato não encontrado ou indisponível.")

# Loja exclusiva da jogadora, mostrando o nome do produto e o preço
def loja_jogadora():
    print("\n🛒 Loja da Jogadora:")
    for item in lista_produtos_jogadora:
        print(f"{item['Produto']} - {item['Preço']}")

# Loja exclusiva da torcedora mostrando nome e preço do produto
def loja_torcedora():
    print("\n🛒 Loja da Torcedora:")
    for item in lista_produtos_torcedora:
        print(f"{item['Produto']} - {item['Preço']}")


# ==============================
# Programa Principal
# ==============================

def main():
    while True:
        print("""
        Escolha como deseja fazer login:
        1 - Jogadora
        2 - Torcedora
        0 - Sair
        """)
        opcao = input("Digite sua opção: ")

        # Navegação de telas de um usuario com login de jogadora
        if opcao == "1":
            print("=== LOGIN JOGADORA ===")
            nome = input("Nome: ")
            senha = input("Senha: ")
            # Adicionando essa jogadora no array de jogadoras
            jogadoras.append({"Nome": nome, "Senha": senha})
            print(f"✅ Bem-vinda, {nome}!")

            navegacao = -1
            while navegacao != "0":
                # Chamando a função de printar o menu da jogadora
                mostrar_menu_jogadora()
                navegacao = input("Escolha: ")

                match navegacao:
                    case "1":
                        home_page()
                    case "2":
                        chaveamento()
                    case "3":
                        campeonatos_menu()
                    case "4":
                        mapa_evento()
                    case "5":
                        loja_jogadora()
                    case "6":
                        noticias()
                    case "0":
                        print("Saindo da conta da jogadora...")
        
        # Navegação de telas da torcedora
        elif opcao == "2":
            print("=== LOGIN TORCEDORA ===")
            nome = input("Nome: ")
            senha = input("Senha: ")
            # Adicionando a torcedora no array de torcedoras
            torcedoras.append({"Nome": nome, "Senha": senha})
            print(f"✅ Bem-vinda, {nome}!")

            navegacao = -1
            while navegacao != "0":
                # Chamando a função do menu da torcedora
                mostrar_menu_torcedora()
                navegacao = input("Escolha: ")

                match navegacao:
                    case "1":
                        home_page()
                    case "2":
                        chaveamento()
                    case "3":
                        mapa_evento()
                    case "4":
                        loja_torcedora()
                    case "5":
                        noticias()
                    case "6":
                        print("Saindo da conta da torcedora...")

        elif opcao == "0":
            print("Programa finalizando...")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()