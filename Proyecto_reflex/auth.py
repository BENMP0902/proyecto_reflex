# Archivo que contendra la cookie del inicio de sesion

import reflex as rx

class AuthState(rx.State):
    auth_token: str = rx.Cookie(name='Authtoken', secure=True)

    @rx.event
    def generar_token(self, token_acceso):
        self.auth_token = token_acceso