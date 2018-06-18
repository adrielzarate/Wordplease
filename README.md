# Wordplease

Practica Python, Django & Rest

<br>

Wordplease API
------

#### USUARIOS

* Endpoint que permita a cualquier usuario registrarse indicando su nombre, apellidos, nombre de usuario, e-mail y contraseña.

```
POST http://127.0.0.1:8000/api/v1/users/
```
    Parametros:
    * username
    * first_name
    * last_name
    * password

---------------------------------------------------------------------------------------------------------------------------------------------------

* Endpoint que permita ver el detalle de un usuario. Sólo podrán ver el endpoint de detalle de un usuario el propio usuario o un administrador.

```
GET http://127.0.0.1:8000/api/v1/users/<user_id>/
```

---------------------------------------------------------------------------------------------------------------------------------------------------

* Endpoint que permita actualizar los datos de un usuario. Sólo podrán usar el endpoint de un usuario el propio usuario o un administrador.

```
PUT http://127.0.0.1:8000/api/v1/users/<user_id>/
```
    Parametros:
    * username
    * first_name
    * last_name
    * password

---------------------------------------------------------------------------------------------------------------------------------------------------

* Endpoint que permita eliminar un usuario (para darse de baja). Sólo podrán usar el endpoint de un usuario el propio usuario o un administrador.

```
DELETE http://127.0.0.1:8000/api/v1/users/<user_id>/
```
<br>

#### BLOGS

* Endpoint que no requiera autenticación y devuelva el listado de blogs

```
GET http://127.0.0.1:8000/api/v1/blogs/
```
<br>

#### POSTS

• Un endpoint para poder leer los artículos de un blog de manera que, si el usuario no está autenticado, mostrará sólo los artículos publicados. 
Si el usuario está autenticado y es el propietario del blog o un administrador, podrá ver todos los artículos (publicados o no). 
En este endpoint se deberá mostrar únicamente el título del post, la imagen, el resumen y la fecha de publicación. 
Este endpoint debe permitir buscar posts por título o contenido y ordenarlos por título o fecha de publicación. 
Por defecto los posts deberán venir ordenados por fecha de publicación descendente.

```
GET http://127.0.0.1:8000/api/v1/posts/
```

---------------------------------------------------------------------------------------------------------------------------------------------------

* Un endpoint para crear posts en el cual el usuario deberá estar autenticado. En este endpoint el post quedará publicado automáticamente en el blog del usuario autenticado.

```
POST http://127.0.0.1:8000/api/v1/posts/
```
    Parametros:
    * title
    * category (category number)
    * intro
    * image
    * post_body

---------------------------------------------------------------------------------------------------------------------------------------------------

* Un endpoint de detalle de un post, en el cual se mostrará toda la información del POST. Si el post no es público, sólo podrá acceder al mismo el dueño del post o un administrador.

```
GET http://127.0.0.1:8000/api/v1/posts/<post_id>/
```

---------------------------------------------------------------------------------------------------------------------------------------------------

* Un endpoint de actualización de un post. Sólo podrá acceder al mismo el dueño del post o un administrador.

```
PUT http://127.0.0.1:8000/api/v1/posts/<post_id>/
```
    Parametros:
    * title
    * category (category number)
    * intro
    * image
    * post_body

---------------------------------------------------------------------------------------------------------------------------------------------------

* Un endpoint de borrado de un post. Sólo podrá acceder al mismo el dueño del post o un administrador.

```
DELETE http://127.0.0.1:8000/api/v1/posts/<post_id>/
``` 