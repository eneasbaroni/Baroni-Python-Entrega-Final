# BARONI Eneas - Curso CODERHOUSE Python

Pre-entrega del curso de Python en CoderHouse

## Instalación

1. Forkeá y cloná el repositorio

2. Parado en la raíz del proyecto ejecutar 

   ```
   pip install virtualenv
   ```
    para instalar virtualenv

3. Luego Ejecutar 

   ```
   virtualenv venv
   ```

    para crear un entorno virtual

4. Activar el interprete  

5. Ejecutar

    ```
    pip install django
    ```
    
    para instalar django

6. Ejecutar

    ```
    pip install pillow
    ```
    
    para instalar pillow
    
7. Ejecutar

    ```
    pip install "django-phonenumber-field[phonenumbers]"
    ```
    
    para instalar django-phonenumber-field, para poder validar los camppos de formulario con datos de telefonos.


8. moverse a la carpeta del proyecto ejecutando

    ```
    cd baroni
    ```

9. Ejecutar

    ```
    python manage.py runserver
    ```

    para levantar el servidor

10. Abrir el navegador en la dirección http://localhost:8000/     


## Uso

El proyecto es un sitio web para un estudio de arquitectura, y cuenta con Cuatro modelos. Obras, Clientes, Equipo y Usuarios.

Tanto el modelo de clientes como el de Obras, el crud se realiza mediante funciones.
Para el modelo de Equipo y Users se utilizan clases basadas en vistas.

A la ruta de profile solo se puede acceder si el usuario está logueado, en caso de no estarlo, se redirige a la pagina de login.
A las rutas de edicion, creacion y eliminacion de obras, clientes y miembros del equipo, solo se puede acceder si el usuario es admin, en caso de no serlo, si se intenta acceder a estas rutas, aparece un mensaje de error.
El control de acceso se realiza mediante el uso de decoradores y/o mixins.
Para el control de acceso de usuario admin, en el caso de Equipo se realiza desde el archivo views.py, mientra que para los modelos Obras y Clientes se realiza desde los archivos HTML, generando una vista con un mensaje de error en caso de no ser admin.

Rutas: 
 - / Home de la pagina. En la barra navegadora hay un buscador para buscar obras por su nombre.
 
 - /about Seccion de About de la pagina, desde aquí se puede acceder a la seccion de Equipo, donde están los miembros del estudio.
 
 - /obras/list-obras/ para visualizar las obras realizadas, desde aquí se puede acceder al formulario de carga.
 - /obras/obra-detail/:id para ver el detalle de una obra (y acceder a edicion o eliminacion siendo admin). 
 - /obras/create-obra/ para crear una obra. (Solo Admin)
 - /obras/edit-obra/:id para actualizar una obra. (Solo Admin)
 - /obras/delete-obra/:id para eliminar una obra. (Solo Admin)
 
 - /clientes/list-clientes/ para visualizar los clientes, desde aquí se puede acceder al formulario de carga, edicion y eliminacion de cliente. (Solo Admin)
 - /clientes/create-cliente/ para crear un cliente. (Solo Admin)
 - /clientes/edit-cliente/:id para actualizar un cliente. (Solo Admin)
 - /clientes/delete-cliente/:id para eliminar un cliente. (Solo Admin)
 
 - /equipo/list-equipo/ para visualizar el equipo que integra el estudio, desde aquí se puede acceder al formulario de carga.
 - /equipo/member-detail/:id para ver el detalle de un miembro del equipo (y acceder a edicion o eliminacion siendo admin).
 - /equipo/create-member/ para agregar un miembro al equipo. (Solo Admin)
 - /equipo/edit-member/:id para actualizar un miembro del equipo. (Solo Admin)
 - /equipo/delete-member/:id para eliminar un miembro del equipo. (Solo Admin)

 - /accounts/profile/ para acceder al perfil del usuario logueado y acceder a la edicion o logout.
 - /accounts/update/ para editar los datos de usuario logueado.
 
 - /admin/ para acceder al panel de administrador.


Para acceder al panel de administrador, o loguearse en la pagina como admin, usar el Usuario admin y el Pass admin123
Para loguearse con un usuario que no sea admin, usar el usuario Eneas y el pass copenague125