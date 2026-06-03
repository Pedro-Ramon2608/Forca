# 🪓 Jogo da Forca Dinâmico em Python

Este é um jogo da forca interativo baseado em terminal desenvolvido em Python. O grande diferencial desta versão é que a palavra secreta (focada em séries e desenhos clássicos) é sorteada de forma totalmente aleatória a cada nova partida.  

🕹️ Como Funciona o Jogo
---

Sorteio Automático: O sistema utiliza o módulo nativo `random` para escolher uma obra temática surpresa contida na lista de palavras.

* O jogador visualiza os traços `_` correspondentes a cada letra da palavra sorteada. 

* A cada rodada, o usuário digita uma letra:  

  - Se a letra estiver correta, ela é revelada na posição exata (tratando letras maiúsculas e minúsculas).  
  
  - Se a letra estiver errada, ela entra para a lista de erros e o jogador perde uma tentativa.
  
* O jogador tem um limite máximo de 5 tentativas erradas antes do Game Over.  

* O jogo monitora letras repetidas para evitar que o usuário perca chances com o mesmo palpite.  

🛠️ Conceitos Praticados
---
* Geração Aleatória (Randomização): Uso da biblioteca `random` do Python para garantir a rejogabilidade, fazendo com que cada partida tenha um desafio diferente.

* Estruturas de Repetição: Uso do laço `while True` para manter o fluxo do jogo ativo até que haja uma vitória ou derrota.  

* Controle de Fluxo: Validações com `if`, `elif` e `else` para gerenciar a lógica de acertos, erros e repetições de letras.  

* Manipulação de Listas: Uso de métodos como `.append()` para armazenar erros e a função `enumerate()` para descobrir os índices corretos * das letras acertadas.  

* Tratamento de Strings: Aplicação de `.upper()` e `.lower()` para garantir que o jogo seja case-insensitive (não diferencie maiúsculas de minúsculas ao validar).  

📂 Estrutura do Arquivo
---
O projeto é composto por um único arquivo principal:

* `forca.py`: Contém a lista de palavras temáticas, a lógica de sorteio e toda a execução do jogo no terminal.  

⚙️ Como Executar
---
Bash
```bash
Bash

# Execute o script para iniciar uma partida com uma palavra aleatória

python forca.py
```
Exemplo de Execução no Terminal:
```plaintext
Plaintext

Vamos jogar o jogo da forca!
_ _ _ _ _ _ _ _ _ _ _   _ _ _ _   _ _ _ _

Digite uma letra: o   # input do usuário

A letra o está na palavra!
Palavra:  _ _ o _ _ _ _ _ _   _ _ _ _   _ _ _ _
Letras erradas:  
Tentativas restantes: 5
```
