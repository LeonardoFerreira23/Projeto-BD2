class Jogo():
    def __init__(self, nome, ano, genero, multiplayer, desenvolvedora):
        self.nome = nome
        self.ano = ano
        self.genero = genero
        self.multiplayer = multiplayer
        self.desenvolvedora = desenvolvedora

    def to_dict(self):
        return {
            "nome": self.nome,
            "ano": self.ano,
            "genero": self.genero,
            "multiplayer" : self.multiplayer,
            "desenvolvedora" : self.desenvolvedora
        }

class Software():
    def __init__(self, nome, ano, versao, descricao, idioma):
        self.nome = nome
        self.ano = ano
        self.versao = versao
        self.descricao = descricao
        self.idioma = idioma

    def to_dict(self):
        return {
            "nome": self.nome,
            "ano": self.ano,
            "versao": self.versao,
            "descricao": self.descricao,
            "idioma": self.idioma
        }



class Usuario:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.softwares = []
        self.jogos = []

    def adicionar_software(self, software):
        self.softwares.append(software)

    def adicionar_jogo(self, jogo):
        self.jogos.append(jogo)

