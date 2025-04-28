# Docker container isolation

Запустить контейнер:

```bash
docker run -it --rm ubuntu bash
```

Обновить пакеты внутри:

```bash
apt-get update
```

## Способ 1

Перезаписать `/etc/resolv.conf`:

```bash
> /etc/resolv.conf
```

Проверить сеть:

```bash
apt-get update
```

## Способ 2

Перезаписать `/etc/hosts`:

```bash
> /etc/hosts
```

Проверить сеть:

```bash
apt-get update
```
