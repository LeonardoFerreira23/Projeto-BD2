from pymongo import MongoClient
from bson.objectid import ObjectId

class UsuarioDAO:
    def __init__(self, database):
        self.db = database

    def create_user(self, nome: str, email: str, softwares: list, jogos: list):
        """Cria um usuário com lista de softwares e jogos."""
        try:
            user_data = {"nome": nome, "email": email, "softwares": softwares, "jogos": jogos}
            res = self.db.collection.insert_one(user_data)
            print(f"User created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating user: {e}")
            return None

    def read_user(self, id: str):
        """Lê um usuário pelo ID."""
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            return res
        except Exception as e:
            print(f"An error occurred while reading user: {e}")
            return None

    def update_user(self, id: str, nome: str = None, email: str = None, softwares: list = None, jogos: list = None):
        """Atualiza um usuário pelo ID."""
        try:
            update_fields = {}
            if nome:
                update_fields["nome"] = nome
            if email:
                update_fields["email"] = email
            if softwares is not None:
                update_fields["softwares"] = softwares
            if jogos is not None:
                update_fields["jogos"] = jogos

            if update_fields:
                res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": update_fields})
                print(f"User updated: {res.modified_count} document(s) modified")
                return res.modified_count
            else:
                print("No fields to update.")
                return 0
        except Exception as e:
            print(f"An error occurred while updating user: {e}")
            return None

    def delete_user(self, id: str):
        """Deleta um usuário pelo ID."""
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"User deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting user: {e}")
            return None
