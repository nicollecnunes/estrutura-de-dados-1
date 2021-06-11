import random
import sys
import numpy as np

INT_MAX = sys.maxsize
RAM = [0] * 100
memoriaInstrucoes = np.empty((10, 4)) #mudar 100

def iniciaRAM():
    for i in range(100):
        RAM[i] = random.randint(0, 1000)
        
def montarInstAleatorias():
    umaInstrucao = [0,0,0,0]
    for i in range(9):#mudar 99
        umaInstrucao[0] = random.randint(0,1) #gera 0 ou 1
        umaInstrucao[1] = random.randint(0, 1000)
        umaInstrucao[2] = random.randint(0, 1000)
        umaInstrucao[3] = random.randint(0, 1000)
        memoriaInstrucoes[i] = umaInstrucao
        print(memoriaInstrucoes[i])
        
    umaInstrucao[0] = -1
    umaInstrucao[1] = -1
    umaInstrucao[2] = -1
    umaInstrucao[3] = -1
    memoriaInstrucoes[9] = umaInstrucao
    print(memoriaInstrucoes[9])
    
    maquina()
        

def maquina():
    PC = 0
    opcode = INT_MAX
    while opcode != -1:
        umaInstrucao = [0] * 4
        umaInstrucao = memoriaInstrucoes[PC]
        opcode = umaInstrucao[0]
        if opcode == 0:
            RAM[umaInstrucao[2]] = umaInstrucao[1]
        elif opcode == 1:
            end1 = umaInstrucao[1]
            end2 = umaInstrucao[2]
            cntRAM1 = RAM[end1]
            cntRAM2 = RAM[end2]
            soma = cntRAM1 + cntRAM2
            RAM[umaInstrucao[3]] = soma
        elif opcode == 2:
            end1 = umaInstrucao[1]
            end2 = umaInstrucao[2]
            cntRAM1 = RAM[end1]
            cntRAM2 = RAM[end2]
            sub = cntRAM1 - cntRAM2
            RAM[umaInstrucao[3]] = sub
        elif opcode == 3:
            umaInstrucao[1] = RAM[umaInstrucao[2]]
        PC += 1


def somar(num1, num2):    
    for n in range(len(memoriaInstrucoes), 3): # 0 1 2
        memoriaInstrucoes.append(0)

    umaInstrucao = levaPraMemo(num1, 0)
    memoriaInstrucoes[0] = umaInstrucao

    umaInstrucao = levaPraMemo(num2, 1)
    memoriaInstrucoes[1] = umaInstrucao

    umaInstrucao = [-1] * 4
    memoriaInstrucoes[2] = umaInstrucao
    
    maquina()

    umaInstrucao = adicionaInstru(0, 1, 1) #??
    memoriaInstrucoes[0] = umaInstrucao

    umaInstrucao = [-1] * 4
    memoriaInstrucoes[1] = umaInstrucao

    maquina()
    
    
def subtrair(num1, num2):
    for n in range(len(memoriaInstrucoes), 3):
      memoriaInstrucoes.append(0)

    umaInstrucao = levaPraMemo(num1, 0)
    memoriaInstrucoes[0] = umaInstrucao

    umaInstrucao = levaPraMemo(num2, 1)
    memoriaInstrucoes[1] = umaInstrucao

    umaInstrucao = [-1] * 4
    memoriaInstrucoes[2] = umaInstrucao
    
    maquina()

    umaInstrucao = subInstru(0, 1, 1)
    memoriaInstrucoes[0] = umaInstrucao

    umaInstrucao = [-1] * 4
    memoriaInstrucoes[1] = umaInstrucao

    maquina()

    

#principal
op = INT_MAX
montarInstAleatorias()

print("+-+-+-+-+-+-+-+ +-+-+-+")
print("|M|A|Q|U|I|N|A| |N|I|C|")
print("+-+-+-+-+-+-+-+ +-+-+-+\n")

print("1) Instruções Aleatorias")
print("2) Soma")
print("3) Subtração")

print("-1) Sair\n")


while op != -1:
        op = int(input("Digite a opção desejada: "))
        iniciaRAM()
        if op == 1:
            ##random aqui
            maquina()
        elif op == 2:
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
            somar(num1, num2)
            print("Soma de {:.2f} + {:.2f} = ".format(num1, num2))
        elif op == 3:
            num1 = float(input("Digite o minuendo: "))
            num2 = float(input("Digite o subtraendo: "))
            subtrair(num1, num2)
            print("Subtração de {:.2f} - {:.2f} = ".format(num1, num2))
        else:
            if op != -1: print("Opção Inválida!\n")
            continue
        print("{:.2f}".format(RAM[1]))
        
print("Finalizando a máquina...")