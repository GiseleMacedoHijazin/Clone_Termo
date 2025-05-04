import random  # Importa o módulo random para escolher palavras aleatórias

# Lista de palavras separadas por dificuldade (número de letras)
palavras = {
    5: ["manga", "cobra", "vento", "piano", "sonho"],
    6: ["baleia", "garoto", "xadrez", "cabelo", "tomate"],
    7: ["abacate", "canetas", "natural", "vitrola", "tabuada"],
}

# Função que exibe as regras do jogo
def mostrar_regras():
    print("=" * 50)
    print("JOGO DA PALAVRA SECRETA")
    print("=" * 50)
    print("""
REGRAS DO JOGO
1. Escolha a dificuldade: 5, 6 ou 7 letras.
2. Você terá tantas tentativas quanto o tamanho da palavra.
3. Após cada palpite, você verá:
   - Letras corretas no lugar certo. Ex:[A]
   - Letras corretas no lugar errado. Ex:(a)
   - Letras erradas. Ex: a
4. O jogo termina quando você acerta ou acaba as tentativas.
5. No final, a resposta será mostrada.

Boa sorte! Vamos jogar!
    """)

# Função principal que executa o jogo
def jogar():
    while True:  # Loop principal do jogo, para permitir jogar várias vezes
        mostrar_regras()  # Mostra as regras a cada nova rodada

        # Solicita ao jogador que escolha a dificuldade
        dificuldade = None
        while dificuldade not in palavras:  # Garante que a entrada seja válida
            entrada = input("Escolha a dificuldade (5, 6 ou 7 letras): ")
            if entrada.isdigit():  # Verifica se a entrada é um número
                dificuldade = int(entrada)
                if dificuldade not in palavras:
                    print("Dificuldade inválida. Tente novamente.")
            else:
                print("Por favor, insira um número válido.")

        # Seleciona a lista de palavras de acordo com a dificuldade escolhida
        if dificuldade == 5:
            lista_de_palavras = palavras[5]
        elif dificuldade == 6:
            lista_de_palavras = palavras[6]
        else:
            lista_de_palavras = palavras[7]  # Se não for 5 ou 6, é 7

        # Escolhe uma palavra aleatória da lista
        palavra_secreta = random.choice(lista_de_palavras)

        # Define o número de tentativas com base no tamanho da palavra
        tentativas = len(palavra_secreta)

        # Informa ao jogador que o jogo vai começar
        print()
        print("Uma palavra foi escolhida. Boa sorte!")
        print()

        # Loop para os palpites do jogador
        while tentativas > 0:
            print(f"Tentativas restantes: {tentativas}")
            palpite = input(f"Digite seu palpite de {dificuldade} letras: ")
            palpite = palpite.lower()  # Converte o palpite para minúsculas

            # Verifica se o palpite tem o tamanho correto
            if len(palpite) != dificuldade:
                print()
                print(f"A palavra deve ter exatamente {dificuldade} letras.")
                print()
                continue  # Volta para o início do loop

            # Gera a dica com base no palpite do jogador
            dica = ""
            for i in range(dificuldade):
                if palpite[i] == palavra_secreta[i]:
                    dica += f"[{palpite[i].upper()}]"  # Letra certa no lugar certo
                elif palpite[i] in palavra_secreta:
                    dica += f"({palpite[i]})"  # Letra certa no lugar errado
                else:
                    dica += f" {palpite[i]} "  # Letra errada

            print(f"Dica: {dica}")
            print()

            # Verifica se o jogador acertou a palavra completa
            if palpite == palavra_secreta:
                print(f"Parabéns! Você acertou a palavra '{palavra_secreta.upper()}'!")
                break  # Sai do loop de tentativas

            tentativas -= 1  # Reduz o número de tentativas restantes

        # Se o jogador não acertou a palavra após todas as tentativas
        if palpite != palavra_secreta:
            print(f"Você perdeu! A palavra secreta era: '{palavra_secreta.upper()}'.")

        # Pergunta se o jogador deseja jogar novamente
        print()
        jogar_novamente = input("Gostaria de jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até logo!")
            break  # Sai do loop principal e encerra o jogo

# Inicia o jogo chamando a função principal
jogar()
