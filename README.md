# Dog API

Esta es una aplicación en Python que funciona como una API para obtener y almacenar datos sobre razas de perros. La API se conecta a un servicio externo para obtener información sobre diferentes razas de perros y almacena estos datos en una base de datos MySQL.

## Requisitos

- Docker
- Python 3.x
- MySQL

## Configuración

1. Clona este repositorio en tu máquina local:

    ```
    git clone https://github.com/tuusuario/dog-api.git
    ```

2. Crea un archivo `.env` en el directorio raíz del proyecto y configura las siguientes variables de entorno:

    ```
    DB_USER=usuario
    DB_PASSWORD=contraseña
    DB_HOST=localhost
    DB_NAME=nombre_de_la_base_de_datos
    ```

3. Asegúrate de tener Docker instalado y en funcionamiento en tu sistema.

## Ejecución

Para ejecutar la aplicación, simplemente ejecuta el siguiente comando en el directorio raíz del proyecto:

`docker-compose up --build`


Esto creará y ejecutará los contenedores de la aplicación y la base de datos.

## Uso

Una vez que la aplicación esté en funcionamiento, puedes interactuar con ella a través de la API RESTful. Aquí hay algunos ejemplos de cómo puedes usarla:

- Obtener todos los datos de las razas de perros:

    ```
    GET /api/data
    ```

- Obtener un registro de datos específico por su ID:

    ```
    GET /api/data/{id}
    ```

- Almacenar nuevos datos de razas de perros en la base de datos:

    ```
    POST /api/data
    ```

Para más detalles sobre los endpoints disponibles, consulta la documentación en la aplicación o revisa el código fuente.
