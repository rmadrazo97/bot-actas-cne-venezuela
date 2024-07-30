# Bot de Telegram para Consultar Actas del CNE

Este es un bot de Telegram que permite a los usuarios consultar actas del CNE utilizando su número de cédula. El bot valida el formato de la cédula, consulta un endpoint y devuelve una imagen del acta correspondiente.

## Requisitos

- Python 3.9+
- Docker (opcional para despliegue)

## Instalación y Configuración

### Clonar el Repositorio

Clona este repositorio en tu máquina local:

```sh
git clone https://github.com/tu-usuario/telegram-bot-actas-cne.git
cd telegram-bot-actas-cne
```

### Crear un Entorno Virtual

Crea y activa un entorno virtual:

```sh
python3 -m venv venv
source venv/bin/activate
```

### Instalar Dependencias

Instala las dependencias necesarias utilizando `pip`:

```sh
pip install -r requirements.txt
```

### Obtener el Token del Bot de Telegram

1. Abre Telegram y busca `@BotFather`.
2. Inicia una conversación con `@BotFather` y utiliza el comando `/newbot`.
3. Sigue las instrucciones para crear un nuevo bot y obtener el token.
4. Guarda el token en un archivo `.env` en el directorio raíz del proyecto:

```plaintext
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

### Ejecutar el Bot Localmente

Para ejecutar el bot localmente, usa el siguiente comando:

```sh
python bot.py
```

### Probar el Bot

1. Abre Telegram y busca tu bot utilizando el nombre de usuario que configuraste con `@BotFather`.
2. Inicia una conversación con tu bot enviando el comando `/start`.
3. Envía tu cédula en el formato correcto (por ejemplo, `V12345678`).

## Despliegue con Docker

### Crear el Archivo Dockerfile

Asegúrate de que tu archivo `Dockerfile` tenga el siguiente contenido:

```Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
```

### Construir la Imagen de Docker

Construye la imagen de Docker utilizando el siguiente comando:

```sh
docker build -t telegram-bot .
```

### Ejecutar el Contenedor Docker Localmente

Ejecuta el contenedor Docker con el siguiente comando:

```sh
docker run --env-file .env -d --name telegram-bot telegram-bot
```

### Verificar que el Contenedor está Corriendo

Verifica que el contenedor está corriendo correctamente:

```sh
docker ps
```

### Verificar los Logs del Contenedor

Para ver los logs del contenedor y asegurarte de que no hay errores:

```sh
docker logs telegram-bot
```

## Despliegue en AWS EC2

### Lanzar una Instancia EC2

1. Ve a la consola de AWS y lanza una nueva instancia EC2 utilizando Amazon Linux 2 AMI.
2. Asegúrate de que la instancia tenga acceso a Internet (ya sea mediante una IP pública o una configuración de VPC adecuada).

### Instalar Docker en la Instancia EC2

Conéctate a tu instancia EC2 a través de SSH y ejecuta los siguientes comandos para instalar Docker:

```sh
sudo yum update -y
sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
exit
```

### Reconectar y Ejecutar el Contenedor Docker

1. Reconéctate a tu instancia EC2.
2. Copia tu archivo `.env` a la instancia.
3. Copia tu imagen Docker a la instancia o construye la imagen directamente en la instancia.
4. Ejecuta el contenedor Docker utilizando el siguiente comando:

```sh
docker run --env-file .env -d --name telegram-bot telegram-bot
```

## Uso

Una vez que el bot esté en funcionamiento, los usuarios pueden interactuar con él en Telegram:

1. Enviar `/start` para iniciar la conversación.
2. Enviar su cédula en el formato `V12345678`, `E12345678`, `J12345678` o `P12345678`.
3. El bot validará la cédula, consultará el endpoint y devolverá la imagen del acta correspondiente.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que desees realizar.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
```