from datetime import datetime
import  time
import os
import sys
cpf_lista = []
nome_lista = []
saldo_lista = []
numero_conta_lista = []
valor_pix_lista = []
destinatario_lista = []
lista_comprovantes = []
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
      for i in range(0,12):
            print()


def menu_cadastro():
      limpar()
      traco()
      cpf = int(input("digite seu cpf"))
      nome = input("digite seu nome")
      numero_conta = int(input("digite o número da conta"))
      saldo = float(input("quanto deseja depositar??"))
      deposito_data = datetime.now()
      traco()
      data_deposito_lista.append(deposito_data)
      cpf_lista.append(cpf)
      nome_lista.append(nome)
      saldo_lista.append(saldo)
      valor_deposito.append(saldo)
      numero_conta_lista.append(numero_conta)
      limpar()
      traco()
      print(
            "\nAgora, para onde deseja ir?\n"
            "1.MENU PRINCIPAL\n"
            "2.SAIR DO BANCO"
            )
      b = escolha() 
      limpar()
      if b == 1 :# menu principal
            menu_principal()  
      elif b == 2:
            sair()       
      traco()

def menu_principal():
      limpar()
      traco()
      print(
            "BEM-VINDO AO BANCO\n"
            "MENU PRINCIPAL\n"
            "1. INSERIR\n"
            "2. ALTERAR\n"
            "3. CONSULTAR\n"
            "4. EXCLUIR CONTA\n"
            "5. SAIR DO BANCO"
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
            f"CPF:{cpf_lista[0]}\n"
            f"NOME:{nome_lista[0]}\n"
            f"NÚMERO DA CONTA:{numero_conta_lista[0]}\n"
            f"SALDO BANCÁRIO: {saldo_lista[0]}"
            )
            time.sleep(10)
            traco()
            menu_principal()
      elif c == 4 : # menu excluir conta
            limpar()
            traco()
            excluir = input("EXCLUIR CONTA?")
            if excluir.lower() == "sim" :
                  cpf_lista[0] = 0
                  numero_conta_lista[0] = 0
                  saldo_lista[0] = 0.0
                  nome_lista[0] = ''
                  print("EXCLUINDO CONTA")
                  time.sleep(3)
                  sair()
            elif excluir.lower() == "não" :
                  menu_principal()  
      elif c == 5 :
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
      valor_pix =  float(input("Digite o valor do pix"))   
      valor_pix_lista.append(valor_pix)
      enviar = input("Deseja enviar?")
      if saldo_lista[-1] >= valor_pix_lista[-1] :
            if enviar.lower() == "sim":
                  data_pix  = datetime.now()
                  destinatario_lista.append(destinatario)                
                  data_pix_lista.append(data_pix)                
                  saldo_lista[-1] = saldo_lista[-1] - valor_pix_lista[-1]
                  print(f"PIX NO VALO DE {valor_pix_lista[-1]} FOI ENVIADO PARA {destinatario_lista[-1]} POR {numero_conta_lista[-1]} NA DATA {data_pix_lista[-1]} :")
                  print(f"AGORA, VOCÊ POSSUI {saldo_lista[-1]} REAIS")
                  print('O comprovante desaparecerá em 7 segundos. Se quiser vê-lo,  vá à guia "3" do menu inserir')
                  time.sleep(10)
                  inserir()         
            elif enviar.lower() == "não":
                  inserir()
      else : 
            valor_pix_lista.pop()
            print("PARECE QUE SEU SALDO É INSUFICIENTE, TENTE COM UM VALOR MENOR OU IGUAL AO SEU SALDO BANCÁRIO QUE É : ",saldo_lista[0]) 
            time.sleep(7)
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
            "2.COMPROVANTES PIX "
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
      traco()  
def alterar() :
      limpar()
      traco()
      print("O que você deseja alterar? :\n"
      f"1. Cpf: {cpf_lista[0]}\n"
      f"2. Nome: {nome_lista[0]}\n"
      f"3. Número da conta: {numero_conta_lista[0]}\n"
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

def new_cpf() :
      limpar()
      cpf_lista[0] = novo_cpf = int(input("digite seu novo cpf")) 
      print("PARABÉNS, VOCÊ ATUALIZOU SEU CPF") 
      time.sleep(3)
      alterar()  
def new_nome() :
      limpar()
      nome_lista[0] = novo_nome = input("digite seu novo nome")
      print("PARABÉNS, VOCÊ ATUALIZOU SEU NOME")
      time.sleep(3)
      alterar()
def new_Nconta():
      limpar()
      numero_conta_lista[0] = novo_numero = int(input("digite  seu novo número da conta"))
      print("PARABÉNS, VOCÊ ATUALIZOU SEU NÚMERO DA CONTA")
      time.sleep(3)
      alterar()
def sair():
      limpar()
      print("Saindo do banco felix")
      time.sleep(3)
      limpar()
      exit()

print("bem-vindo ao banco Félix, comece escolhendo uma opção\n"
      "1.CADASTRAR\n"
      "2.SAIR DO BANCO"
      )

a = escolha()

if a == 1 :
      menu_cadastro()  
elif a == 2 :
      sair()
      