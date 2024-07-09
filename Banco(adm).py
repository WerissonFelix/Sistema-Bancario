from datetime import datetime
from time import sleep
import os
import sys
pessoas = []
transacao = []
def traco(x = 50):
    for i in range(0,x):
        print("=", end="")
    print("\n")

def escolha(limite='123', txt='Sua escolha : (APENAS NÚMEROS) ', num = False):
    if (num):
        nome = ' '     
        while True :
            nome = str(input(f"{txt}"))
            if len(nome) > 0:
                if nome[0] in limite:
                    try:
                        nome = float(nome)
                        break
                    except ValueError:
                        print('Erro, digite apenas números! ')
                        sleep(3)
                        continue
                else:
                    print('Apenas números! ')
            else:
                continue
        return nome
    else:
        guia = ' '
        while True:
            guia = str(input(txt)).upper().strip() 
            if len(guia) > 0:
                if guia[0] in limite:
                    break
            else:
                continue        
        return guia

def limpar():
    os.system('cls')

def iniciar():
    limpar()
    traco() 
    print('''
    Bem-vindo ao banco Félix, comece escolhendo uma opção      
    1.CADASTRAR
    2.SAIR DO BANCO
    '''
    )
    a = escolha('12')
    if a == '1' :
        menu_cadastro()
    elif a == '2' :    
        print('tchau')
        exit()
        
def menu_cadastro():
    limpar()
    traco() 
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu cpf: ")
    for i in pessoas:
        if cpf == i[1]:
            print("Alguém já tem este cpf, tente com outro")
            sleep(5)
            iniciar()

    saldo = escolha('SN','Quer depositar? (S/N) ')  
    if saldo[0] == 'S':
        saldo = escolha('123456789','Seu depósito: ',True)
    else:
        saldo = '0'
        saldo = float(saldo)   
    pessoas.append([nome, cpf, saldo])
        
    global posi

    for posicao, valor  in enumerate(pessoas):
        if valor[1] == cpf:
            posi = posicao   
    transacao.append([{'Valor':[],'Destinatário':[],'Data':[]},{'Valor_depo':[],'Data_depo':[]}]) 
    if saldo > 0:
        transacao[posi][1]['Valor_depo'].append(saldo)
        transacao[posi][1]['Data_depo'].append(datetime.now())                           
    limpar()
    traco()
    print(
        "\nAgora, para onde deseja ir?\n"
        "1.MENU PRINCIPAL\n"
        "2.SAIR DA CONTA\n"
        "3.SAIR DO BANCO"
        )
    b = escolha('123','Sua escolha: ') 
    if b == '1' :# menu principal
        menu_principal()  
    elif b == '2':
        limpar()
        traco()
        print('Saindo da conta')
        sleep(2)
        print('Pronto')
        sleep(1)
        iniciar()       
    elif b == '3' :
        print('Tchau!')
        exit()
  
def menu_principal():
    limpar()
    traco() 
    print(f"BEM-VINDO AO BANCO FÉLIX, {pessoas[posi][0]}\n"
    '''MENU PRINCIPAL
    1. INSERIR
    2. ALTERAR
    3. CONSULTAR
    4. EXCLUIR CONTA
    5. SAIR DA CONTA
    6. SAIR DO BANCO'''
    )
    c = escolha('123456')
    if c == '1' : # menu do inserir
        inserir()
    elif c == '2' :# menu  alterar inser
        limpar()
        print('='*40)
        print(f"{'ATUALIZAR INFORMAÇÕES':^40}")
        print('='*40)
        print('''
        1. NOME
        2. CPF
        3. VOLTAR       
        ''')
        trocar = ' '
        while trocar not in '123':
            trocar = input('Sua escolha: (1/2/3) ')
        if trocar == '1':
            pessoas[posi][0] = input('Novo Nome: ')
            input('Quando quiser ')
            menu_principal()
        elif trocar == '2': 
            pessoas[posi][1] = input('Novo cpf: ')        
            input('Quando quiser ')
            menu_principal()
        else:
            menu_principal()   
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
        exclui = input("EXCLUIR CONTA? (sim/não) ")
        if exclui.lower() == "sim" :
            print('Desativando conta')
            sleep(3)
            print('Tchau!')
            iniciar()
        elif exclui.lower() == "não" :
            menu_principal()  
    elif c == '5' :
        limpar()
        traco()
        print('Saindo da conta')
        sleep(2)
        print('Pronto')
        sleep(1)
        iniciar()      
    elif c == '6' :
        limpar()
        traco()
        print('Saindo do banco')             
        sleep(2)
        exit()
  
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
    d = escolha('1234')
    if d == '1' : # opção de enviar pix
        pix()
    elif d == '2' :
        depositar()
    elif d == '3' :
        extrato()
    elif d == '4' :
        menu_principal() 

def pix(): # 1° opção do menu inserir
    limpar()
    traco()
    # ei, coloca a verificação ae pae
    destinatario = input("Digite a chave pix do destinatário(a): ")
    if destinatario == pessoas[posi][1]:
        print('Você digitou o número da sua conta, se quiser depositar, vá à segunda guia do menu "inserir"')
        input('Quando você quiser: ')
        inserir()
    else :    
        valor_pix = escolha('123456789.','Digite o valor do pix: ', True)  
        if valor_pix > 0 :      
            enviar = escolha('SN','Deseja enviar? (S/N) ')       
            if pessoas[posi][2] >= valor_pix :
                if enviar[0] == "S":
                    transacao[posi][0]['Valor'].append(valor_pix)
                    transacao[posi][0]['Destinatário'].append(destinatario)
                    transacao[posi][0]['Data'].append(datetime.now())                        
                    pessoas[posi][2] -= valor_pix           
                    print(f"PIX NO DE {valor_pix} FOI ENVIADO PARA {destinatario} POR {pessoas[posi][1]} NA DATA {datetime.now().hour}")
                    print(f"AGORA, VOCÊ POSSUI {pessoas[posi][2]} REAIS")
                    input('NO SEU TEMPO, MEU NOBRE! ')
                    inserir()         
                elif enviar[0] == "N":
                    print('PIX CANCELADO!')
                    sleep(3)
                    inserir()
            else : 
                print(f"INFELIZMENTE, SEU SALDO NÃO É O SUFICIENTE. SALDO ATUAL: {pessoas[posi][2]} ") 
                input('Quando quiser: ')
                inserir()  
        else :
            print("Digite um valor maior que 0 ") 
            input('No seu tempo: ')
            inserir()             

def depositar(): # 2° opção do menu inserir
    limpar()
    traco()
    deposito = escolha('123456789.','Digite o valor do seu depósito', True)
    depositar = escolha('SN',f'Deseja depositar {deposito} reais? ')
    if depositar[0] == "S":
        horario = datetime.now()
        transacao[posi][1]['Valor_depo'].append(deposito)
        transacao[posi][1]['Data_depo'].append(horario)
        pessoas[posi][2] += deposito
        print(f"PARABÉNS, VOCÊ DEPOSITOU {deposito} REAIS EM {horario.hour} HORAS E {horario.minute} MINUTOS")
        print(f"AGORA, VOCÊ TEM {pessoas[posi][2]} REAIS")
        input("Quando quiser, meu comandante :D ")
        inserir()
    elif depositar[0] == "N":     
        print("TENTE FAZER OUTRO DEPÓSITO OU OUTRA COISA :)")
        input("No seu tempo, meu nobre :) ")
        inserir() 

def extrato():# 3 opção do menu inserir
    limpar()
    traco()
    print("BEM-VINDO AOS COMPROVANTES\n"
        "1.COMPROVANTES PIX\n"
        "2.COMPROVANTES DEPÓSITOS\n"
        "3.Voltar para o menu inserir"
        )
    escolha_comprovante = escolha('123')
    if  escolha_comprovante == '1' :
        limpar()
        print('='*40)
        print(f"{'PIX':^40}")
        print('='*40)     
        print(f"{'Valores':<14}",end=':')
        for valores_pix in transacao[posi][0]['Valor']:
            print(f"{valores_pix:^13}",end='|')    
        print(f"\n{'Destinatários'} ",end=':')        
        for destinatarios_pix in transacao[posi][0]['Destinatário']:
            print(f"{destinatarios_pix:^13}", end='|')   
        print(f"\n{'Datas (HORAS)':<14}",end=':') 
        for datas_pix in transacao[posi][0]['Data']:
            print(f"{datas_pix.hour:^13}",end='|') 
        input('\nPode ir, chefe ')      
        inserir()
    elif  escolha_comprovante == '2' :
        limpar()
        print('='*40)
        print(f"{'DEPÓSITOS':^40}")
        print('='*40)
        print(f"{'Valores':<14}",end=':')
        for valores in transacao[posi][1]['Valor_depo']:
            print(f"{valores:^13}",end='|')
        print(f"\n{'Datas':<14}",end=':')  
        for datas in transacao[posi][1]['Data_depo']:
            print(f"{datas.hour:^13}",end='|')  
        input(' \n Ao seu comando, meu guerreiro ')                      
        inserir()
    elif escolha_comprovante == '3' :
        inserir()      
iniciar() 