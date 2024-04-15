<h1 align="center">Blum Blum Shub (BBS)</h1>

<p align="center">Atividade desenvolvida em Python durante a disciplina de Segurança em Sistemas de Computação <a href="https://sites.google.com/a/ice.ufjf.br/edelbertofranco/disciplinas/gradua%C3%A7%C3%A3o/2024-1-dcc075-seguran%C3%A7a?authuser=0">DCC075</a></p>

## Conceito

Blum Blum Shub (BBS) é um gerador de números pseudoaleatórios proposto por Lenore Blum, Manuel Blum e Michael Shub em 1986.

O algoritmo BBS é:

$$
x_{n+1} = (x_n)^2 \mod M
$$

onde $$M = p*q$$ é o produto de dois números primos muito grandes p e q. Em cada passo do algoritmo, obtém-se um resultado para $x_n$; o resultado é geralmente o bit de paridade de $x_n$ ou um ou mais dos bits menos significativos de $x_n$. Os dois números primos, p e q, devem ser ambos congruentes a 3 (mod 4).

## Instalação do SimPy 

```bash
# Instale o simpy
$ pip install simpy

```
