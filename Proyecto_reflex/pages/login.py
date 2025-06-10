import reflex as rx
import bcrypt
import jwt # <- Nos permite crear tarjetas de acceso

import os
# Carga variables de entorno
from dotenv import load_dotenv
load_dotenv()
# Usar la clave secreta desde el entorno
SECRET_KEY = os.getenv('SECRET_KEY')

from sqlmodel import select
from ..models.usuarios import Usuario
from datetime import datetime, timedelta, timezone
from ..auth import AuthState


class EstadoLogin(rx.State):
    # Creamos un atributo por cada dato que buscamos capturar
    email: str = ''
    password:  str = ''
 # Metodo que se ejecuta cuando email detecte un cambio
    @rx.event   
    def asignarCorreo(self, correo_ingresado):
        self.email = correo_ingresado
# Metodo que se ejecuta cuando password detecte un cambio
    @rx.event
    def asignarPassword(self, pass_ingresado):
        self.password = pass_ingresado

# Metodo que se ejecuta al iniciar sesion
    @rx.event
    def autenticar_usuario(self):
        # Buscamos al usuario por correo
        with rx.session() as sesion:
            usuario = sesion.exec(
                select(Usuario).where(Usuario.email == self.email)
            ).first()
        # Verificamos que el usuario exista
        if usuario:
            # Comparar contraseñas
            if bcrypt.checkpw(self.password.encode(), usuario.password.encode()):
                print('Autenticacion exitosa')
                # Creamos credencial de acceso al tener autenticacion
                data_token={
                    'user_id': usuario.id,
                    'user_name': usuario.name, 
                    'exp' : datetime.now(timezone.utc) + timedelta(minutes=5)
                }
                token = jwt.encode(data_token, SECRET_KEY, algorithm='HS256')
                #print(f'Token creado: {token}')
                yield AuthState.generar_token(token)
                return rx.redirect('/dashboard')

            else:
                print("Correo y/o contraseña incorrectos")
                
               
        else:
            print("Usuario no encontrado")

        # Limpiamos los campos por seguridad
        self.email = ''
        self.password = ''

# Imprimimos los datos en la consola
    @rx.event
    def mostrar_info(self):
        print(self.email)
        print(self.password)
        print('-------------------------------')
        

@rx.page(route='/login', title='Inicio de sesion')
def pagina_login() -> rx.Component:
    return rx.container(
        rx.center(
            rx.vstack(
                rx.heading('Inicio de sesion'),

                rx.input(
                    placeholder='Correo',
                    type='email', 
                    value=EstadoLogin.email,
                    on_change=EstadoLogin.asignarCorreo
                ),
                rx.input(
                    placeholder='Contraseña',
                    type='password',
                    value=EstadoLogin.password,
                    on_change=EstadoLogin.asignarPassword
                ),
                rx.button(
                    'Iniciar sesion',
                    on_click=EstadoLogin.autenticar_usuario
                )
            )
        )
    )