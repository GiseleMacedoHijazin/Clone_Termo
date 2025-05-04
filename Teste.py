import random

# Lista de palavras por dificuldade
palavras = {
    5: ["manga", "cobra", "vento", "piano", "sonho"],
    6: ["baleia", "garoto", "xadrez", "cabelo", "tomate"],
    7: ["abacate", "canetas", "natural", "vitrola", "tabuada"],
}

# Função que mostra as regras do jogo
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

# Função principal do jogo
def jogar():
    while True:
        mostrar_regras()

        # Solicitar a dificuldade
        dificuldade = None
        while dificuldade not in palavras:
            entrada = input("Escolha a dificuldade (5, 6 ou 7 letras): ")
            if entrada.isdigit():
                dificuldade = int(entrada)
                if dificuldade not in palavras:
                    print("Dificuldade inválida. Tente novamente.")
            else:
                print("Por favor, insira um número válido.")

        # Primeiro, pegamos a lista de palavras com o tamanho escolhido pelo jogador
        if dificuldade == 5:
            lista_de_palavras = palavras[5]
        elif dificuldade == 6:
            lista_de_palavras = palavras[6]
        else:  # Se não for 5 nem 6, só pode ser 7
            lista_de_palavras = palavras[7]

        # Agora, escolhemos uma palavra aleatória dessa lista
        palavra_secreta = random.choice(lista_de_palavras)

        # O número de tentativas será igual ao número de letras da palavra
        tentativas = len(palavra_secreta)

        # Informamos ao jogador que o jogo vai começar
        print()
        print("Uma palavra foi escolhida. Boa sorte!")
        print()

        # Loop para os palpites
        while tentativas > 0:
            print(f"Tentativas restantes: {tentativas}")
            palpite = input(f"Digite seu palpite de {dificuldade} letras: ")
            palpite = palpite.lower()

            # Verifica se o palpite tem o tamanho correto
            if len(palpite) != dificuldade:
                print()
                print(f"A palavra deve ter exatamente {dificuldade} letras.")
                print()
                continue

            # Analisando o palpite
            dica = ""
            for i in range(dificuldade):
                if palpite[i] == palavra_secreta[i]:
                    dica += f"[{palpite[i].upper()}]"  # Letra correta no lugar certo
                elif palpite[i] in palavra_secreta:
                    dica += f"({palpite[i]})"  # Letra correta no lugar errado
                else:
                    dica += f" {palpite[i]} "  # Letra errada

            print(f"Dica: {dica}")
            print()

            # Verifica se o jogador acertou a palavra
            if palpite == palavra_secreta:
                print(f"Parabéns! Você acertou a palavra '{palavra_secreta.upper()}'!")
                break

            tentativas -= 1

        if palpite != palavra_secreta:
            print(f"Você perdeu! A palavra secreta era: '{palavra_secreta.upper()}'.")

        # Pergunta se o jogador quer jogar novamente
        print()
        jogar_novamente = input("Gostaria de jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até logo!")
            break

# Inicia o jogo
jogar()
