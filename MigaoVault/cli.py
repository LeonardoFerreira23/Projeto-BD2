from classes import Usuario, Software, Jogo


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com um comando: ")
            if command == "quit":
                print("Obrigado por fazer parte da MigaoVault!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido! Tente novamente.")


class UserCLI(SimpleCLI):
    def __init__(self, user_model):
        super().__init__()
        self.user_model = user_model
        self.add_command("create", self.create_user)
        self.add_command("read", self.read_user)
        self.add_command("update", self.update_user)
        self.add_command("delete", self.delete_user)

    def create_user(self):
            username = input("Entre com o nome do usuário: ")
            email = input("Entre com o email do usuário: ")

            usuario = Usuario(username, email)
            flag = False

            while not flag:
                i = int(input("Você deseja adicionar:\n 1 - Jogo \n 2 - Software \n 3 - Sair "))
                if i == 1:
                    nome_jogo = input("Entre com o nome do jogo: ")
                    ano_jogo = int(input("Entre com o ano do jogo: "))
                    genero_jogo = input("Entre com o gênero do jogo: ")
                    multiplayer = input("É multiplayer? (Não ou, se sim, se é local ou online): ")
                    desenvolvedora = input("Entre com o nome da desenvolvedora: ")
                    jogo = Jogo(nome_jogo, ano_jogo, genero_jogo, multiplayer, desenvolvedora)
                    usuario.adicionar_jogo(jogo)

                elif i == 2:
                    nome_software = input("Entre com o nome do software: ")
                    ano_software = int(input("Entre com o ano do software: "))
                    versao_software = int(input("Entre com a versão do software: "))
                    descricao_software = input("Entre com a descrição do software: ")
                    idioma_software = input("Entre com o idioma nativo do software: ")
                    software = Software(nome_software, ano_software, versao_software, descricao_software,
                                        idioma_software)
                    usuario.adicionar_software(software)

                elif i == 3:
                    print("Saindo da criação do usuário e de sua biblioteca")
                    flag = True
                else:
                    print("Valor errado!")

            # Transforma os jogos e softwares em dicionário para salvar no BD
            softwares_dict = [software.to_dict() for software in usuario.softwares]
            jogos_dict = [jogo.to_dict() for jogo in usuario.jogos]

            # Salva o usuário no banco de dados
            self.user_model.create_user(username, email, softwares_dict, jogos_dict)

    def read_user(self):
        user_id = input("Entre com o ID do usuário que deseja consultar: ")
        user_data = self.user_model.read_user(user_id)
        if user_data:
            print("Dados do Usuário:")
            print(user_data)
        else:
            print("Usuário não encontrado.")

    def update_user(self):
            user_id = input("Entre com o ID do usuário que deseja atualizar: ")

            novos_jogos = []
            novos_softwares = []

            if input("Deseja adicionar novos jogos? (s/n): ").lower() == "s":
                while True:
                    nome_jogo = input("Nome do jogo (ou pressione Enter para finalizar): ")
                    if not nome_jogo:
                        break
                    ano_jogo = int(input("Ano do jogo: "))
                    genero_jogo = input("Gênero do jogo: ")
                    multiplayer = input("É multiplayer? (Não ou, se sim, se é local ou online): ")
                    desenvolvedora = input("Desenvolvedora: ")
                    print("JOGO ADICIONADO NA BIBLIOTECA! ADICIONE UM NOVO JOGO")
                    jogo = Jogo(nome_jogo, ano_jogo, genero_jogo, multiplayer, desenvolvedora)
                    novos_jogos.append(jogo.to_dict())  # Certifique-se de converter para dicionário

            if input("Deseja adicionar novos softwares? (s/n): ").lower() == "s":
                while True:
                    nome_software = input("Nome do software (ou pressione Enter para finalizar): ")
                    if not nome_software:
                        break
                    ano_software = int(input("Ano do software: "))
                    versao_software = int(input("Versão do software: "))
                    descricao_software = input("Descrição: ")
                    idioma_software = input("Idioma: ")
                    print("SOFTWARE ADICIONADO NA BIBLIOTECA! ADICIONE UM NOVO SOFTWARE")
                    software = Software(nome_software, ano_software, versao_software, descricao_software,
                                        idioma_software)
                    novos_softwares.append(software.to_dict())  # Certifique-se de converter para dicionário

            self.user_model.update_user(user_id, softwares=novos_softwares, jogos=novos_jogos)

    def delete_user(self):
        user_id = input("Entre com o ID do usuário que deseja deletar: ")
        result = self.user_model.delete_user(user_id)
        if result:
            print("Usuário deletado com sucesso.")
        else:
            print("Erro ao deletar usuário.")

    def run(self):
        print("Bem vindo ao gerenciamento da MigaoVault!")
        print("Comandos disponíves para manipulação de Usuários: create, read, update, delete, quit")
        super().run()
