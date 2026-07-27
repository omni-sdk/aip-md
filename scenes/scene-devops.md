# DevOps 自动化

## 多服务器批量部署

```atp
ssh#s1:server1
host:192.168.0.101
user:deploy
pass:****
cmd:cd /app && git pull && systemctl restart app
```

```json
{"id":"s1","code":0,"text":"success","data":"server1: deployed"}
```

```atp
ssh#s2:server2
host:192.168.0.102
user:deploy
pass:****
cmd:cd /app && git pull && systemctl restart app
```

```json
{"id":"s2","code":0,"text":"success","data":"server2: deployed"}
```

---

## 健康检查

```atp
fetch#f1:https://api.example.com/health
```

```json
{"id":"f1","code":0,"text":"success","data":"{\"status\":\"ok\",\"uptime\":\"72h\"}"}
```

---

## 日志收集

```atp
terminal#t1:tail -100 /var/log/app.log | grep ERROR
timeout:10s
```

```json
{"id":"t1","code":0,"text":"success","data":"no errors found"}
```

---

## 证书检查

```atp
terminal#t2:echo | openssl s_client -connect example.com:443 2>/dev/null | openssl x509 -noout -enddate
```

```json
{"id":"t2","code":0,"text":"success","data":"notAfter=Dec 15 23:59:59 2026 GMT"}
```