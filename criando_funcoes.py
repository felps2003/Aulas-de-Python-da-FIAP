# -*- coding: utf-8 -*-
"""
Codigo criado em aula para aprendermos como funciona a criação de funções em python
"""

def saudacao(msg, nome):
  print(msg+" "+nome+", seja bem vindo a FIAP")

saudacao("Boa noite","Felype")

def saudacao1(hora,nome):
  if hora > 4 and hora < 12:
    print(f"Bom dia {nome}, seja bem vindo a FIAP")
  elif hora > 12 and hora < 19:
    print(f"Boa tarde {nome}, seja bem vindo a FIAP")
  else:
    print(f"Boa noite {nome}, seja bem vindo a FIAP")

saudacao1(16,"Felype")

def proximoNum(numero):
  print(numero+1)

proximoNum(5)

def maiorNum(n1,n2):
  if n1 > n2:
    print(n1)
  else:
    print(n2)

maiorNum(12,42)

def maiorNum3(n1,n2,n3):
  if n1 > n2:
    x = n1
  else:
    x = n2
  if n3 > x:
    print(n3)
  else:
    print(x)

maiorNum3(100,80,70)

