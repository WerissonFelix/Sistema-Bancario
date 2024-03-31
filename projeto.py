from datetime import datetime
from random import randrange
import random
import time
import os
import sys
cpf_lista = []
nome_lista = []
saldo_lista = []
numero_conta_lista = []
valor_pix_lista = []
destinatario_lista = []
valor_deposito = []
data_pix_lista = []
data_deposito_lista = []

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
            "2.SAIR DO BANCO"
            )
      a = escolha()
      traco()
      if a == 1 :
            resetar(valor_pix_lista,destinatario_lista,valor_deposito,data_deposito_lista,data_pix_lista)  
      elif a == 2 :
            sair()
def random_conta():
      numero_conta =  random.randrange(0,1000,3)
      numero_conta_lista.append(numero_conta)
def verificacao(x,y):
      if x in y:
            print("Alguém já tem este cpf, tente com outro")
            time.sleep(5)
            menu_cadastro()
      else :
            y.append(x)      
def menu_cadastro():
      limpar()
      traco()    
      cpf = int(input("Digite seu cpf"))
      nome = input("Digite seu nome")
      saldo = float(input("Quanto deseja depositar??"))
      verificacao(cpf,cpf_lista)
      deposito_data = datetime.now()
      data_deposito_lista.append(deposito_data)
      nome_lista.append(nome)
      saldo_lista.append(saldo)
      valor_deposito.append(saldo)  
      random_conta()
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
      print(
            f"BEM-VINDO AO BANCO FÉLIX,{nome_lista[-1]}\n"
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
            f"CPF:{cpf_lista[-1]}\n"
            f"NOME:{nome_lista[-1]}\n"
            f"NÚMERO DA CONTA:{numero_conta_lista[-1]}\n"
            f"SALDO BANCÁRIO: {saldo_lista[-1]}"
            )
            time.sleep(10)
            traco()
            menu_principal()
      elif c == 4 : 
            limpar()
            traco()
            exclui = input("EXCLUIR CONTA?")
            if exclui.lower() == "sim" :
                  excluir(cpf_lista,data_pix_lista,numero_conta_lista,saldo_lista,valor_pix_lista)
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
      if destinatario == numero_conta_lista[-1]:
            print('Você digitou o número da sua conta, se quiser depositar, vá à segunda guia do menu "inserir"')
            time.sleep(7)
            inserir()
      else :      
            valor_pix =  float(input("Digite o valor do pix")) 
            if valor_pix > 0 : 
                  valor_pix_lista.append(valor_pix)
                  enviar = input("Deseja enviar?")
                  if saldo_lista[-1] >= valor_pix_lista[-1] :
                        if enviar.lower() == "sim":
                              data_pix  = datetime.now()
                              destinatario_lista.append(destinatario)                
                              data_pix_lista.append(data_pix)                
                              saldo_lista[-1] = saldo_lista[-1] - valor_pix_lista[-1]
                              print(f"PIX NO VALO DE {valor_pix_lista[-1]} FOI ENVIADO PARA {destinatario_lista[-1]} POR {numero_conta_lista[-1]} NA DATA {data_pix_lista[-1]}")
                              print(f"AGORA, VOCÊ POSSUI {saldo_lista[-1]} REAIS")
                              print('O comprovante desaparecerá em 7 segundos. Se quiser vê-lo, vá à guia "3" do menu inserir')
                              time.sleep(10)
                              inserir()         
                        elif enviar.lower() == "não":
                              inserir()
                  else : 
                        valor_pix_lista.pop()
                        print("PARECE QUE SEU SALDO É INSUFICIENTE, TENTE COM UM VALOR MENOR OU IGUAL AO SEU SALDO BANCÁRIO QUE É : ",saldo_lista[-1]) 
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
            saldo_lista[-1] = saldo_lista[-1] + valor_deposito[-1]
            print(f"PARABÉNS, VOCÊ DEPOSITOU {valor_deposito[-1]} REAIS EM {data_deposito_lista[-1]}")
            print(f"AGORA, VOCÊ TEM {saldo_lista[-1]} REAIS")
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
                  print(f"PIX NO VALO DE {valor} FOI ENVIADO PARA {destino} POR {numero_conta_lista[-1]} EM {hora}") 
            time.sleep(10)                       
            inserir()
      elif escolha_comprovante == 3 :
            inserir()      
      traco()  
def alterar() : #menu alterar
      limpar()
      traco()
      print("O que você deseja alterar? :\n"
      f"1. Cpf: {cpf_lista[-1]}\n"
      f"2. Nome: {nome_lista[-1]}\n"
      f"3. Número da conta: {numero_conta_lista[-1]}\n"
      "4. voltar para o menu principal"
      )
      e = escolha() 
      if e == 1 :
            new_cpf()                      
      elif e == 2 : 
            new_nome()
      elif e == 3 :
            new_Nconta()
      elif e == 4 :
            menu_principal()         
def new_cpf() : #inicio das funções do menu alterar.
      limpar()
      cpf_lista[-1] = novo_cpf = int(input("digite seu novo cpf")) 
      print("PARABÉNS, VOCÊ ATUALIZOU SEU CPF") 
      time.sleep(3)
      alterar()  
def new_nome() :
      limpar()
      nome_lista[-1] = novo_nome = input("digite seu novo nome")
      print("PARABÉNS, VOCÊ ATUALIZOU SEU NOME")
      time.sleep(3)
      alterar()
def new_Nconta():
      limpar()
      numero_conta_lista[-1] = novo_numero = int(input("digite  seu novo número da conta"))
      print("PARABÉNS, VOCÊ ATUALIZOU SEU NÚMERO DA CONTA")
      time.sleep(3)
      alterar()
def resetar(a,b,c,d,e):#função resetar para não bugar o comprovante de outro usuário
      if len(a) > 0 :
            a.clear()
            b.clear()
            c.clear()
            d.clear()
            e.clear()
            menu_cadastro()
      else :
            menu_cadastro()
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
      print(f"Saindo da sua conta,{nome_lista[-1]}")
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