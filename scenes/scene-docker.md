# Docker 容器管理

## 启动容器

```atp
terminal#t1:docker run -d --name my_nginx -p 8080:80 nginx:latest
```

```json
{"id":"t1","code":0,"text":"success","data":"container my_nginx started"}
```

---

## 查看运行中的容器

```atp
terminal#t2:docker ps
```

```json
{"id":"t2","code":0,"text":"success","data":"my_nginx  nginx:latest  Up 5 minutes  0.0.0.0:8080->80/tcp"}
```

---

## 停止容器

```atp
terminal#t3:docker stop my_nginx
```

```json
{"id":"t3","code":0,"text":"success","data":"my_nginx stopped"}
```

---

## 查看容器日志

```atp
terminal#t4:docker logs my_nginx --tail 20
```

```json
{"id":"t4","code":0,"text":"success","data":"127.0.0.1 - GET /index.html 200"}
```

---

## Docker Compose 启动

```atp
terminal#t5:docker-compose up -d
workdir:./project
```

```json
{"id":"t5","code":0,"text":"success","data":"all services started"}
```