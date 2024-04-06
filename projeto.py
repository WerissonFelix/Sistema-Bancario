from datetime import datetime
from random import randrange
import random
import time
import os
import sys
cpf = 0
nome = ''
saldo = 0.0
numero_conta = 0
pessoas = []
valor_pix_lista = []
destinatario_lista = []
valor_deposito = []
data_pix_lista = []
data_deposito_lista = []
comprovante_depo = []
comprovante_pix = []

def traco(x = 50):
      for i in range(0,x):
            print("=", end="")
      print("\n")

def escolha():
      guia = int(input("digite o número da guia que deseja ir"))
      return guia

def limpar():
      os.system('cls') or None

def iniciar():
      limpar()
      traco() 
      print("Bem-vindo ao banco Félix, comece escolhendo uma opção\n"
            "1.CADASTRAR\n"
            "2.ENTRAR\n"
            "3.SAIR DO BANCO"
            )
      a = escolha()
      traco()
      if a == 1 :
            menu_cadastro()
      elif a == 2 :
            cpf = int(input("digite o cpf da conta que desejar entrar"))
            nome = input("digite o nome da conta que deseja entrar")
            saldo = float(input("digite o saldo da conta que deseja entrar"))
            numero_conta = int(input("digite o número da conta da pessoa que deseja entra"))
            try :
                  cpf,nome,saldo,numero_conta = pessoa
            except(NameError):
                  print("parece que ainda não há nenhuma conta cadastrada")
                  time.sleep(5)
                  iniciar()      
            if pessoa in pessoas:
                  print(f"entrando em {cpf}")
                  time.sleep(3)
                  menu_principal()   
            else:
                  print("cpf não encontrado, tente com outro ;)")
                  time.sleep(5)
                  iniciar()                   
      elif a == 3 :
            sair()
     
def menu_cadastro():
      limpar()
      traco()  
      nome = input("Digite seu nome")
      cpf = int(input("Digite seu cpf"))
      saldo = float(input("Quanto deseja depositar??"))
      numero_conta =  random.randrange(0,1000,3)
      if cpf in pessoas:
            print("Alguém já tem este cpf, tente com outro")
            time.sleep(5)
            menu_cadastro()
      else :
            pessoas.append([nome,cpf,saldo,numero_conta])
            deposito_data = datetime.now()
            data_deposito_lista.append(deposito_data)
            valor_deposito.append(saldo)
            
                
      global p 
      if nome in pessoas :
            p = pessoas.index(nome)
      else : 
            p = -1
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
      if b == 1 :# menu principal
            menu_principal()  
      elif b == 2:
            sairConta()     
      elif b == 3 :
            sair()    
      traco()
def menu_principal():
      limpar()
      traco()
      global pessoa
      for i in range(len(pessoas)): 
            if cpf in pessoas : 
                  pessoa = pessoas[i]
                  break
            else:
                  pessoa = pessoas[i]      
      print(
            f"BEM-VINDO AO BANCO FÉLIX,{pessoa[0]}\n"
            "MENU PRINCIPAL\n"
            "1. INSERIR\n"
            "2. ALTERAR\n"
            "3. CONSULTAR\n"
            "4. EXCLUIR CONTA\n"
            "5. SAIR DA CONTA\n"
            "6. SAIR DO BANCO"
            )
      c = escolha()
      if c == 1 : # menu do inserir
            inserir()
      elif c == 2 :# menu  alterar, deixar os comprovantes pix e deposito aqui, porém ainda deixa-los lá.
            alterar()
      elif c == 3 : # menu consultar
            limpar()
            traco()
            print("INFORMAÇÕES DA CONTA :\n"
            f"NOME:{pessoa[0]}\n"
            f"CPF:{pessoa[1]}\n"            
            f"SALDO BANCÁRIO: {pessoa[2]}\n"
            f"NÚMERO DA CONTA:{pessoa[3]}\n"            
            )
            time.sleep(10)
            traco()
            menu_principal()
      elif c == 4 : 
            limpar()
            traco()
            exclui = input("EXCLUIR CONTA?")
            if exclui.lower() == "sim" :
                  exit()
            elif exclui.lower() == "não" :
                  menu_principal()  
      elif c == 5 :
            sairConta()  
      elif c == 6 :
            sair()              
      traco() 
def inserir():
      limpar()
      traco()
      print(
            "TRANSFERÊNCIAS\n"
            "1.FAZER PIX\n"
            "2.DEPOSITAR\n"
            "3.VER EXRATO\n"
            "4.VOLTAR PARA O MENU PRINCIPAL"
            )
      d = escolha()
      if d == 1 : # opção de enviar pix
            pix()
      elif d == 2 :
            depositar()
      elif d == 3 :
            comprovante()
      elif d == 4 :
            menu_principal()  
      traco()      
def pix(): # 1 opção do menu inserir
      limpar()
      traco()
      destinatario = int(input("Digite o número da conta do destinatário do pix"))
      if destinatario == pessoa[0]:
            print('Você digitou o número da sua conta, se quiser depositar, vá à segunda guia do menu "inserir"')
            time.sleep(7)
            inserir()
      else :      
            valor_pix =  float(input("Digite o valor do pix")) 
            if valor_pix > 0 : 
                  valor_pix_lista.append(valor_pix)
                  enviar = input("Deseja enviar?")
                  if pessoa[2] >= valor_pix_lista[-1] :
                        if enviar.lower() == "sim":
                              data_pix  = datetime.now()
                              destinatario_lista.append(destinatario)                
                              data_pix_lista.append(data_pix)                
                              pessoa[2] = pessoa[2] - valor_pix_lista[-1]
                              print(f"PIX NO VALO DE {valor_pix_lista[-1]} FOI ENVIADO PARA {destinatario_lista[-1]} POR {pessoa[3]} NA DATA {data_pix_lista[-1]}")
                              print(f"AGORA, VOCÊ POSSUI {pessoa[2]} REAIS")
                              print('O comprovante desaparecerá em 7 segundos. Se quiser vê-lo, vá à guia "3" do menu inserir')
                              time.sleep(10)
                              inserir()         
                        elif enviar.lower() == "não":
                              inserir()
                  else : 
                        valor_pix_lista.pop()
                        print("PARECE QUE SEU SALDO É INSUFICIENTE, TENTE COM UM VALOR MENOR OU IGUAL AO SEU SALDO BANCÁRIO QUE É : ",pessoa[2]) 
                        time.sleep(7)
                        inserir()  
            else :
                  print("Dgite um valor maior que 0") 
                  time.sleep(5)
                  inserir()             
      traco()      
def depositar(): # 2 opção do menu inserir
      limpar()
      traco()
      deposito = float(input("Digite o valor do seu depósito"))
      valor_deposito.append(deposito) 
      deposita = input(f"Deseja depositar {valor_deposito[-1]} reais?")
      if deposita.lower() == "sim":
            deposito_data = datetime.now()                   
            data_deposito_lista.append(deposito_data)
            pessoa[2] = saldo_lista[2] + valor_deposito[-1]
            print(f"PARABÉNS, VOCÊ DEPOSITOU {valor_deposito[-1]} REAIS EM {data_deposito_lista[-1]}")
            print(f"AGORA, VOCÊ TEM {pessoa[2]} REAIS")
            time.sleep(5)
            inserir()
      elif deposita.lower() == "não":
            valor_deposito.pop()
            print("TENTE FAZER OUTRO DEPÓSITO OU OUTRA COISA :)")
            time.sleep(5)
            inserir()
      traco()     
def comprovante():# 3 opção do menu inserir
      limpar()
      traco()
      print("BEM-VINDO AOS COMPROVANTES\n"
            "1.COMPROVANTES DEPOSITOS\n"
            "2.COMPROVANTES PIX\n"
            "3.Voltar para o menu inserir"
            )
      escolha_comprovante = escolha()
      if  escolha_comprovante == 1 :
            limpar()
            print("============DEPÓSITOS===========")       
            for valo , horario  in zip(valor_deposito,data_deposito_lista) :
                  print(f"PARABÉNS, VOCÊ DEPOSITOU {valo} REAIS EM {horario}")    
            time.sleep(5)      
            inserir()
      elif  escolha_comprovante == 2 :
            limpar()
            print("==========PIX=========")
            for valor , destino , hora in zip(valor_pix_lista,destinatario_lista,data_pix_lista) :
                  print(f"PIX NO VALO DE {valor} FOI ENVIADO PARA {destino} POR {pessoa[3]} EM {hora}") 
            time.sleep(10)                       
            inserir()
      elif escolha_comprovante == 3 :
            inserir()      
      traco()  
def alterar() : #menu alterar
      limpar()
      traco()
      print("O que você deseja alterar? :\n"
      f"1. Nome: {pessoa[0]}\n"
      f"2. Cpf: {pessoa[1]}\n"  
      f"3. Número da conta: {pessoa[3]}\n"
      "4. voltar para o menu principal"
      )
      e = escolha() 
      if e == 1 :
            new_nome()                   
      elif e == 2 :         
            new_cpf() 
      elif e == 3 :
            new_Nconta()
      elif e == 4 :
            menu_principal() 

def new_nome() :#inicio das funções do menu alterar.
      limpar()
      pessoa[0] = novo_nome = input("digite seu novo nome")
      print("PARABÉNS, VOCÊ ATUALIZOU SEU NOME")
      time.sleep(3)
      alterar()
def new_cpf() :
      limpar()
      pessoa[1] = novo_cpf = int(input("digite seu novo cpf")) 
      print("PARABÉNS, VOCÊ ATUALIZOU SEU CPF") 
      time.sleep(3)
      alterar()  

def new_Nconta():
      limpar()
      pessoa[3] = novo_numero = int(input("digite  seu novo número da conta"))
      print("PARABÉNS, VOCÊ ATUALIZOU SEU NÚMERO DA CONTA")
      time.sleep(3)
      alterar()

def excluir(a,b,c,d,e):
      if len(a) > 0 :
            a.pop()
            b.pop()
            c.pop()
            d.pop()
            e.clear()
            print("EXCLUINDO CONTA")
            time.sleep(3)
            iniciar()
      else :    
            menu_principal()      
def sairConta():#funções sair conta e sair do banco
      limpar()
      print(f"Saindo da sua conta,{pessoa[0]}")
      time.sleep(3)
      limpar()
      iniciar()
def sair():
      limpar()
      print("Saindo do banco felix")
      time.sleep(3)
      limpar()
      exit()
iniciar()      
 