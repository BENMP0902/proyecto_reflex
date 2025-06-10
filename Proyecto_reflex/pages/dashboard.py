import reflex as rx

@rx.page(route='/dashboard', title="Panel de usuario")
def pagina_dashboard() -> rx.Component:
    return rx.container(
        # Barra superior de navegación
        rx.hstack(
            rx.heading("Dashboard", size="7"),
            rx.spacer(),
            rx.button("Cerrar sesión", color_scheme="red", on_click=rx.redirect("/")),
            padding="1rem",
            border_bottom="1px solid #ccc"
        ),
        
        # Cuerpo del dashboard
        rx.vstack(
            rx.heading("Bienvenido usuario", size="6", padding_top="1rem"),

            # Secciones tipo "card"
            rx.hstack(
                rx.box(
                    rx.text("Estadísticas generales", size="4", weight="bold"),
                    rx.text("Aquí puedes ver datos importantes."),
                    padding="1rem",
                    border="1px solid #ccc",
                    border_radius="1rem",
                    width="30%",
                ),
                rx.box(
                    rx.text("Accesos rápidos", size="4", weight="bold"),
                    rx.text("Atajos a funcionalidades clave."),
                    padding="1rem",
                    border="1px solid #ccc",
                    border_radius="1rem",
                    width="30%",
                ),
                spacing="2"
            ),
            padding="2rem",
            spacing="2"
        ),
        max_width="800px",
        margin="auto"
    )
