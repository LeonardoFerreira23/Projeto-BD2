from classes import Usuario, Software, Jogo


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


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
                software = Software(nome_software, ano_software, versao_software, descricao_software, idioma_software)
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
        username = input("Novo nome do usuário (ou deixe em branco para manter o atual): ")
        email = input("Novo email do usuário (ou deixe em branco para manter o atual): ")

        jogos = []
        softwares = []

        if input("Deseja atualizar os jogos? (s/n): ").lower() == "s":
            while True:
                nome_jogo = input("Nome do jogo (ou pressione Enter para finalizar): ")
                if not nome_jogo:
                    break
                ano_jogo = int(input("Ano do jogo: "))
                genero_jogo = input("Gênero do jogo: ")
                multiplayer = input("É multiplayer? (Não ou, se sim, se é local ou online): ")
                desenvolvedora = input("Desenvolvedora: ")
                jogos.append({"nome": nome_jogo, "ano": ano_jogo, "genero": genero_jogo, "multiplayer": multiplayer, "desenvolvedora": desenvolvedora})

        if input("Deseja atualizar os softwares? (s/n): ").lower() == "s":
            while True:
                nome_software = input("Nome do software (ou pressione Enter para finalizar): ")
                if not nome_software:
                    break
                ano_software = int(input("Ano do software: "))
                versao_software = int(input("Versão do software: "))
                descricao_software = input("Descrição: ")
                idioma_software = input("Idioma: ")
                softwares.append({"nome": nome_software, "ano": ano_software, "versao": versao_software, "descricao": descricao_software, "idioma": idioma_software})

        self.user_model.update_user(user_id, username, email, softwares, jogos)

    def delete_user(self):
        user_id = input("Entre com o ID do usuário que deseja deletar: ")
        result = self.user_model.delete_user(user_id)
        if result:
            print("Usuário deletado com sucesso.")
        else:
            print("Erro ao deletar usuário.")

    def run(self):
        print("Welcome to the user CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
