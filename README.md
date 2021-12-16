# Docker tutorial
## Task 1

```shell
cd first_example
```

Launch:
```shell
docker build -t first_docker .
docker run -p 8080:8080 first_docker 
```
Go to [localhost:8080](http://localhost:8080). Login: admin, Password: admin


Save docker image (first_docker) to file:
```shell
 docker save first_docker > first_docker.tar
```

Load docker image (first_docker) from file. Already in repo:
```shell
docker load < first_docker.tar
docker run first_docker
```

## Task 2

```shell
cd second_example
```

Launch docker images:
```shell
docker-compose up
```
Go to [localhost:5050](http://localhost:5050) Login: admin@admin.com, Password: root

* **Home assignment:** add docker image from task 1 to this composition. Create a database to store Google trends that are generated in task 1

## Usefull commands

Remove all Docker containers:
```shell
 docker rm -f $(docker ps -a -q)
```

Remove all Docker images:
```shell
docker rmi -f $(docker images -aq)
```