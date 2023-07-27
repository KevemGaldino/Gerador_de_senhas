# Gerador de senhas

#Importando módulos

import random
import sys

#Definindo variáveis

num = '0123456789'
letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sym = '!@#$%*&:;/?][-.'
all = num + letras + sym

print('Criando sua senha!\n')
print('Escolha seus parâmetros!\n')

#Escolhas do usuário

tamanho = int(input('Digite quantos caracteres terá sua senha (tamanho da senha): '))
qtd_num = int(input('Digite a quantidade de números que deseja em sua senha: '))
qtd_letras = int(input('Digite a quantidade de letras que terá sua senha: '))
qtd_sym = int(input('Digite a quantidade de símbolos que terá sua senha: '))
somar = qtd_num + qtd_letras + qtd_sym

#Verificação de erros

while(True):
    if somar > tamanho:
        print('A soma dos valores tem que bater com o tamanho da senha escolhida!')
        sys.exit()
    else:
        break

#Gerando a senha

#Senha com todos os caracteres
password = '' .join(random.sample(all, tamanho))

#Gerando a senha segura
password_num = '' .join(random.sample(num, qtd_num))
password_letras = '' .join(random.sample(letras, qtd_letras))
password_sym = '' .join(random.sample(sym, qtd_sym))
soma = password_sym + password_num + password_letras
juntar = '' .join(random.sample(soma, tamanho))

print('Esta aqui é a sua senha: {}'.format(juntar))
