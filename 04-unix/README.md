# Docker container isolation

Запустить контейнер:

```bash
docker run -it --rm ubuntu bash
```

Обновить пакеты внутри:

```bash
apt-get update
```

<img width="1470" alt="1" src="https://github.com/user-attachments/assets/10bb5a2e-d0ec-4440-b556-43ca1a41d8ad" />

## Способ 1

Перезаписать `/etc/resolv.conf`:

```bash
> /etc/resolv.conf
```

Проверить сеть:

```bash
apt-get update
```

<img width="1470" alt="2" src="https://github.com/user-attachments/assets/d09c4fae-17c3-4e4d-b2dd-3eb74a39da23" />


## Способ 2

Перезаписать `/etc/hosts`:

```bash
> /etc/hosts
```

Проверить сеть:

```bash
apt-get update
```

<img width="1470" alt="3" src="https://github.com/user-attachments/assets/38442adf-b2ac-455f-b45e-3230f5de4cb4" />
