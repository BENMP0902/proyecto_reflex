import reflex as rx

# Clase que hereda cosas de "rx.State"
# El codigo podra modificar el estado de una variable
class ContadorEstado(rx.State):
    contador:int = 0

    # Decorador que indica a la funcion "incrementar_contador", ser 
    # un evento reactivo
    @rx.event
    def incrementar_contador(self):
        self.contador += 1

    @rx.event
    def decrementar_contador(self):
        self.contador -= 1

# Decorador que crea la ruta donde se renderiza este componente
@rx.page(route='/informacion', title='About us')
def pagina_info() -> rx.Component:

    #Creamos un espacio de trabajo (continer)
    return rx.container(
        rx.center(
        rx.vstack(
            rx.text('Cambio de estado', size='4', align='center'),
            rx.text(ContadorEstado.contador, size='9'),
            rx.button(
                'Incrementar',on_click=ContadorEstado.incrementar_contador,),
            rx.button(
                'Decrementar',on_click=ContadorEstado.decrementar_contador,)

            )
        )
    )