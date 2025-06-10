"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from Proyecto_reflex.rxconfig import config
from .pages.info import pagina_info
from .pages.login import pagina_login
from .pages.signup import pagina_signup
from .pages.dashboard import pagina_dashboard


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.center(
            rx.color_mode.button(position="top-right"),
        ),
        rx.vstack(
            rx.heading("Bienvenido a mi app!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),

            # Botones para Login y Sign Up
            rx.hstack(
                rx.link(
                    rx.button("Login", color_scheme="blue"),
                    href="/login"
                ),
                rx.link(
                    rx.button("Sign Up", color_scheme="blue"),
                    href="/signup"
                ),
                spacing='4'
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )




app = rx.App()
app.add_page(index)
app.add_page(pagina_info)
app.add_page(pagina_login)
app.add_page(pagina_signup)
app.add_page(pagina_dashboard)
