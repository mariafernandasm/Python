from datetime import datetime

def validarData(dataHora):
    try:
        datetime.strptime(dataHora,"%d/%m/%Y %H:%M")
        return True
    except:
        return False

def adicionarTarefa(nomeTarefa,descricaoTarefa,dataTarefa, horaTarefa,lista):
    lista.append (nomeTarefa + ";" + descricaoTarefa + ";" + dataTarefa + ";" + horaTarefa)
    
def listarTarefas(lista):
    for i,tarefa in enumerate(lista):
        print (40*"-")
        print (f"Tarefa {i+1}")
        print (40*"-")
        informacoes = tarefa.split(";")
        print ("\n")
        print (f"Nome:{informacoes[0]}")
        print (f"Descricao:{informacoes[1]}")
        print (f"Data:{informacoes[2]}")
        print (f"Hora:{informacoes[3]}")
        print ("\n")

def removerTarefa(indice,lista):
    lista.pop(indice-1)

def editarTarefa(lista, tarefa):
     for tarefa in enumerate(lista):
        nomeTarefa = input ("Informe o nome da tarefa: ")
        descricaoTarefa = input ("Informe a descrição da tarefa: ")
        dataTarefa = input ("Informe a data da tarefa (data/mes/ano): ")
        horaTarefa = input ("Informe o horário da tarefa(hora:minuto): ")

lista = []
print (40*"-")
print ("Bem-vindo(a) ao meu projeto!")
print (40*"-")
while True:
    print ("O que deseja fazer?")
    print ("1. Adicionar uma nova tarefa")
    print ("2. Listar tarefas")
    print ("3. Remover uma tarefa")
    print ("4. Sair")
    try:
        escolha = int(input("Escolha: "))
    except ValueError:
        print ("Opção inválida, escolha um número inteiro!")
        continue
    if (escolha==1):
        nomeTarefa = input ("Informe o nome da tarefa: ")
        descricaoTarefa = input ("Informe a descrição da tarefa: ")
        dataTarefa = input ("Informe a data da tarefa (data/mes/ano): ")
        horaTarefa = input ("Informe o horário da tarefa(hora:minuto): ")
    
        dataHora = dataTarefa + " " + horaTarefa
        if (validarData(dataHora)):
            adicionarTarefa(nomeTarefa,descricaoTarefa,dataTarefa, horaTarefa,lista)
        else:
            print ("Erro, data ou hora inválida!")
    elif (escolha==2):
        listarTarefas(lista)
    elif (escolha==3):
        listarTarefas(lista)
        try: 
            numTarefa = int(input("Digite qual tarefa deseja remover: "))
            removerTarefa(numTarefa,lista)
        except ValueError:
            print ("Escolha um inteiro!")
    else:
        print ("Espero ter ajudado!")
        break 

        
        