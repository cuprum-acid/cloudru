# echo-server

Веб-приложение на Python, которое слушает входящие соединения на порту `8000` и предоставляет страницу с информацией:

- имя хоста
- ip адрес хоста
- имя автора, которое передаётся через переменную окружения `$AUTHOR`

## Build Docker Image

Чтобы собрать приложение, необходимо выполнить следующую команду в терминале в директории `01-application`

```bash
docker build -t ebob/echo-server .
```

## Run Docker Container

Команда для запуска Docker контейнера

```bash
docker run -p 8000:8000 -e AUTHOR="Evgeny B" ebob/echo-server
```

Так же, можно выполнить команду без переменной окружающей среды `-e AUTHOR="Evgeny B"`, тогда по умолчанию `AUTHOR=Default Author`

Приложение будет доступно в браузере по адресу `http://localhost:8000`

## Push to Private Docker Hub Registry

Чтобы запушить образ в приватный registry на Docker Hub, нужно сперва создать новый репозиторий, дать ему имя, например `echo-server`, указать в настройках приватность.

Затем, выполнить в консоли команды:

- Войти в Docker CLI:

    ```bash
    docker login
    ```

- Отправить образ в репозиторий:

    ```bash
    docker push ebob/echo-server
    ```

### Build and Push Multi-arch Image

Собрать и запушить образ для процессорных архитектур ARM и AMD64

```bash
docker buildx build --platform linux/amd64,linux/arm64 -t ebob/echo-server --push .
```
