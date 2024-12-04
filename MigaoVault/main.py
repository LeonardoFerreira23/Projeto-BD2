from database import Database
from userModel import UsuarioDAO
from cli import UserCLI

# Criação do CLI e execução
db = Database(database="Ludobox", collection="Usuarios")
#db.resetDatabase()  # Certifique-se de chamar este método antes de qualquer inserção.

UserModel = UsuarioDAO(database=db)

userCLI = UserCLI(UserModel)
userCLI.run()

