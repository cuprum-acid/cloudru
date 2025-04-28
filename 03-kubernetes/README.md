# K8s

## Запуск в `minikube`

```bash
minikube start
```

Ставим helm chart:

```bash
helm install echo-release ./echo-server-chart --namespace echo-server-ns --create-namespace
```

Создаём secret:

```bash
kubectl create secret docker-registry dockerhub-secret \
  --namespace echo-server-ns \
  --docker-server=https://index.docker.io/v1/ \
  --docker-username=<dockerhub-username> \
  --docker-password=<'dockerhub-password'> \
  --docker-email=<dockerhub-email>
```

Добавляем ingress:

```bash
minikube addons enable ingress
```

Запускаем туннель:

```bash
minikube tunnel
```
