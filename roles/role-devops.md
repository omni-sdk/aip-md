# DevOps 工程师

## 角色描述
DevOps 工程师负责 CI/CD 流水线、容器编排、批量部署和自动化运维。

## 常用指令

### 构建项目

```atp
terminal#t1:go build -o app.exe ./cmd/main.go
workdir:./project
timeout:120s
```

```json
{"id":"t1","code":0,"text":"success","data":"build completed"}
```

### 运行测试

```atp
terminal#t2:go test ./... -cover
workdir:./project
timeout:120s
```

```json
{"id":"t2","code":0,"text":"success","data":"ok  atp/commands  0.234s  coverage: 87.5%"}
```

### Docker 构建与推送

```atp
terminal#t3:docker build -t myapp:latest . && docker push registry.example.com/myapp:latest
workdir:./project
timeout:300s
```

```json
{"id":"t3","code":0,"text":"success","data":"image pushed"}
```

### 多服务器部署

```atp
ssh#s1:server1
host:192.168.0.101
user:deploy
cmd:cd /app && git pull && systemctl restart app
```

```json
{"id":"s1","code":0,"text":"success","data":"server1: deployed"}
```

### 健康检查

```atp
fetch#f1:https://api.example.com/health
```

```json
{"id":"f1","code":0,"text":"success","data":"{\"status\":\"ok\",\"uptime\":\"72h\"}"}
```

### 回滚部署

```atp
terminal#t4:git revert HEAD --no-edit && git push && ssh deploy@server "cd /app && git pull && systemctl restart app"
workdir:./project
```

```json
{"id":"t4","code":0,"text":"success","data":"rollback deployed"}
```