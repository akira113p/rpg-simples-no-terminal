# RPG Simples no Terminal

Um jogo de RPG por turnos, em modo texto, feito em Python para rodar direto no terminal.

Este projeto foi desenvolvido como **trabalho de escola** (FIAP), então é intencionalmente simples: tudo está em um único arquivo (`app.py`) e roda por meio de `print()` e `input()`.

## Como funciona o jogo

Ao iniciar, você escolhe um nome e uma classe. Cada classe tem atributos e ataques diferentes:

| Classe | Vida | Magia | Agilidade | Força | Ataques |
|---|---|---|---|---|---|
| Mago | 80 | 15 | 6 | 1 | Fireball, ThunderBolt, IceDagger |
| Guerreiro | 150 | 0 | 3 | 10 | Ruptura, Impacto, Devastação |
| Arqueiro | 100 | 1 | 10 | 5 | Perfuração, Tempestade, Disparo Pesado |

O dano de cada ataque é calculado a partir da combinação de força, magia e agilidade da classe.

Depois de escolher a classe, um menu principal permite:

- **Status** – ver vida, XP, nível, atributos e dano dos ataques atuais.
- **Classificação** – ver seu ranking atual (Bronze, Prata, Ouro ou Lendário, de acordo com o nível).
- **Batalha** – enfrentar um inimigo sorteado aleatoriamente entre Goblin, Bandido e Golem de Pedra, com vida/ataque/XP que escalam conforme a fase.
- **Sair do jogo** – encerrar a partida, com confirmação.

### Combate

O combate é por turnos. A cada turno você escolhe um dos ataques disponíveis (ou poupa o inimigo), com chance de acerto crítico (dano dobrado). O inimigo também pode acertar um crítico contra você. Você tem ainda uma **habilidade especial**, que carrega a cada turno e causa dano em dobro quando atinge o máximo.

### Progressão

- São necessários 1000 de XP para subir de nível.
- O 2º ataque de cada classe é desbloqueado no nível 4, e o 3º ataque no nível 11.
- Ao subir de nível, você escolhe um atributo para aprimorar (vida, magia, agilidade ou força).
- Vencer batalhas também avança a "fase" do jogo, deixando os próximos inimigos mais fortes.

Se sua vida chegar a zero, o jogo termina e mostra um resumo final (nome, classe, ranking e quantidade de inimigos derrotados).

## Tecnologia

- Python 3 (biblioteca padrão apenas, usa o módulo `random`)

## Como rodar

```bash
python app.py
```

Depois é só seguir as instruções que aparecem no terminal.

## Licença

Projeto acadêmico sem licença definida. Sinta-se livre para explorar o código como referência de estudo.
