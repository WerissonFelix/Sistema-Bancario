from datetime import datetime
from time import sleep
import platform
import os

pessoas = []
desativadas = []
transacao = []
def traco(x = 50):
    for i in range(0,x):
        print("=", end="")
    print("\n")

def escolha(limite='123', txt='Sua escolha : (APENAS NÚMEROS) ', num = False, tamanho = 0):
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
                if tamanho > 0:
                    if guia[0] in limite and len(guia) == tamanho:
                        break
                else:    
                    if guia[0] in limite:
                        break
            else:
                continue        
        return guia

def limpar():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        print("\n" * os.get_terminal_size().lines) 

def animacao(animar = False, vari = 0, lista = [1,2,3]):
    if (animar):
        for i in range(0,3):
            print('.',end='',flush=True)
    else:
        for vari in lista:
            print(f"{vari:^13}",end='|')

def iniciar():
    limpar()
    traco() 
    print('''
    Bem-vindo ao banco Félix, comece escolhendo uma opção      
    1.ENTRAR
    2.CADASTRAR
    3.SAIR DO BANCO
    '''
    )
    a = escolha('123',tamanho=1)
    if a == '1' :
        entrar()
    elif a == '2':
        menu_cadastro()
    elif a == '3' :    
        print('tchau')
        exit()
def entrar():
    if len(pessoas) == 0:
        print("\033[31mAinda não há nenhuma conta para entrar\033[m")
        sleep(2)
        iniciar()
    else:    
        num_conta = int(escolha('1234567890','Número da conta: '))
        cpf = escolha('1234567890','Cfp da conta: ',tamanho=11)
        for procu in desativadas:
            if cpf in procu and num_conta in procu:
                print('A conta que você está tentando entrar foi desativada!')
                sleep(2)
                iniciar()
        for i in pessoas:
            if num_conta in i and cpf in i:
                print('Entrando')
                sleep(3) 
                global posi     
                for posicao, valor  in enumerate(pessoas):
                    if valor[1] == cpf:
                        posi = posicao     
                menu_principal()
        else:
            print('Nº da conta/Cpf não existem. Tente novamente')
            sleep(2)
            iniciar()          

def menu_cadastro():
    limpar()
    traco() 
    nome = input("Digite seu nome: ")
    cpf = escolha('1234567890','Seu cpf (11 dígitos) : ', tamanho= 11)
    while len(cpf) != 11:
        cpf = escolha('1234567890','Cpf (11 ) ', tamanho =11)      
    for i in pessoas:
        if cpf == i[1]:
            print("Alguém já tem este cpf, tente com outro")
            sleep(5)
            menu_cadastro()
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
    pessoas[posi].insert(3,posi)        
    transacao.append([{'Valor':[],'Destinatário':[],'Data':[]},{'Valor_depo':[],'Data_depo':[]},
    {'Pagador':[],'Pagamento':[]}]) 
    pessoas[posi].insert(4,transacao)
    if saldo > 0:
        transacao[posi][1]['Valor_depo'].append(saldo)
        transacao[posi][1]['Data_depo'].append(datetime.now())                                 
    menu_principal()
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
    c = escolha('123456',tamanho=1)
    if c == '1' : # menu do inserir
        inserir()
    elif c == '2' :# menu  alterar inser
        limpar()
        print('='*40)
        print(f"{'ATUALIZAR INFORMAÇÕES':^40}")
        print('='*40)
        print('''
        1. NOME
        2. VOLTAR       
        ''')
        trocar = escolha('12',tamanho=1)
        if trocar == '1':
            print(f"Nome atual: {pessoas[posi][0]}")
            pessoas[posi][0] = input('Novo Nome: ')
            input('Quando quiser ')
            menu_principal()
        elif trocar == '2': 
            menu_principal()
    elif c == '3' : # menu consultar
        limpar()
        traco()
        print("INFORMAÇÕES DA CONTA :\n"
        f"NOME: {pessoas[posi][0]}\n"
        f"CPF: {pessoas[posi][1]}\n"            
        f"SALDO BANCÁRIO: {pessoas[posi][2]}\n"
        f"Número DA CONTA: {pessoas[posi][3]}"           
        )
        input('Quando quiser ')
        traco()
        menu_principal()
    elif c == '4' : 
        limpar()
        traco()
        excluir = escolha('SN','Quer excluir a sua conta? ')
        if excluir[0] == "S" :
            print('Desativando conta')
            for i in range(0,3):
                sleep(1.5)
                print('.',end='',flush=True)
            desativadas.append(pessoas[posi])    
            iniciar()
        elif excluir[0] == "N" :
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
    d = escolha('1234',tamanho=1)
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
    posi_desti = 0
    veridico = False
    if len(pessoas) == 1:
        print('Atenção! Você ainda não pode fazer pix, pois só você está cadastro no momento')
        sleep(3)
        inserir()
    else:    
        destinatario = escolha('1234567890','Digite a chave pix do destinatário (cpf) ',tamanho=11) 
        for procurar in desativadas:
            for procurado in procurar:
                if procurado == destinatario:
                    print("\033[31mO destinatário digitado está com a conta suspensa \033[m ")  
                    input('Quando quiser ')
                    inserir() 
        for i in pessoas:
            for valor in i:
                if destinatario == valor:
                    print(f"Destinatário encontrado: {i[0]} ")   
                    posi_desti = pessoas.index(i)
                    veridico = True 
        if veridico == False:
            print(f"O cpf {destinatario} não foi encontrado/não existe. ")
            input('Quando quiser ')
            inserir()
        else:    
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

                            transacao[posi_desti][2]['Pagador'].append(pessoas[posi][1])
                            transacao[posi_desti][2]['Pagamento'].append(valor_pix)                        
                            pessoas[posi][2] -= valor_pix
                            pessoas[posi_desti][2] += valor_pix           
                            print(f"PIX NO VALOR DE {valor_pix} FOI ENVIADO PARA {destinatario} POR {pessoas[posi][1]} NO HORÁRIO: {datetime.now().hour} h  ")
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
    deposito = escolha('123456789.','Digite o valor do seu depósito ', True)
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
    print('''BEM-VINDO AOS COMPROVANTES
        1.COMPROVANTES PIX
        2.COMPROVANTES DEPÓSITOS
        3.PAGAMENTOS RECEBIDOS 
        4.Voltar para o menu inserir'''
        )
    escolha_comprovante = escolha('1234',tamanho=1)
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
        input('\nAo seu comando, meu guerreiro ')                      
        inserir()
    elif escolha_comprovante == '3':
        limpar()
        print('='*40)
        print(f"{'PAGAMENTOS RECEBIDOS ':^40}")  
        print('='*40)
        print(f"{'Pagadores':<14}",end=':')
        for valores in transacao[posi][2]['Pagador']:
            print(f"{valores:^13}",end='|')
        print(f"\n{'Valor (R$)':<14}",end=':')  
        for pagos in transacao[posi][2]['Pagamento']:
            print(f"{pagos:^13}",end='|')  
        input('\nAo seu comando, meu guerreiro ')                      
        inserir()
    elif escolha_comprovante == '4' :
        inserir()      
iniciar() 
