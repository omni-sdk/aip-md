# 后端开发者

## 角色描述
后端开发者负责 API 开发、数据库设计、服务部署和日志分析。

## 常用指令

### 启动开发服务器

```atp
terminal#t1:go run ./cmd/server.go
workdir:./project
async:true
```

```json
{"id":"t1","code":2,"text":"async pending","data":"server starting on :8080"}
```

### 数据库迁移

```atp
terminal#t2:mariadb -u root -p123456 my_app < ./migrations/001_init.sql
workdir:./project
```

```json
{"id":"t2","code":0,"text":"success","data":"migration completed"}
```

### 查看 API 日志

```atp
terminal#t3:tail -50 /var/log/app.log | grep "GET\|POST\|ERROR"
```

```json
{"id":"t3","code":0,"text":"success","data":"GET /api/users 200\nPOST /api/login 200\nERROR: database timeout"}
```

### 清理缓存

```atp
terminal#t4:redis-cli FLUSHDB
```

```json
{"id":"t4","code":0,"text":"success","data":"OK"}
```

### 代码格式检查

```atp
terminal#t5:gofmt -l .
workdir:./project
```

```json
{"id":"t5","code":0,"text":"success","data":"main.go\ncommands/terminal.go"}
```