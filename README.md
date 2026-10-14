# Projeto 1 — Jogo MNK

Projeto académico desenvolvido para a unidade curricular **Fundamentos da Programação**. Implementa as operações e a lógica de um jogo MNK: num tabuleiro com `M` linhas e `N` colunas, os jogadores alternam jogadas e vence quem formar uma sequência de `K` peças consecutivas na horizontal, vertical ou diagonal.

O tabuleiro é representado por tuplos de tuplos: `1` corresponde a `X`, `-1` a `O` e `0` a uma posição livre. As posições são numeradas a partir de 1, da esquerda para a direita e de cima para baixo.

## Requisitos

- Python 3
- `pytest` para executar os testes

O módulo do jogo usa apenas a biblioteca padrão do Python.

## Como executar

O projeto não define um comando de linha de comandos; o jogo é iniciado através da função `jogo_mnk`. Por exemplo, para jogar num tabuleiro 3×3, com 3 peças para vencer e o jogador a usar `X`:

```bash
python3 -c 'import projectoFP; projectoFP.jogo_mnk((3, 3, 3), 1, "facil")'
```

Introduza o número da posição pretendida quando solicitado. A função recebe a configuração `(M, N, K)`, o símbolo do jogador (`1` para `X` ou `-1` para `O`) e a dificuldade (`"facil"`, `"normal"` ou `"dificil"`).

## Testes

Instale as dependências de desenvolvimento e execute a suite de testes públicos:

```bash
python3 -m pip install -r requirements-dev.txt
python3 -m pytest -q
```

Na versão atual, 46 dos 53 testes passam; os restantes assinalam diferenças entre o comportamento implementado e o esperado na ordenação de posições, validação de entradas, estratégias do computador e resultado devolvido pelo jogo.

## Estrutura

| Ficheiro | Descrição |
| --- | --- |
| `projectoFP.py` | Implementação das funções de tabuleiro, validação, jogadas, estratégias e jogo. |
| `test_public.py` | Testes públicos para as funções do projeto e para alguns jogos. |
| `requirements-dev.txt` | Dependências necessárias para executar os testes. |
| `Enunciado.pdf` | Enunciado do projeto fornecido para a cadeira. |

A folha auxiliar de avaliação fornecida para a cadeira é um material local e não faz parte deste repositório.
