import sys 
from datetime import date
import os
cpf = 0
nome = ''
saldo = 0
numero_conta = 0

print("bem-vindo ao banco, começe escolhendo uma opção\n"
      "1.CADASTRAR\n"
      "2.SAIR DO BANCO\n"
 )


def escolha():
      guia = int(input("digite a guia que deseja ir"))
      return guia
def menu_principal():
      print(
        "BEM-VINDO AO BANCO\n"
        "MENU PRINCIPAL\n"
        "1. INSERIR\n"
        "2. ALTERAR\n"
        "3. CONSULTAR\n"
        "4. EXCLUIR CONTA\n"
      )
def inserir():
      print("TRANSFERÊNCIAS\n "
            "1.FAZER PIX\n"
            "2.DEPOSITAR\n"
            "3.VER EXRATO"
      )
def limpar():
  os.system("cls") or None


a = escolha()
if a == 1 :

    cpf = int(input("digite seu cpf"))
    nome = input("digite seu nome")
    numero_conta = int(input("digite o número da conta"))
    saldo = int(input("qual é o seu saldo?"))
    print('\nAgora,  para onde deseja ir?\n'
          "1.MENU PRINCIPAL\n"
         "2.SAIR DO BANCO"
      )
    
    b = escolha()

    if b == 1 :
      limpar()  
      print(menu_principal())
      c = escolha()

      if c == 1 :

          print(inserir())
          d = escolha()

          if d == 1 :
             destinatario = int(input("digite o número da conta do destinatário do pix"))
             valor_pix =  int(input("digite o valor do pix"))
             enviar = input("deseja enviar?")
             if enviar == "sim":
                print("PIX NO VALO DE ", valor_pix ," FOI ENVIADO PARA ",destinatario," POR ",numero_conta,
                " NO DIA ", date.today()," AS ",date.hour()," DO MÊS ",date.month()," NO ANO ", date.year())
            
             elif d == 2 :
               valor_deposito = int(input("digite o valor do seu depósito"))
               saldo = saldo + valor_deposito
               depositar = input("deseja depositar ",valor_deposito," reais?")
             if depositar.lower() == "sim":
                        print("PARABÉNS, VOCÊ DEPOSITOU ",valor_deposito," REAIS ",
                        date.today(),"/",date.month(),"/",date.year())
                        print("AGORA, VOCÊ TEM ",saldo," REAIS")


      elif c == 2 :

        print(cpf,nome,numero_conta,saldo)

      elif c == 3 :
           print(" INFORMAÇÕES DA CONTA : \n ",cpf,nome,numero_conta,saldo)

      elif c == 4 :
          excluir = input("EXCLUIR CONTA?")
          if excluir.lower() == "não" :
            cpf,numero_conta,saldo = 0
            nome = ''
    elif b == 2:
      print("Saindo do banco felix")
      limpar()
      exit()       

elif a == 2 :
      print("Saindo do banco felix")
      limpar()
      exit()
      