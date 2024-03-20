import os

TURNO = ['Matutino', "Vespertino", "Noturno"] 
DIFICULDADE = ["Fácil", "Médio", 'Difícil'] # A dificuldade da tarefa inscrita pelo usuário
STATUS = ['Feito', "Pendente"] # O status do tarefa

list_task = []
list_task_trash = []  

def funct_task(): # A funçõa "funct_task" além de atua como entrada de dados, também armazena eles na "list_task"
    dict_task = {"tarefa": "", "turno": "", "dificuldade": "", "status": False}  # O ddionário foi alocado para o escopo desta função, pois evitar que os valores sejam repetidos
    dict_task['tarefa'] = input('\nNome da tarefa: ')
    
    while True: # Loop infinito para tornar a entrada de dados mais eficência
        print("\n\t1. Vespertino\n\t2. Matutino\n\t3. Noturno")
        turno = input('Turno: ')
        
        print("\n\t1. Fácil\n\t2. Médio\n\t3. Difícil")
        dificuldade = input('Dificuldade: ')
    
        print("\n\t1. Feito\n\t2. Pendente")
        status = input('Status: ')
        
        if turno in ['1', '2', '3'] and dificuldade in ['1', '2', '3'] and status in  ['1', '2']: # Caso as condicionais sejam todas, o daos sõa armazenados no dicionário e é finalizado o 
            dict_task['turno'] = TURNO[int(turno)-1]                                              # o loop infinito
            dict_task["dificuldade"] = DIFICULDADE[int(dificuldade)-1]
            dict_task['status'] = STATUS[int(status)-1]
            break
        
        else:
            
            print("Faça novamente")  # Aqui, é uma representação visual para que usuário repita novamente as digitações
            
    list_task.append(dict_task)
 
 
def trash_of_task():
    reboot = list_task.pop()
    list_task_trash.append(reboot)


def reboot_of_task():
    iterator = iter(list_task_trash) # O iterador "iterator" que recebe o método iter(), pega cada valor até a cada chamda da função
    list_item = next(iterator) # e o next(), por fim, pegar valor sozinho.  
                               # Por exemplo: [{"tarefa": "malhar", "turno": "Vespertino", "dificuldade": "Médio", "status": "Pendente"}] da lista "list_task_trash"
    if list_item not in list_task:  # vai para a lista "list_task" caso ele não esteja inscrito nele. 
        list_task.append(list_item)
        list_task_trash.remove(list_item)
    

def list_to_do_list(array):
    print(f"{"TAREFA":<15} {"TURNO":<15} {"DIFICULDADE":<15}{"STATUS"}")
    for index in array:
        print(f"{index['tarefa']:<15} {index['turno']:<15} {index['dificuldade']:<15} {index['status']}")
        
        
print("LISTA DE TAREFAS")    # Localicação do programa principal
while True:
    print('\n\t1. inserir tarefa\n\t2. listar\n\t3. desfazer\n\t4. refazer\n\t5. sair\n\t6. clear') # As opções ofericidade pelo usuário
    command_user = input("Comando: ")
    if command_user in ['1', '2', '3', '4', '5', '6']:  
        # Cada condicional executa um funçõa ou método
        if command_user == '1': # inserir tarefa
            funct_task()
            
        elif command_user == '2': # listar as tarefas
            list_to_do_list(list_task)
            
        elif command_user == '3': # desfazer as tarefas
            trash_of_task()
            
        elif command_user == '4': # refazer as tarefas
            reboot_of_task()
            
        elif command_user == '5': # sair do while True
            print("\n\n\tObrigado pela atenção, volte sempre!!!")
            break
        
        elif command_user == '6': # limpar a "tela" para que não fique uma bagunça a tela do usuário
            os.system('cls')
            
    else:
        print("\n\tDigite um dos valores")

# Exemplo
    """
        Comando: 1
    1° tarefa: 
    Nome da tarefa: malhar

            1. Vespertino
            2. Matutino  
            3. Noturno   
    Turno: 1

            1. Fácil
            2. Médio
            3. Difícil
    Dificuldade: 1

            1. Feito
            2. Pendente
    Status: 1 --> malhar - Matutino - Fácil - Feito
    
    2° tarefa:
    Nome da tarefa: comer

            1. Vespertino
            2. Matutino
            3. Noturno
    Turno: 2

            1. Fácil
            2. Médio
            3. Difícil
    Dificuldade: 2

            1. Feito
            2. Pendente
    Status: 1 --> comer - Vespertino - Médio - Feito
    
        TAREFA          TURNO           DIFICULDADE    STATUS
    malhar          Matutino        Fácil           Feito
    comer           Vespertino      Médio           Feito
    correr          Vespertino      Fácil           Pendente
    dormir          Vespertino      Fácil           Feito
    trabalhar       Vespertino      Fácil           Pendente
    
    """