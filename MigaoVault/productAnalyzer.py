from pymongo import MongoClient
from helper.writeAJson import writeAJson


class ProductAnalyzer:
    def __init__(self, database, collection):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[database]
        self.collection = self.db[collection]

    # Adicionando consultas relacionadas a jogos e softwares
    def games_by_genre(self, genre):
        pipeline = [
            {"$unwind": "$jogos"},
            {"$match": {"jogos.genero": genre}},
            {"$group": {"_id": "$jogos.genero", "jogos": {"$push": "$jogos.nome"}}}
        ]
        result = list(self.collection.aggregate(pipeline))
        writeAJson(result, f"Jogos do gênero {genre}")

    def software_with_different_versions(self):
        pipeline = [
            {"$unwind": "$softwares"},
            {"$group": {"_id": "$softwares.nome", "versoes": {"$addToSet": "$softwares.versao"}}},
            {"$match": {"$expr": {"$gt": [{"$size": "$versoes"}, 1]}}}
        ]
        result = list(self.collection.aggregate(pipeline))
        writeAJson(result, "Softwares com diferentes versões")

    def latest_games(self):
        pipeline = [
            {"$unwind": "$jogos"},
            {"$sort": {"jogos.ano": -1}},
            {"$limit": 5},
            {"$project": {"_id": 0, "nome": "$jogos.nome", "ano": "$jogos.ano"}}
        ]
        result = list(self.collection.aggregate(pipeline))
        writeAJson(result, "Jogos mais recentes")

    def oldest_games(self):
        pipeline = [
            {"$unwind": "$jogos"},
            {"$sort": {"jogos.ano": 1}},
            {"$limit": 5},
            {"$project": {"_id": 0, "nome": "$jogos.nome", "ano": "$jogos.ano"}}
        ]
        result = list(self.collection.aggregate(pipeline))
        writeAJson(result, "Jogos mais antigos")


if __name__ == "__main__":
    analyzer = ProductAnalyzer(database="MigaoVault", collection="Usuarios")

    # Consultas relacionadas a jogos e softwares
    analyzer.games_by_genre("Aventura")  # Alterar para o gênero desejado
    analyzer.software_with_different_versions()
    analyzer.latest_games()
    analyzer.oldest_games()