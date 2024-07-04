from datetime import datetime
from random import randrange
import random
import time
import os
import sys
pessoas = []
transacao = []
def traco(x = 50):
    for i in range(0,x):
        print("=", end="")
    print("\n")

def escolha():
    guia = ' '
    print('sasd')
    while guia not in '0123456789':
        guia = input('Sua escolha : (APENAS NÚMEROS) ') 
    return guia

def limpar():
    os.system('cls') or None

def iniciar():
    limpar()
    traco() 
    print('''
        Bem-vindo ao banco Félix, comece escolhendo uma opção"
        1.CADASTRAR
        2.SAIR DO BANCO
        '''
    )
    a = escolha()
    traco()
    if a == '1' :
        menu_cadastro()
    elif a == '2' :    
        print('espera')
def menu_cadastro():
    limpar()
    traco()  
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu cpf: ")
    saldo = float(input("Quanto deseja depositar? "))
    if cpf in pessoas:
        print("Alguém já tem este cpf, tente com outro")
        time.sleep(5)
        menu_cadastro()
    else :
        pessoas.append([nome, cpf, saldo])

    global posi

    for posicao, valor  in enumerate(pessoas):
        if valor[1] == cpf:
            posi = posicao   
    transacao.append([{'Valor':[],'Destinatário':[],'Data':[]},
                      {}])                            
    limpar()
    traco()
    print(
        "\nAgora, para onde deseja ir?\n"
        "1.MENU PRINCIPAL\n"
        "2.SAIR DA CONTA\n"
        "3.SAIR DO BANCO"
        )
    b = escolha() 
    limpar()
    if b == '1' :# menu principal
        menu_principal()  
    elif b == '2':
        print('espera')     
    elif b == 3 :
        print('espera')   
    traco()
    
def menu_principal():
    limpar()
    traco() 
    print(
        f"BEM-VINDO AO BANCO FÉLIX,{pessoas[posi][0]}\n"
        '''MENU PRINCIPAL
        1. INSERIR
        2. ALTERAR
        3. CONSULTAR
        4. EXCLUIR CONTA
        5. SAIR DA CONTA
        6. SAIR DO BANCO'''
        )
    c = escolha()
    if c == '1' : # menu do inserir
        inserir()
    elif c == '2' :# menu  alterar, deixar os comprovantes pix e deposito aqui, porém ainda deixa-los lá.
        print('calma')
    elif c == '3' : # menu consultar
        limpar()
        traco()
        print("INFORMAÇÕES DA CONTA :\n"
        f"NOME: {pessoas[posi][0]}\n"
        f"CPF: {pessoas[posi][1]}\n"            
        f"SALDO BANCÁRIO: {pessoas[posi][2]}\n"           
        )
        input('Quando quiser ')
        traco()
        menu_principal()
    elif c == '4' : 
        limpar()
        traco()
        exclui = input("EXCLUIR CONTA?")
        if exclui.lower() == "sim" :
            exit()
        elif exclui.lower() == "não" :
            menu_principal()  
    elif c == '5' :
        print('saiu da conta')
    elif c == '6' :
        print('fim')             
    traco() 
def inserir():
    limpar()
    traco()
    print(
    '''TRANSFERÊNCIAS
    1.FAZER PIX
    2.DEPOSITAR
    3.VER EXRATO
    4.VOLTAR PARA O MENU PRINCIPAL'''
    )
    d = escolha()
    if d == '1' : # opção de enviar pix
        pix()
    elif d == '2' :
        print('depo')
        #depositar()
    elif d == '3' :
        print('conpo')
        #comprovante()
    elif d == '4' :
        menu_principal() 
    traco() 

def pix(): # 1 opção do menu inserir
    limpar()
    traco()
    destinatario = input("Digite a chave pix do destinatário(a): ")
    if destinatario == pessoas[posi][1]:
        print('Você digitou o número da sua conta, se quiser depositar, vá à segunda guia do menu "inserir"')
        input('Quando você quiser: ')
        inserir()
    else :      
        valor_pix =  float(input("Digite o valor do pix")) 
        if valor_pix > 0 :             
            enviar = input("Deseja enviar? ")
            if pessoas[posi][2] >= valor_pix :
                if enviar.lower() == "sim":
                    transacao[posi][0]['Valor'].append(valor_pix)
                    transacao[posi][0]['Destinatário'].append(destinatario)
                    transacao[posi][0]['Data'].append(datetime.now())                        
                    pessoas[posi][2] -= valor_pix           
                    print(f"PIX NO DE {valor_pix} FOI ENVIADO PARA {destinatario} POR {pessoas[posi][1]} NA DATA {datetime.now()}")
                    print(f"AGORA, VOCÊ POSSUI {pessoas[posi][2]} REAIS")
                    input('NO SEU TEMPO, MEU NOBRE! ')
                    inserir()         
                elif enviar.lower() == "não":
                    inserir()
            else : 
                print(f"INFELIZMENTE, SEU SALDO NÃO É O SUFICIENTE. SALDO ATUAL: {pessoas[posi][2]} ") 
                input('Quando quiser: ')
                inserir()  
        else :
            print("Dgite um valor maior que 0 ") 
            input('No seu tempo: ')
            inserir()             
    traco()
'''
def depositar(): # 2 opção do menu inserir
    limpar()
    traco()
    deposito = float(input("Digite o valor do seu depósito"))
    valor_deposito.append(deposito) 
    deposita = input(f"Deseja depositar {valor_deposito[-1]} reais?")
    if deposita.lower() == "sim":
        deposito_data = datetime.now()                   
        data_deposito_lista.append(deposito_data)
        # pessoa[2] = saldo_lista[2] + valor_deposito[-1]
        print(f"PARABÉNS, VOCÊ DEPOSITOU {valor_deposito[-1]} REAIS EM {data_deposito_lista[-1]}")
        print(f"AGORA, VOCÊ TEM {pessoa[2]} REAIS")
        time.sleep(5)
        inserir()
    elif deposita.lower() == "não":
        valor_deposito.pop()
        print("TENTE FAZER OUTRO DEPÓSITO OU OUTRA COISA :)")
        time.sleep(5)
        inserir()
    traco()'''          
iniciar() 
'''   
tra = []
tra.append([{'valor':(1,2,3),'Destinário':(123,432,743),'Data':(13,14,15)},{}])
for oi, bom in tra[0][0].items():
    print(oi)
    print(bom)

tra = []
tra.append([{'valor':[1,2,3],'Destinário':[123,432,743],'Data':[13,14,15]},{}])
tra[0][0]['valor'].append(78989879)
for i in tra[0][0].values():
    print(i)
    
    
    '''
   