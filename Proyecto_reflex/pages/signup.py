import reflex as rx
from ..models.usuarios import Usuario
from sqlmodel import select

class EstadoSignup(rx.State):
    # Creamos un atributo por cada dato que buscamos capturar
    name: str = ''
    email: str = ''
    password:  str = ''

 # Metodo que se ejecuta cuando name detecte un cambio
    @rx.event
    def asignarNombre(self, nombre_ingresado):
        self.name = nombre_ingresado

 # Metodo que se ejecuta cuando email detecte un cambio
    @rx.event   
    def asignarCorreo(self, correo_ingresado):
        self.email = correo_ingresado

# Metodo que se ejecuta cuando password detecte un cambio
    @rx.event
    def asignarPassword(self, pass_ingresado):
        self.password = pass_ingresado

# Metodo que se ejecuta para buscar usuarios en la db
    @rx.event # <- Solo para debug
    def buscar_usuario(self):

        with rx.session() as sesion:

            # Comando que ejecuta query desde python
            # para ver si el correo ya existe en la db
            usuario_registrado = sesion.exec(
                select(Usuario).where(Usuario.email==self.email)
            ).first()
        return usuario_registrado
        
# Metodo que se ejecuta cuando se crea un usuario
    @rx.event
    def registrar_usuario(self):

        usuario_registrado = self.buscar_usuario()

        if usuario_registrado:
            print('Usuario registrado')
            self.email = ''
        
        else:
            nuevo_usuario = Usuario.crear_usuario(
                self.name,
                self.email,
                self.password
            )
            print(nuevo_usuario)
            try:
                with rx.session() as sesion:
                    # Agrega usuario creado dentro de la db
                    sesion.add(nuevo_usuario)
                    # Guarda los cambio en la db
                    sesion.commit()
            except Exception as e:
                print(f"Error al guardar en la base de datos {e}")

            # Redirigimos al usuario al login
        return rx.redirect('/login')
        

# Imprimimos los datos en la consola
    @rx.event
    def mostrar_info(self):
        print(self.name)
        print(self.email)
        print(self.password)
        print('-------------------------------')
        self.name = ''
        self.email = ''
        self.password = ''
        


@rx.page(route='/signup', title='Registrarse')
def pagina_signup() -> rx.Component:
    return rx.container(
        rx.center(
            rx.vstack(
                rx.heading('Registrarse'),

                rx.input(
                    placeholder='Name (ID)',
                    type='text',
                    value=EstadoSignup.name,
                    on_change=EstadoSignup.asignarNombre
                ),
                rx.input(
                    placeholder='Correo',
                    type='email', 
                    value=EstadoSignup.email,
                    on_change=EstadoSignup.asignarCorreo
                ),
                rx.input(
                    placeholder='Contraseña',
                    type='password',
                    value=EstadoSignup.password,
                    on_change=EstadoSignup.asignarPassword
                ),
                rx.button(
                    'Crear una cuenta',
                    on_click=[
                         EstadoSignup.registrar_usuario, 
                       ]
                    
                )
            )
        )
    )
