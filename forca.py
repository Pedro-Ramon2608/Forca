from random import choice

palavras = ["Brooklyng nine-nine", "Grey's anatomy", "Os três é demais", "Um maluco no pedaço", "Manda-chuva"]

palavra_secreta = choice(palavras)

letras_descobertas = ["_"] * len(palavra_secreta)

erros = []

max_erros = 5

print("Vamos jogar o jogo da forca!")
print(" ".join(letras_descobertas))

while True:
    letra = input("Digite uma letra: ")[0]

    if (letra in letras_descobertas) or (letra in erros) or (letra.upper() in letras_descobertas) or (letra.upper() in erros):
        print("\nVocê já tentou essa letra.\n")
        continue

    if letra.upper() in palavra_secreta or letra.lower() in palavra_secreta:
        print(f"\nA letra {letra} está na palavra!")
        for i, char in enumerate(palavra_secreta):
            if char in letra:
                letras_descobertas[i] = letra
            elif char in letra.upper():
                letras_descobertas[i] = letra.upper()
    else: 
        print(f"\nA letra {letra} NÃO está na palavra.")
        erros.append(letra)

    print("\nPalavra: ", " ".join(letras_descobertas))
    print("Letras erradas: ", ", ".join(erros))
    print(f"Tentativas restantes: {max_erros - len(erros)}\n")
    
    if "_" not in letras_descobertas:
        print(f"\nVocê ganhou!!! Parabéns! A palavra secreta era '{palavra_secreta}'")
        break

    if len(erros) >= max_erros:
        print(f"\nVocê perdeu! A palavra secreta era '{palavra_secreta}'")
        break
