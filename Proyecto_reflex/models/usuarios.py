# Este archivo controlara la informacion que viaje entre
# la aplicacion y la base de datos correspondiente a la
# tabla usuarios

import reflex as rx
import bcrypt  
from sqlmodel import Field

class Usuario(rx.Model, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str

    @classmethod
    def crear_usuario(cls, nombre_usuario, correo_usuario, pass_usuario):
        # Codificamos el password en bytes
        pass_codificada = pass_usuario.encode()

        # Hasheo de password y la regresa en bytes
        pass_hasheada = bcrypt.hashpw(pass_codificada, bcrypt.gensalt())

        # Convertimos de bytes a str con decode para almacenar en la db
        return cls(name= nombre_usuario, email=correo_usuario, password=pass_hasheada.decode())
