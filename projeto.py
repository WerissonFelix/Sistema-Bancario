from datetime import date
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



def escolha():
    guia = int(input("digite a guia que deseja ir"))
    return guia

          

def limpar():
  os.system("cls") or None

            
def menu_cadastro():
    limpar()
    cpf = int(input("digite seu cpf"))
    nome = input("digite seu nome")
    numero_conta = int(input("digite o número da conta"))
    saldo = int(input("quanto deseja depositar??"))
    cpf_lista.append(cpf)
    nome_lista.append(nome)
    saldo_lista.append(saldo)
    numero_conta_lista.append(numero_conta)
    limpar()
    print('\nAgora,  para onde deseja ir?\n'
          "1.MENU PRINCIPAL\n"
         "2.SAIR DO BANCO"
      )

         
def menu_principal():
    limpar()  
    print(
        "BEM-VINDO AO BANCO\n"
        "MENU PRINCIPAL\n"
        "1. INSERIR\n"
        "2. ALTERAR\n"
        "3. CONSULTAR\n"
        "4. EXCLUIR CONTA\n"
      )
def inserir():
      limpar()
      c = escolha()   
      print("TRANSFERÊNCIAS\n "
            "1.FAZER PIX\n"
            "2.DEPOSITAR\n"
            "3.VER EXRATO"
            "4.VOLTA PARA O MENU PRINCIPAL")
      d = escolha()  
      pix()
      depositar()
def pix():
      limpar()
      destinatario = int(input("digite o número da conta do destinatário do pix"))
      valor_pix =  int(input("digite o valor do pix"))
      destinatario_lista.append(destinatario)
      valor_pix_lista.append(valor_pix)
      enviar = input("deseja enviar?")
      if enviar.lower() == "sim":
            print("PIX NO VALO DE ",valor_pix ," FOI ENVIADO PARA ",destinatario," POR ",numero_conta_lista[-1])
            permanecer = input("deseja permanecer no comprovante?") 
            inserir()     
      elif enviar.lower() == "não":            
            inserir()  
def depositar():
      limpar()
      deposito = int(input("digite o valor do seu depósito"))
      valor_deposito.append(deposito)
      saldo_lista[-1] = saldo_lista[-1] + valor_deposito[-1]    
      deposita = input("deseja depositar ",valor_deposito[-1]," reais?")

      if deposita.lower() == "sim":                
         print("PARABÉNS, VOCÊ DEPOSITOU ",valor_deposito[-1]," REAIS ",date.today())
         print("AGORA, VOCÊ TEM ",saldo_lista[-1]," REAIS")
         inserir()
      elif deposita.lower() == "não":  
           print("sei lá") 
           inserir() 
def comprovante():
      print("""BEM-VINDO AOS COMPROVANTES
            1.COMPROVANTES DEPOSITOS 
            2.COMPROVANTES PIX     
             """
       )    
      escolha_comprovante = escolha() 
      if  escolha_comprovante == 1 :
            for v in valor_deposito :
                  print("PARABÉNS, VOCÊ DEPOSITOU ",v," REAIS ")
            print()
            print() 
            print()
            inserir()     
      elif  escolha_comprovante == 2 : 
            for v in valor_pix_lista :
                  for w in destinatario_lista:
                        print("PIX NO VALO DE ",v," FOI ENVIADO PARA ",w," POR ",numero_conta_lista[-1])
            inserir()

print("bem-vindo ao banco, comece escolhendo uma opção\n"
      "1.CADASTRAR\n"
      "2.SAIR DO BANCO\n"
      )

a = escolha()

if a == 1 :
    menu_cadastro()
    b = escolha()
    limpar()  
    if b == 1 :# menu principal
     
      print(menu_principal())
      c = escolha()

      if c == 1 : # meno do inserir

          inserir()
          d = escolha()

          if d == 1 : # opção de enviar pix
             pix()  
          elif d == 2 :
            depositar()
          elif d == 3 :
            comprovante()  
             

      elif c == 2 :

        print(cpf_lista[-1],nome_lista[-1],numero_conta_lista[-1],saldo_lista[-1])

      elif c == 3 :
           print(" INFORMAÇÕES DA CONTA : \n ",cpf,nome,numero_conta,saldo_lista[-1])

      elif c == 4 :
          excluir = input("EXCLUIR CONTA?")
          if excluir.lower() == "sim" :
            cpf,numero_conta,saldo = 0
            nome = ''
    elif b == 2:
      # fazer def sair
      print("Saindo do banco felix")
      limpar()
      exit()

elif a == 2 :
      # fazer def sair
      print("Saindo do banco felix")
      limpar()
      exit()
