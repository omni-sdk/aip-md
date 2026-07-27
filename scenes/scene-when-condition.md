# 条件触发执行

## 构建成功 → 自动部署

```atp
when#w1:terminal#build:go build -o app.exe
workdir:./project
if:[build.code]==0
then@then1:
terminal#deploy:scp app.exe user@server:/app/
then1
else@else1:
terminal#alert:echo "Build failed!" | mail -s "Alert" admin@example.com
else1
```

```json
{"id":"build","code":0,"text":"success","data":"build completed"}
{"id":"deploy","code":0,"text":"success","data":"deployed to server"}
```

---

## 文件存在 → 读取内容

```atp
when#w2:stat#s1:./config.yaml
if:[s1.code]==0
then@then2:
read#r1:./config.yaml
then2
```

```json
{"id":"s1","code":0,"text":"success","data":"Name: config.yaml, Size: 256 bytes"}
{"id":"r1","code":0,"text":"success","data":"server:\n  port: 8080\n  host: 0.0.0.0"}
```

---

## 健康检查 → 重启服务

```atp
when#w3:fetch#f1:https://api.example.com/health
if:[f1.data]!=ok
then@then3:
terminal#restart:systemctl restart app
then3
```

```json
{"id":"f1","code":0,"text":"success","data":"ok"}
```