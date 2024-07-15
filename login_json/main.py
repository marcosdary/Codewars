import data_input
import os
users = data_input.Json().read_json([])
class Main:
    id_ = 1 if users == [] else users[-1]['id'] + 1
    def new_user(self):
        print('----------------------------------- Novo Usuário -----------------------------------\n')
        user_id = self.id_
        nome = input('\nNOME: ')
        nick = input('NICK: ')
        senha = input('SENHA: ')
        Main.id_ += 1
        user = {
            'id': user_id, 'nome': nome, 
            'nick':nick, 'senha': senha
        }
        users.append(user)
        data_input.Json().write_json(users)
        print('-------------------------------------------------------------------------------------\n')    
    
    def display_users(self):
        print('------------------------------------- Usuários --------------------------------------\n')
        print(f'{"ID":<20}{"NOME":<50}{"NICK":<20}{"SENHA"}')
        for user in users:
            print(f'{user["id"]:<20}{user["nome"]:<50}{user["nick"]:<20}{user["senha"]}')
        
        print('\n------------------------------------------------------------------------------------')

    def remove_user(self):
        print('------------------------------------- Remover usuário --------------------------------\n')
        user_id = input('ID: ')
        if user_id.isnumeric():
            user_id = int(user_id)
            msg = '\n\tUsuário não encontrado\n'
            for user in users:
                if user['id'] == user_id:
                    print(f'{user['nome']} removido com sucesso!!')
                    users.remove(user)
                    return
            else:
                print(msg)
        print('--------------------------------------------------------------------------------------\n')


while True:
    print('1.                 Adicionar usuário\n2.                 Exibir os usuários\n3.                 Remover usuário',
          '\n4.                 Limpa Terminal\n5.                 Sair')
    try:
        main = Main()
        opcao = int(input('OPÇÃO: '))
        match opcao:
            case 1:
                main.new_user()
            case 2:
                main.display_users()
            case 3:
                main.remove_user()
            case 4:
                os.system('cls')
            case 5:
                print('\n\tTenha uma boa semana, meu caro usuário!!\n')
                break 
            case _:
                print('\n\tEscolha uma das opções\n')
    except ValueError:
        print('\n\tOpção Inválida\n')


    