import random, time
char = ["7","#","2","9","1"]
balance= 0
linha1=["","",""]
linha2=["","",""]
linha3=["","",""]
earning= 0
#TO DO:
#limitacao do saldo negativo !FEITO!
#mostrar melhor quanto foi ganho !FEITO!

def desenho(): #DESENHAR NA TELA
    x=24
    y=8
    print ("SLOT MACHINE " + " // Você tem: "+ str(balance) + "$", end="")
    if earning!=0:
        print (" GANHOU! + " + str(earning) + "$")
    else:
        print()

    for i in range(y):
        if i==0 or i==y-1:#Começo e fim
            print ("x" * x, end= "")
        if i==1:
            print ("|" +  " "* (x//2-7)+ "SLOT MACHINE" + " "*5 +  "|" ,end="")# Printar slot machine
        elif i==2:
            print ("|" +  " " * (x//2-6) + str(linha1[0]) + " | " + str(linha1[1]) + " | " + str(linha1[2]) + " "*6 +  " |" ,end="")# NUMEROS
        elif i == 3:
            print ("|" +  " " * (x//2-6) + str(linha2[0]) + " | " + str(linha2[1]) + " | " + str(linha2[2]) + " "*6 +  " |" ,end="")
        elif i==4:
            print ("|" +  " " * (x//2-6) + str(linha3[0]) + " | " + str(linha3[1]) + " | " + str(linha3[2]) + " "*6 +  " |" ,end="")
        elif i!=0 and i!=y-1:# restante da "maquina"
            print ("|" +  " "* (x-2) + "|" ,end="")
        print()
def girar(): #lista com 3 valores aleatorios
    for i in range (3):
        linha1[i] = random.choice(char)
        linha2[i] = random.choice(char)
        linha3[i] = random.choice(char)


def dindin():
    multiplicadores=[10,20,2,5,1]
    ganhos=0
    if linha1[0]==linha1[1] and linha1[1]== linha1[2]:
        sla1 = linha1[0]
        index = char.index(sla1)
        ganhos += (int(aposta) * int(multiplicadores[index]))
    if linha2[0]==linha2[1] and linha2[1]== linha2[2]:
        sla2 = linha2[0]
        index = char.index(sla2)
        ganhos += (int(aposta) * int(multiplicadores[index]))
    if linha3[0]==linha3[1] and linha3[1]== linha3[2]:
        sla3 = linha3[0]
        index = char.index(sla3)
        ganhos += (int(aposta) * int(multiplicadores[index]))
    return ganhos




while True:
    print ("Quanto deseja depositar? ")
    try:
        balance = int(input())
        break
    except ValueError:
        print ("VALOR INVÁLIDO")
girar()
desenho()
while True:
    girar()
    print ("Quanto deseja apostar? Digite q para sair / p para depositar mais. / r para saber as regras. ")
    aposta = input()
    if aposta.lower() == "q":
        print ("Muito obrigado!")
        break
    elif aposta.lower() == "p":
        balance = balance + int(input("Quanto deseja depositar? : "))
        earning = 0
        desenho()
        continue
    elif aposta.lower() == "r":
        print ("7 VALE 10X\n"
               "9 VALE 5X\n"
               "2 VALE 2X\n"
               "1 VALE 1X\n"
               "# VALE 20X"
               )
        time.sleep(3)
        desenho()
        continue
    try:
        if balance - int(aposta) < 0:
            print("Saldo insuficiente! Digite p para depositar mais!")
            earning = 0
            time.sleep(1)
            desenho()
            continue
        balance -= int(aposta)

    except ValueError:
        print ("Digite uma opção válida!")
        continue
    balance = balance + dindin()
    earning = dindin()
    desenho()